import tensorflow as tf
import os
import cv2
import numpy as np
import scipy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from google.colab import drive
from tensorflow.keras.models import load_model

drive.mount('/content/drive')
# Define the batch size and image dimensions
batch_size =2
img_height = 70
img_width =70

# Define the number of frames to use for each video
num_frames = 50
# Define paths to the training, validation, and test data directories
#replace 'path/to/validation directory' with your own path
val_dir = path/to/validation directory
val_data = []
val_labels = []
val_labels_opt = []
val_data_opt = []

for subdir in ["Fight", "NonFight"]:
    subdir_path = os.path.join(val_dir, subdir)

    # Loop through each AVI video file in the subfolder
    for filename in os.listdir(subdir_path):
        if filename.endswith(".avi"):
            # Open the video file using OpenCV
            video_path = os.path.join(subdir_path, filename)
            cap = cv2.VideoCapture(video_path)

            # Keep track of the number of frames added to the training data and labels
            num_frames_added = 0
            prev_gray = None

            # Loop through each frame and add it to the training data and labels for RGB model
            while (cap.isOpened() and num_frames_added < num_frames):
                ret, frame = cap.read()
                if ret == False:
                    break
                frame_resized = cv2.resize(frame, (img_height, img_width))
                val_data.append(frame_resized)
                val_labels.append(1 if subdir == "Fight" else 0)
                num_frames_added += 1

            # Re-initialize the capture object
            cap.release()
            cap = cv2.VideoCapture(video_path)
            num_frames_added = 0

            # Loop through each frame and add it to the training data and labels for optical flow model
            while (cap.isOpened() and num_frames_added < num_frames):
                ret, frame = cap.read()
                if ret == False:
                    break
                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                if prev_gray is not None:
                    flow = cv2.calcOpticalFlowFarneback(prev_gray, frame_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
                    flow_resized = cv2.resize(flow, (img_height, img_width))
                    val_data_opt.append(flow_resized)
                    val_labels_opt.append(1 if subdir == "Fight" else 0)
                    num_frames_added += 1
                prev_gray = frame_gray

            # Release the video capture object
            cap.release()


# Evaluate the performance of each model on a validation set
val_data = np.array(val_data)
val_labels = np.array(val_labels)
val_data_opt=np.array(val_data_opt)
val_labels_opt = np.array(val_labels_opt)
print(val_data_opt.shape)
# Merge RGB and optical flow data into a single input tensor
val_data_combined = np.concatenate([val_data, val_data_opt], axis=-1)

# Load the weights of the two models
model1 = load_model('opt_model.h5')
model1._name="Optical_model"
model2 = load_model('my_video_trained_model.h5')

# Define input layers for the RGB and optical flow data
rgb_input = tf.keras.Input(shape=(img_height, img_width, 3), name='rgb_input')
opt_input = tf.keras.Input(shape=(img_height, img_width, 2), name='opt_input')

# Pass the RGB and optical flow data through the respective models
rgb_output = model2(rgb_input)
opt_output = model1(opt_input)

# Concatenate the outputs from both models
concatenated = tf.keras.layers.concatenate([rgb_output, opt_output])

# Add a dense layer for the final prediction
x = tf.keras.layers.Dense(1, activation='sigmoid')(concatenated)

# Create the combined model
combined_model = tf.keras.Model(inputs=[rgb_input, opt_input], outputs=x)

# Compile the model
combined_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Save the combined model
combined_model.save('combined_model.h5')