import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math
from skimage import color
from skimage import io


def load(image_path):
    """ Loads an image from a file path

    Args:
        image_path: file path to the image

    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """
    out = None

    # YOUR CODE HERE
    # Use skimage io.imread
    out = io.imread(image_path)
    # END YOUR CODE

    return out


def change_value(image):
    """ Change the value of every pixel by following x_n = 0.5*x_p^2
        where x_n is the new value and x_p is the original value

    Args:
        image: numpy array of shape(image_height, image_width, 3)

    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """

    out = None

    # YOUR CODE HERE
    out = 0.5 * np.square(image)
    # END YOUR CODE

    return out


def convert_to_grey_scale(image):
    """ Change image to gray scale

    Args:
        image: numpy array of shape(image_height, image_width, 3)

    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """
    out = None

    # YOUR CODE HERE
    out = 0.3 * image[:, :, 0] + 0.59 * image[:, :, 1] + 0.11 * image[:, :, 2]
    # END YOUR CODE

    return out


def rgb_decomposition(image, channel):
    """ Return image **excluding** the rgb channel specified

    Args:
        image: numpy array of shape(image_height, image_width, 3)
        channel: str specifying the channel

    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """

    out = None

    # YOUR CODE HERE
    color = {'R': 0, 'G': 1, 'B': 2}
    out = np.array(image)
    out[:, :, color[channel]] = 0
    # END YOUR CODE

    return out


def lab_decomposition(image, channel):
    """ Return image decomposed to just the lab channel specified

    Args:
        image: numpy array of shape(image_height, image_width, 3)
        channel: str specifying the channel

    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """

    lab = color.rgb2lab(image)
    out = None

    # YOUR CODE HERE
    color_dict = {'l': 0, 'a': 1, 'b': 2}
    out = (lab + np.abs(np.min(lab)))
    out = out / np.max(lab)
    out[:, :, color_dict[channel.lower()]] = 0
    # END YOUR CODE

    return out


def hsv_decomposition(image, channel='H'):
    """ Return image decomposed to just the hsv channel specified

    Args:
        image: numpy array of shape(image_height, image_width, 3)
        channel: str specifying the channel

    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """

    hsv = color.rgb2hsv(image)
    out = None

    # YOUR CODE HERE
    color_dict = {'h': 0, 's': 1, 'v': 2}
    hsv[:, :, color_dict[channel.lower()]] = 0
    out = hsv
    # END YOUR CODE

    return out


def mix_images(image1, image2, channel1, channel2):
    """ Return image which is the left of image1 and right of image 2 excluding
    the specified channels for each image

    Args:
        image1: numpy array of shape(image_height, image_width, 3)
        image2: numpy array of shape(image_height, image_width, 3)
        channel1: str specifying channel used for image1
        channel2: str specifying channel used for image2

    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """

    out = None
    # YOUR CODE HERE
    out = np.zeros_like(image1)
    _, image_width, _ = image1.shape
    image1 = rgb_decomposition(image1, channel1)
    image2 = rgb_decomposition(image2, channel2)
    out[:, :image_width // 2] = image1[:, :image_width // 2]
    out[:, image_width // 2:] = image2[:, image_width // 2:]
    # END YOUR CODE

    return out
