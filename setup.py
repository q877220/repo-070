from setuptools import setup, find_packages

setup(
    name="repo-070",
    version="1.0.0",
    description="基础 Abstra 项目实现",
    author="元芳",
    author_email="",
    packages=find_packages(),
    install_requires=[
        "abstra",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)