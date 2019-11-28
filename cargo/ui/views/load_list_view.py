from collections import OrderedDict

from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
from PyQt5.QtWidgets import QWidget, QAbstractItemView

from cargo.ui.views.ui_load import Ui_Form
from cargo.utils.table_utils import table_cleaner, table_append_rows

H_HEADERS_LOAD = OrderedDict([
    ('id', 'Номер'),
    ('length', 'Длина'),
    ('height', 'Высота'),
    ('width', 'Ширина'),
    ('weight', 'Вес'),
    ('load_from', 'Начальный пункт'),
    ('load_to', 'Конечный пункт'),
    # ('info', 'Дополнительная информация'),
])


class LoadListView(QWidget):

    signal_create_load = Signal(dict)
    signal_read_load = Signal(dict)
    signal_update_load = Signal(dict)
    signal_delete_load = Signal(dict)

    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.load_id = None

        self.ui.tw_load.setColumnCount(len(H_HEADERS_LOAD))
        self.ui.tw_load.setHorizontalHeaderLabels(H_HEADERS_LOAD.values())
        self.ui.tw_load.horizontalHeader().setVisible(True)
        self.ui.tw_load.verticalHeader().setVisible(True)
        self.ui.tw_load.setAlternatingRowColors(True)
        # self.ui.tw_load.setColumnHidden(0, True)
        self.ui.tw_load.resizeColumnsToContents()
        self.ui.tw_load.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tw_load.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tw_load.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.ui.tw_load.clicked.connect(self.load_table_clicked)
        self.ui.pb_create_load.clicked.connect(self.create_load_clicked)
        self.ui.pb_update_load.clicked.connect(self.update_load_clicked)
        self.ui.pb_delete_load.clicked.connect(self.delete_load_clicked)

    def load_table_clicked(self, idx):
        self.load_id = self.ui.tw_load.item(idx.row(), 0).text()
        self.read_load_clicked()

    def create_load_clicked(self):
        self.signal_create_load.emit(self.get_load_data())

    def read_load_clicked(self):
        if self.load_id:
            load = {'load': {
                'id': self.load_id
            }}
            self.signal_read_load.emit(load)

    def update_load_clicked(self):
        load = self.get_load_data()
        load['load']['id'] = self.load_id
        self.signal_update_load.emit(load)

    def delete_load_clicked(self):
        if self.load_id:
            load = {'load': {
                'id': self.load_id
            }}
            self.signal_delete_load.emit(load)

    def populate_load_table(self, items):
        table_cleaner(self.ui.tw_load)
        table_append_rows(self.ui.tw_load, items, H_HEADERS_LOAD)

    def populate_load_card(self, item):
        self.ui.dsb_length.setValue(item.get('length'))
        self.ui.dsb_height.setValue(item.get('height'))
        self.ui.dsb_width.setValue(item.get('width'))
        self.ui.dsb_weight.setValue(item.get('weight'))
        self.ui.le_load_from.setText(item.get('load_from'))
        self.ui.le_load_to.setText(item.get('load_to'))
        self.ui.te_info.setText(item.get('info'))

    def get_load_data(self):
        print('Start read load data')
        length = self.ui.dsb_length.value()
        height = self.ui.dsb_height.value()
        width = self.ui.dsb_width.value()
        weight = self.ui.dsb_weight.value()
        load_from = self.ui.le_load_from.text()
        load_to = self.ui.le_load_to.text()
        info = self.ui.te_info.toPlainText()
        load = {'load': {
            'length': length,
            'height': height,
            'width': width,
            'weight': weight,
            'load_from': load_from,
            'load_to': load_to,
            'info': info,
        }}
        return load
