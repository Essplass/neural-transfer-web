# Allows us to use deploy a model from the Tensorflow repository
import tensorflow_hub as hub
# Importing Tensorflow
import tensorflow as tf
# Importing matplotlib to show our images
from matplotlib import pyplot as plt
# Using numpy to format images
import numpy as np
# Importing openCV to allow us to do file saves
import cv2.cv2

# Loading the arbitrary image stylisation model from tensorflow.
model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')


# Prepare image for style transfer by converting the image to a compatible float32 datatype
def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img


# Performs image stylisation takes the image path, the image name and style type as argument.
def stylise(img_path, img_name, style_value):
    # If statements to match style value from the dropdown box to the correlating art style.
    if style_value == "1":
        style_image = load_image('C:\\Users\\samue\\Desktop\\creativecomputinga1\\style_image\\Lichenstein.jpg')
    if style_value == "2":
        style_image = load_image('C:\\Users\\samue\\Desktop\\creativecomputinga1\\style_image\\Monet.jpg')
    if style_value == "3":
        style_image = load_image('C:\\Users\\samue\\Desktop\\creativecomputinga1\\style_image\\vangogh.jpg')
    if style_value == "4":
        style_image = load_image('C:\\Users\\samue\\Desktop\\creativecomputinga1\\style_image\\andywarhol.jpg')
    if style_value == "5":
        style_image = load_image('C:\\Users\\samue\\Desktop\\creativecomputinga1\\style_image\\davinci.jpg')
    if style_value == "6":
        style_image = load_image('C:\\Users\\samue\\Desktop\\creativecomputinga1\\style_image\\picasso.jpg')
    if style_value == "7":
        style_image = load_image('C:\\Users\\samue\\Desktop\\creativecomputinga1\\style_image\\salvadordali.jpg')
    if style_value == "8":
        style_image = load_image('C:\\Users\\samue\\Desktop\\creativecomputinga1\\style_image\\banksy.jpg')
    content_image = load_image(img_path)
    plt.imshow(np.squeeze(content_image))
    # Perform neural transfer on image, write the image to the out_folder to be displayed in the uploads page.
    stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
    plt.imshow(np.squeeze(stylized_image))
    cv2.imwrite(f'C:\\Users\\samue\\Desktop\\creativecomputinga1\\OUT_FOLDER\\{img_name}',
                cv2.cvtColor(np.squeeze(stylized_image) * 255, cv2.COLOR_BGR2RGB))

