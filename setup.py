from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.1'
DESCRIPTION = 'Este paquete solo tiene como finalidad retornar los nombres de los personajes de harry potter con sus respectivas casas.'
PACKAGE_NAME = 'yonier_harrypotter'
AUTHOR = 'Yonier Gomez'
EMAIL = 'yonieer13@gmail.com'
GITHUB_URL = 'https://github.com/YonierGomez/yonier_harrypotter'

setup(
    name = PACKAGE_NAME,
    packages = [DESCRIPTION],
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = ["Harry Potter", "Harry", "Potter", "Gryffindor", "Slytherin"],
    install_requires=[ 
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)