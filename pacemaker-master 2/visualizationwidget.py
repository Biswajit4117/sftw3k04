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
        view = QChartView(self.ui.electrogramGroup)  # 创建图表视图并添加到sue,以容纳电图的显示
        chart = QChart()  # 创建图表和线系列，将这些添加到图表中
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
        timer = QTimer(self)  # 定时器，每隔10秒，定时time连接到upe,以便定期更新电图的数据
        timer.setInterval(10)
        timer.timeout.connect(self.updateElectrogram)
        self.t = 0  # 初始，跟踪时间
        self.ui.electrogramGroup.layout().addWidget(view)
        self.ui.splitter.setStretchFactor(0, 1)
        self.ui.splitter.setStretchFactor(1, 1)
        timer.start()

        layout = QFormLayout()  # 创建一个布局，循环添加十个参数，用于显示模拟参数的值
        for i in range(10):
            layout.addRow(f'param_{i}', QSpinBox())
        self.ui.allParams.setLayout(layout)

    def updateElectrogram(self):
        y = math.sin(self.t)  # 使用sin函数计算电图的y值，模拟一个正弦波形
        self.series.append(self.t, y)  # 将括号里的数据点追加到先系列中，
        if self.t > 10:
            self.series.remove(0)
            self.chart.axisX().setRange(self.t - 10, self.t)
        self.t += 0.01
