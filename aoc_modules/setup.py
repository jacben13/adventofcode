from setuptools import setup, find_packages

setup(
    name="aoc_modules",  # The name you'll use for 'pip install'
    version="0.1.0",
    packages=find_packages(),   # Automatically finds folders with __init__.py
    install_requires=[],        # List any external dependencies here
    python_requires=">=3.8",
)