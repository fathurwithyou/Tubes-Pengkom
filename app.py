# Author: Muhammad Fathur Rizky
# Start Date: 15/10/2023

# Module Import Requirements
from PyQt5 import QtCore, QtGui, QtWidgets
import re
import sys

user = {
    "kwh": 91.87,
    "token": [
        ('53185330183292054367', 74.0), ('61738188796457856001', 74.0), ('12700951329939139693', 37.0), ('78990741058764539643', 14.8), ('07912160821106990357', 14.8), ('06661540602451426770', 37.0), ('75448794092617492345', 37.0), ('21282758825415520205', 74.0), ('60934893120604665682', 369.8), ('85162576942456266643', 369.8), ('37617653516489881716', 147.9), ('17865166341933111683', 369.8), ('97414749505679010130', 14.8), ('10198867939641233110', 14.8), ('10667133000759848080', 74.0), ('66616488375102899986', 147.9), ('79205481489508535397', 37.0), ('26016159090366859851', 37.0), ('41389117591943482379', 14.8), ('38525466571700721229', 369.8), ('23384789095354267104', 147.9), ('56492606546030730085', 74.0), ('94029875068977723377', 369.8), ('74266861446620596841', 37.0), ('33803065936553682704', 147.9), ('11916434866675054491', 74.0), ('64816993199024017175', 14.8), ('21969763291497355837', 14.8), ('00815838918169751645', 14.8), ('11823037648343872338', 369.8)],
    "00": "00000000000",
    "03": "1232.96",
    "07": "1530",
    "09": "",
    "41": 229.6,
    "44": "",
    "47": 0.956,
    "54": "18557449572920944856",
    "59": 37.0,
    "69": "0159",
    "75": "14 - 2626 7617 - 1",
    "78": "999",
    "79": 5.00,
}


