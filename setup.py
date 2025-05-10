# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

import setuptools

install_requires=['algorithm']
setuptools.setup(
    name=install_requires[0],
    version='1.0',
    author='Mostafa Algorithm',
    author_email='mostafa.algorithm@gmail.com',
    packages=setuptools.find_packages(),
    python_requires='>=3.6'
)