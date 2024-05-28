from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='louvainsplit',
    version='0.2.0.3',
    description='Efficient graph partitioning using LouvainSplit algorithm',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mehrdad Javadi',
    author_email='mehrdaddjavadi@gmail.com',
    url='https://github.com/mehrdaddjavadi/louvainsplit',
    packages=find_packages(),
    install_requires=[
        'torch',
        'networkx',
        'numpy',
        'python-louvain',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
