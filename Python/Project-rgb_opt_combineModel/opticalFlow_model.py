import tensorflow as tf
import os
import cv2
import numpy as np
import scipy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from google.colab import drive

drive.mount('/content/drive')

# Define paths to the training, validation, and test data directories
#replace the following paths with the paths to your training and validation directories
train_dir = "path"
val_dir = "path"

# Define the batch size and image dimensions
batch_size = 8
img_height = 70
img_width = 70

# Define the number of frames to use for each video
num_frames = 40

# Loop through the two subfolders
train_data_optical_flow = []
train_labels = []
for subdir in ["Fight", "NonFight"]:
    subdir_path = os.path.join(train_dir, subdir)

    # Loop through each AVI video file in the subfolder
    for filename in os.listdir(subdir_path):
        if filename.endswith(".avi"):
            # Open the video file using OpenCV
            video_path = os.path.join(subdir_path, filename)
            cap = cv2.VideoCapture(video_path)

            # Keep track of the number of frames added to the training data
            num_frames_added = 0
            prev_gray = None

            # Loop through each frame and add its optical flow to the training data
            while (cap.isOpened() and num_frames_added < num_frames):
                ret, frame = cap.read()
                if ret == False:
                    break
                frame_resized = cv2.resize(frame, (img_height, img_width))

                # Convert the current frame to grayscale
                gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
                
                # Calculate the optical flow from the previous frame to the current frame
                if prev_gray is not None:
                    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
                    train_data_optical_flow.append(flow)
                    train_labels.append(1 if subdir == "Fight" else 0)

                prev_gray = gray
                num_frames_added += 1

            # Release the video capture object
            cap.release()

# Shuffle the training data and labels
train_data_optical_flow = np.array(train_data_optical_flow)
train_labels = np.array(train_labels)
idx = np.random.permutation(len(train_data_optical_flow))
train_data_optical_flow, train_labels = train_data_optical_flow[idx], train_labels[idx]
print("finished with frames")

# Define a custom data generator that takes in optical flow data instead of RGB images
def optical_flow_data_generator(data, labels, batch_size, aug=None):
    i = 0
    while True:
        batch_data = data[i:i+batch_size]
        batch_labels = labels[i:i+batch_size]
        if aug is not None:
            batch_data = aug.flow(batch_data, batch_size=batch_size, shuffle=False).next()
        yield batch_data, batch_labels
        i += batch_size
        if i >= len(data):
            i = 0

# Use data augmentation for the training data
train_datagen = ImageDataGenerator(rescale=1./255,
rotation_range=20,
width_shift_range=0.2,
height_shift_range=0.2,
shear_range=0.2,
zoom_range=0.2,
horizontal_flip=True,
)
    

# No data augmentation for the validation data
val_datagen = ImageDataGenerator(rescale=1./255,
rotation_range=20,
width_shift_range=0.2,
height_shift_range=0.2,
shear_range=0.2,
zoom_range=0.2,
horizontal_flip=True,
)

# Load the data from the arrays using the custom data generator
train_data_gen = optical_flow_data_generator(train_data_optical_flow, train_labels, batch_size, train_datagen)

val_data_gen = val_datagen.flow_from_directory(
    directory=val_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary'
)
model = tf.keras.Sequential([
tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(img_height, img_width, 2)),
tf.keras.layers.MaxPooling2D((2,2)),
tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
tf.keras.layers.MaxPooling2D((2,2)),
tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
tf.keras.layers.MaxPooling2D((2,2)),
tf.keras.layers.Flatten(),
tf.keras.layers.Dense(128, activation='relu'),
tf.keras.layers.Dropout(0.5),
tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
optimizer='adam',
loss='binary_crossentropy',
metrics=['accuracy']
)

history = model.fit(
train_data_gen,
steps_per_epoch=len(train_labels) // batch_size,
epochs=10,
validation_data=val_data_gen,
validation_steps=val_data_gen.samples // batch_size
)

model.save('/content/drive/MyDrive/RWF-videos-2000/RWF-2000/opt_model.h5')