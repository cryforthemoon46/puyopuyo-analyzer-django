from typing import List

import base64
import cv2
import numpy as np

from .puyo import Puyo


# TODO 位置がおかしい
def convert_for_zncc(puyo_image: np.ndarray) -> np.ndarray:
    puyo_image = cv2.resize(puyo_image, (PUYO_SIZE, PUYO_SIZE))
    puyo_image = np.array(puyo_image, dtype="float")
    return puyo_image - np.mean(puyo_image)


PUYO_SIZE = 20

TEMPLATES = {
    "R": convert_for_zncc(cv2.imread("./static/puyo_r.jpg")),
    "G": convert_for_zncc(cv2.imread("./static/puyo_g.jpg")),
    "B": convert_for_zncc(cv2.imread("./static/puyo_b.jpg")),
    "Y": convert_for_zncc(cv2.imread("./static/puyo_y.jpg")),
    "P": convert_for_zncc(cv2.imread("./static/puyo_p.jpg")),
    "N": convert_for_zncc(cv2.imread("./static/puyo_n.jpg")),
}

THRESHOLD = 0.6


def image_data_to_image(image_data: str) -> np.ndarray:
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


# TODO boardクラス内に移動するべきか検討
def board_image_to_array(image: np.ndarray) -> List[List[Puyo]]:
    """
    :param image: 盤面の画像
    :return: 盤面の配列
    """
    height, width = image.shape[:2]
    puyo_height, puyo_width = height / 12, width / 6
    array = []
    for i in range(0, 12):
        row = []
        for j in range(0, 6):
            xmin = round(puyo_width * j)
            ymin = round(puyo_height * i)
            xmax = round(puyo_width * (j + 1))
            ymax = round(puyo_height * (i + 1))
            puyo_image = trim_image(image, xmin, ymin, xmax, ymax)
            puyo_image = convert_for_zncc(puyo_image)
            row.append(infer_puyo_type(puyo_image))
        array.append(row)
    return array


def infer_puyo_type(puyo_image: np.ndarray) -> str:
    """
    :param puyo_image: ぷよの画像
    :return puyo_type: 推論されたぷよの種類を表す文字列
    """
    infered_puyo_type = "-"
    max_zncc = THRESHOLD
    for puyo_type, template_image in TEMPLATES.items():
        zncc = calc_zncc(puyo_image, template_image)
        if zncc > max_zncc:
            infered_puyo_type = puyo_type
            max_zncc = zncc
    return infered_puyo_type


def calc_zncc(puyo_image: np.ndarray, template_image: np.ndarray) -> float:
    """
    :param puyo_image: ぷよ画像
    :param template_image: テンプレート画像
    :return: 2つの画像の類似度 (ZNCC)
    """
    puyo_image -= np.mean(puyo_image)
    puyo_image = cv2.resize(puyo_image, (PUYO_SIZE, PUYO_SIZE))
    puyo_image = np.array(puyo_image, dtype="float")
    numerator = np.sum(puyo_image * template_image)
    denominator = np.sqrt(np.sum(puyo_image ** 2)) * np.sqrt(
        np.sum(template_image ** 2))
    return numerator / denominator
