import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout


class Task1(QWidget):
    def __init__(self):
        super().__init__()
        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.btn = QPushButton("->")

        layout = QHBoxLayout()
        layout.addWidget(self.l1)
        layout.addWidget(self.btn)
        layout.addWidget(self.l2)
        self.setLayout(layout)

        self.btn.clicked.connect(self.swap)

    def swap(self):
        if self.btn.text() == "->":
            self.l2.setText(self.l1.text())
            self.l1.clear()
            self.btn.setText("<-")
        else:
            self.l1.setText(self.l2.text())
            self.l2.clear()
            self.btn.setText("->")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Task1()
    ex.show()
    sys.exit(app.exec())