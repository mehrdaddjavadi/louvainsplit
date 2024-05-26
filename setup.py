from setuptools import setup, find_packages

setup(
    name='louvainsplit',
    version='0.1.0',
    description='Efficient graph partitioning using LouvainSplit algorithm',
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
