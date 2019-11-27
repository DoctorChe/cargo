from PyQt5.QtWidgets import QTableWidgetItem


def table_appender(table_widget, row, h_headers):
    row_position = table_widget.rowCount()
    table_widget.insertRow(row_position)

    # h_headers = []
    # for column in range(table_widget.columnCount()):
    #     cell = table_widget.horizontalHeaderItem(column).text()
    #     h_headers.append(cell)

    for col_position, head in enumerate(h_headers):
        item = str(row.get(head)) if row.get(head) is not None else ''
        table_widget.setItem(row_position, col_position, QTableWidgetItem(item))


def table_append_rows(table_widget, rows, h_headers):
    for row in rows:
        table_appender(table_widget, row, h_headers)
    table_widget.resizeColumnsToContents()


def table_cleaner(table_widget):
    table_widget.setRowCount(0)
