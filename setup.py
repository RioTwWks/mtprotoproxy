#!/usr/bin/env python3
"""
Setup script for mtprotoproxy
"""

from setuptools import setup, find_packages
import os

# Read README if available
readme = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()

setup(
    name="mtprotoproxy",
    version="1.0.0",
    description="Fast and simple to setup MTProto proxy written in Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="RioTwWks",
    author_email="",
    url="https://github.com/RioTwWks/mtprotoproxy",
    py_modules=["mtprotoproxy"],
    python_requires=">=3.7",
    install_requires=[
        "cryptography>=41.0.0",
        "pyaes>=1.3.0",
    ],
    extras_require={
        "performance": [
            "uvloop>=0.19.0; sys_platform != 'win32'",
        ],
    },
    entry_points={
        "console_scripts": [
            "mtprotoproxy=mtprotoproxy:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)

