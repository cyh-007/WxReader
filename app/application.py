# -*- coding: utf-8 -*-

"""
@File    : application.py
@Time    : 2022/9/27 17:48
@Author  : DoooReyn<jl88744653@gmail.com>
@Desc    : 应用程序
"""
import sys
from traceback import format_exception

from PyQt5.QtWidgets import QApplication
from conf.resources import qInitResources

from conf.res_map import ResMap
from helper.gui import GUI
from helper.i18n import I18n
from helper.preferences import Preferences
from helper.signals import Signals
from view.window import Window


class Application(object):
    """应用程序"""
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        super(Application, self).__init__()

        # 全局异常捕获代理
        self._old_error_hook = sys.excepthook
        sys.excepthook = self._error_hook

        # 初始化 qrc 资源
        qInitResources()

        # 初始化用户配置
        Preferences.init()

        # 创建 Qt 窗口
        self.qt_app = QApplication(sys.argv)
        self.qt_app.setApplicationName(I18n.text("app:name"))
        self.qt_app.setApplicationDisplayName(I18n.text("app:name"))
        self.qt_app.setWindowIcon(GUI.icon(ResMap.icon_app))
        self.qt_win = Window()

    def _error_hook(self, error_type, error_target, error_stack):
        """全局异常捕获"""
        traceback_format = format_exception(error_type, error_target, error_stack)
        traceback_msg = "".join(traceback_format)
        Signals().logger_error.emit(traceback_msg)
        self._old_error_hook(error_type, error_target, error_stack)

    def run(self):
        self.qt_win.show()
        sys.exit(self.qt_app.exec_())
