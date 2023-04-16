import tensorflow as tf
import os
import cv2
import numpy as np
import scipy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from google.colab import drive

drive.mount('/content/drive')

# Define paths to the training, validation, and test data directories
#replace the paths to directory with the actual paths to your video training directories
train_dir = "path to ttrain directory"
val_dir = "path to validation directory"

# Define the batch size and image dimensions
batch_size =2
img_height = 70
img_width =70

# Define the number of frames to use for each video
num_frames = 50

# Loop through the two subfolders
train_data = []
train_labels = []
for subdir in ["Fight", "NonFight"]:
    subdir_path = os.path.join(train_dir, subdir)
    # Loop through each AVI video file in the subfolder
    for filename in os.listdir(subdir_path):
        if filename.endswith(".avi"):
            # Open the video file using OpenCV
            video_path = os.path.join(subdir_path, filename)
            cap = cv2.VideoCapture(video_path)

            # Keep track of the number of frames added to the training data and labels
            num_frames_added = 0

            # Loop through each frame and add it to the training data and labels
            while (cap.isOpened() and num_frames_added < num_frames):
                ret, frame = cap.read()
                if ret == False:
                    break
                frame_resized = cv2.resize(frame, (img_height, img_width))
                train_data.append(frame_resized)
                train_labels.append(1 if subdir == "Fight" else 0)
                num_frames_added += 1

            # Release the video capture object
            cap.release()

# Shuffle the training data and labels
train_data = np.array(train_data)
train_labels = np.array(train_labels)
idx = np.random.permutation(len(train_data))
train_data, train_labels = train_data[idx], train_labels[idx]
print("finished with frames")
# Use data augmentation for the training data
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

# No data augmentation for the validation data
val_datagen = ImageDataGenerator(rescale=1./255,    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True)

# Load the data from the arrays
train_data_gen = train_datagen.flow(train_data, train_labels, batch_size=batch_size)
val_data_gen = val_datagen.flow_from_directory(
    val_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    classes=['NonFight', 'Fight']
)

# Get the number of samples in the train and validation sets
num_train = len(train_data)
num_val = val_data_gen.samples

# model architecture- convulutional network 3 layers
model = tf.keras.models.Sequential([
    # Add some convolutional layers
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),

tf.keras.layers.Flatten(),
tf.keras.layers.Dense(128, activation='relu'),
tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("started training")

history = model.fit(train_data_gen,
epochs=10,
steps_per_epoch=num_train//batch_size,
validation_data=val_data_gen,
validation_steps=num_val//batch_size)
print("finished with training")

#test_dir = "C:/Users/ohad/Videos/RWF-2000/test"
#test_datagen = ImageDataGenerator(rescale=1./255)
#test_data_gen = test_datagen.flow_from_directory(
#test_dir,
#target_size=(img_height, img_width),
#batch_size=batch_size,
#class_mode='binary',
#classes=['NonFight', 'Fight']
#)
#num_test = test_data_gen.samples
#model.evaluate(test_data_gen, steps=num_test//batch_size)

model.save('my_video_trained_model2.h5')