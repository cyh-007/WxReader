# -*- coding: utf-8 -*-

"""
@File    : Options.py
@Time    : 2022/10/1 11:52
@Author  : DoooReyn<jl88744653@gmail.com>
@Desc    : 用户自定义选项视图
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QLineEdit, QPushButton, QSpinBox

from conf.Lang import LanguageKeys
from conf.Views import Views
from helper.GUI import GUI
from helper.I18n import I18n
from helper.Preferences import Preferences, UserKey
from helper.Signals import Signals
from ui.model.ReaderHelper import ReaderActions


class _View(GUI.View):
    def __init__(self):
        super(_View, self).__init__()

        self.ui_lab_speed = QLabel('滚速')
        self.ui_lab_speed.setToolTip('直接修改阅读速度 (1-100)')
        self.ui_spin_speed = QSpinBox()
        self.ui_spin_speed.setMinimum(1)
        self.ui_spin_speed.setMaximum(100)
        self.ui_lab_step = QLabel('步幅')
        self.ui_lab_step.setToolTip('调整加速、减速步幅 (1-10)')
        self.ui_spin_step = QSpinBox()
        self.ui_spin_step.setMinimum(1)
        self.ui_spin_step.setMaximum(10)
        self.ui_lab_call = QLabel('读完通知')
        self.ui_edit_call = QLineEdit()
        self.ui_edit_call.setPlaceholderText('读完通知，接受GET请求')
        self.ui_btn_call = QPushButton('测试')
        self.ui_edit_call.setFixedHeight(32)

        self.ui_layout = QGridLayout()
        self.ui_layout.setAlignment(Qt.AlignTop)
        self.ui_layout.addWidget(self.ui_lab_speed, 0, 0, 1, 1)
        self.ui_layout.addWidget(self.ui_spin_speed, 0, 1, 1, 1)
        self.ui_layout.addWidget(self.ui_lab_step, 1, 0, 1, 1)
        self.ui_layout.addWidget(self.ui_spin_step, 1, 1, 1, 1)
        self.ui_layout.addWidget(self.ui_lab_call, 2, 0, 1, 1)
        self.ui_layout.addWidget(self.ui_edit_call, 2, 1, 1, 2)
        self.ui_layout.addWidget(self.ui_btn_call, 2, 3, 1, 1)
        self.ui_layout.setColumnStretch(2, 1)

        self.setLayout(self.ui_layout)


class Options(QDialog, _View):
    def __init__(self):
        super(Options, self).__init__()

        self.setWindowTitle(I18n.text(LanguageKeys.toolbar_profile))
        self.setFixedHeight(120)
        self.setModal(True)
        self.setWindowCode(Views.Profile)
        self.setWinRectKey(UserKey.Profile.WinRect)
        self.setupPreferences()
        self.setupSignals()

    # noinspection PyUnresolvedReferences
    def setupSignals(self):
        self.ui_btn_call.clicked.connect(self.onCallBtnClicked)
        self.ui_spin_speed.valueChanged.connect(self.onSpeedChanged)
        self.ui_spin_step.valueChanged.connect(self.onStepChanged)

    def setupPreferences(self):
        self.ui_spin_speed.setValue(Preferences().get(UserKey.Reader.Speed))
        self.ui_spin_step.setValue(Preferences().get(UserKey.Reader.Step))
        url = Preferences().get(UserKey.Profile.NoticeUrl)
        if len(url) > 0:
            self.ui_edit_call.setText(url)

    @staticmethod
    def onSpeedChanged(value: int):
        Preferences().set(UserKey.Reader.Speed, value)
        Signals().reader_setting_changed.emit(ReaderActions.SpeedDown)
        Signals().reader_refresh_speed.emit()

    @staticmethod
    def onStepChanged(value: int):
        Preferences().set(UserKey.Reader.Step, value)
        Signals().reader_setting_changed.emit(ReaderActions.SpeedDown)
        Signals().reader_refresh_speed.emit()

    def onCallBtnClicked(self):
        api = self.ui_edit_call.text()
        print(api)

    def closeEvent(self, event: QCloseEvent):
        super(Options, self).closeEvent(event)