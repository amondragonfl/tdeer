from setuptools import setup, find_packages

setup(
    name='tdeer',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tdeer = tdeer.main:main', 
        ],
    },
    install_requires=[
        'numpy',  
        'scikit-learn',  
    ],
)