#!/usr/bin/python3
# -*- coding: utf-8 -*-

from UserInterface.UserInterfaceController import UserInterfaceController
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = UserInterfaceController()
    ui.show()
    sys.exit(app.exec_())