from setuptools import setup, find_packages

setup(
    name='pyqt-common-tab-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QTabWidget which is the most common type. '
                'This has a lot of common feature such as close tab, close tabs to the left/right, '
                'close other tabs and so on.',
    url='https://github.com/yjg30737/pyqt-common-tab-widget.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)