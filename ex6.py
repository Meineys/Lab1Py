import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QGridLayout


class Task6(QWidget):
    def __init__(self):
        super().__init__()
        self.expr = ""
        self.display = QLineEdit()
        self.display.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.display)

        grid = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row, col = 0, 0
        for b in buttons:
            btn = QPushButton(b)
            btn.clicked.connect(self.press)
            grid.addWidget(btn, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        layout.addLayout(grid)
        self.setLayout(layout)

    def press(self):
        val = self.sender().text()
        if val == '=':
            try:
                res = eval(self.expr)
                self.display.setText(str(res))
                self.expr = str(res)
            except ZeroDivisionError:
                self.display.setText("Ошибка: деление на ноль")
                self.expr = ""
            except Exception:
                self.display.setText("Ошибка")
                self.expr = ""
        else:
            self.expr += val
            self.display.setText(self.expr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Task6()
    ex.show()
    sys.exit(app.exec())