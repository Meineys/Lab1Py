import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QCheckBox, QSpinBox,
                             QPushButton, QPlainTextEdit, QVBoxLayout, QHBoxLayout)


class Task5(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = {"Вода из лужи": 25000000, "Вчерашний помидор": 500, "Просто блюдо": 1}
        self.items = []

        layout = QVBoxLayout()

        for name, price in self.menu.items():
            row = QHBoxLayout()
            cb = QCheckBox(f"{name} ({price} руб.)")
            spin = QSpinBox()
            spin.setMinimum(1)

            self.items.append((name, price, cb, spin))
            row.addWidget(cb)
            row.addWidget(spin)
            layout.addLayout(row)

        self.btn = QPushButton("Сформировать чек")
        self.receipt = QPlainTextEdit()

        layout.addWidget(self.btn)
        layout.addWidget(self.receipt)
        self.setLayout(layout)

        self.btn.clicked.connect(self.generate_receipt)

    def generate_receipt(self):
        total = 0
        text = "--- ЧЕК ---\n"

        for name, price, cb, spin in self.items:
            if cb.isChecked():
                qty = spin.value()
                cost = price * qty
                total += cost
                text += f"{name} x{qty} = {cost} руб.\n"

        text += f"Итого: {total} руб."
        self.receipt.setPlainText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Task5()
    ex.show()
    sys.exit(app.exec())