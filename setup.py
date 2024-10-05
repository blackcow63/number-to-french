from setuptools import setup, find_packages

setup(
    name="number_to_french",
    version="0.1.0",
    description="A package to convert numbers to their French word equivalents",
    author="Zofia Smolen",
    author_email="zofsmolen@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
