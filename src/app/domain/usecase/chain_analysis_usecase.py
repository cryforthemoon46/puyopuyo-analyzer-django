from typing import Dict, List

class ChainAnalysisUseCase:
    def __init__(self, board_areas: List[Dict], captured_image_data: str):
        """
        :param board_areas: 盤面領域
        :param captured_image_data: キャプチャ画面データ (base64)
        """
        self._board_areas = board_areas
        self._captured_image_data = captured_image_data

