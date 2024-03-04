import math
import traceback
import matplotlib.pyplot as plt

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

from task3.functions import *
from compmath.nonlinear import *
from compmath.plot import plot_functions, plot_equation_2d
from compmath.nonlinear import simple_iteration_2d

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


equations_functions = {
    'f1_button': f1,
    'f2_button': f2,
    'f3_button': f3
}

equations_functions_phi = {
    'f1_button': phi1,
    'f2_button': phi2,
    'f3_button': phi3
}

methods_functions = {
    'chords_button': 'chord_method',
    'newton_button': 'newton_method',
    'simple_iteration_button': 'simple_iteration'
}

systems_functions = {
    'sys1_button': (sys_f11, sys_f12),
    'sys2_button': (sys_f21, sys_f22)
}

systems_functions_phi = {
    'sys1_button': (sys_phi11, sys_phi12),
    'sys2_button': (sys_phi21, sys_phi22)
}

equation_f = f1
equation_phi = phi1
method_f = 'chord_method'
eps_nle = 0.01
a = 0
b = 1


init_approx = [0, 0]
sys_f1 = sys_f11
sys_f2 = sys_f12
sys_phi1 = sys_phi11
sys_phi2 = sys_phi12

eps_sonle = 0.01


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        uic.loadUi("main.ui", self)

        self.nle_solver = NLESolver(eps=1e-2)
        self.table_window = None
        self.plot_window = None

        self.show()
        self.initUI()

    def initUI(self):
        self.load_equations_imgs()
        self.load_systems_imgs()
        self.load_pig()

        self.f1_button.clicked.connect(self.f_radio_button_clicked)
        self.f2_button.clicked.connect(self.f_radio_button_clicked)
        self.f3_button.clicked.connect(self.f_radio_button_clicked)

        self.chords_button.clicked.connect(self.method_radio_button_clicked)
        self.newton_button.clicked.connect(self.method_radio_button_clicked)
        self.simple_iteration_button.clicked.connect(self.method_radio_button_clicked)

        self.sys1_button.clicked.connect(self.system_radio_button_clicked)
        self.sys2_button.clicked.connect(self.system_radio_button_clicked)

        validator = QRegExpValidator(QRegExp("[+-]?\\d*\\.?\\d+"))

        self.a_line_edit.setValidator(validator)
        self.a_line_edit.setText('0')

        self.b_line_edit.setValidator(validator)
        self.b_line_edit.setText('0')

        self.x_approx_sys_line_edit.setValidator(validator)
        self.x_approx_sys_line_edit.setText('0')

        self.y_approx_sys_line_edit.setValidator(validator)
        self.y_approx_sys_line_edit.setText('0')

        self.eps_line_edit.setValidator(validator)
        self.eps_line_edit.setText('0.01')

        self.eps_sonle_line_edit.setValidator(validator)
        self.eps_sonle_line_edit.setText('0.01')

        self.solve_nle_button.clicked.connect(self.solve_nle)
        self.solve_sonle_button.clicked.connect(self.solve_sonle)

    def parse_a(self):
        global a

        if len(self.a_line_edit.text()) == 0:
            self.a_line_edit.setText('0')
            a = 0
            return
        try:
            a = float(self.a_line_edit.text().replace(',', '.'))
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Invalid a value')
            return

    def parse_b(self):
        global b

        if len(self.b_line_edit.text()) == 0:
            self.b_line_edit.setText('0')
            b = 0
            return
        try:
            b = float(self.b_line_edit.text().replace(',', '.'))
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Invalid b value')
            return

    def parse_eps(self):
        global eps_nle

        if len(self.eps_line_edit.text()) == 0:
            self.eps_line_edit.setText('0.01')
            eps_nle = 0.01
            return
        try:
            eps_nle = float(self.eps_line_edit.text().replace(',', '.'))
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Invalid eps value')
            return

    def parse_eps_sonle(self):
        global eps_sonle

        if len(self.eps_sonle_line_edit.text()) == 0:
            self.eps_sonle_line_edit.setText('0.01')
            eps_sonle = 0.01
            return
        try:
            eps_sonle = float(self.eps_sonle_line_edit.text().replace(',', '.'))
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Invalid eps value')
            return

    def f_radio_button_clicked(self):
        global equation_f, equation_phi

        sender = self.sender()
        if sender.isChecked():
            equation_f = equations_functions[sender.objectName()]
            equation_phi = equations_functions_phi[sender.objectName()]

    def method_radio_button_clicked(self):
        global method_f

        sender = self.sender()
        if sender.isChecked():
            method_f = methods_functions[sender.objectName()]

    def solve_nle(self):
        global a, b, equation_f, equation_phi, method_f

        self.parse_a()
        self.parse_b()
        self.parse_eps()

        if a >= b:
            QMessageBox.warning(self, 'Error', 'Invalid interval')
            return

        if eps_nle <= 0:
            QMessageBox.warning(self, 'Error', 'Invalid eps value')
            return

        self.nle_solver.eps = eps_nle

        try:
            self.plot_window = PlotWindow([equation_f, y_0], a, b)
            self.plot_window.show()
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Invalid interval')
            return

        try:
            log = self.nle_solver.solve(
                f=equation_f,
                phi=equation_phi,
                method=method_f,
                a=a,
                b=b
            )
        except ValueError as e:
            if str(e) == 'math domain error':
                QMessageBox.warning(self, 'Error', 'try another interval')
            else:
                QMessageBox.warning(self, 'Error', str(e))
            return

        self.table_window = TableWindow(log)
        self.table_window.show()

    def system_radio_button_clicked(self):
        global sys_f1, sys_f2, sys_phi1, sys_phi2

        sender = self.sender()
        if sender.isChecked():
            sys_f1, sys_f2 = systems_functions[sender.objectName()]
            sys_phi1, sys_phi2 = systems_functions_phi[sender.objectName()]

    def parse_init_guess(self):
        global init_approx

        for i, line_edit in enumerate([self.x_approx_sys_line_edit, self.y_approx_sys_line_edit]):
            if len(line_edit.text()) == 0:
                line_edit.setText('0')
                init_approx[i] = 0,
                return
            else:
                try:
                    init_approx[i] = float(line_edit.text().replace(',', '.'))
                except ValueError:
                    QMessageBox.warning(self, 'Error', 'Invalid initial guess')
                    return

    def solve_sonle(self):
        global init_approx, sys_f1, sys_f2, sys_phi1, sys_phi2, eps_sonle

        self.parse_init_guess()
        self.parse_eps_sonle()

        if eps_sonle <= 0:
            QMessageBox.warning(self, 'Error', 'Invalid eps value')
            return

        try:
            self.plot_window = PlotWindow([sys_f1, sys_f2], init_approx[0] - 3, init_approx[1] + 3)
            self.plot_window.show()
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Invalid initial guess')
            return

        try:
            log = simple_iteration_2d(sys_f1, sys_f2, sys_phi1, sys_phi2, init_approx, eps=eps_sonle)

            self.table_window = TableWindow(log)
            self.table_window.show()

        except Exception as e:
            traceback.print_exc()
            if str(e) == 'math domain error':
                QMessageBox.warning(self, 'Error', 'try another initial guess')
            else:
                QMessageBox.warning(self, 'Error', str(e))
            return

    def load_equations_imgs(self):
        pixmap = QPixmap("./img/equations/f1.png")
        self.f1_label.setPixmap(pixmap)
        self.f1_label.setScaledContents(True)

        pixmap = QPixmap("./img/equations/f2.png")
        self.f2_label.setPixmap(pixmap)
        self.f2_label.setScaledContents(True)

        pixmap = QPixmap("./img/equations/f3.png")
        self.f3_label.setPixmap(pixmap)
        self.f3_label.setScaledContents(True)

    def load_systems_imgs(self):
        pixmap = QPixmap("./img/systems/sys1.png")
        self.sys1_label.setPixmap(pixmap)
        self.sys1_label.setScaledContents(True)

        pixmap = QPixmap("./img/systems/sys2.png")
        self.sys2_label.setPixmap(pixmap)
        self.sys2_label.setScaledContents(True)

    def load_pig(self):
        pixmap = QPixmap("./img/pig.png")
        self.pig_img.setPixmap(pixmap)
        self.pig_img.setScaledContents(True)


