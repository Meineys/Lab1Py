import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLabel, QVBoxLayout, QHBoxLayout


class Task3(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.widgets_map = {}

        for i in range(3):
            row = QHBoxLayout()
            cb = QCheckBox(f"Показать виджет {i + 1}")
            cb.setChecked(True)
            lbl = QLabel(f"Текстовый виджет {i + 1}")

            self.widgets_map[cb] = lbl
            cb.stateChanged.connect(self.toggle_widget)

            row.addWidget(cb)
            row.addWidget(lbl)
            layout.addLayout(row)

        self.setLayout(layout)

    def toggle_widget(self):
        cb = self.sender()
        widget = self.widgets_map[cb]
        widget.setVisible(cb.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Task3()
    ex.show()
    sys.exit(app.exec())