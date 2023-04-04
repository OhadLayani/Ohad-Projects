!pip install opencv-python-headless
import tensorflow as tf
import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from google.colab import drive
import pandas as pd

drive.mount('/content/drive')

# Define paths to the training, validation, and test data directories
train_dir = "/content/drive/MyDrive/RWF-2000/train"
val_dir = "/content/drive/MyDrive/RWF-2000/val"

# Define the batch size and image dimensions
batch_size = 32
img_height = 255
img_width = 255

# Initialize the training data and labels
train_data_rgb = []
train_data_flow = []
train_labels = []

for subdir in os.listdir(train_dir):
    subdir_path = os.path.join(train_dir, subdir)
    if os.path.isdir(subdir_path):
        # Loop through each video file in the subfolder
        for filename in os.listdir(subdir_path):
            if filename.endswith(".avi"):
                # Open the video file using OpenCV
                vid_path = os.path.join(subdir_path, filename)
                cap = cv2.VideoCapture(vid_path)

                # Check if the video is loaded properly and has a valid size
                if cap.isOpened() and cap.get(cv2.CAP_PROP_FRAME_COUNT) > 0:
                    # Loop through each frame in the video
                    while True:
                        ret, frame = cap.read()
                        if not ret:
                            break

                        # Resize the frame to the desired dimensions
                        frame_resized = cv2.resize(frame, (img_height, img_width))

                        # Add the frame to the training data and labels
                        train_data_rgb.append(frame_resized)
                        train_data_flow.append(frame_resized)
                        train_labels.append(1 if subdir == "Fight" else 0)
                else:
                    print(f"Invalid video: {vid_path}")

# Shuffle the training data and labels
train_data_rgb = np.array(train_data_rgb)
train_data_flow = np.array(train_data_flow)
train_labels = np.array(train_labels)
idx = np.random.permutation(len(train_data_rgb))
train_data_rgb, train_data_flow, train_labels = train_data_rgb[idx], train_data_flow[idx], train_labels[idx]

# No data augmentation for the validation data
train_datagen = ImageDataGenerator(
rescale=1./255,
rotation_range=20,
zoom_range=0.2,
horizontal_flip=True
)

# Load the data from the arrays

# Create the grayscale data generator
train_data_gen_grayscale = ImageDataGenerator(
rescale=1./255,
rotation_range=20,
width_shift_range=0.2,
height_shift_range=0.2,
shear_range=0.2,
zoom_range=0.2,
horizontal_flip=True,
validation_split=0.2,
)



# Create the grayscale data generator

train_rgb_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=True,
    subset='training',
    color_mode='rgb')

train_flow_generator = train_data_gen_grayscale.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=True,
    subset='training',
    color_mode='grayscale')


val_datagen = ImageDataGenerator(rescale=1./255)

val_rgb_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False,
    color_mode='rgb')

val_flow_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False,
    color_mode='grayscale')
# Create a generator that yields tuples of (rgb_image, grayscale_image)




num_train = len(train_labels)
num_val = val_data_gen.samples

# Define the model architecture

 # Define the input layer
# Define the input layers
input_layer_rgb = tf.keras.layers.Input(shape=(img_height, img_width, 3))
input_layer_gray = tf.keras.layers.Input(shape=(img_height, img_width, 1))

# Define the number of filters in each layer
filters1 = 32
filters2 = 64

# Create the RGB model
rgb_model = tf.keras.models.Sequential([
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

# Create the Optical Flow model
opt_model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(img_height, img_width,1)),
    tf.keras.layers.Conv2D(filters=filters1, kernel_size=(3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    tf.keras.layers.Conv2D(filters=filters2, kernel_size=(3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
rgb_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
opt_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Define the input layers for the RGB and grayscale models

# Get the output from the RGB model
rgb_output = rgb_model(input_layer_rgb)

# Get the output from the grayscale model
gray_output = opt_model(input_layer_gray)

# Concatenate the outputs from the RGB and grayscale models
concat_layer = tf.keras.layers.concatenate([rgb_output, gray_output])

# Add a dense layer and an output layer to the concatenated output
dense_layer = tf.keras.layers.Dense(128, activation='relu')(concat_layer)
output_layer = tf.keras.layers.Dense(1, activation='sigmoid')(dense_layer)

# Define the combined model with the input layers and output layer
combined_model = tf.keras.models.Model(inputs=[input_layer_rgb, input_layer_gray], outputs=output_layer)

# Compile the combined model
combined_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])



# Define the number of epochs to train for
epochs = 10

# Train the model

rgb_model.fit(train_rgb_generator, 
    steps_per_epoch=num_train // batch_size,
    epochs=epochs,
    validation_data=val_data_gen,
    validation_steps=num_val // batch_size,)
rgb_model.save_weights('rgb_model_weights.h5')

# Train the grayscale model
opt_model.fit(train_flow_generator, steps_per_epoch=num_train // batch_size,
    epochs=epochs,
    validation_data=val_data_gen,
    validation_steps=num_val // batch_size,)
opt_model.save_weights('grayscale_model_weights.h5')

# Load the saved weights into the combined model
combined_model.load_weights('rgb_model_weights.h5', by_name=True)
combined_model.load_weights('grayscale_model_weights.h5', by_name=True)
# Save the model
model.save("/content/drive/MyDrive/optical_flow_conv_lstm_model.h5")

# Create a dataframe to store the training history
#history_df = pd.DataFrame(history.history)

# Save the training history to a CSV file
#history_df.to_csv('/content/drive/MyDrive/optical_flow_conv_lstm_history.csv', index=False)