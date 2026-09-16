import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout


class Task2(QWidget):
    def __init__(self):
        super().__init__()
        self.expr = QLineEdit()
        self.res = QLineEdit()
        self.btn = QPushButton("Вычислить")

        layout = QHBoxLayout()
        layout.addWidget(self.expr)
        layout.addWidget(self.btn)
        layout.addWidget(self.res)
        self.setLayout(layout)

        self.btn.clicked.connect(self.calc)

    def calc(self):
        try:
            val = str(eval(self.expr.text()))
            self.res.setText(val)
        except Exception:
            self.res.setText("Ошибка")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Task2()
    ex.show()
    sys.exit(app.exec())