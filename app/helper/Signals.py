# -*- coding: utf-8 -*-

"""
@File    : Signals.py
@Time    : 2022/9/27 16:59
@Author  : DoooReyn<jl88744653@gmail.com>
@Desc    : 基础信号源
"""
from PyQt5.QtCore import pyqtSignal as QSignal, QObject

from helper.Cmm import Cmm


@Cmm.Decorator.Singleton
class Signals(QObject):
    """Qt信号"""

    # 日志
    logger_trace = QSignal(str)
    logger_debug = QSignal(str)
    logger_info = QSignal(str)
    logger_warn = QSignal(str)
    logger_error = QSignal(str)
    logger_fatal = QSignal(str)

    # 窗口
    win_closed = QSignal(int)
    win_focus_main = QSignal()

    # 多语言
    lang_changed = QSignal(str)

    # 阅读器
    reader_setting_changed = QSignal(int)
    reader_load_progress = QSignal(int)
    reader_status_tip_updated = QSignal(str)
    reader_download_note = QSignal(str, str)
    reader_refresh_speed = QSignal()
    reader_reading_finished = QSignal()
