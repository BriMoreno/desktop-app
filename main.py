# getting the components needed
from PySide6.QtWidgets import QApplication, QWidget

# sys is used to process command line arguments
import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

# starting the event loop
app.exec()