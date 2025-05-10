from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="algorithm",
    version="2.0.1",
    author="Mostafa Algorithm",
    author_email="mostafa.algorithm@gmail.com",
    description="Advanced algorithm and utility library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mostafa-Algorithm/algorithm-lib",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.28.1",
        "validators>=0.20.0",
        "netifaces>=0.11.0",
        "pyfiglet>=0.8.post1",
        "progress>=1.6",
        "alive-progress>=3.0.1",
        "progressbar2>=4.0.0",
        "psutil>=5.9.4",
        "getmac>=0.8.3",
        "speedtest-cli>=2.1.3",
        "fake-email>=0.1.1",
        "scapy>=2.5.0",
        "dnspython>=2.3.0",
        "pyftpdlib>=1.5.7",
        "selenium>=4.0.0",
        "undetected-chromedriver>=3.1.0",
        "webdriver-manager>=3.8.0",
        "paramiko>=3.1.0",
        "pywin32>=305; sys_platform == 'win32'",
    ],
    extras_require={
        "dev": [
            "pytest>=7.2.2",
            "pytest-cov>=4.0.0",
            "mypy>=1.0.1",
            "flake8>=6.0.0",
            "black>=23.1.0",
            "isort>=5.12.0",
            "sphinx>=6.1.3",
            "twine>=4.0.2",
        ],
    },
    keywords="algorithm utilities networking strings threading webdriver",
    project_urls={
        "Source": "https://github.com/Mostafa-Algorithm/algorithm-lib",
    },
)