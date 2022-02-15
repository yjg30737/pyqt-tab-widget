# pyqt-common-tab-widget
PyQt ```QTabWidget``` which is the most common type (if you doubt it, see the 'feature' section below). This has a lot of common features such as close a tab, close tabs to the left/right, close other tabs and so on.

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-common-tab-widget.git --upgrade```

## Feature
* List which is able to do with context menu
  * close a tab
  * close tabs to the left
  * close tabs to the right
  * close other tabs
  * close all tabs
  * reopen closed tab
* Alt+Left to change the current tab to the very left tab
* Alt+Right to change the current tab to the very right tab
* Ctrl+F4 to close current tab
* Close any tabs with clicking the close button (close button's style is defaut, i will customize it)

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from pyqt_common_tab_widget import CommonTabWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        tabWidget = CommonTabWidget()
        tabWidget.addTab(QWidget(), 'A')
        tabWidget.addTab(QWidget(), 'B')
        tabWidget.addTab(QWidget(), 'C')
        tabWidget.addTab(QWidget(), 'D')
        tabWidget.addTab(QWidget(), 'E')
        self.setCentralWidget(tabWidget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
```

Result

![image](https://user-images.githubusercontent.com/55078043/153697769-5134c02a-9cb8-4759-ae8a-53caae219659.png)

