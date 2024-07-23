from PySide6.QtCore import QObject, Signal

class interact_signal(QObject):
    interact = Signal(str,int)
global_signal_instance = interact_signal()
