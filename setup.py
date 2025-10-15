from setuptools import setup, find_packages

setup(
    name="sphero_z_nb",
    version="0.1.0",
    description="Navigation Ball: Extended Sphero API for BLE control",
    author="Jinwoo Lee",
    packages=find_packages(),
    install_requires=[
        "bleak",
        "spherov2",
        "sphero_unsw"
    ],
    python_requires=">=3.9",
)
