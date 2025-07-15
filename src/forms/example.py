"""
示例表单 - 展示如何扩展项目
Example form - demonstrating how to extend the project
"""

import sys
import os

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import abstra.forms as st
from src.utils import get_project_info

def example_form():
    """示例表单功能"""
    st.title("示例功能演示")
    
    # 用户信息收集
    st.subheader("用户信息")
    
    user_name = st.text_input("姓名:")
    user_age = st.number_input("年龄:", min_value=1, max_value=120, value=25)
    user_city = st.selectbox("城市:", ["北京", "上海", "广州", "深圳", "其他"])
    
    if st.button("提交信息"):
        if user_name:
            st.success("信息提交成功!")
            
            # 显示收集的信息
            st.subheader("收集的信息:")
            st.write(f"**姓名:** {user_name}")
            st.write(f"**年龄:** {user_age}")
            st.write(f"**城市:** {user_city}")
            
            # 项目信息
            project_info = get_project_info()
            st.divider()
            st.caption(f"由 {project_info['name']} v{project_info['version']} 提供支持")
        else:
            st.error("请输入姓名!")

if __name__ == "__main__":
    example_form()