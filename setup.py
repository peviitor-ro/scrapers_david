from setuptools import setup, find_packages

setup(
    name='scraper_david',
    version='0.0.1',
    description='A simple scraper',
    url="",
    author='David Mondoc',

    packages=find_packages(),

    install_requires=[
        'peviitor_pyscraper',
    ],
    python_requires='>=3.6',
)