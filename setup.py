import setuptools

with open("README.md", "r" ,encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="newlandface_r",
    version="0.1",
    author="krishuang",
    author_email="huangzikun2008@hotmail.com",
    description="修改了fjndfazp/newlandface的默认home路径问题等 ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krishuang2008/newlandface_r",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=[
    'numpy>=1.14.0',
    'pandas>=0.23.4',
    'gdown>=3.10.1',
    'tqdm>=4.30.0',
    'Pillow>=5.2.0',
    'opencv-python>=3.4.4',
    'tensorflow>=1.9.0',
    'keras>=2.2.0',
    'Flask>=1.1.2',
    'mtcnn>=0.1.0',
    'dlib',
    'gdown'
    ]
)