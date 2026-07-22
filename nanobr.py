import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QToolBar,
)
from PyQt6.QtWebEngineWidgets import QWebEngineView


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nano Browser")
        self.resize(1000, 700)

        self.web = QWebEngineView()
        self.setCentralWidget(self.web)

        bar = QToolBar()
        self.addToolBar(bar)

        back = bar.addAction("←")
        forward = bar.addAction("→")
        reload = bar.addAction("⟳")
        home = bar.addAction("🏠")

        self.url = QLineEdit()
        self.url.returnPressed.connect(self.load_url)
        bar.addWidget(self.url)

        back.triggered.connect(self.web.back)
        forward.triggered.connect(self.web.forward)
        reload.triggered.connect(self.web.reload)
        home.triggered.connect(
            lambda: self.web.setUrl(QUrl("https://google.com"))
        )

        self.web.urlChanged.connect(
            lambda u: self.url.setText(u.toString())
        )

        self.web.setUrl(QUrl("https://google.com"))


    def load_url(self):
        text = self.url.text().strip()

        if "://" not in text:
            if "." in text:
                text = "https://" + text
            else:
                text = "https://www.google.com/search?q=" + text.replace(" ", "+")

        self.web.setUrl(QUrl(text))


app = QApplication(sys.argv)

window = Browser()
window.show()

sys.exit(app.exec())
