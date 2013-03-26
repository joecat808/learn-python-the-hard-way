try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'A Text Adventure Game',
        'author': 'King Zeng',
        'url': 'https://github.com/kingnez/my-hard-way',
        'download_url': 'http://github.com/kingnez/my-hard-way.git',
        'author_email': 'king.fudan@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['myhardway'],
        'scripts': [],
        'name': 'my-hard-way'
}

setup(**config)
