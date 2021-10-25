from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="cavl",
    version="0.4.1",
    author="Justin Doornbos",
    author_email="jstndevel@gmail.com",
    url="https://github.com/jstnd/cavl",
    license="MIT",
    description="A simple library for visualizing cellular automata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=["matplotlib >= 3.4.3", "numpy >= 1.21.2"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
)
