from typing import List

import numpy as np
from collections import deque

from pprint import pprint

class Board:
    def __init__(self, array: List[List]):
        """
        :param array: 盤面の状態を表す配列
        """
        self._array = array

    def get_chain_array(self):
        """
        連鎖数を計算した配列を返す
        :return:
        """
        chain_array = np.zeros((12, 6), dtype=int)
        visited = [[False] * 6 for i in range(12)]
        for i in range(12):
            for j in range(6):
                if not self.is_trigger(i, j, visited):
                    continue

                connected_puyo, visited = self.get_connected_puyo(i, j, visited)
                print(connected_puyo)

    def is_trigger(self, y: int, x: int, visited: List[List[bool]]) -> bool:
        # 探索済の場合Falseを返す
        if visited[y][x]:
            return False
        visited[y][x] = True

        # 空かおじゃまぷよの場合Falseを返す
        target_puyo = self._array[y][x]
        if target_puyo == "-" or target_puyo == "N":
            return False

        # 上左右にぷよを置けない場合Falseを返す
        for ny, nx in [(y - 1, x), (y, x - 1), (y, x + 1)]:
            # 探索範囲外であれば処理を飛ばす
            if nx < 0 or nx > 5 or ny < 0 or ny > 11:
                continue
            # ぷよを置ける場合はTrueを返す
            if self._array[ny][nx] == "-":
                return True
        return False
                
    def get_connected_puyo(self, y:int, x:int, visited:List[List[bool]]):
        """
        連結しているぷよのリストを返す
        :param y:
        :param x:
        :return connected_puyo_lst:
        """
        connected_puyo_lst = [[y, x]]
        target_puyo = self._array[y][x]
        queue = deque([[y, x]])
        while len(queue) > 0:
            cy, cx = queue.popleft()
            for ny, nx in [(cy - 1, cx), (cy, cx + 1), (cy + 1, cx), (cy, cx - 1)]:
                if nx < 0 or nx > 5 or ny < 0 or ny > 11:
                    continue

                # 探索済の場合処理を飛ばす
                if visited[ny][nx]:
                    continue
                visited[ny][nx] = True

                # 隣のぷよが同色でない場合処理を飛ばす
                if self._array[ny][nx] != target_puyo:
                    continue

                connected_puyo_lst.append([ny, nx])
                queue.append([ny, nx])
        return connected_puyo_lst, visited