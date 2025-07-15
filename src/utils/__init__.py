"""
项目工具模块
Project utilities module
"""

def greet_user(name: str) -> str:
    """
    生成问候语
    Generate greeting message
    """
    return f"你好, {name}! 欢迎使用这个项目。"

def get_project_info() -> dict:
    """
    获取项目信息
    Get project information
    """
    return {
        "name": "repo-070",
        "version": "1.0.0",
        "description": "基础 Abstra 项目实现"
    }