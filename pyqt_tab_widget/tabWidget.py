from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QTabWidget, QAction, QMenu


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.__context_menu_p = 0
        self.__initLastRemovedTabInfo()
        self.__initUi()

    def __initLastRemovedTabInfo(self):
        self.__last_removed_tab_idx = []
        self.__last_removed_tab_widget = []
        self.__last_removed_tab_title = []

    def __initUi(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.__prepareMenu)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.removeTab)

    def __prepareMenu(self, p):
        tab_idx = self.tabBar().tabAt(p)
        if tab_idx != -1:
            self.__context_menu_p = p
            closeTabAction = QAction('Close Tab')
            closeTabAction.triggered.connect(self.closeTab)

            closeAllTabAction = QAction('Close All Tabs')
            closeAllTabAction.triggered.connect(self.closeAllTab)

            closeOtherTabAction = QAction('Close Other Tabs')
            closeOtherTabAction.triggered.connect(self.closeOtherTab)

            closeTabToTheLeftAction = QAction('Close Tabs to the Left')
            closeTabToTheLeftAction.triggered.connect(self.closeTabToLeft)

            closeTabToTheRightAction = QAction('Close Tabs to the Right')
            closeTabToTheRightAction.triggered.connect(self.closeTabToRight)

            reopenClosedTabAction = QAction('Reopen Closed Tab')
            reopenClosedTabAction.triggered.connect(self.reopenClosedTab)

            menu = QMenu(self)
            menu.addAction(closeTabAction)
            menu.addAction(closeAllTabAction)
            menu.addAction(closeOtherTabAction)
            menu.addAction(closeTabToTheLeftAction)
            menu.addAction(closeTabToTheRightAction)
            menu.addAction(reopenClosedTabAction)
            menu.exec(self.mapToGlobal(p))

    def removeTab(self, idx):
        self.__saveLastRemovedTabInfo(idx)
        return super(TabWidget, self).removeTab(idx)

    def __saveLastRemovedTabInfo(self, idx):
        self.__last_removed_tab_idx.append(idx)
        self.__last_removed_tab_widget.append(self.widget(idx))
        self.__last_removed_tab_title.append(self.tabText(idx))

    def keyPressEvent(self, e):
        if e.modifiers() & Qt.AltModifier and e.key() == Qt.Key_Left:
            self.setCurrentIndex(self.currentIndex()-1)
        elif e.modifiers() & Qt.AltModifier and e.key() == Qt.Key_Right:
            self.setCurrentIndex(self.currentIndex()+1)
        elif e.modifiers() & Qt.ControlModifier and e.key() == Qt.Key_F4:
            self.closeTab()
        return super().keyPressEvent(e)

    def closeTab(self):
        if isinstance(self.__context_menu_p, QPoint):
            tab_idx = self.tabBar().tabAt(self.__context_menu_p)
            self.removeTab(tab_idx)
            self.__context_menu_p = 0
        else:
            self.removeTab(self.currentIndex())

    def closeAllTab(self):
        self.clear()

    def closeOtherTab(self):
        if isinstance(self.__context_menu_p, QPoint):
            tab_idx = self.tabBar().tabAt(self.__context_menu_p)
            self.__removeTabFromLeftTo(tab_idx)
            tab_idx = 0
            self.setCurrentIndex(tab_idx)
            self.__removeTabFromRightTo(tab_idx)

    def closeTabToLeft(self):
        if isinstance(self.__context_menu_p, QPoint):
            tab_idx = self.tabBar().tabAt(self.__context_menu_p)
            self.__removeTabFromLeftTo(tab_idx)

    def __removeTabFromLeftTo(self, idx):
        for i in range(idx - 1, -1, -1):
            self.removeTab(i)

    def __removeTabFromRightTo(self, idx):
        for i in range(self.count()-1, idx, -1):
            self.removeTab(i)

    def closeTabToRight(self):
        if isinstance(self.__context_menu_p, QPoint):
            tab_idx = self.tabBar().tabAt(self.__context_menu_p)
            self.__removeTabFromRightTo(tab_idx)

    def reopenClosedTab(self):
        # todo enable/disable action dynamically by existence of closed tab
        if len(self.__last_removed_tab_idx) > 0:
            for i in range(len(self.__last_removed_tab_idx)-1, -1, -1):
                self.insertTab(self.__last_removed_tab_idx[i],
                               self.__last_removed_tab_widget[i],
                               self.__last_removed_tab_title[i])
            self.setCurrentIndex(self.__last_removed_tab_idx[-1])
            self.__initLastRemovedTabInfo()

