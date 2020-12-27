
from setuptools import find_packages, setup

setup(
    name="unchi",
    version="1.0.1",
    description="Set the noun of the sentence on the clipboard to うんち.",
    license="MIT License",
    author="Yuto Watanabe",
    url="https://github.com/yuto51942/unchi-maker",
    install_requires=[
        "pyperclip",
        "janome"
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cp-unchi = unchi.main:main',
        ],
    },
)
