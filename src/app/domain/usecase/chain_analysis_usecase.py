from typing import Dict, List

from ..service import *


class ChainAnalysisUseCase:
    def __init__(self, board_areas: List[Dict], captured_image_data: str):
        """
        :param board_areas: 盤面領域
        :param captured_image_data: キャプチャ画面データ (base64)
        """
        self._board_areas = board_areas
        self._captured_image_data = captured_image_data

    def make_boards(self):
        captured_image = image_data_to_ndarray(self._captured_image_data)
        boards = []
        for board_area in self._board_areas:
            board_image = trim_image(captured_image, board_area["xmin"],
                                     board_area["ymin"], board_area["xmax"],
                                     board_area["ymax"])

            # boards.append(board_image)
        return
