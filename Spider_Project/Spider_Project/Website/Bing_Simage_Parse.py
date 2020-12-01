# from PyQt5.QtCore import QObject, pyqtSignal
#
# MsgSlot = list()
#
#
# class QTypeSIgnal(QObject):
#     # 定义显示和进度的信号
#     sendmsg = pyqtSignal(str, int)
#
#     def __init__(self):
#         super().__init__()
#
#     def send(self):
#         # 发射信号
#         self.sendmsg.emit(MsgSlot.pop(0))