class TableWindow(QDialog):
    def __init__(self, log):
        super(TableWindow, self).__init__()
        uic.loadUi("table.ui", self)

        self.log = log

        self.num_rows = len(self.log)
        self.num_cols = len(self.log[0])

        self.show()
        self.initUI()

    def initUI(self):
        self.history_table.setStyleSheet("QTableWidget::item:selected { background-color: lightgray; }")

        self.history_table.setRowCount(self.num_rows)
        self.history_table.setColumnCount(self.num_cols)

        self.fill_table()

    def fill_table(self):
        self.history_table.setHorizontalHeaderLabels(self.log[0])

        for i, line in enumerate(self.log[1:]):
            for j, value in enumerate(line):
                val = str(round(float(value), 5))
                item = QTableWidgetItem(val)
                self.history_table.setItem(i, j, item)


class PlotWindow(QDialog):
    def __init__(self, functions, a, b):
        super(PlotWindow, self).__init__()
        uic.loadUi("plot.ui", self)

        self.functions = functions
        self.a = a
        self.b = b

        self.show()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        if self.functions[0].__code__.co_argcount == 1:
            fig = plot_functions(self.functions, self.a, self.b)
        else:
            fig = plot_equation_2d(self.functions, self.a, self.b)

        canvas = FigureCanvas(fig)

        pixmap = QPixmap(canvas.size())
        canvas.render(pixmap)
        label = QLabel(self)
        label.setPixmap(pixmap)

        layout.addWidget(label)
        self.setLayout(layout)


def main():
    app = QApplication([])
    window = App()

    app.exec_()


if __name__ == '__main__':
    main()

