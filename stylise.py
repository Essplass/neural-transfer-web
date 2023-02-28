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
    # Define a dictionary to map style_value to corresponding image paths
    styles = {
        "1": "Lichenstein.jpg",
        "2": "Monet.jpg",
        "3": "vangogh.jpg",
        "4": "andywarhol.jpg",
        "5": "davinci.jpg",
        "6": "picasso.jpg",
        "7": "salvadordali.jpg",
        "8": "banksy.jpg"
    }

    # Load content and style images
    content_image = load_image(img_path)
    style_image_path = os.path.join('C:\\Users\\amend\\this\\path\\style_image\\', styles.get(style_value))
    style_image = load_image(style_image_path)

    # Perform neural transfer on image, write the image to the out_folder to be displayed in the uploads page.
    stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
    cv2.imwrite(f'C:\\Users\\amend\\this\\path\\OUT_FOLDER\\{img_name}',
                cv2.cvtColor(np.squeeze(stylized_image) * 255, cv2.COLOR_BGR2RGB))

