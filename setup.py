from setuptools import find_packages, setup

setup(
    name="probability-simulation-toolkit",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Your Name",
    description="A toolkit for probability simulations",
    python_requires=">=3.8",
)