str_input = ""
command = ["00", "01", "02", "03", "07", "09", "10", "37", "41", "44", "47", "54",
           "59", "69", "75", "78", "79", "90", "123", "456"]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(213, 312)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 90, 211, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # Font style initialization
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        # Angka 1
        self.btn1 = QtWidgets.QPushButton(
            self.gridLayoutWidget, clicked=lambda: self.press("1"))
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)

        # Angka 2
        self.btn2 = QtWidgets.QPushButton(
            self.gridLayoutWidget, clicked=lambda: self.press("2"))
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)

        # Angka 3
        self.btn3 = QtWidgets.QPushButton(
            self.gridLayoutWidget, clicked=lambda: self.press("3"))
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)

        # Angka 4
        self.btn4 = QtWidgets.QPushButton(
            self.gridLayoutWidget, clicked=lambda: self.press("4"))
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)

        # Angka 5
        self.btn5 = QtWidgets.QPushButton(
            self.gridLayoutWidget, clicked=lambda: self.press("5"))
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)

        # Angka 6
        self.btn6 = QtWidgets.QPushButton(
            self.gridLayoutWidget, clicked=lambda: self.press("6"))
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)

        # Angka 7
        self.btn7 = QtWidgets.QPushButton(
            self.gridLayoutWidget, clicked=lambda: self.press("7"))
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)

        # Angka 8
        self.btn8 = QtWidgets.QPushButton(
            self.gridLayoutWidget, clicked=lambda: self.press("8"))
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)

        # Angka 9
        self.btn9 = QtWidgets.QPushButton(
            self.gridLayoutWidget, clicked=lambda: self.press("9"))
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)

        # Angka 0
        self.btn0 = QtWidgets.QPushButton(
            self.gridLayoutWidget, clicked=lambda: self.press("0"))
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.gridLayout.addWidget(self.btn0, 3, 1, 1, 1)

        # Delete button
        self.deletebtn = QtWidgets.QPushButton(
            self.gridLayoutWidget, clicked=lambda: self.press("del"))
        self.deletebtn.setFont(font)
        self.deletebtn.setObjectName("deletebtn")
        self.deletebtn.setIcon(QtGui.QIcon("img/delete_arrow.svg"))
        self.gridLayout.addWidget(self.deletebtn, 3, 0, 1, 1)

        # Enter button
        self.enterbtn = QtWidgets.QPushButton(
            self.gridLayoutWidget, clicked=lambda: self.press("enter"))
        self.enterbtn.setEnabled(True)
        self.enterbtn.setFont(font)
        self.enterbtn.setTabletTracking(False)
        self.enterbtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.enterbtn.setStyleSheet(
            "background-color: red; border-radius: 10px")
        self.enterbtn.setAutoFillBackground(False)
        self.enterbtn.setIcon(QtGui.QIcon("img/enter_arrow.svg"))
        self.enterbtn.setObjectName("enterbtn")
        self.gridLayout.addWidget(self.enterbtn, 3, 2, 1, 1)

        # Signal Label
        self.signalLabel = QtWidgets.QLabel(self.centralwidget)
        self.signalLabel.setGeometry(QtCore.QRect(10, 10, 31, 15))
        self.signalLabel.setStyleSheet("border-image: url(img/signal.svg)")
        # self.signalLabel.setPixmap(QtGui.QPixmap("img/signal.svg"))
        
        # Count Label
        self.countLabel = QtWidgets.QLabel(self.centralwidget)
        self.countLabel.setGeometry(QtCore.QRect(180, 10, 21, 16))
        self.countLabel.setFont(font)

        # Unit Label
        font.setPointSize(10)
        font.setWeight(75)
        self.unitLabel = QtWidgets.QLabel(self.centralwidget)
        self.unitLabel.setGeometry(QtCore.QRect(90, 10, 41, 16))
        self.unitLabel.setFont(font)
        self.unitLabel.setText("kW h")

        # Output Label
        font.setWeight(75)
        font.setPointSize(16)
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(0, 0, 211, 81))
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.outputLabel.setObjectName("outputLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 213, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Isi token
    def fillToken(self, stroom):
        for i in range(len(user['token'])):
            if user['token'][i][0] == stroom:
                user['kwh'] += user['token'][i][1]
                user["54"] = str(user['token'][i][0])
                user["59"] = str(user['token'][i][1])
                user['token'].pop(i)
                return "b e n a r"
        return "g a g a l"

    def showIndicator(self):
        self.unitLabel.setText("kW h")
        self.countLabel.setText("")
        self.outputLabel.setText(f"{user['kwh']}")
        self.signalLabel.setStyleSheet("border-image: url(img/signal.svg)")


    def cmd_00(self):
        self.unitLabel.setText("kW h")
        self.signalLabel.setStyleSheet("border-image: url(img/signal.svg)")
        self.countLabel.setText("00")
        self.outputLabel.setText(f"000000000000")

    def cmd_01(self):
        self.countLabel.setText("01")
        self.outputLabel.setText("b e n a r")

    def cmd_03(self):
        self.countLabel.setText("03")
        self.unitLabel.setText("kW h")
        self.outputLabel.setText("123192")

    def cmd_07(self):
        self.countLabel.setText("07")
        self.unitLabel.setText("kW")
        self.outputLabel.setText("PL           1530")

    def cmd_09(self):
        self.countLabel.setText("09")
        self.unitLabel.setText("kW")
        self.outputLabel.setText("P             0039")

    def cmd_10(self):
        self.countLabel.setText("10")
        self.unitLabel.setText("")
        self.outputLabel.setText("Ver              10")

    def cmd_37(self):
        self.unitLabel.setText("kW h")
        self.countLabel.setText("37")
        self.outputLabel.setText(f"{user['kwh']}")

    def cmd_41(self):
        self.countLabel.setText("41")
        self.unitLabel.setText("V")
        self.outputLabel.setText("229.6")

    def cmd_44(self):
        self.countLabel.setText("44")
        self.unitLabel.setText("A")
        self.outputLabel.setText("0.956")

    def cmd_47(self):
        self.countLabel.setText("47")
        self.unitLabel.setText("kW")
        self.outputLabel.setText(
            f'P{" "*12}{round(user["41"]*user["47"]/1000, 3)}')

    def cmd_54(self):
        self.countLabel.setText("54")
        self.unitLabel.setText("")
        self.outputLabel.setText(f"{user['54']}")

    def cmd_59(self):
        self.countLabel.setText("59")
        self.unitLabel.setText("kW h")
        self.outputLabel.setText(f"{user['59']}")

    def cmd_69(self):
        self.countLabel.setText("69")
        self.unitLabel.setText("")
        self.outputLabel.setText(f"{user['69']}")

    def cmd_75_1(self):
        self.countLabel.setText("75")
        self.unitLabel.setText("")
        self.outputLabel.setText(f"{user['75'][0:9]}")

    def cmd_75_2(self):
        self.outputLabel.setText(f"{user['75'][10::]}")

    def cmd_78(self):
        self.countLabel.setText("78")
        self.unitLabel.setText("")
        self.outputLabel.setText(f"{user['78']}")

    def cmd_79(self):
        self.countLabel.setText("79")
        self.unitLabel.setText("kW h")
        self.outputLabel.setText(f"{user['79']}0")

    # Matikan lampu LED
    def cmd_90(self):
        self.countLabel.setText("90")
        self.outputLabel.setText("n i h i l")

    def cmd_123(self, inp):
        if len(inp) == 5:
            self.countLabel.setText("08")
            self.outputLabel.setText(f"gagal{' '*7}")
        else:
            user["78"] = inp[3:]
            self.unitLabel.setText("")
            self.outputLabel.setText(user["78"])

    def cmd_456(self, inp):
        self.countLabel.setText("")
        self.unitLabel.setText("kW h")
        if int(str_input[3:5]) >= 5:
            user["79"] = float(str_input[3:5])
        else:
            user["79"] = 5.00
        self.outputLabel.setText(f"{user['79']}0")

    # Pressed button function

    def press(self, pressed):
        global str_input
        timer = QtCore.QTimer()
        delay = 0
        if pressed not in ["del", "enter"]:
            str_input += pressed
        elif pressed == "del":
            str_input = str_input[:-1]
        elif pressed == "enter":
            if len(str_input) == 20 or len(str_input) == 4:
                self.outputLabel.setText(self.fillToken(str_input))
            elif str_input == "00":
                self.cmd_00()
            elif str_input == "01":
                self.cmd_01()
            elif str_input == "03":
                self.cmd_03()
            elif str_input == "07":
                self.cmd_07()
            elif str_input == "09":
                self.cmd_09()
            elif str_input == "10":
                self.cmd_10()
            elif str_input == "37":
                self.cmd_37()
            elif str_input == "41":
                self.cmd_41()
            elif str_input == "44":
                self.cmd_44()
            elif str_input == "47":
                self.cmd_47()
            elif str_input == "54":
                self.cmd_54()
            elif str_input == "59":
                self.cmd_59()
            elif str_input == "69":
                self.cmd_69()
            elif str_input == "75":
                self.cmd_75_1()
                delay = 3000
                timer.singleShot(delay, self.cmd_75_2)
            elif str_input == "78":
                self.cmd_78()
            elif str_input == "79":
                self.cmd_79()
            elif len(str_input) in [5, 6]:
                if str_input[:3] == "123":
                    self.cmd_123(str_input)
                elif str_input[:3] == "456" and len(str_input) == 5:
                    self.cmd_456(str_input)
            elif str_input == "90":
                self.cmd_90()

            if str_input in command or len(str_input) == 20 or str_input[:3] in command:
                delay += 3000
                str_input = ""
        if str_input == "":
            timer.singleShot(delay, self.showIndicator)
        else:
            self.signalLabel.setStyleSheet("")
            self.unitLabel.setText("")
            if len(str_input) < 10:
                self.countLabel.setText(f"0{len(str_input)}")
            else:
                self.countLabel.setText(f"{len(str_input)}")
            self.outputLabel.setText(
                re.sub(r'(\d{4})(?=\d)', r'\1 - ', str_input))

    # Translate Button Meaning
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.deletebtn.setText(_translate("MainWindow", ""))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.enterbtn.setText(_translate("MainWindow", ""))
        self.outputLabel.setText(_translate(
            "MainWindow", str(user["kwh"])))


# Main Driver
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())