"""
基础 Abstra 项目主入口
Main entry point for basic Abstra project
"""

import sys
import os

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import abstra.forms as st
from src.utils import greet_user, get_project_info

# 获取项目信息
project_info = get_project_info()

# 主页面
st.title(f"欢迎使用 {project_info['name']}")
st.write(f"版本: {project_info['version']}")
st.write(f"描述: {project_info['description']}")

st.divider()

# 用户交互
st.subheader("用户交互演示")
name = st.text_input("请输入您的姓名:", placeholder="输入您的名字")

if name:
    greeting = greet_user(name)
    st.success(greeting)
    st.balloons()
    
    # 显示额外信息
    st.info("项目已成功启动和运行！")
    
    # 项目状态
    st.subheader("项目状态")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("当前版本", project_info['version'])
    
    with col2:
        st.metric("状态", "运行中", delta="正常")