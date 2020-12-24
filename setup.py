
from setuptools import find_packages, setup

setup(
    name="template",
    version="1.0.0",
    description="template code",
    license="MIT License",
    author="Yuto Watanabe",
    url="https://github.com/yuto51942/python-template",
    install_requires=[],
    packages=find_packages("src"),
    # entry_points={
    #     'console_scripts': [
    #         'name = src.main:sample',
    #     ],
    # },
)
