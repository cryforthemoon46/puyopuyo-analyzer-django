from typing import Dict, List

from ..board import Board
from ..service import *


class ChainAnalysisUseCase:
    def __init__(self, board_areas: List[Dict], captured_image_data: str):
        """
        :param board_areas: 盤面領域
        :param captured_image_data: キャプチャ画面データ (base64)
        """
        self._board_areas = board_areas
        self._captured_image_data = captured_image_data

    def make_boards(self) -> List[Board]:
        """
        :return boards: 盤面クラスを格納したリスト
        """
        captured_image = image_data_to_image(self._captured_image_data)
        boards = []
        for board_area in self._board_areas:
            board_image = trim_image(captured_image, board_area["xmin"],
                                     board_area["ymin"], board_area["xmax"],
                                     board_area["ymax"])
            board_array = board_image_to_array(board_image)
            board = Board(board_array)
            boards.append(board)
        return boards

    def calc_chain(self, boards: List[Board]):
        """
        :param boards:
        :return:
        """
        for board in boards:
            board.get_chain_array()