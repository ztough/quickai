import sys
import os
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon,QClipboard
from ui_form_3 import Ui_Form
from PySide6.QtCore import QSettings
from PySide6.QtCore import Qt,QPoint,QSize,QTimer
from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEngineSettings,QWebEnginePage
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QObject, Slot, Signal, QUrl
from interact_signal import global_signal_instance
from pynput.keyboard import Controller, Key
import ctypes
user32 = ctypes.windll.user32
class Backend(QObject):
    message_received = Signal(str)

    @Slot(str)
    def send_message(self, message):
        print(f"Message from Web: {message}")
        self.message_received.emit(f"Received: {message}")
class web(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        flags = Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        self.setWindowIcon(QIcon("img/logo.png"))
        self.settings = QSettings("QuickAi", "Settings")
        self.restoreWindowState()
        current_path = os.getcwd()
        self.profile = QWebEngineProfile("Chromeium",self.ui.webEngineView)
        self.profile.setCachePath(os.path.join(current_path, "cache"))
        self.profile.setPersistentStoragePath(os.path.join(current_path, "persistent_storage"))
        self.profile.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies)
        self.ui.webEngineView.setPage(QWebEnginePage(self.profile, self.ui.webEngineView))
        self.backend = Backend()
        self.channel = QWebChannel()
        self.channel.registerObject("backend", self.backend)
        self.ui.webEngineView.page().setWebChannel(self.channel)
        self.backend.message_received.connect(self.on_message_received)
        global_signal_instance.interact.connect(self.ai)
    @Slot(str)
    def on_message_received(self, message):
        pass
    def simulate_ctrl_v(self):
        keyboard = Controller()
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')
    def simulate_ctrl_c(self):
        keyboard = Controller()
        with keyboard.pressed(Key.ctrl):
            keyboard.press('c')
            keyboard.release('c')
    def simulate_enter(self):
        keyboard = Controller()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def ai(self,text,index):
        hwnd = user32.GetForegroundWindow()
        if not self.isVisible():
            self.open_ai(self.settings.value("model",0))
        clipboard = QApplication.clipboard()
        if index==0:
            script = '''
            var element = document.querySelector('#prompt-textarea');
                   element.focus()
                   '''
            self.ui.webEngineView.page().runJavaScript(script)
            self.activateWindow()
            QTimer.singleShot(100,lambda:clipboard.setText(text.replace("{text}",clipboard.text())))
            QTimer.singleShot(200,lambda:self.simulate_ctrl_v())
            QTimer.singleShot(500,lambda:self.simulate_enter())
            # clipboard_text = clipboard.text().replace("\\", "\\\\").replace("\n", "\\n").replace("\r", "\\r").replace("'", "\\'").replace('"', '\\"')
            # self.ui.webEngineView.page().runJavaScript('''var textarea = document.getElementById('prompt-textarea');textarea.value = '%s';
            # var event = new Event('input', { bubbles: true });
            # var changeEvent = new Event('change', { bubbles: true });
            # textarea.dispatchEvent(event);
            # textarea.dispatchEvent(changeEvent);
            # '''%text.replace("{text}",clipboard_text))
            # self.ui.webEngineView.page().runJavaScript(r"var button = document.querySelector('[data-testid=\"send-button\"]'); button.disabled = false; button.click();");
        if index==1:
            self.ui.webEngineView.page().runJavaScript('''
            var textarea = document.querySelector('textarea.textarea--g7EUvnQR');
            textarea.focus()
            ''')
            self.activateWindow()
            QTimer.singleShot(100,lambda:clipboard.setText(text.replace("{text}",clipboard.text())))
            QTimer.singleShot(200,lambda:self.simulate_ctrl_v())
            QTimer.singleShot(300,lambda:self.simulate_enter())
        if index==2:

            script = '''
            var element = document.querySelector('.yc-editor-paragraph');
            element.click()
            var ele = document.querySelector('.yc-editor');
            ele.focus()
                   '''
            scripts = '''
            var element = document.querySelector('.VAtmtpqL');
            element.click()
                  '''
            self.ui.webEngineView.page().runJavaScript(script)
            self.activateWindow()
            QTimer.singleShot(100,lambda:clipboard.setText(text.replace("{text}",clipboard.text())))
            QTimer.singleShot(200,lambda:self.simulate_ctrl_v())
            QTimer.singleShot(500,lambda:self.ui.webEngineView.page().runJavaScript(scripts))

        if index==3:

            script = '''
            var element = document.querySelector('.ask-window_small_input_wrap__dlFWu');
                   element.click()
                   '''
            self.ui.webEngineView.page().runJavaScript(script)
            self.activateWindow()
            QTimer.singleShot(100,lambda:clipboard.setText(text.replace("{text}",clipboard.text())))
            QTimer.singleShot(200,lambda:self.simulate_ctrl_v())
            QTimer.singleShot(500,lambda:self.simulate_enter())

        if index==4:
            script = '''
            var element = document.querySelector('textarea.scroll-display-none');
                   element.focus()
                   '''
            self.ui.webEngineView.page().runJavaScript(script)
            self.activateWindow()
            QTimer.singleShot(100,lambda:clipboard.setText(text.replace("{text}",clipboard.text())))
            QTimer.singleShot(200,lambda:self.simulate_ctrl_v())
            QTimer.singleShot(500,lambda:self.simulate_enter())
        if index==5:
            script = '''
            var element = document.querySelector('textarea.semi-input-textarea');
                   element.focus()
                   '''
            self.ui.webEngineView.page().runJavaScript(script)
            self.activateWindow()
            QTimer.singleShot(100,lambda:clipboard.setText(text.replace("{text}",clipboard.text())))
            QTimer.singleShot(200,lambda:self.simulate_ctrl_v())
            QTimer.singleShot(500,lambda:self.simulate_enter())
        if index==6:
            script = '''
            var element = document.querySelector('#chat-input');
                   element.focus()
                   '''
            self.ui.webEngineView.page().runJavaScript(script)
            self.activateWindow()
            QTimer.singleShot(100,lambda:clipboard.setText(text.replace("{text}",clipboard.text())))
            QTimer.singleShot(200,lambda:self.simulate_ctrl_v())
            QTimer.singleShot(500,lambda:self.simulate_enter())
        if index==7:

            script = '''
            var element = document.querySelector('.eeditor___KShcc editor___DSPKC matchHomePageLayout___XTlpC');
                   element.click()
                   '''
            self.ui.webEngineView.page().runJavaScript(script)
            self.activateWindow()
            QTimer.singleShot(100,lambda:clipboard.setText(text.replace("{text}",clipboard.text())))
            QTimer.singleShot(200,lambda:self.simulate_ctrl_v())
            QTimer.singleShot(500,lambda:self.simulate_enter())
        if index==8:
            script = '''
            var element = document.querySelector('.chat-tan-input');
                   element.focus()
                   '''
            self.ui.webEngineView.page().runJavaScript(script)
            self.activateWindow()
            QTimer.singleShot(100,lambda:clipboard.setText(text.replace("{text}",clipboard.text())))
            QTimer.singleShot(200,lambda:self.simulate_ctrl_v())
            QTimer.singleShot(500,lambda:self.simulate_enter())
        QTimer.singleShot(1500,lambda:user32.SetForegroundWindow(hwnd))
    def open_ai(self,index:int):
        ai=""
        if index==0:
            ai="https://chatgpt.com"
            self.setWindowTitle("ChatGpt")

        if index==1:
            ai="https://tongyi.aliyun.com/qianwen"
            self.setWindowTitle("通义千问")

        if index==2:
            ai="https://yiyan.baidu.com"
            self.setWindowTitle("文心一言")

        if index==3:
            ai="https://xinghuo.xfyun.cn/desk"
            self.setWindowTitle("讯飞星火")

        if index==4:
            ai="https://chatglm.cn/main/alltoolsdetail"
            self.setWindowTitle("智谱清言")
        if index==5:
            ai="https://www.doubao.com"
            self.setWindowTitle("字节豆包")
        if index==6:
            ai="https://chat.deepseek.com"
            self.setWindowTitle("deepseek")
        if index==7:
            ai="https://kimi.moonshot.cn"
            self.setWindowTitle("kimi")
        if index==8:
            ai="https://mytan.maiseed.com.cn/chat"
            self.setWindowTitle("mytan")
        if ai not in self.ui.webEngineView.url().toString():
            self.ui.webEngineView.setUrl(ai)
        self.showNormal()
    def moveEvent(self, event):
        self.settings.setValue("web_pos", self.pos())
        event.accept()

    def resizeEvent(self, event):
        self.settings.setValue("web_size", self.size())
        event.accept()
    def restoreWindowState(self):
            if self.settings.contains("web_pos"):
                pos = self.settings.value("web_pos", QPoint())
                self.move(pos)
            if self.settings.contains("web_size"):
                size = self.settings.value("web_size", QSize())
                self.resize(size)


