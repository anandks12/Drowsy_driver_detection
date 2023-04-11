import sys
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

# Create a message box
msg_box = QMessageBox()
msg_box.setText("Hello, World!")
msg_box.setWindowTitle("My Message Box")

# Show the message box
msg_box.exec()

sys.exit(app.exec())
