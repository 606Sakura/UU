
#### 5. setup.py （可选，让项目可 pip install）

from setuptools import setup, find_packages

setup(
    name="probability-simulation-toolkit",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "matplotlib>=3.8.0",
        "numpy>=1.24.0",
    ],
    author="Your Name",
    description="A toolkit for probability simulations",
    python_requires=">=3.8",
)