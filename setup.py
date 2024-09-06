from setuptools import setup, find_packages

setup(
    name='calcutool',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'sympy',
    ],
    description='A simple Python package for integration and differentiation using sympy.',
    author='Suraj Powar',
    author_email='suraj91096atgmail.com',
    url='https://github.com/surajpowar/calcutool',  #
)
