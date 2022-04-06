from setuptools import setup, find_packages

setup(
    name='pyqt-tab-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QTabWidget which is the most common type. '
                'This has a lot of common features such as close a tab, close tabs to the left/right, '
                'close other tabs and so on.',
    url='https://github.com/yjg30737/pyqt-tab-widget.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)