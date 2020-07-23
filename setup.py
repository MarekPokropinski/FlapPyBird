from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='FlapPyBird_Env',
    version='0.1',
    author='Marek Pokropiński',
    author_email='marek.pokropinski@outlook.com',
    description='Flappy Bird Environment for Gym',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarekPokropinski/FlapPyBird",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    # data_files=[
    #     ('assets/sprites', ['assets/sprites/*.png']),
    #     ('', ['flappy.ico']),
    # ],
    # packages=['FlapPyBird_Env'],
    package_dir={'FlapPyBird_Env':'FlapPyBird_Env'},
    package_data={'FlapPyBird_Env':['assets/sprites/*.png']}
)