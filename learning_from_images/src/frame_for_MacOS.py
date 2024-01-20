
# doesn't work in venv

import sys
#import platform
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer

class TransparentWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Get screen size
        screen_rect = QtWidgets.QApplication.desktop().screenGeometry()
        self.setGeometry(screen_rect)

        # Set the size of the frame (border width)
        self.frame_width = 5

        # Re-assert window flags every 1000 milliseconds (1 second)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.keepOnTop)
        self.timer.start(1000)
        self.show()

    def keepOnTop(self):
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.show()


    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        color = QtGui.QColor(0, 255, 0, 127)  # Example: Semi-transparent green

        # Drawing the borders
        painter.fillRect(0, 0, self.width(), self.frame_width, color)  # Top border
        painter.fillRect(0, 0, self.frame_width, self.height(), color)  # Left border
        painter.fillRect(self.width() - self.frame_width, 0, self.frame_width, self.height(), color)  # Right border
        painter.fillRect(0, self.height() - self.frame_width, self.width(), self.frame_width, color)  # Bottom border
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = TransparentWindow()
    app.exec_()
