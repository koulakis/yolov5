import setuptools


setuptools.setup(
    name="yolov5",
    version="0.0.1",
    description="An installable version of yolov5 forked from https://github.com/ultralytics/yolov5.",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent - Tested on Ubuntu 18.04",
    ],
    install_requires=[
        "matplotlib>=3.2.2",
        "numpy>=1.18.5",
        "opencv-python>=4.1.2",
        "Pillow",
        "PyYAML>=5.3.1",
        "scipy>=1.4.1",
        "torch>=1.7.0",
        "torchvision>=0.8.1",
        "tqdm>=4.41.0",
        "tensorboard>=2.4.1",
        "seaborn>=0.11.0",
        "pandas",
        "thop"
    ],
    python_requires='>=3.7.*',
)
