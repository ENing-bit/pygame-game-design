from gameObject.level_loader import LevelLoader
from typing import List
import os
import csv

class Level:
    def __init__(self):
        self.level_number:int
        self.level_name:str = "未命名"
        self.file_path:str
        self.width = 0
        self.height = 0
        self.map_data = []
        self.is_open_roll:bool = True
        self.is_open_fall:bool = True

class LevelManager:
    def __init__(self):
        self.level_list:List[Level] = None

    def select_level(self,level_number:int)->Level:
        if self.level_list:
            return self.level_list[level_number]
        else:
            raise Exception("未读取关卡")
        pass

    def load_levels(self, floder_path:str):
        # 先打开文件夹，记录文件夹中都有哪些文件，几个文件
        file_names = [f for f in os.listdir(floder_path) if os.path.isfile(os.path.join(floder_path, f))]
        # 使用level_loader将每个文件读取进level_list
        self.level_list = []
        for file_name in file_names:
            file_path = os.path.join(floder_path, file_name)
            level = self.load_level(file_path)
            self.level_list.append(level)

    def load_level(self, file_path) -> Level:
        """
        从文件中加载关卡数据，返回Level对象。
        """
        try:
            with open(file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                rows = list(reader)

                level = Level()
                level.file_path = file_path
                level.level_name = os.path.basename(file_path)  # 读取文件名作为关卡名
                level.width = int(rows[0][0])   # 第一行第一列是宽度
                level.height = int(rows[1][0])  # 第二行第一列是高度
                level.map_data = [
                    list(map(int, row))
                    for row in rows[2:] if row  # 跳过空行
                ]
                # 可根据需要设置level_number等属性
                return level
        except Exception as e:
            print(f"读取关卡文件失败: {file_path}, 错误信息: {e}")
            raise Exception(f"读取关卡文件失败: {file_path}, 错误信息: {e}")