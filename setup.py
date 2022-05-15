import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-tab-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_tab_widget.ico': ['close.svg'],
                  'pyqt_tab_widget.style': ['tab_widget.css']},
    description='PyQt QTabWidget which is the most common type. '
                'This has a lot of common features such as close a tab, close tabs to the left/right, '
                'close other tabs and so on.',
    url='https://github.com/yjg30737/pyqt-tab-widget.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.8'
    ]
)