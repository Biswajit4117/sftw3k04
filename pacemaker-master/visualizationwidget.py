from PySide6.QtWidgets import QWidget, QGridLayout, QFormLayout, QSpinBox
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import QTimer
from ui_visualizationwidget import Ui_visualizationWidget
import math

class VisualizationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_visualizationWidget()
        self.ui.setupUi(self)
        self.ui.electrogramGroup.setLayout(QGridLayout())
        self.ui.electrogramGroup.layout().setContentsMargins(0, 0, 0, 0)
        view = QChartView(self.ui.electrogramGroup)
        chart = QChart()
        self.series = QLineSeries()
        series = self.series
        self.chart = chart
        chart.legend().hide()
        chart.addSeries(series)
        chart.setTitle('Electrogram')
        chart.createDefaultAxes()
        chart.axisX().setRange(0, 10)
        chart.axisY().setRange(-1, 1)
        view.setChart(chart)
        timer = QTimer(self)
        timer.setInterval(10)
        timer.timeout.connect(self.updateElectrogram)
        self.t = 0
        self.ui.electrogramGroup.layout().addWidget(view)
        self.ui.splitter.setStretchFactor(0, 1)
        self.ui.splitter.setStretchFactor(1, 1)
        timer.start()

        layout = QFormLayout()
        for i in range(10):
            layout.addRow(f'param_{i}', QSpinBox())
        self.ui.allParams.setLayout(layout)
    
    def updateElectrogram(self):
        y = math.sin(self.t)
        self.series.append(self.t, y)
        if self.t > 10:
            self.series.remove(0)
            self.chart.axisX().setRange(self.t - 10, self.t)            
        self.t += 0.01
