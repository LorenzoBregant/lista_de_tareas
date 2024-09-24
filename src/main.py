import sys
from PySide6.QtWidgets import QApplication, QWidget
from src.interfaz.ventana_principal import VentanaPrincipal

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    ventana = VentanaPrincipal(window)
    window.show()
    sys.exit(app.exec())
