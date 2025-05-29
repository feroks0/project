import sys
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QGraphicsScene
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg 

from arayuz import Ui_Form


class DataAPP(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.figure = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.scene.addWidget(self.canvas)
        self.ui.loadButton.clicked.connect(self.LoadAndPlot) 
        self.ui.saveButton.clicked.connect(self.SavePDF)
        self.ui.saveButton.setEnabled(False)

    def LoadAndPlot(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)")
        if not file_path:
            return

        try:
            try:
                df = pd.read_csv(file_path, decimal=",", sep=";")
            except pd.errors.ParserError:
                df = pd.read_csv(file_path, decimal=",")

            if "UV_Index" not in df.columns:
                QMessageBox.warning(self, "Error", f"'UV_Index' column not found.\nAvailable columns: {df.columns.tolist()}")
                return

            df["Measurement"] = range(1, len(df) + 1)
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(df["Measurement"], df["UV_Index"], marker='o', linestyle='-', color='blue', label="UV Index")
            ax.set_title("UV Index by Measurement")
            ax.set_xlabel("Measurement Number")
            ax.set_ylabel("UV Index")
            ax.set_ylim(df["UV_Index"].min() - 0.5, df["UV_Index"].max() + 0.5)
            ax.grid(True, linestyle='--', alpha=0.6)
            ax.legend()
            self.canvas.draw()
            self.ui.saveButton.setEnabled(True)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def SavePDF(self):
        pdf_path, _ = QFileDialog.getSaveFileName(self, "Save as PDF", "", "PDF Files (*.pdf)")
        if not pdf_path:
            return

        if not pdf_path.endswith(".pdf"):
            pdf_path += ".pdf"

        self.figure.savefig(pdf_path)
        QMessageBox.information(self, "Success", f"Graph saved as PDF:\n{pdf_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataAPP()
    window.show()
    sys.exit(app.exec_())
