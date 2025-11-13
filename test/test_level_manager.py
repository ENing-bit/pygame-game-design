import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tempfile
import csv
import pytest
from gameObject.level_manager import LevelManager

def create_temp_level_file(tmpdir, width=5, height=3, map_data=None, filename="level1.csv"):
    file_path = os.path.join(tmpdir, filename)
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([width])
        writer.writerow([height])
        if map_data is None:
            map_data = [
                [1, 0, 0, 1, 1],
                [0, 1, 1, 0, 0],
                [1, 1, 0, 0, 1]
            ]
        for row in map_data:
            writer.writerow(row)
    return file_path

def test_load_level_success(tmp_path):
    file_path = create_temp_level_file(tmp_path)
    manager = LevelManager()
    level = manager.load_level(str(file_path))
    assert level.width == 5
    assert level.height == 3
    assert level.level_name == os.path.basename(file_path)
    assert level.map_data == [
        [1, 0, 0, 1, 1],
        [0, 1, 1, 0, 0],
        [1, 1, 0, 0, 1]
    ]

def test_load_level_file_not_exist():
    manager = LevelManager()
    with pytest.raises(Exception) as excinfo:
        manager.load_level("not_exist_file.csv")
    assert "读取关卡文件失败" in str(excinfo.value)

def test_load_levels(tmp_path):
    # 创建多个关卡文件
    create_temp_level_file(tmp_path, filename="level1.csv")
    create_temp_level_file(tmp_path, filename="level2.csv")
    manager = LevelManager()
    manager.load_levels(str(tmp_path))
    assert len(manager.level_list) == 2
    names = [level.level_name for level in manager.level_list]
    assert "level1.csv" in names
    assert "level2.csv" in names
