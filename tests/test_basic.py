"""
项目基础测试
Basic project tests
"""

import sys
import os
import unittest

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import greet_user, get_project_info


class TestProjectBasics(unittest.TestCase):
    """基础项目功能测试"""
    
    def test_greet_user(self):
        """测试用户问候功能"""
        result = greet_user("测试用户")
        self.assertIn("测试用户", result)
        self.assertIn("你好", result)
    
    def test_get_project_info(self):
        """测试项目信息获取"""
        info = get_project_info()
        self.assertIsInstance(info, dict)
        self.assertIn("name", info)
        self.assertIn("version", info)
        self.assertIn("description", info)
        self.assertEqual(info["name"], "repo-070")
    
    def test_project_structure(self):
        """测试项目结构"""
        # 检查主要文件是否存在
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        essential_files = [
            "main.py",
            "abstra.json",
            "requirements.txt",
            "setup.py"
        ]
        
        for file_name in essential_files:
            file_path = os.path.join(project_root, file_name)
            self.assertTrue(os.path.exists(file_path), f"文件 {file_name} 不存在")


if __name__ == "__main__":
    unittest.main()