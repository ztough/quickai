import sys
from PySide6.QtWidgets import QApplication, QWidget, QToolButton, QMenu,QSizePolicy
from PySide6.QtGui import QIcon,QShowEvent,QAction,QCursor
from ui_form_2 import Ui_Form
from PySide6.QtCore import QSettings,Signal, Slot,QTimer
from PySide6.QtCore import Qt,QPoint,QSize, QEvent
import ctypes
from ctypes import wintypes
import json
from interact_signal import global_signal_instance
import keyboard
from functools import partial
from pynput.keyboard import Controller, Key

user32 = ctypes.windll.user32

SW_HIDE = 0
SW_SHOW = 5
GWL_EXSTYLE = -20
WS_EX_NOACTIVATE = 0x08000000
WS_EX_APPWINDOW = 0x00040000

class action(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("img/logo.png"))
        self.settings = QSettings("QuickAi", "Settings")
        #flags = Qt.Tool | Qt.FramelessWindowHint| Qt.WindowStaysOnTopHint
        flags = Qt.Tool  |Qt.CustomizeWindowHint| Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        self.m_dragging = False
        self.m_dragPos = QPoint()
        self.restoreWindowState()
    def showEvent(self, event: QShowEvent) -> None:
        hwnd = self.winId()
        ex_style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        user32.SetWindowLongW(hwnd, GWL_EXSTYLE, ex_style | WS_EX_NOACTIVATE | WS_EX_APPWINDOW)
        super().showEvent(event)
    def restoreWindowState(self):
            if self.settings.contains("action_pos"):
                pos = self.settings.value("action_pos", QPoint())
                self.move(pos)
            if self.settings.contains("action_size"):
                size = self.settings.value("action_size", QPoint())
                self.resize(size)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_dragging = True
            self.m_dragPos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if self.m_dragging:
            self.move(event.globalPos() - self.m_dragPos)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_dragging = False
            event.accept()
    def moveEvent(self, event):
        self.settings.setValue("action_pos", self.pos())
        event.accept()

    def resizeEvent(self, event):
        self.settings.setValue("action_size", self.size())
        event.accept()
    def simulate_ctrl_c(self):
        keyboard = Controller()
        with keyboard.pressed(Key.ctrl):
            keyboard.press('c')
            keyboard.release('c')
    def option_click(self):
        self.simulate_ctrl_c()
        action = self.sender()
        QTimer.singleShot(100,lambda:global_signal_instance.interact.emit(action.text(),self.settings.value("model",0)))
    def on_hotkey(self,text):
        self.simulate_ctrl_c()
        QTimer.singleShot(100,lambda:global_signal_instance.interact.emit(text,self.settings.value("model",0)))
    def clear_layout(self,layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    class NoActivateMenu(QMenu):
        def __init__(self,parent=None):
            super().__init__(parent)
        def showEvent(self,event: QShowEvent) -> None:
            hwnd = self.winId()
            ex_style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            user32.SetWindowLongW(hwnd, GWL_EXSTYLE, ex_style | WS_EX_NOACTIVATE)
            super().showEvent(event)
        # def leaveEvent(self, event):
        #     self.hide()
        #     super().leaveEvent(event)
    class ExpandableToolButton(QToolButton):
        def __init__(self, parent=None):
            super().__init__(parent)
        def enterEvent(self, event):
            super().enterEvent(event)
            self.showMenu()

        def showMenu(self):
            #event = QEvent(QEvent.Enter)
            #QApplication.sendEvent(self.menu(), event)
            menu_pos = self.mapToGlobal(self.rect().bottomLeft())
            menu_center = QPoint(menu_pos.x() + 20, menu_pos.y() + 15)
            QCursor.setPos(menu_center)
            self.menu().exec(self.mapToGlobal(self.rect().bottomLeft()))
    def menu(self):
        self.clear_layout(self.ui.verticalLayout)
        category = json.loads(self.settings.value("category","[]"))
        for i in category:
            tool_button = QToolButton()
            tool_button.setText(i)
            tool_button.setFixedHeight(30)
            tool_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            menu = self.NoActivateMenu(tool_button)
            prompt= json.loads(self.settings.value(i,"[]"))
            for j,k in prompt:
                action = QAction(j, self)
                action.triggered.connect(self.option_click)
                menu.addAction(action)
                if k!="":
                    callback_with_args = partial(self.on_hotkey, j)
                    keyboard.add_hotkey(k,callback_with_args)
            tool_button.setMenu(menu)
            tool_button.setPopupMode(QToolButton.InstantPopup)
            self.ui.verticalLayout.addWidget(tool_button)
