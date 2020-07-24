import base64
import cv2
import numpy as np


def image_data_to_ndarray(image_data: str) -> np.ndarray:
    """
    :param image_data:
    :return image_ndarray:
    """
    image_data = base64.b64decode(image_data.split(',')[1])
    image_ndarray = np.fromstring(image_data, np.uint8)
    image_ndarray = cv2.imdecode(image_ndarray, cv2.IMREAD_ANYCOLOR)
    return image_ndarray


def trim_image(image: np.ndarray, xmin: int, ymin: int, xmax: int,
               ymax: int) -> np.ndarray:
    """
    :param image:
    :param xmin:
    :param ymin:
    :param xmax:
    :param ymax:
    :return: 
    """
    return image[ymin:ymax, xmin:xmax]
