import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QGridLayout


class Task4(QWidget):
    def __init__(self):
        super().__init__()
        self.morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                      'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                      'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                      'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                      'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}

        self.out = QLineEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.out)

        grid = QGridLayout()
        letters = list(self.morse.keys())

        row, col = 0, 0
        for letter in letters:
            btn = QPushButton(letter)
            btn.clicked.connect(self.add_morse)
            grid.addWidget(btn, row, col)
            col += 1
            if col > 5:
                col = 0
                row += 1

        layout.addLayout(grid)
        self.setLayout(layout)

    def add_morse(self):
        btn = self.sender()
        char = btn.text()
        current = self.out.text()
        self.out.setText(current + self.morse[char] + " ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Task4()
    ex.show()
    sys.exit(app.exec())