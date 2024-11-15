from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import getpass
import sys
from pprint import pprint
from PyQt6.QtWidgets import(
    QApplication,
    QWidget,
    QLabel,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QTableWidget,
    QTableWidgetItem,
    QMainWindow
)
import pymysql
connection = pymysql.connect(host = 'localhost', user = 'root', password = 'SQLbea', db = 'restaurant_supply_express', charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Add User")
        Main.resize(1000, 600)

        self.QtStack = QtWidgets.QStackedLayout()
        
        #Home Page
        self.stack1 = QtWidgets.QWidget()
        
        #Owner
        self.stack2 = QtWidgets.QWidget()
        self.stack3 = QtWidgets.QWidget()
        self.stack4 = QtWidgets.QWidget()
        self.stack5 = QtWidgets.QWidget()
        
        #Delivery service 
        self.stack6 = QtWidgets.QWidget()
        self.stack7 = QtWidgets.QWidget()
        self.stack8 = QtWidgets.QWidget()
        self.stack9 = QtWidgets.QWidget()
        self.stack10 = QtWidgets.QWidget()
        self.stack11 = QtWidgets.QWidget()

        #Ingredient stacks
        self.stack12= QtWidgets.QWidget()
        self.stack13= QtWidgets.QWidget()
        self.stack14= QtWidgets.QWidget()
        self.stack15= QtWidgets.QWidget()

        #location stacks
        self.stack16= QtWidgets.QWidget()
        self.stack17= QtWidgets.QWidget()
        self.stack18= QtWidgets.QWidget()

        #restarurant stacks
        self.stack19= QtWidgets.QWidget()
        self.stack20= QtWidgets.QWidget()
        self.stack21= QtWidgets.QWidget()

        #employee, pilot, worker stacks
        self.stack22 = QtWidgets.QWidget()
        self.stack23 = QtWidgets.QWidget()
        self.stack24 = QtWidgets.QWidget()
        self.stack25 = QtWidgets.QWidget()
        self.stack26 = QtWidgets.QWidget()
        self.stack27 = QtWidgets.QWidget()
        self.stack28 = QtWidgets.QWidget()
        self.stack29 = QtWidgets.QWidget()
        self.stack30 = QtWidgets.QWidget()
        self.stack31 = QtWidgets.QWidget()

        #Drone Stacks
        self.stack32 = QtWidgets.QWidget()
        self.stack33 = QtWidgets.QWidget()
        self.stack34 = QtWidgets.QWidget()
        self.stack35 = QtWidgets.QWidget()
        self.stack36 = QtWidgets.QWidget()
        self.stack37 = QtWidgets.QWidget()
        self.stack38 = QtWidgets.QWidget()
        self.stack39 = QtWidgets.QWidget()

        #Home Page
        self.HomePage()

        #Owner
        self.OwnerUI()
        self.ViewOwnerUI()
        self.AddOwnerUI()
        self.StartFundingUI()

        #Delivery Service
        self.DeliveryServiceUI()
        self.AddServiceUI()
        self.ManageServiceUI()
        self.HireEmployeeUI()
        self.FireEmployeeUI()
        self.ViewServiceUI()

        #Ingredient
        self.IngredientUI()
        self.addIngredientUI()
        self.viewIngredientUI()
        self.removeIngredientUI()

        #Employee, Pilot, Worker
        self.EmployeeUI()
        self.PilotUI()
        self.WorkerUI()
        self.AddEmployeeUI()
        self.ViewEmployeeUI()
        self.AddPilotUI()
        self.ViewPilotUI()
        self.RemovePilotUI()
        self.TakeoverDroneUI()
        self.AddWorkerUI()

        #Location pages
        self.LocationUI()
        self.addLocationUI()
        self.viewLocationUI()

        #Restaurant Pages
        self.RestUI()
        self.addRestUI()
        self.PurchaseIngUI()

        #Drone Pages
        self.dronesUI()
        self.addDronesUI() #33
        self.removeDroneUI() #34
        self.leaveSwarmUI()
        self.loadDroneUI()
        self.refuelDroneUI()
        self.flyDroneUI()
        self.joinSwarmUI() #39

        #Home
        self.QtStack.addWidget(self.stack1)

        #Owner
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)

        #Delivery Service
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)
        self.QtStack.addWidget(self.stack10)
        self.QtStack.addWidget(self.stack11)

        #Ingredient
        self.QtStack.addWidget(self.stack12)
        self.QtStack.addWidget(self.stack13)
        self.QtStack.addWidget(self.stack14)
        self.QtStack.addWidget(self.stack15)
        
        #Location 
        self.QtStack.addWidget(self.stack16)
        self.QtStack.addWidget(self.stack17)
        self.QtStack.addWidget(self.stack18)
        
        #Restaraunt 
        self.QtStack.addWidget(self.stack19)
        self.QtStack.addWidget(self.stack20)
        self.QtStack.addWidget(self.stack21)
        
        #Employee, Pilot, Worker
        self.QtStack.addWidget(self.stack22)
        self.QtStack.addWidget(self.stack23)
        self.QtStack.addWidget(self.stack24)
        self.QtStack.addWidget(self.stack25)
        self.QtStack.addWidget(self.stack26)
        self.QtStack.addWidget(self.stack27)
        self.QtStack.addWidget(self.stack28)
        self.QtStack.addWidget(self.stack29)
        self.QtStack.addWidget(self.stack30)
        self.QtStack.addWidget(self.stack31)

        #Drone
        self.QtStack.addWidget(self.stack32)
        self.QtStack.addWidget(self.stack33)
        self.QtStack.addWidget(self.stack34)
        self.QtStack.addWidget(self.stack35)
        self.QtStack.addWidget(self.stack36)
        self.QtStack.addWidget(self.stack37)
        self.QtStack.addWidget(self.stack38)
        self.QtStack.addWidget(self.stack39)
        
        
    def HomePage(self):
        self.stack1.resize(1000, 600)
        self.stack1.setWindowTitle("Restaurant Supply Express")
        self.stack1.BGcolor = 'aliceblue'
        self.stack1.setStyleSheet(f"background-color: {self.stack1.BGcolor};")

        box = QVBoxLayout()

        #Add Label
        self.homeLabel = QLabel("I wish to access...")
        self.homeLabel.setStyleSheet("color: pink; font: bold 40px;")
        self.homeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.homeLabel.setGeometry(QtCore.QRect(437, 0, 200, 100))
        box.addWidget(self.homeLabel)

        #Ingredients
        self.IngredientsButton = QtWidgets.QPushButton(self.stack1)
        self.IngredientsButton.setText("Ingredients")
        self.IngredientsButton.setGeometry(QtCore.QRect(437, 50, 125, 50))
        self.IngredientsButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.IngredientsButton)

        #Delivery Services
        self.DSButton = QtWidgets.QPushButton(self.stack1)
        self.DSButton.setText("Delivery Services")
        self.DSButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.DSButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.DSButton)

        #Owners
        self.OwnersButton = QtWidgets.QPushButton(self.stack1)
        self.OwnersButton.setText("Owners")
        self.OwnersButton.setGeometry(QtCore.QRect(437, 200, 125, 50))
        self.OwnersButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.OwnersButton)

        #Employee
        self.EmployeeButton = QtWidgets.QPushButton(self.stack1)
        self.EmployeeButton.setText("Employees")
        self.EmployeeButton.setGeometry(QtCore.QRect(437, 275, 125, 50))
        self.EmployeeButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.EmployeeButton)

        #Locations
        self.LocationsButton = QtWidgets.QPushButton(self.stack1)
        self.LocationsButton.setText("Locations")
        self.LocationsButton.setGeometry(QtCore.QRect(437, 350, 125, 50))
        self.LocationsButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.LocationsButton)

        #Restaurants
        self.RestaurantsButton = QtWidgets.QPushButton(self.stack1)
        self.RestaurantsButton.setText("Restaurants")
        self.RestaurantsButton.setGeometry(QtCore.QRect(437, 425, 125, 50))
        self.RestaurantsButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.RestaurantsButton)

        #Drones
        self.DronesButton = QtWidgets.QPushButton(self.stack1)
        self.DronesButton.setText("Drones")
        self.DronesButton.setGeometry(QtCore.QRect(437, 500, 125, 50))
        self.DronesButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.DronesButton)

        box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #Set Layout (adds all items in box as the layout)
        self.stack1.setLayout(box)    

    def OwnerUI(self):
        self.stack2.resize(1000, 600)
        self.stack2.setWindowTitle("Owner")
        self.stack2.BGcolor = 'aliceblue'
        self.stack2.setStyleSheet(f"background-color: {self.stack2.BGcolor};")

        box = QVBoxLayout()

        #Add Label
        self.stack2.ownerLabel = QLabel("I wish to access...")
        self.stack2.ownerLabel.setStyleSheet("color: pink; font: bold 40px;")
        self.stack2.ownerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack2.ownerLabel.setGeometry(QtCore.QRect(437, 0, 200, 100))
        box.addWidget(self.stack2.ownerLabel)

        #Add Owner
        self.addOwnerButton = QtWidgets.QPushButton(self.stack2)
        self.addOwnerButton.setText("Add Owner")
        self.addOwnerButton.setGeometry(QtCore.QRect(437, 50, 125, 50))
        self.addOwnerButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.addOwnerButton)

        #View Owner
        self.viewOwnerButton = QtWidgets.QPushButton(self.stack2)
        self.viewOwnerButton.setText("View Owners")
        self.viewOwnerButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.viewOwnerButton.setStyleSheet("background-color: yellow;")
        self.viewOwnerButton.clicked.connect(self.ViewOwnerUI)
        box.addWidget(self.viewOwnerButton)

        #Start Funding
        self.viewFundingButton = QtWidgets.QPushButton(self.stack2)
        self.viewFundingButton.setText("Start Funding")
        self.viewFundingButton.setGeometry(QtCore.QRect(437, 200, 125, 50))
        self.viewFundingButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.viewFundingButton)

        #Return to the main window
        self.menuButton1 = QPushButton("Back to Main Menu")
        self.menuButton1.setGeometry(QtCore.QRect(10, 10, 200, 30))
        self.menuButton1.setStyleSheet("background-color: yellow;")
        box.addWidget(self.menuButton1)

        box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack2.setLayout(box)

        
    def ViewOwnerUI(self):
        self.stack3.resize(1000, 600)
        self.stack3.setWindowTitle("View Owner")
        self.updateViewOwner()

    def updateViewOwner(self):
        try:
            result = []
            with connection.cursor() as cursor:
                query = "select username, first_name, last_name, address, count(long_name), count(distinct location) , max(COALESCE( rating , 0)) as max_rating, min(COALESCE(rating,0)) as min_rating, sum(COALESCE(spent,0)) as total_debt from users left join restaurants on users.username= restaurants.funded_by where username in (select username from restaurant_owners) group by users.username"
                cursor.execute(query, None)
                result = cursor.fetchall()
                connection.commit()
            
            data = {'username':[],
                    'first_name':[],
                    'last_name':[],
                    'address': [],
                    'num_restaurants':[],
                    'num_places':[],
                    'highs':[],
                    'lows': [],
                    'debt': []
                    }
            
            for owner in result:
                data['username'].append(owner['username'])
                data['first_name'].append(owner['first_name'])
                data['last_name'].append(owner['last_name'])
                data['address'].append(owner['address'])
                data['num_restaurants'].append(owner['count(distinct location)'])
                data['num_places'].append(owner['count(long_name)'])
                data['highs'].append(owner['max_rating'])
                data['lows'].append(owner['min_rating'])
                data['debt'].append(owner['total_debt'])

            self.stack3.layout = QVBoxLayout()
            self.stack3.tableWidget = QTableWidget(len(result), 9)
            self.stack3.tableWidget.setHorizontalHeaderLabels(["username", "first_name", "last_name", "address", "num_restaurants", "num_places", "highs", "lows", "debt"])
            self.stack3.tableWidget.setColumnWidth(0, 150)


            for num in range(len(result)):
                self.stack3.tableWidget.setItem(num,0, QTableWidgetItem(data['username'][num]))
                self.stack3.tableWidget.setItem(num,1, QTableWidgetItem(data['first_name'][num]))
                self.stack3.tableWidget.setItem(num,2, QTableWidgetItem(data['last_name'][num]))
                self.stack3.tableWidget.setItem(num,3, QTableWidgetItem(data['address'][num]))
                self.stack3.tableWidget.setItem(num,4, QTableWidgetItem(str(data['num_restaurants'][num])))
                self.stack3.tableWidget.setItem(num,5, QTableWidgetItem(str(data['num_places'][num])))
                self.stack3.tableWidget.setItem(num,6, QTableWidgetItem(str(data['highs'][num])))
                self.stack3.tableWidget.setItem(num,7, QTableWidgetItem(str(data['lows'][num])))
                self.stack3.tableWidget.setItem(num,8, QTableWidgetItem(str(data['debt'][num])))
            
            self.btoButton2 = QPushButton("Back to Owner Menu")
            self.btoButton2.setGeometry(QtCore.QRect(10, 10, 200, 30))

            self.stack3.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.stack3.layout.addWidget(self.stack3.tableWidget)
            self.stack3.layout.addWidget(self.btoButton2)
            self.stack3.setLayout(self.stack3.layout)

        except:
            self.stack3.resize(1000, 600)
            self.stack3.setStyleSheet("background: pink")
            errorBox= QVBoxLayout()
            self.stack3.user = QLabel("View Failed to Open")
            self.stack3.user.setStyleSheet('font: bold 40px')
            self.stack3.user.setAlignment(Qt.AlignmentFlag.AlignCenter)
            errorBox.addWidget(self.stack3.user)
            self.stack3.setLayout(errorBox)

            
    def AddOwnerUI(self):
        self.stack4.resize(1000, 600)
        self.stack4.setWindowTitle("Add Owner")

        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack4.BGcolor = 'aliceblue'
        self.stack4.setStyleSheet(f"background-color: {self.stack4.BGcolor};")

        #Title USER
        self.stack4.user = QLabel("Add Owner")
        self.stack4.user.setStyleSheet('font: bold 40px;')
        self.stack4.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack4.nlabel= QLabel("If a value is null type 'null'")
        self.stack4.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack4.nlabel.setStyleSheet('font: bold 20px;')
        self.stack4.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack4.AOUN = QLabel("Username: ")
        self.stack4.AOUN.setFixedSize(200, 40)
        self.stack4.AOUN.setStyleSheet("font: 30px;")
        self.stack4.AOUNIN = QLineEdit("")
        self.stack4.AOUNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack4.AOFN = QLabel("First Name: ")
        self.stack4.AOFN.setFixedSize(200, 40)
        self.stack4.AOFN.setStyleSheet("font: 30px;")
        self.stack4.AOFNIN = QLineEdit("")
        self.stack4.AOFNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack4.AOLN = QLabel("Last Name: ")
        self.stack4.AOLN.setFixedSize(200, 40)
        self.stack4.AOLN.setStyleSheet("font: 30px;")
        self.stack4.AOLNIN = QLineEdit("")
        self.stack4.AOLNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack4.Address = QLabel("Address: ")
        self.stack4.Address.setFixedSize(200, 40)
        self.stack4.Address.setStyleSheet("font: 30px;")
        self.stack4.AddIN = QLineEdit("")
        self.stack4.AddIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack4.birthday = QLabel("Birthday: ")
        self.stack4.birthday.setFixedSize(200, 40)
        self.stack4.birthday.setStyleSheet("font: 30px;")
        self.stack4.bdIN = QLineEdit("")
        self.stack4.bdIN.setStyleSheet("background-color: white; border: 1px solid black;")

        #Horizontal Boxes
        hboxUN = QHBoxLayout()
        hboxname = QHBoxLayout()
        hboxAB = QHBoxLayout()

        self.stack4.inputnum = [""]

        hboxUN.addWidget(self.stack4.AOUN)
        hboxUN.addWidget(self.stack4.AOUNIN)

        hboxname.addWidget(self.stack4.AOFN)
        hboxname.addWidget(self.stack4.AOFNIN)
        hboxname.addWidget(self.stack4.AOLN)
        hboxname.addWidget(self.stack4.AOLNIN)

        hboxAB.addWidget(self.stack4.Address)
        hboxAB.addWidget(self.stack4.AddIN)
        hboxAB.addWidget(self.stack4.birthday)
        hboxAB.addWidget(self.stack4.bdIN)


        #Add all Horizontal Boxes
        self.stack4.addOwner = QPushButton("Add Owner", self.stack4)
        self.stack4.addOwner.setFixedSize(200, 40)
        self.stack4.addOwner.setStyleSheet("background-color: yellow;")
        self.stack4.addOwner.clicked.connect(self.addOwner)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack4.addOwner)
        
        self.btoButton1 = QPushButton("Back to Owner Menu")
        self.btoButton1.setFixedSize(200, 40)
        self.btoButton1.setStyleSheet("background-color: yellow;")
        buttonbox.addWidget(self.btoButton1)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack4.user) #this is the label that says USER
        BIGbox.addWidget(self.stack4.nlabel)
        BIGbox.addLayout(hboxUN) #this is the label that says 'username:' and the response box
        BIGbox.addLayout(hboxname) #same for first and last name
        BIGbox.addLayout(hboxAB) #same for address and birthday
        BIGbox.addLayout(buttonbox) #same for the Add Owner button
        
        self.stack4.setLayout(BIGbox)

    def addOwner(self):

        try:
            username = self.stack4.AOUNIN.text()
            first_name = self.stack4.AOFNIN.text()
            last_name = self.stack4.AOLNIN.text()
            address = self.stack4.AddIN.text()
            birthdate = self.stack4.bdIN.text()
            with connection.cursor() as cursor:
                query = "call add_owner('{}', '{}', '{}', '{}', '{}')".format(username, first_name, last_name, address, birthdate)
                cursor.execute(query, None)
                connection.commit()
            self.stack4.AOUNIN.clear()
            self.stack4.AOFNIN.clear()
            self.stack4.AOLNIN.clear()
            self.stack4.AddIN.clear()
            self.stack4.bdIN.clear()
        except:
            error_dialog.showMessage('Add Owner Failed! Make sure you have all fields entered correctly.')

            
    def StartFundingUI(self):
        self.stack5.resize(1000, 600)
        self.stack5.setWindowTitle("Start Funding")

        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack5.BGcolor = 'aliceblue'
        self.stack5.setStyleSheet(f"background-color: {self.stack5.BGcolor};")

        #Title USER
        self.stack5.user = QLabel("Start Funding")
        self.stack5.user.setStyleSheet('font: bold 40px;')
        self.stack5.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack5.nlabel= QLabel("If a value is null type 'null'")
        self.stack5.nlabel.setStyleSheet('font: bold 20px;')
        self.stack5.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack5.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack5.SFUN = QLabel("Username: ")
        self.stack5.SFUN.setFixedSize(200, 40)
        self.stack5.SFUN.setStyleSheet("font: 30px;")
        self.stack5.SFUIN = QLineEdit("")
        self.stack5.SFUIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack5.SFRN = QLabel("Restaurant \nName: ")
        self.stack5.SFRN.setFixedSize(200, 100)
        self.stack5.SFRN.setStyleSheet("font: 30px;")
        self.stack5.SFRNIN = QLineEdit("")
        self.stack5.SFRNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        #Horizontal Boxes
        hboxUN = QHBoxLayout()
        hboxname = QHBoxLayout()

        self.stack5.inputnum = [""]

        hboxUN.addWidget(self.stack5.SFUN)
        hboxUN.addWidget(self.stack5.SFUIN)

        hboxname.addWidget(self.stack5.SFRN)
        hboxname.addWidget(self.stack5.SFRNIN)

        #Add all Horizontal Boxes
        self.stack5.startFunding = QPushButton("Start Funding", self.stack5)
        self.stack5.startFunding.setFixedSize(200, 40)
        self.stack5.startFunding.setStyleSheet("background-color: yellow;")
        self.stack5.startFunding.clicked.connect(self.startFunding)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack5.startFunding)
        
        self.btoButton3 = QPushButton("Back to Owner Menu")
        self.btoButton3.setFixedSize(200, 40)
        self.btoButton3.setStyleSheet("background-color: yellow;")
        buttonbox.addWidget(self.btoButton3)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack5.user) #this is the label that says USER
        BIGbox.addWidget(self.stack5.nlabel)
        BIGbox.addLayout(hboxUN) #this is the label that says 'username:' and the response box
        BIGbox.addLayout(hboxname) # ^^ for restaurant name
        BIGbox.addLayout(buttonbox) #same for the Add Owner button

        self.stack5.setLayout(BIGbox)
        
    def startFunding(self):

        try:
            username = self.stack5.SFUIN.text()
            long_name = self.stack5.SFRNIN.text()
            with connection.cursor() as cursor:
                query = "call start_funding('{}', '{}')".format(username, long_name)
                cursor.execute(query, None)
                connection.commit()
            self.stack5.SFUIN.clear()
            self.stack5.SFRNIN.clear()
        except:
            error_dialog.showMessage('Start Funding Failed! Make sure you have all fields entered correctly.')

    def DeliveryServiceUI(self):
        self.stack6.resize(1000, 600)
        self.stack6.setWindowTitle("Delivery Service")
        self.stack6.BGcolor = 'aliceblue'
        self.stack6.setStyleSheet(f"background-color: {self.stack6.BGcolor};")

        box = QVBoxLayout()

        #Add Label
        self.stack6.dsLabel = QLabel("I wish to access...")
        self.stack6.dsLabel.setStyleSheet("color: pink; font: bold 40px;")
        self.stack6.dsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack6.dsLabel.setGeometry(QtCore.QRect(437, 0, 200, 100))
        box.addWidget(self.stack6.dsLabel)

        #Add Service
        self.addServiceButton = QtWidgets.QPushButton(self.stack6)
        self.addServiceButton.setText("Add Service")
        self.addServiceButton.setGeometry(QtCore.QRect(437, 50, 125, 50))
        self.addServiceButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.addServiceButton)

        #Manage Service
        self.manageServiceButton = QtWidgets.QPushButton(self.stack6)
        self.manageServiceButton.setText("Manage Service")
        self.manageServiceButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.manageServiceButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.manageServiceButton)

        #Hire Employee
        self.hireEmployeeButton = QtWidgets.QPushButton(self.stack6)
        self.hireEmployeeButton.setText("Hire Employee")
        self.hireEmployeeButton.setGeometry(QtCore.QRect(437, 200, 125, 50))
        self.hireEmployeeButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.hireEmployeeButton)

        #Fire Employee
        self.fireEmployeeButton = QtWidgets.QPushButton(self.stack6)
        self.fireEmployeeButton.setText("Fire Employee")
        self.fireEmployeeButton.setGeometry(QtCore.QRect(437, 275, 125, 50))
        self.fireEmployeeButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.fireEmployeeButton)

        #Display Service View
        self.viewServiceButton = QtWidgets.QPushButton(self.stack6)
        self.viewServiceButton.setText("Display Service View")
        self.viewServiceButton.setGeometry(QtCore.QRect(437, 350, 125, 50))
        self.viewServiceButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.viewServiceButton)

        #Return to the main window
        self.menuButton3 = QPushButton("Back to Main Menu")
        self.menuButton3.setGeometry(QtCore.QRect(10, 10, 200, 30))
        self.menuButton3.setStyleSheet("background-color: yellow;")
        box.addWidget(self.menuButton3)

        box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack6.setLayout(box)


    def AddServiceUI(self):
        self.stack7.resize(1000, 600)
        self.stack7.setWindowTitle("Add Service")

        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack7.BGcolor = 'aliceblue'
        self.stack7.setStyleSheet(f"background-color: {self.stack7.BGcolor};")

        #Title USER
        self.stack7.user = QLabel("Add Service")
        self.stack7.user.setStyleSheet('font: bold 40px;')
        self.stack7.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack7.nlabel= QLabel("If a value is null type 'null'")
        self.stack7.nlabel.setStyleSheet('font: bold 20px;')
        self.stack7.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack7.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        # Inputs
        self.stack7.ASID = QLabel("ID: ")
        self.stack7.ASID.setFixedSize(200, 40)
        self.stack7.ASID.setStyleSheet("font: 30px;")
        self.stack7.ASIDIN = QLineEdit("")
        self.stack7.ASIDIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack7.ASSN = QLabel("Service Name: ")
        self.stack7.ASSN.setFixedSize(200, 40)
        self.stack7.ASSN.setStyleSheet("font: 30px;")
        self.stack7.ASSNIN = QLineEdit("")
        self.stack7.ASSNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack7.ASHB = QLabel("Home Base: ")
        self.stack7.ASHB.setFixedSize(200, 40)
        self.stack7.ASHB.setStyleSheet("font: 30px;")
        self.stack7.ASHBIN = QLineEdit("")
        self.stack7.ASHBIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack7.ASMU = QLabel("Manager \nUsername: ")
        self.stack7.ASMU.setFixedSize(200, 100)
        self.stack7.ASMU.setStyleSheet("font: 30px;")
        self.stack7.ASMUIN = QLineEdit("")
        self.stack7.ASMUIN.setStyleSheet("background-color: white; border: 1px solid black;")

        #Horizontal Boxes
        hboxtop = QHBoxLayout()
        hboxbottom = QHBoxLayout()

        self.stack7.inputnum = [""]

        hboxtop.addWidget(self.stack7.ASID)
        hboxtop.addWidget(self.stack7.ASIDIN)
        hboxtop.addWidget(self.stack7.ASSN)
        hboxtop.addWidget(self.stack7.ASSNIN)

        hboxbottom.addWidget(self.stack7.ASHB)
        hboxbottom.addWidget(self.stack7.ASHBIN)
        hboxbottom.addWidget(self.stack7.ASMU)
        hboxbottom.addWidget(self.stack7.ASMUIN)


        #Add all Horizontal Boxes
        self.stack7.addService = QPushButton("Add Service", self.stack7)
        self.stack7.addService.setFixedSize(200, 40)
        self.stack7.addService.clicked.connect(self.addService)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack7.addService)
        
        self.btdsButton1 = QPushButton("Back to Delivery Service Menu")
        self.btdsButton1.setFixedSize(200, 40)
        buttonbox.addWidget(self.btdsButton1)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack7.user) 
        BIGbox.addWidget(self.stack7.nlabel)
        BIGbox.addLayout(hboxtop) 
        BIGbox.addLayout(hboxbottom) 
        BIGbox.addLayout(buttonbox)

        self.stack7.setLayout(BIGbox)

    def addService(self):

        try:
            ID = self.stack7.ASIDIN.text()
            SN = self.stack7.ASSNIN.text()
            HB = self.stack7.ASHBIN.text()
            MU = self.stack7.ASMUIN.text()
            with connection.cursor() as cursor:
                query = "call add_service('{}', '{}', '{}', '{}')".format(ID, SN, HB, MU)
                cursor.execute(query, None)
                connection.commit()
            self.stack7.ASIDIN.clear()
            self.stack7.ASSNIN.clear()
            self.stack7.ASHBIN.clear()
            self.stack7.ASMUIN.clear()

        except:
            error_dialog.showMessage('Add Service Failed! Make sure you have all fields entered correctly.')

    def ManageServiceUI(self):
        self.stack8.resize(1000, 600)
        self.stack8.setWindowTitle("Manage Service")

        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack8.BGcolor = 'aliceblue'
        self.stack8.setStyleSheet(f"background-color: {self.stack8.BGcolor};")

        #Title USER
        self.stack8.user = QLabel("Manage Service")
        self.stack8.user.setStyleSheet('font: bold 40px;')
        self.stack8.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack8.nlabel= QLabel("If a value is null type 'null'")
        self.stack8.nlabel.setStyleSheet('font: bold 20px;')
        self.stack8.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack8.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack8.MSUN = QLabel("Username: ")
        self.stack8.MSUN.setFixedSize(200, 40)
        self.stack8.MSUN.setStyleSheet("font: 30px;")
        self.stack8.MSUNIN = QLineEdit("")
        self.stack8.MSUNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack8.MSID = QLabel("ID: ")
        self.stack8.MSID.setFixedSize(200, 40)
        self.stack8.MSID.setStyleSheet("font: 30px;")
        self.stack8.MSIDIN = QLineEdit("")
        self.stack8.MSIDIN.setStyleSheet("background-color: white; border: 1px solid black;")

        #Horizontal Boxes
        hboxUN = QHBoxLayout()
        hboxname = QHBoxLayout()

        self.stack8.inputnum = [""]

        hboxUN.addWidget(self.stack8.MSUN)
        hboxUN.addWidget(self.stack8.MSUNIN)

        hboxname.addWidget(self.stack8.MSID)
        hboxname.addWidget(self.stack8.MSIDIN)

        #Add all Horizontal Boxes
        self.stack8.manageService = QPushButton("Manage Service", self.stack8)
        self.stack8.manageService.setFixedSize(200, 40)
        self.stack8.manageService.setStyleSheet("background-color: yellow;")
        self.stack8.manageService.clicked.connect(self.manageService)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack8.manageService)
        
        self.btdsButton2 = QPushButton("Back to Delivery Service Menu")
        self.btdsButton2.setFixedSize(200, 40)
        self.btdsButton2.setStyleSheet("background-color: yellow;")
        buttonbox.addWidget(self.btdsButton2)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack8.user) #this is the label that says USER
        BIGbox.addWidget(self.stack8.nlabel)
        BIGbox.addLayout(hboxUN) 
        BIGbox.addLayout(hboxname) 
        BIGbox.addLayout(buttonbox) #same for the Add Owner button

        self.stack8.setLayout(BIGbox)

    def manageService(self):

        try:
            ID = self.stack8.MSIDIN.text()
            username = self.stack8.MSUNIN.text()
            with connection.cursor() as cursor:
                query = "call manage_service('{}', '{}')".format(username, ID)
                cursor.execute(query, None)
                connection.commit()

            self.stack8.MSIDIN.clear()
            self.stack8.MSUNIN.clear()

        except:
            error_dialog.showMessage('Manage Service Failed! Make sure you have all fields entered correctly.')

    def HireEmployeeUI(self):
        self.stack9.resize(1000, 600)
        self.stack9.setWindowTitle("Hire Employee")

        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack9.BGcolor = 'aliceblue'
        self.stack9.setStyleSheet(f"background-color: {self.stack8.BGcolor};")

        #Title USER
        self.stack9.user = QLabel("Hire Employee")
        self.stack9.user.setStyleSheet('font: bold 40px;')
        self.stack9.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack9.nlabel= QLabel("If a value is null type 'null'")
        self.stack9.nlabel.setStyleSheet('font: bold 20px;')
        self.stack9.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack9.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack9.HEUN = QLabel("Username: ")
        self.stack9.HEUN.setFixedSize(200, 40)
        self.stack9.HEUN.setStyleSheet("font: 30px;")
        self.stack9.HEUNIN = QLineEdit("")
        self.stack9.HEUNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack9.HEID = QLabel("ID: ")
        self.stack9.HEID.setFixedSize(200, 40)
        self.stack9.HEID.setStyleSheet("font: 30px;")
        self.stack9.HEIDIN = QLineEdit("")
        self.stack9.HEIDIN.setStyleSheet("background-color: white; border: 1px solid black;")

        #Horizontal Boxes
        hboxUN = QHBoxLayout()
        hboxname = QHBoxLayout()

        self.stack9.inputnum = [""]

        hboxUN.addWidget(self.stack9.HEUN)
        hboxUN.addWidget(self.stack9.HEUNIN)

        hboxname.addWidget(self.stack9.HEID)
        hboxname.addWidget(self.stack9.HEIDIN)

        #Add all Horizontal Boxes
        self.stack9.hireEmployee = QPushButton("Hire Employee", self.stack9)
        self.stack9.hireEmployee.setFixedSize(200, 40)
        self.stack9.hireEmployee.setStyleSheet("background-color: yellow;")
        self.stack9.hireEmployee.clicked.connect(self.hireEmployee)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack9.hireEmployee)
        
        self.btdsButton3 = QPushButton("Back to Delivery Service Menu")
        self.btdsButton3.setFixedSize(200, 40)
        self.btdsButton3.setStyleSheet("background-color: yellow;")
        buttonbox.addWidget(self.btdsButton3)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack9.user) #this is the label that says USER
        BIGbox.addWidget(self.stack9.nlabel)
        BIGbox.addLayout(hboxUN) 
        BIGbox.addLayout(hboxname) 
        BIGbox.addLayout(buttonbox) #same for the Add Owner button

        self.stack9.setLayout(BIGbox)

    def hireEmployee(self):

        try:
            ID = self.stack9.HEIDIN.text()
            username = self.stack9.HEUNIN.text()
            with connection.cursor() as cursor:
                query = "call hire_employee('{}', '{}')".format(username, ID)
                cursor.execute(query, None)
                connection.commit()
            self.stack9.HEIDIN.clear()
            self.stack9.HEUNIN.clear()

        except:
            error_dialog.showMessage('Hire Employee Failed! Make sure you have all fields entered correctly.')

    def FireEmployeeUI(self):
        self.stack10.resize(1000, 600)
        self.stack10.setWindowTitle("Hire Employee")

        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack10.BGcolor = 'aliceblue'
        self.stack10.setStyleSheet(f"background-color: {self.stack10.BGcolor};")

        #Title USER
        self.stack10.user = QLabel("Fire Employee")
        self.stack10.user.setStyleSheet('font: bold 40px;')
        self.stack10.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack10.nlabel= QLabel("If a value is null type 'null'")
        self.stack10.nlabel.setStyleSheet('font: bold 20px;')
        self.stack10.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack10.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack10.FEUN = QLabel("Username: ")
        self.stack10.FEUN.setFixedSize(200, 40)
        self.stack10.FEUN.setStyleSheet("font: 30px;")
        self.stack10.FEUNIN = QLineEdit("")
        self.stack10.FEUNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack10.FEID = QLabel("ID: ")
        self.stack10.FEID.setFixedSize(200, 40)
        self.stack10.FEID.setStyleSheet("font: 30px;")
        self.stack10.FEIDIN = QLineEdit("")
        self.stack10.FEIDIN.setStyleSheet("background-color: white; border: 1px solid black;")

        #Horizontal Boxes
        hboxUN = QHBoxLayout()
        hboxname = QHBoxLayout()

        self.stack9.inputnum = [""]

        hboxUN.addWidget(self.stack10.FEUN)
        hboxUN.addWidget(self.stack10.FEUNIN)

        hboxname.addWidget(self.stack10.FEID)
        hboxname.addWidget(self.stack10.FEIDIN)

        #Add all Horizontal Boxes
        self.stack10.fireEmployee = QPushButton("Fire Employee", self.stack10)
        self.stack10.fireEmployee.setFixedSize(200, 40)
        self.stack10.fireEmployee.setStyleSheet("background-color: yellow;")
        self.stack10.fireEmployee.clicked.connect(self.fireEmployee)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack10.fireEmployee)
        
        self.btdsButton4 = QPushButton("Back to Delivery Service Menu")
        self.btdsButton4.setFixedSize(200, 40)
        self.btdsButton4.setStyleSheet("background-color: yellow;")
        buttonbox.addWidget(self.btdsButton4)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack10.user) #this is the label that says USER
        BIGbox.addWidget(self.stack10.nlabel)
        BIGbox.addLayout(hboxUN) 
        BIGbox.addLayout(hboxname) 
        BIGbox.addLayout(buttonbox) #same for the Add Owner button

        self.stack10.setLayout(BIGbox)

    def fireEmployee(self):

        try:
            ID = self.stack10.FEIDIN.text()
            username = self.stack10.FEUNIN.text()
            with connection.cursor() as cursor:
                query = "call fire_employee('{}', '{}')".format(username, ID)
                cursor.execute(query, None)
                connection.commit()
            self.stack10.FEIDIN.clear()
            self.stack10.FEUNIN.clear()

        except:
            error_dialog.showMessage('Fire Employee Failed! Make sure you have all fields entered correctly.')

    def ViewServiceUI(self):
        self.stack11.resize(1000, 600)
        self.stack11.setWindowTitle("View Services")
        self.updateViewService()

    def updateViewService(self):
        try:
            result = []
            with connection.cursor() as cursor:
                query = "select distinct delivery_services.id, long_name, home_base, manager, sum(distinct drones.sales) as revenue, count(distinct payload.barcode) as ingredients_carried, "
                query +="cast(((sum(price*quantity))/count(distinct drones.tag)) as float) as cost_carried, cast(((sum(quantity*weight))/count(distinct drones.tag))as float) as weight_carried "
                query += "from delivery_services left outer join payload on delivery_services.id=payload.id left outer join ingredients on ingredients.barcode= payload.barcode left outer join drones on drones.id= delivery_services.id "
                query += "GROUP BY delivery_services.id;"
                cursor.execute(query, None)
                result = cursor.fetchall()
                connection.commit()
            
            data = {'id':[],
                    'long_name':[],
                    'home_base':[],
                    'manager': [],
                    'revenue':[],
                    'ingredients_carried':[],
                    'cost_carried':[],
                    'weight_carried': []
                    }
            
            for ds in result:
                data['id'].append(ds['id'])
                data['long_name'].append(ds['long_name'])
                data['home_base'].append(ds['home_base'])
                data['manager'].append(ds['manager'])
                data['revenue'].append(ds['revenue'])
                data['ingredients_carried'].append(ds['ingredients_carried'])
                data['cost_carried'].append(ds['cost_carried'])
                data['weight_carried'].append(ds['weight_carried'])

            self.stack11.layout = QVBoxLayout()
            self.stack11.tableWidget = QTableWidget(len(result), 8)
            self.stack11.tableWidget.setHorizontalHeaderLabels(["id", "long_name", "home_base", "manager", "revenue", "ingredients_carried", "cost_carried", "weight_carried"])
            self.stack11.tableWidget.setColumnWidth(0, 150)


            for num in range(len(result)):
                self.stack11.tableWidget.setItem(num,0, QTableWidgetItem(str(data['id'][num])))
                self.stack11.tableWidget.setItem(num,1, QTableWidgetItem(str(data['long_name'][num])))
                self.stack11.tableWidget.setItem(num,2, QTableWidgetItem(str(data['home_base'][num])))
                self.stack11.tableWidget.setItem(num,3, QTableWidgetItem(str(data['manager'][num])))
                self.stack11.tableWidget.setItem(num,4, QTableWidgetItem(str(data['revenue'][num])))
                self.stack11.tableWidget.setItem(num,5, QTableWidgetItem(str(data['ingredients_carried'][num])))
                self.stack11.tableWidget.setItem(num,6, QTableWidgetItem(str(data['cost_carried'][num])))
                self.stack11.tableWidget.setItem(num,7, QTableWidgetItem(str(data['weight_carried'][num])))
            
            self.btdsButton5 = QPushButton("Back to Delivery Service Menu")
            self.btdsButton5.setGeometry(QtCore.QRect(10, 10, 200, 30))

            self.stack11.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.stack11.layout.addWidget(self.stack11.tableWidget)
            self.stack11.layout.addWidget(self.btdsButton5)
            self.stack11.setLayout(self.stack11.layout)
            
        except:
            self.stack11.resize(1000, 600)
            self.stack11.setStyleSheet("background: pink")
            oops= QVBoxLayout()
            self.stack11.user = QLabel("View Failed")
            self.stack11.user.setStyleSheet('font: bold 40px')
            self.stack11.user.setAlignment(Qt.AlignmentFlag.AlignCenter)
            oops.addWidget(self.stack11.user)
            self.stack11.setLayout(oops)
            
#Ingredient stuff
    def IngredientUI(self):
        self.stack12.resize(1000, 600)
        self.stack12.setWindowTitle("Restaurant Supply Express")
        self.stack12.BGcolor = 'aliceblue'
        self.stack12.setStyleSheet(f"background-color: {self.stack12.BGcolor};")

        Ibox = QVBoxLayout()

        #Add Label
        self.stack12.ingredientLabel = QLabel("I wish to access...")
        self.stack12.ingredientLabel.setStyleSheet("color: pink; font: bold 40px;")
        self.stack12.ingredientLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack12.ingredientLabel.setGeometry(QtCore.QRect(437, 0, 200, 100))
        Ibox.addWidget(self.stack12.ingredientLabel)

        #Add Ingredient
        self.addIngButton = QtWidgets.QPushButton(self.stack12)
        self.addIngButton.setText("Add Ingredient")
        self.addIngButton.setGeometry(QtCore.QRect(437, 50, 125, 50))
        self.addIngButton.setStyleSheet("background-color: yellow;")
        Ibox.addWidget(self.addIngButton)

        #View Ingredient
        self.viewIngButton = QtWidgets.QPushButton(self.stack12)
        self.viewIngButton.setText("View Ingredients")
        self.viewIngButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.viewIngButton.setStyleSheet("background-color: yellow;")
        Ibox.addWidget(self.viewIngButton)


        #Remove Ingredient
        self.removeIngButton = QtWidgets.QPushButton(self.stack12)
        self.removeIngButton.setText("Remove Ingredients")
        self.removeIngButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.removeIngButton.setStyleSheet("background-color: yellow;")
        Ibox.addWidget(self.removeIngButton)


        #Return to the main window
        self.menuButton2 = QPushButton("Back to Main Menu")
        self.menuButton2.setGeometry(QtCore.QRect(10, 10, 200, 30))
        self.menuButton2.setStyleSheet("background-color: yellow;")
        Ibox.addWidget(self.menuButton2)

        Ibox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack12.setLayout(Ibox)

    def addIngredientUI(self):
        self.stack13.resize(1000, 600)
        self.stack13.setWindowTitle("Add Ingredient")

        BIGIbox = QVBoxLayout()

        #Background of the GUI
        self.stack13.BGcolor = 'aliceblue'
        self.stack13.setStyleSheet(f"background-color: {self.stack13.BGcolor};")

        #Title USER
        self.stack13.ingredient = QLabel("Ingredient")
        self.stack13.ingredient.setStyleSheet('font: bold 40px;')
        self.stack13.ingredient.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack13.nlabel= QLabel("If a value is null type 'null'")
        self.stack13.nlabel.setStyleSheet('font: bold 20px;')
        self.stack13.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack13.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack13.BC = QLabel("Barcode: ")
        self.stack13.BC.setFixedSize(200, 40)
        self.stack13.BC.setStyleSheet("font: 30px;")
        self.stack13.BCIN = QLineEdit("")
        self.stack13.BCIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack13.IngN = QLabel("Ingredient: ")
        self.stack13.IngN.setFixedSize(200, 40)
        self.stack13.IngN.setStyleSheet("font: 30px;")
        self.stack13.IngNIN = QLineEdit("")
        self.stack13.IngNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack13.WN = QLabel("Unit Weight: ")
        self.stack13.WN.setFixedSize(200, 40)
        self.stack13.WN.setStyleSheet("font: 30px;")
        self.stack13.WNIN = QLineEdit("")
        self.stack13.WNIN.setStyleSheet("background-color: white; border: 1px solid black;")


        #Horizontal Boxes
        hboxBC = QHBoxLayout()
        hboxIname = QHBoxLayout()
        hboxW = QHBoxLayout()

        self.stack13.inputnum = [""]

        hboxBC.addWidget(self.stack13.BC)
        hboxBC.addWidget(self.stack13.BCIN)

        hboxIname.addWidget(self.stack13.IngN)
        hboxIname.addWidget(self.stack13.IngNIN)

        hboxW.addWidget(self.stack13.WN)
        hboxW.addWidget(self.stack13.WNIN)



        #Add all Horizontal Boxes
        self.stack13.addIngredient = QPushButton("Add Ingredient", self.stack13)
        self.stack13.addIngredient.setFixedSize(200, 40)
        self.stack13.addIngredient.setStyleSheet("background-color: yellow;")
        self.stack13.addIngredient.clicked.connect(self.addIngredient)

        buttonboxi = QHBoxLayout()
        buttonboxi.addWidget(self.stack13.addIngredient)
        
        self.btiButton1 = QPushButton("Back to Ingredient Menu")
        self.btiButton1.setFixedSize(200, 40)
        self.btiButton1.setStyleSheet("background-color: yellow;")
        buttonboxi.addWidget(self.btiButton1)
        buttonboxi.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGIbox.addWidget(self.stack13.ingredient) #this is the label that says USER
        BIGIbox.addWidget(self.stack13.nlabel)
        BIGIbox.addLayout(hboxBC) #this is the label that says 'username:' and the response box
        BIGIbox.addLayout(hboxIname) #same for first and last name
        BIGIbox.addLayout(hboxW) #same for address and birthday
        BIGIbox.addLayout(buttonboxi) #same for the Add Owner button

        self.stack13.setLayout(BIGIbox)

    def addIngredient(self):

        try:
            barcode = self.stack13.BCIN.text()
            ingredient_name = self.stack13.IngNIN.text()
            weight = self.stack13.WNIN.text()
            with connection.cursor() as cursor:
                query = "call add_ingredient('{}', '{}', '{}')".format(barcode, ingredient_name, weight)
                cursor.execute(query, None)
                connection.commit()

            self.stack13.BCIN.clear()
            self.stack13.IngNIN.clear()
            self.stack13.WNIN.clear()
        except:
            # Error Message needed
            error_dialog.showMessage('Add Ingredient Failed! Make sure you have all fields entered correctly.')

    def viewIngredientUI(self):
        self.stack14.resize(1000, 600)
        self.stack14.setWindowTitle("View Ingredient")
        try:
            result = []
            with connection.cursor() as cursor:
                query = "select ingredients.iname, hover, sum(quantity) as amount_available, min(price) as low_price, max(price) as high_price from payload left outer join ingredients on ingredients.barcode= payload.barcode left outer join drones on (drones.id, drones.tag)= (payload.id, payload.tag) group by ingredients.iname, drones.hover;"
                cursor.execute(query, None)
                result = cursor.fetchall()
                connection.commit()
           
            Idata = {'name':[],
                    'location':[],
                    'available':[],
                    'low_price': [],
                    'high_price':[],
                    }
            for ingredient in result:
                Idata['name'].append(ingredient['iname'])
                Idata['location'].append(ingredient['hover'])
                Idata['available'].append(ingredient['amount_available'])
                Idata['low_price'].append(ingredient['low_price'])
                Idata['high_price'].append(ingredient['high_price'])


            
            self.stack14.layout = QVBoxLayout()
            self.stack14.tableWidget = QTableWidget(len(result), 5)
            self.stack14.tableWidget.setHorizontalHeaderLabels(["Ingredient", "Location", "Amount_Available", "Lowest_Price", "Highest_price"])
            self.stack14.tableWidget.setColumnWidth(0, 150)

    
            for num in range(len(result)):
                self.stack14.tableWidget.setItem(num,0, QTableWidgetItem(Idata['name'][num]))
                self.stack14.tableWidget.setItem(num,1, QTableWidgetItem(Idata['location'][num]))
                self.stack14.tableWidget.setItem(num,2, QTableWidgetItem(str(Idata['available'][num])))
                self.stack14.tableWidget.setItem(num,3, QTableWidgetItem(str(Idata['low_price'][num])))
                self.stack14.tableWidget.setItem(num,4, QTableWidgetItem(str(Idata['high_price'][num])))


            self.btiButton2 = QPushButton("Back to Ingredient Menu")
            self.btiButton2.setGeometry(QtCore.QRect(10, 10, 200, 30))


            self.stack14.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.stack14.layout.addWidget(self.stack14.tableWidget)

            self.stack14.layout.addWidget(self.btiButton2)
            
            self.stack14.setLayout(self.stack14.layout)

        except:
            self.stack14.resize(1000, 600)
            self.stack14.setStyleSheet("background: pink")
            errorBox= QVBoxLayout()
            self.stack14.ingredient = QLabel("View Failed to Open")
            self.stack14.ingredient.setStyleSheet('font: bold 40px;')
            self.stack14.ingredient.setAlignment(Qt.AlignmentFlag.AlignCenter)  
            errorBox.addWidget(self.stack14.ingredient)
            self.stack14.setLayout(errorBox)
            
    def removeIngredientUI(self):
        self.stack15.resize(1000, 600)
        self.stack15.setWindowTitle("Remove Ingredient")

        BIGribox = QVBoxLayout()

        #Background of the GUI
        self.stack15.BGcolor = 'aliceblue'
        self.stack15.setStyleSheet(f"background-color: {self.stack15.BGcolor};")

        #Title Location
        self.stack15.ri = QLabel("Remove Ingredient")
        self.stack15.ri.setStyleSheet('font: bold 40px;')
        self.stack15.ri.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack15.nlabel= QLabel("If a value is null type 'null'")
        self.stack15.nlabel.setStyleSheet('font: bold 20px;')
        self.stack15.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack15.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack15.IBN = QLabel("Barcode: ")
        self.stack15.IBN.setFixedSize(200, 40)
        self.stack15.IBN.setStyleSheet("font: 30px;")
        self.stack15.IBIN = QLineEdit("")
        self.stack15.IBIN.setStyleSheet("background-color: white; border: 1px solid black;")

        
        #Horizontal Boxes
        hboxri = QHBoxLayout()

        self.stack15.inputnum = [""]

        hboxri.addWidget(self.stack15.IBN)
        hboxri.addWidget(self.stack15.IBIN)

        #Add all Horizontal Boxes
        self.stack15.removeIng = QPushButton("Remove Ingredient", self.stack15)
        self.stack15.removeIng.setFixedSize(200, 40)
        self.stack15.removeIng.setStyleSheet("background-color: yellow;")
        self.stack15.removeIng.clicked.connect(self.removeIng)

        buttonboxri = QHBoxLayout()
        buttonboxri.addWidget(self.stack15.removeIng)
        
        self.btiButton3 = QPushButton("Back to Ingredient Menu")
        self.btiButton3.setFixedSize(200, 40)
        self.btiButton3.setStyleSheet("background-color: yellow;")
        buttonboxri.addWidget(self.btiButton3)
        buttonboxri.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)
        BIGribox.addWidget(self.stack15.ri)
        BIGribox.addWidget(self.stack15.nlabel)
        BIGribox.addLayout(hboxri) #this is the label that says 'username:' and the response box
        BIGribox.addLayout(buttonboxri)

        self.stack15.setLayout(BIGribox)

    def removeIng(self):

        try:
            barcode = self.stack15.IBIN.text()
            with connection.cursor() as cursor:
                query = "call remove_ingredient('{}')".format(barcode)
                cursor.execute(query, None)
                connection.commit()

            self.stack15.IBIN.clear()
        except:
            # Error message here
            error_dialog.showMessage('Remove Ingredient Failed! Make sure you have all fields entered correctly.')

    def LocationUI(self):
        self.stack16.resize(1000, 600)
        self.stack16.setWindowTitle("Restaurant Supply Express")
        self.stack16.BGcolor = 'white'
        self.stack16.setStyleSheet(f"background-color: {self.stack1.BGcolor};")

        lbox = QVBoxLayout()

        #Add Label
        self.stack16.locationLabel = QLabel("I wish to access...")
        self.stack16.locationLabel.setStyleSheet("color: pink; font: bold 40px;")
        self.stack16.locationLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack16.locationLabel.setGeometry(QtCore.QRect(437, 0, 200, 100))
        lbox.addWidget(self.stack16.locationLabel)

        #Add Ingredient
        self.addlocButton = QtWidgets.QPushButton(self.stack16)
        self.addlocButton.setText("Add Location")
        self.addlocButton.setGeometry(QtCore.QRect(437, 50, 125, 50))
        self.addlocButton.setStyleSheet("background-color: yellow;")
        lbox.addWidget(self.addlocButton)

        #View Ingredient
        self.viewlocButton = QtWidgets.QPushButton(self.stack16)
        self.viewlocButton.setText("View Location")
        self.viewlocButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.viewlocButton.setStyleSheet("background-color: yellow;")
        lbox.addWidget(self.viewlocButton)

        #Return to the main window
        self.menuButton5 = QPushButton("Back to Main Menu")
        self.menuButton5.setGeometry(QtCore.QRect(10, 10, 200, 30))
        self.menuButton5.setStyleSheet("background-color: yellow;")
        lbox.addWidget(self.menuButton5)

        lbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack16.setLayout(lbox)

    def addLocationUI(self):
        self.stack17.resize(1000, 600)
        self.stack17.setWindowTitle("Add Location")

        BIGLbox = QVBoxLayout()

        #Background of the GUI
        self.stack17.BGcolor = 'aliceblue'
        self.stack17.setStyleSheet(f"background-color: {self.stack17.BGcolor};")

        #Title Location
        self.stack17.location = QLabel("Location")
        self.stack17.location.setStyleSheet('font: bold 40px;')
        self.stack17.location.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack17.nlabel= QLabel("If a value is null type 'null'")
        self.stack17.nlabel.setStyleSheet('font: bold 20px;')
        self.stack17.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack17.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack17.LL = QLabel("Label: ")
        self.stack17.LL.setFixedSize(200, 40)
        self.stack17.LL.setStyleSheet("font: 30px;")
        self.stack17.LLIN = QLineEdit("")
        self.stack17.LLIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack17.XN = QLabel("X_coord: ")
        self.stack17.XN.setFixedSize(200, 40)
        self.stack17.XN.setStyleSheet("font: 30px;")
        self.stack17.XNIN = QLineEdit("")
        self.stack17.XNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack17.YN = QLabel("Y_coord: ")
        self.stack17.YN.setFixedSize(200, 40)
        self.stack17.YN.setStyleSheet("font: 30px;")
        self.stack17.YNIN = QLineEdit("")
        self.stack17.YNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack17.SN = QLabel("space: ")
        self.stack17.SN.setFixedSize(200, 40)
        self.stack17.SN.setStyleSheet("font: 30px;")
        self.stack17.SNIN = QLineEdit("")
        self.stack17.SNIN.setStyleSheet("background-color: white; border: 1px solid black;")


        #Horizontal Boxes
        hboxL = QHBoxLayout()
        hboxLname = QHBoxLayout()
        hboxS = QHBoxLayout()

        self.stack17.inputnum = [""]

        hboxL.addWidget(self.stack17.LL)
        hboxL.addWidget(self.stack17.LLIN)

        hboxLname.addWidget(self.stack17.XN)
        hboxLname.addWidget(self.stack17.XNIN)

        hboxLname.addWidget(self.stack17.YN)
        hboxLname.addWidget(self.stack17.YNIN)

        hboxS.addWidget(self.stack17.SN)
        hboxS.addWidget(self.stack17.SNIN)

        #Add all Horizontal Boxes
        self.stack17.addLocation = QPushButton("Add Location", self.stack13)
        self.stack17.addLocation.setFixedSize(200, 40)
        self.stack17.addLocation.setStyleSheet("background-color: yellow;")
        self.stack17.addLocation.clicked.connect(self.addLocation)

        buttonboxl = QHBoxLayout()
        buttonboxl.addWidget(self.stack17.addLocation)
        
        self.btlButton1 = QPushButton("Back to Location Menu")
        self.btlButton1.setFixedSize(200, 40)
        self.btlButton1.setStyleSheet("background-color: yellow;")
        buttonboxl.addWidget(self.btlButton1)
        buttonboxl.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGLbox.addWidget(self.stack17.location) #this is the label that says USER
        BIGLbox.addWidget(self.stack17.nlabel)
        BIGLbox.addLayout(hboxL) #this is the label that says 'username:' and the response box
        BIGLbox.addLayout(hboxLname) #same for first and last name
        BIGLbox.addLayout(hboxS) #same for address and birthday
        BIGLbox.addLayout(buttonboxl) #same for the Add Owner button

        self.stack17.setLayout(BIGLbox)

    def addLocation(self):

        try:
            label = self.stack17.LLIN.text()
            x_coord = self.stack17.XNIN.text()
            y_coord = self.stack17.YNIN.text()
            space = self.stack17.SNIN.text()
            with connection.cursor() as cursor:
                query = "call add_location('{}', '{}', '{}', '{}')".format(label, x_coord, y_coord, space)
                cursor.execute(query, None)
                connection.commit()

            self.stack17.LLIN.clear()
            self.stack17.XNIN.clear()
            self.stack17.YNIN.clear()
            self.stack17.SNIN.clear()
        except:
            # Error Msg Here
            error_dialog.showMessage('Add Location Failed! Make sure you have all fields entered correctly.')

    def viewLocationUI(self):
        self.stack18.resize(1000, 600)
        self.stack18.setWindowTitle("View Location")
        try:
            Lresult = []
            with connection.cursor() as cursor:
                query = "select label, x_coord, y_coord, COUNT(distinct restaurants.long_name) as num_restaurants, COUNT(distinct delivery_services.id) as num_delivery_services, COUNT(distinct drones.tag)  as num_drones from locations left outer join restaurants on locations.label=restaurants.location left outer  join delivery_services on locations.label= delivery_services.home_base left outer join drones on locations.label=drones.hover group by label;"
                cursor.execute(query, None)
                Lresult = cursor.fetchall()
                connection.commit()

            Ldata = {'Label':[],
                    'x_coord':[],
                    'y_coord':[],
                    '#_restaurants': [],
                    '#_services':[],
                    '#_drones':[], 
                    }

            for location in Lresult:
                Ldata['Label'].append(location['label'])
                Ldata['x_coord'].append(location['x_coord'])
                Ldata['y_coord'].append(location['y_coord'])
                Ldata['#_restaurants'].append(location['num_restaurants'])
                Ldata['#_services'].append(location['num_delivery_services'])
                Ldata['#_drones'].append(location['num_drones'])


            self.stack18.layout = QVBoxLayout()
            self.stack18.tableWidget = QTableWidget(len(Lresult), 6)
            self.stack18.tableWidget.setHorizontalHeaderLabels(["Label", "x_coord", "y_coord", "# of Restaurants", "# of Services", '# of drones'])
            self.stack18.tableWidget.setColumnWidth(0, 150)


            for num in range(len(Lresult)):
                self.stack18.tableWidget.setItem(num,0, QTableWidgetItem(Ldata['Label'][num]))
                self.stack18.tableWidget.setItem(num,1, QTableWidgetItem(str(Ldata['x_coord'][num])))
                self.stack18.tableWidget.setItem(num,2, QTableWidgetItem(str(Ldata['y_coord'][num])))
                self.stack18.tableWidget.setItem(num,3, QTableWidgetItem(str(Ldata['#_restaurants'][num])))
                self.stack18.tableWidget.setItem(num,4, QTableWidgetItem(str(Ldata['#_services'][num])))
                self.stack18.tableWidget.setItem(num,5, QTableWidgetItem(str(Ldata['#_drones'][num])))

            self.btlButton2 = QPushButton("Back to Location Menu")
            self.btlButton2.setGeometry(QtCore.QRect(10, 10, 200, 30))


            self.stack18.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.stack18.layout.addWidget(self.stack18.tableWidget)

            self.stack18.layout.addWidget(self.btlButton2)
            self.stack18.setLayout(self.stack18.layout)

        except:
            self.stack18.resize(1000, 600)
            self.stack18.setStyleSheet("background: pink")
            errorBox= QVBoxLayout()
            self.stack18.location = QLabel("View Failed to Open")
            self.stack18.location.setStyleSheet('font: bold 40px;')
            self.stack18.location.setAlignment(Qt.AlignmentFlag.AlignCenter)  
            errorBox.addWidget(self.stack18.location)
            self.stack18.setLayout(errorBox)

    def RestUI(self):
        self.stack19.resize(1000, 600)
        self.stack19.setWindowTitle("Restaurant Supply Express")
        self.stack19.BGcolor = 'white'
        self.stack19.setStyleSheet(f"background-color: {self.stack1.BGcolor};")

        rbox = QVBoxLayout()

        #Add Label
        self.stack19.restLabel = QLabel("I wish to access...")
        self.stack19.restLabel.setStyleSheet("color: pink; font: bold 40px;")
        self.stack19.restLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack19.restLabel.setGeometry(QtCore.QRect(437, 0, 200, 100))
        rbox.addWidget(self.stack19.restLabel)

        #Add Restarautn
        self.addrestButton = QtWidgets.QPushButton(self.stack19)
        self.addrestButton.setText("Add Restaurant")
        self.addrestButton.setGeometry(QtCore.QRect(437, 50, 125, 50))
        self.addrestButton.setStyleSheet("background-color: yellow;")
        rbox.addWidget(self.addrestButton)

        #Purchase Ingredient
        self.PurchaseIngButton = QtWidgets.QPushButton(self.stack19)
        self.PurchaseIngButton.setText("Purchase Ingredients")
        self.PurchaseIngButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.PurchaseIngButton.setStyleSheet("background-color: yellow;")
        rbox.addWidget(self.PurchaseIngButton)



        #Return to the main window
        self.menuButton6 = QPushButton("Back to Main Menu")
        self.menuButton6.setGeometry(QtCore.QRect(10, 10, 200, 30))
        self.menuButton6.setStyleSheet("background-color: yellow;")
        rbox.addWidget(self.menuButton6)

        rbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack19.setLayout(rbox)

    def addRestUI(self):
        self.stack20.resize(1000, 600)
        self.stack20.setWindowTitle("Add Restaurant")

        BIGRbox = QVBoxLayout()

        #Background of the GUI
        self.stack20.BGcolor = 'aliceblue'
        self.stack20.setStyleSheet(f"background-color: {self.stack20.BGcolor};")

        #Title Location
        self.stack20.restaurant = QLabel("Restaurant")
        self.stack20.restaurant.setStyleSheet('font: bold 40px;')
        self.stack20.restaurant.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack20.nlabel= QLabel("If a value is null type 'null'")
        self.stack20.nlabel.setStyleSheet('font: bold 20px;')
        self.stack20.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack20.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack20.LN = QLabel("Long Name: ")
        self.stack20.LN.setFixedSize(200, 40)
        self.stack20.LN.setStyleSheet("font: 30px;")
        self.stack20.LNIN = QLineEdit("")
        self.stack20.LNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack20.RN = QLabel("Rating: ")
        self.stack20.RN.setFixedSize(200, 40)
        self.stack20.RN.setStyleSheet("font: 30px;")
        self.stack20.RNIN = QLineEdit("")
        self.stack20.RNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack20.MN = QLabel("$ Spent: ")
        self.stack20.MN.setFixedSize(200, 40)
        self.stack20.MN.setStyleSheet("font: 30px;")
        self.stack20.MNIN = QLineEdit("")
        self.stack20.MNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack20.PN = QLabel("Location: ")
        self.stack20.PN.setFixedSize(200, 40)
        self.stack20.PN.setStyleSheet("font: 30px;")
        self.stack20.PNIN = QLineEdit("")
        self.stack20.PNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        #Horizontal Boxes
        hboxrname = QHBoxLayout()
        hboxrs = QHBoxLayout()
        hboxlf = QHBoxLayout()

        self.stack20.inputnum = [""]

        hboxrname.addWidget(self.stack20.LN)
        hboxrname.addWidget(self.stack20.LNIN)

        hboxrs.addWidget(self.stack20.RN)
        hboxrs.addWidget(self.stack20.RNIN)

        hboxrs.addWidget(self.stack20.MN)
        hboxrs.addWidget(self.stack20.MNIN)

        hboxlf.addWidget(self.stack20.PN)
        hboxlf.addWidget(self.stack20.PNIN)

        #Add all Horizontal Boxes
        self.stack20.addRestaurant = QPushButton("Add Restaurant", self.stack20)
        self.stack20.addRestaurant.setFixedSize(200, 40)
        self.stack20.addRestaurant.setStyleSheet("background-color: yellow;")
        self.stack20.addRestaurant.clicked.connect(self.addRestaurant)

        buttonboxr = QHBoxLayout()
        buttonboxr.addWidget(self.stack20.addRestaurant)
        
        self.btrButton1 = QPushButton("Back to Restaurant Menu")
        self.btrButton1.setFixedSize(200, 40)
        self.btrButton1.setStyleSheet("background-color: yellow;")
        buttonboxr.addWidget(self.btrButton1)
        buttonboxr.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGRbox.addWidget(self.stack20.restaurant) #this is the label that says USER
        BIGRbox.addWidget(self.stack20.nlabel)
        BIGRbox.addLayout(hboxrname) #this is the label that says 'username:' and the response box
        BIGRbox.addLayout(hboxrs) #same for first and last name
        BIGRbox.addLayout(hboxlf) #same for address and birthday
        BIGRbox.addLayout(buttonboxr) #same for the Add Owner button

        self.stack20.setLayout(BIGRbox)

    def addRestaurant(self):

        try:
            name = self.stack20.LNIN.text()
            rating = self.stack20.RNIN.text()
            spent = self.stack20.MNIN.text()
            location = self.stack20.PNIN.text()
            with connection.cursor() as cursor:
                query = "call add_restaurant('{}', {}, {}, '{}')".format(name, rating, spent, location)
                cursor.execute(query, None)
                connection.commit()
            self.stack20.LNIN.clear()
            self.stack20.RNIN.clear()
            self.stack20.MNIN.clear()
            self.stack20.PNIN.clear()
            
        except:
            # Error Msg here
            error_dialog.showMessage('Add Restaurant Failed! Make sure you have all fields entered correctly.')
            
    def PurchaseIngUI(self):
        self.stack21.resize(1000, 600)
        self.stack21.setWindowTitle("Purchase Ingredient")

        BIGpibox = QVBoxLayout()

        #Background of the GUI
        self.stack21.BGcolor = 'aliceblue'
        self.stack21.setStyleSheet(f"background-color: {self.stack21.BGcolor};")

        #Title Location
        self.stack21.pi = QLabel("Purchase Ingredient")
        self.stack21.pi.setStyleSheet('font: bold 40px;')
        self.stack21.pi.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack21.nlabel= QLabel("If a value is null type 'null'")
        self.stack21.nlabel.setStyleSheet('font: bold 20px;')
        self.stack21.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack21.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack21.LN = QLabel("Long Name: ")
        self.stack21.LN.setFixedSize(200, 40)
        self.stack21.LN.setStyleSheet("font: 30px;")
        self.stack21.LNIN = QLineEdit("")
        self.stack21.LNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack21.ID = QLabel("Ing.ID: ")
        self.stack21.ID.setFixedSize(200, 40)
        self.stack21.ID.setStyleSheet("font: 30px;")
        self.stack21.IDIN = QLineEdit("")
        self.stack21.IDIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack21.TG = QLabel("Ing.Tag: ")
        self.stack21.TG.setFixedSize(200, 40)
        self.stack21.TG.setStyleSheet("font: 30px;")
        self.stack21.TGIN = QLineEdit("")
        self.stack21.TGIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack21.IBC = QLabel("Ing.Barcode: ")
        self.stack21.IBC.setFixedSize(200, 40)
        self.stack21.IBC.setStyleSheet("font: 30px;")
        self.stack21.IBCN = QLineEdit("")
        self.stack21.IBCN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack21.QN = QLabel("Quantity: ")
        self.stack21.QN.setFixedSize(200, 40)
        self.stack21.QN.setStyleSheet("font: 30px;")
        self.stack21.QNIN = QLineEdit("")
        self.stack21.QNIN.setStyleSheet("background-color: white; border: 1px solid black;")


        #Horizontal Boxes
        hboxrn = QHBoxLayout()
        hboxii = QHBoxLayout()
        hboxbq = QHBoxLayout()

        self.stack21.inputnum = [""]

        hboxrn.addWidget(self.stack21.LN)
        hboxrn.addWidget(self.stack21.LNIN)

        hboxii.addWidget(self.stack21.ID)
        hboxii.addWidget(self.stack21.IDIN)

        hboxii.addWidget(self.stack21.TG)
        hboxii.addWidget(self.stack21.TGIN)

        hboxbq.addWidget(self.stack21.IBC)
        hboxbq.addWidget(self.stack21.IBCN)
        hboxbq.addWidget(self.stack21.QN)
        hboxbq.addWidget(self.stack21.QNIN)

        #Add all Horizontal Boxes
        self.stack21.purchaseIng = QPushButton("Purchase Ingredient", self.stack21)
        self.stack21.purchaseIng.setFixedSize(200, 40)
        self.stack21.purchaseIng.setStyleSheet("background-color: yellow;")
        self.stack21.purchaseIng.clicked.connect(self.purchaseIng)

        buttonboxpi = QHBoxLayout()
        buttonboxpi.addWidget(self.stack21.purchaseIng)
        
        self.btpiButton1 = QPushButton("Back to Restaurant Menu")
        self.btpiButton1.setFixedSize(200, 40)
        self.btpiButton1.setStyleSheet("background-color: yellow;")
        buttonboxpi.addWidget(self.btpiButton1)
        buttonboxpi.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGpibox.addWidget(self.stack21.pi) #this is the label that says USER
        BIGpibox.addWidget(self.stack21.nlabel)
        BIGpibox.addLayout(hboxrn) #this is the label that says 'username:' and the response box
        BIGpibox.addLayout(hboxii) #same for first and last name
        BIGpibox.addLayout(hboxbq) #same for address and birthday
        BIGpibox.addLayout(buttonboxpi) #same for the Add Owner button

        self.stack21.setLayout(BIGpibox)

    def purchaseIng(self):

        try:

            name = self.stack21.LNIN.text()
  
            ing_id = self.stack21.IDIN.text()
        
            ing_tag = self.stack21.TGIN.text()
   
            barcode = self.stack21.IBCN.text()
           
            quantity = self.stack21.QNIN.text()
    
            with connection.cursor() as cursor:
                query = "call purchase_ingredient('{}', '{}', {}, '{}', {})".format(name, ing_id, ing_tag, barcode, quantity)
                cursor.execute(query, None)
                connection.commit()
            self.stack21.LNIN.clear()
            self.stack21.IDIN.clear()
            self.stack21.TGIN.clear()
            self.stack21.IBCN.clear()
            self.stack21.QNIN.clear()
        except:
            # Error Msg here
            error_dialog.showMessage('Purchase Ingredient Failed! Make sure you have all fields entered correctly.')

    #Beas Code Here: Employee, Pilot, Worker

    def EmployeeUI(self):
        self.stack22.resize(1000, 600)
        self.stack22.setWindowTitle("Restaurant Supply Express")
        self.stack22.BGcolor = 'aliceblue'
        self.stack22.setStyleSheet(f"background-color: {self.stack22.BGcolor};")

        box = QVBoxLayout()

        #Add Label
        self.stack22.empLabel = QLabel("I want to ...")
        self.stack22.empLabel.setStyleSheet("color: pink; font: bold 40px;")
        self.stack22.empLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack22.empLabel.setGeometry(QtCore.QRect(437, 0, 200, 100))
        box.addWidget(self.stack22.empLabel)

        #Add Employee
        self.addEmpButton = QtWidgets.QPushButton(self.stack22)
        self.addEmpButton.setText("Add Employee")
        self.addEmpButton.setGeometry(QtCore.QRect(437, 50, 125, 50))
        self.addEmpButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.addEmpButton)

        #View Employee
        self.viewEmpButton = QtWidgets.QPushButton(self.stack22)
        self.viewEmpButton.setText("View Employees")
        self.viewEmpButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.viewEmpButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.viewEmpButton)

        #Change to Pilot
        self.pilotPageButton= QtWidgets.QPushButton(self.stack22)
        self.pilotPageButton.setText("Access Pilot")
        self.pilotPageButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.pilotPageButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.pilotPageButton)

        #Change to Worker
        self.workerPageButton = QtWidgets.QPushButton(self.stack22)
        self.workerPageButton.setText("Access Worker")
        self.workerPageButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.workerPageButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.workerPageButton)

        #Return to the main window
        self.menuButton4 = QPushButton("Back to Main Menu")
        self.menuButton4.setGeometry(QtCore.QRect(10, 10, 200, 30))
        self.menuButton4.setStyleSheet("background-color: yellow;")
        box.addWidget(self.menuButton4)

        box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack22.setLayout(box)


    def AddEmployeeUI(self):
        self.stack25.resize(1000, 600)
        self.stack25.setWindowTitle("Restaurant Supply Express")
        self.stack25.BGcolor = 'aliceblue'
        self.stack25.setStyleSheet(f"background-color: {self.stack25.BGcolor};")

        box = QVBoxLayout()
        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack25.BGcolor = 'aliceblue'
        self.stack25.setStyleSheet(f"background-color: {self.stack25.BGcolor};")

        #Title USER
        self.stack25.user = QLabel("Employee")
        self.stack25.user.setStyleSheet('font: bold 40px;')
        self.stack25.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack25.nlabel= QLabel("If a value is null type 'null'")
        self.stack25.nlabel.setStyleSheet('font: bold 20px;')
        self.stack25.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack25.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack25.UN = QLabel("Username: ")
        self.stack25.UN.setFixedSize(200, 40)
        self.stack25.UN.setStyleSheet("font: 30px;")
        self.stack25.usernameIN = QLineEdit("")
        self.stack25.usernameIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack25.FN = QLabel("First Name: ")
        self.stack25.FN.setFixedSize(200, 40)
        self.stack25.FN.setStyleSheet("font: 30px;")
        self.stack25.FNIN = QLineEdit("")
        self.stack25.FNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack25.LN = QLabel("Last Name: ")
        self.stack25.LN.setFixedSize(200, 40)
        self.stack25.LN.setStyleSheet("font: 30px;")
        self.stack25.LNIN = QLineEdit("")
        self.stack25.LNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack25.Address = QLabel("Address: ")
        self.stack25.Address.setFixedSize(200, 40)
        self.stack25.Address.setStyleSheet("font: 30px;")
        self.stack25.AddIN = QLineEdit("")
        self.stack25.AddIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack25.birthday = QLabel("Birthday: ")
        self.stack25.birthday.setFixedSize(200, 40)
        self.stack25.birthday.setStyleSheet("font: 30px;")
        self.stack25.bdIN = QLineEdit("")
        self.stack25.bdIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack25.taxID = QLabel("Tax ID: ")
        self.stack25.taxID.setFixedSize(200, 40)
        self.stack25.taxID.setStyleSheet("font: 30px;")
        self.stack25.tidIN = QLineEdit("")
        self.stack25.tidIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack25.hired = QLabel("Hired: ")
        self.stack25.hired.setFixedSize(200, 40)
        self.stack25.hired.setStyleSheet("font: 30px;")
        self.stack25.hIN = QLineEdit("")
        self.stack25.hIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack25.experience = QLabel("Experience: ")
        self.stack25.experience.setFixedSize(200, 40)
        self.stack25.experience.setStyleSheet("font: 30px;")
        self.stack25.experienceIN = QLineEdit("")
        self.stack25.experienceIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack25.salary = QLabel("Salary: ")
        self.stack25.salary.setFixedSize(200, 40)
        self.stack25.salary.setStyleSheet("font: 30px;")
        self.stack25.salaryIN = QLineEdit("")
        self.stack25.salaryIN.setStyleSheet("background-color: white; border: 1px solid black;")

        #Horizontal Boxes
        hboxUN = QHBoxLayout()
        hboxname = QHBoxLayout()
        hboxAB = QHBoxLayout()
        hboxTIDH = QHBoxLayout()
        hboxEES = QHBoxLayout()

        self.stack25.inputnum = [""]

        hboxUN.addWidget(self.stack25.UN)
        hboxUN.addWidget(self.stack25.usernameIN)

        hboxname.addWidget(self.stack25.FN)
        hboxname.addWidget(self.stack25.FNIN)
        hboxname.addWidget(self.stack25.LN)
        hboxname.addWidget(self.stack25.LNIN)

        hboxAB.addWidget(self.stack25.Address)
        hboxAB.addWidget(self.stack25.AddIN)
        hboxAB.addWidget(self.stack25.birthday)
        hboxAB.addWidget(self.stack25.bdIN)

        hboxTIDH.addWidget(self.stack25.taxID)
        hboxTIDH.addWidget(self.stack25.tidIN)
        hboxTIDH.addWidget(self.stack25.hired)
        hboxTIDH.addWidget(self.stack25.hIN)

        hboxEES.addWidget(self.stack25.experience)
        hboxEES.addWidget(self.stack25.experienceIN)
        hboxEES.addWidget(self.stack25.salary)
        hboxEES.addWidget(self.stack25.salaryIN)


        #Add all Horizontal Boxes
        self.stack25.addEmployee = QPushButton("Add Employee", self.stack4)
        self.stack25.addEmployee.setFixedSize(200, 40)
        self.stack25.addEmployee.setStyleSheet("background-color: yellow;")
        self.stack25.addEmployee.clicked.connect(self.addEmployee)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack25.addEmployee)
        
        self.btempButton1 = QPushButton("Back to Employee Menu")
        self.btempButton1.setFixedSize(200, 40)
        self.btempButton1.setStyleSheet("background-color: yellow;")
        buttonbox.addWidget(self.btempButton1)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack25.user) #this is the label that says USER
        BIGbox.addWidget(self.stack25.nlabel)
        BIGbox.addLayout(hboxUN) #this is the label that says 'username:' and the response box
        BIGbox.addLayout(hboxname) #same for first and last name
        BIGbox.addLayout(hboxAB) #same for address and birthday
        BIGbox.addLayout(hboxTIDH)
        BIGbox.addLayout(hboxEES)
        BIGbox.addLayout(buttonbox) 

        self.stack25.setLayout(BIGbox)

    def addEmployee(self):

        try:
            username = self.stack25.usernameIN.text()
            first_name = self.stack25.FNIN.text()
            last_name = self.stack25.LNIN.text()
            address = self.stack25.AddIN.text()
            birthdate = self.stack25.bdIN.text()
            taxID = self.stack25.tidIN.text()
            hired = self.stack25.hIN.text()
            employeeExperience = self.stack25.experienceIN.text()
            salary = self.stack25.salaryIN.text()
            with connection.cursor() as cursor:
                query = "call add_employee('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(username, first_name, last_name, address, birthdate, taxID, hired, employeeExperience, salary)
                cursor.execute(query, None)
                connection.commit()

            self.stack25.usernameIN.clear()
            self.stack25.FNIN.clear()
            self.stack25.LNIN.clear()
            self.stack25.AddIN.clear()
            self.stack25.bdIN.clear()
            self.stack25.salaryIN.clear()
            self.stack25.tidIN.clear()
            self.stack25.hIN.clear()
            self.stack25.experienceIN.clear()

        except:
            error_dialog.showMessage('Add Employee Failed! Make sure you have all fields entered correctly.')

    def ViewEmployeeUI(self):
        self.stack26.resize(1000, 600)
        self.stack26.setWindowTitle("View Employee")
        try:
            result = []
            with connection.cursor() as cursor:
                query = "select employees.username, taxID, salary, hired, employees.experience, IF(pilots.licenseID IS NULL, 'n/a', pilots.licenseID) as licenseID, IF(pilots.experience IS NULL, 'n/a', pilots.experience) as piloting_experience, IF(delivery_services.id IS NULL, 'no', 'yes') as manager_status from (employees LEFT JOIN pilots on employees.username = pilots.username) LEFT JOIN delivery_services on employees.username = delivery_services.manager"
                cursor.execute(query, None)
                result = cursor.fetchall()
                connection.commit()

            data = {'username':[],
                    'taxID':[],
                    'salary':[],
                    'hired': [],
                    'experience':[],
                    'licenseID':[],
                    'piloting_experience':[],
                    'manager_status': [],
                    }

            for employee in result:
                data['username'].append(employee['username'])
                data['taxID'].append(employee['taxID'])
                data['salary'].append(employee['salary'])
                data['hired'].append(employee['hired'])
                data['experience'].append(employee['experience'])
                data['licenseID'].append(employee['licenseID'])
                data['piloting_experience'].append(employee['piloting_experience'])
                data['manager_status'].append(employee['manager_status'])


            self.stack26.layout = QVBoxLayout()
            buttbox = QVBoxLayout
            self.stack26.tableWidget = QTableWidget(len(result), 8)
            self.stack26.tableWidget.setHorizontalHeaderLabels(["username", "taxID", "salary", "hired", "experience", "licenseID", "piloting_experience", "manager_status"])
            self.stack26.tableWidget.setColumnWidth(0, 150)


            for num in range(len(result)):
                self.stack26.tableWidget.setItem(num,0, QTableWidgetItem(data['username'][num]))
                self.stack26.tableWidget.setItem(num,1, QTableWidgetItem(data['taxID'][num]))
                self.stack26.tableWidget.setItem(num,2, QTableWidgetItem(str(data['salary'][num])))
                self.stack26.tableWidget.setItem(num,3, QTableWidgetItem(str(data['hired'][num])))
                self.stack26.tableWidget.setItem(num,4, QTableWidgetItem(str(data['experience'][num])))
                self.stack26.tableWidget.setItem(num,5, QTableWidgetItem(str(data['licenseID'][num])))
                self.stack26.tableWidget.setItem(num,6, QTableWidgetItem(str(data['piloting_experience'][num])))
                self.stack26.tableWidget.setItem(num,7, QTableWidgetItem(str(data['manager_status'][num])))
                
            
            self.btempButton2 = QPushButton("Back to Employee Menu")
            self.btempButton2.setGeometry(QtCore.QRect(10, 10, 200, 30))

            self.stack26.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.stack26.layout.addWidget(self.stack26.tableWidget)
            self.stack26.layout.addWidget(self.btempButton2)
            #buttbox.addWidget(self.btempButton2)
            #self.stack26.layout.addLayout(buttbox)
            self.stack26.setLayout(self.stack26.layout)


        except:
            self.stack26.resize(1000, 600)
            self.stack26.setStyleSheet("background: pink")
            errorBox= QVBoxLayout()
            self.stack26.user = QLabel("View Failed to Open")
            self.stack26.user.setStyleSheet('font: bold 40px')
            self.stack26.user.setAlignment(Qt.AlignmentFlag.AlignCenter)
            errorBox.addWidget(self.stack26.user)
            self.stack26.setLayout(errorBox)


    def PilotUI(self):
        self.stack23.resize(1000, 600)
        self.stack23.setWindowTitle("Restaurant Supply Express")
        self.stack23.BGcolor = 'aliceblue'
        self.stack23.setStyleSheet(f"background-color: {self.stack23.BGcolor};")

        box = QVBoxLayout()

        #Add Label
        self.stack23.Label = QLabel("I want to ...")
        self.stack23.Label.setStyleSheet("color: pink; font: bold 40px;")
        self.stack23.Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack23.Label.setGeometry(QtCore.QRect(437, 0, 200, 100))
        box.addWidget(self.stack23.Label)

        #Add Pilot
        self.addPilotButton = QtWidgets.QPushButton(self.stack23)
        self.addPilotButton.setText("Add Pilot")
        self.addPilotButton.setGeometry(QtCore.QRect(437, 50, 125, 50))
        self.addPilotButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.addPilotButton)

        #View Pilot
        self.viewPilotButton = QtWidgets.QPushButton(self.stack23)
        self.viewPilotButton.setText("View Pilots")
        self.viewPilotButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.viewPilotButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.viewPilotButton)

        #Remove Pilot
        self.removePilotButton = QtWidgets.QPushButton(self.stack23)
        self.removePilotButton.setText("Remove Pilot")
        self.removePilotButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.removePilotButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.removePilotButton)

        #Takeover Drone
        self.takeoverDroneButton = QtWidgets.QPushButton(self.stack23)
        self.takeoverDroneButton.setText("Take Over Drone")
        self.takeoverDroneButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.takeoverDroneButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.takeoverDroneButton)

        #Return to the main window
        self.bteButton1 = QPushButton("Back to Employee")
        self.bteButton1.setGeometry(QtCore.QRect(10, 10, 200, 30))
        self.bteButton1.setStyleSheet("background-color: yellow;")
        box.addWidget(self.bteButton1)

        box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack23.setLayout(box)

    def AddPilotUI(self):
        
        self.stack27.resize(1000, 600)
        self.stack27.setWindowTitle("Restaurant Supply Express")
        self.stack27.BGcolor = 'aliceblue'
        self.stack27.setStyleSheet(f"background-color: {self.stack27.BGcolor};")

        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack27.BGcolor = 'aliceblue'
        self.stack27.setStyleSheet(f"background-color: {self.stack27.BGcolor};")

        #Title USER
        self.stack27.user = QLabel("Pilot")
        self.stack27.user.setStyleSheet('font: bold 40px;')
        self.stack27.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack27.nlabel= QLabel("If a value is null type 'null'")
        self.stack27.nlabel.setStyleSheet('font: bold 20px;')
        self.stack27.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack27.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack27.UN = QLabel("Username: ")
        self.stack27.UN.setFixedSize(200, 40)
        self.stack27.UN.setStyleSheet("font: 30px;")
        self.stack27.usernameIN = QLineEdit("")
        self.stack27.usernameIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack27.licenseID = QLabel("Liscence ID: ")
        self.stack27.licenseID.setFixedSize(200, 40)
        self.stack27.licenseID.setStyleSheet("font: 30px;")
        self.stack27.lidIN = QLineEdit("")
        self.stack27.lidIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack27.pilot_experience = QLabel("Pilot \nExperience: ")
        self.stack27.pilot_experience.setFixedSize(200, 100)
        self.stack27.pilot_experience.setStyleSheet("font: 30px;")
        self.stack27.peIN = QLineEdit("")
        self.stack27.peIN.setStyleSheet("background-color: white; border: 1px solid black;")

    
        #Horizontal Boxes
        hboxUN = QHBoxLayout()
        hbox2 = QHBoxLayout()
        

        self.stack27.inputnum = [""]

        hboxUN.addWidget(self.stack27.UN)
        hboxUN.addWidget(self.stack27.usernameIN)

        hbox2.addWidget(self.stack27.licenseID)
        hbox2.addWidget(self.stack27.lidIN)
        hbox2.addWidget(self.stack27.pilot_experience)
        hbox2.addWidget(self.stack27.peIN)

       
        #Add all Horizontal Boxes
        self.stack27.addPilot = QPushButton("Add Pilot", self.stack27)
        self.stack27.addPilot.setFixedSize(200, 40)
        self.stack27.addPilot.setStyleSheet("background-color: yellow;")
        self.stack27.addPilot.clicked.connect(self.addPilot)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack27.addPilot)
        
        self.btpilotButton1 = QPushButton("Back to Pilot Menu")
        self.btpilotButton1.setFixedSize(200, 40)
        self.btpilotButton1.setStyleSheet("background-color: yellow;")
        buttonbox.addWidget(self.btpilotButton1)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack27.user) 
        BIGbox.addWidget(self.stack27.nlabel)
        BIGbox.addLayout(hboxUN)
        BIGbox.addLayout(hbox2) 
        BIGbox.addLayout(buttonbox) 

        self.stack27.setLayout(BIGbox)

    def addPilot(self):
        
        try:
            username = self.stack27.usernameIN.text()
            licenseID = self.stack27.lidIN.text()
            pilot_experience = self.stack27.peIN.text()
            with connection.cursor() as cursor:
                query = "call add_pilot_role('{}', '{}', {})".format(username, licenseID, pilot_experience)
                cursor.execute(query, None)
                connection.commit()
            self.stack27.usernameIN.clear()
            self.stack27.lidIN.clear()
            self.stack27.peIN.clear()
        except:
            error_dialog.showMessage('Add Pilot Failed! Make sure you have all fields entered correctly.')
    

    def ViewPilotUI(self):
    
        self.stack28.resize(1000, 600)
        self.stack28.BGcolor = 'white'
        self.stack28.setStyleSheet(f"background-color: {self.stack28.BGcolor};")
        self.stack28.setWindowTitle("View Pilot")
        
        try:
            result = []
            with connection.cursor() as cursor:
                query = "select username, licenseID, experience, (count(d1.tag) + count(d2.swarm_tag)) as num_drones, count(distinct D1.hover) as num_locations from pilots left JOIN (drones D1 left join drones D2 on (D1.id, D1.tag) = (D2.swarm_id, D2.swarm_tag)) ON username = D1.flown_by GROUP BY pilots.username"
                cursor.execute(query, None)
                result = cursor.fetchall()
                connection.commit()

            data = {'username':[],
                    'licenseID':[],
                    'experience':[],
                    'num_drones':[],
                    'num_locations':[],            
                    }

            for employee in result:
                data['username'].append(employee['username'])
                data['licenseID'].append(employee['licenseID'])
                data['experience'].append(employee['experience'])
                data['num_drones'].append(employee['num_drones'])
                data['num_locations'].append(employee['num_locations'])

            self.stack28.layout = QVBoxLayout()
            self.stack28.tableWidget = QTableWidget(len(result), 5)
            self.stack28.tableWidget.setHorizontalHeaderLabels(["username","licenseID", "experience", "num_drones", "num_locations"])
            self.stack28.tableWidget.setColumnWidth(0, 150)


            for num in range(len(result)):
                self.stack28.tableWidget.setItem(num,0, QTableWidgetItem(data['username'][num]))
                self.stack28.tableWidget.setItem(num,1, QTableWidgetItem(str(data['licenseID'][num])))
                self.stack28.tableWidget.setItem(num,2, QTableWidgetItem(str(data['experience'][num])))
                self.stack28.tableWidget.setItem(num,3, QTableWidgetItem(str(data['num_drones'][num])))
                self.stack28.tableWidget.setItem(num,4, QTableWidgetItem(str(data['num_locations'][num])))
            
            self.btpilotButton2 = QPushButton("Back to Pilot Menu")
            self.btpilotButton2.setGeometry(QtCore.QRect(10, 10, 200, 30))

            self.stack28.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.stack28.layout.addWidget(self.stack28.tableWidget)
            self.stack28.layout.addWidget(self.btpilotButton2)
            self.stack28.setLayout(self.stack28.layout)


        except:
            self.stack28.resize(1000, 600)
            self.stack28.setStyleSheet("background: pink")
            errorBox= QVBoxLayout()
            self.stack28.user = QLabel("View Failed to Open")
            self.stack28.user.setStyleSheet('font: bold 40px')
            self.stack28.user.setAlignment(Qt.AlignmentFlag.AlignCenter)
            errorBox.addWidget(self.stack28.user)
            self.stack28.setLayout(errorBox)

    def RemovePilotUI(self):
        
        self.stack29.resize(1000, 600)
        self.stack29.setWindowTitle("Restaurant Supply Express")
        self.stack29.BGcolor = 'aliceblue'
        self.stack29.setStyleSheet(f"background-color: {self.stack27.BGcolor};")

        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack29.BGcolor = 'aliceblue'
        self.stack29.setStyleSheet(f"background-color: {self.stack29.BGcolor};")

        #Title USER
        self.stack29.user = QLabel("Remove Pilot")
        self.stack29.user.setStyleSheet('font: bold 40px;')
        self.stack29.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack29.nlabel= QLabel("If a value is null type 'null'")
        self.stack29.nlabel.setStyleSheet('font: bold 20px;')
        self.stack29.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack29.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack29.UN = QLabel("Username: ")
        self.stack29.UN.setFixedSize(200, 40)
        self.stack29.UN.setStyleSheet("font: 30px;")
        self.stack29.usernameIN = QLineEdit("")
        self.stack29.usernameIN.setStyleSheet("background-color: white; border: 1px solid black;")

    
        #Horizontal Boxes
        hboxUN = QHBoxLayout()
        
    
        self.stack29.inputnum = [""]

        hboxUN.addWidget(self.stack29.UN)
        hboxUN.addWidget(self.stack29.usernameIN)

       
        #Add all Horizontal Boxes
        self.stack29.addPilot = QPushButton("Remove Pilot", self.stack29)
        self.stack29.addPilot.setFixedSize(200, 40)
        self.stack29.addPilot.setStyleSheet("background-color: yellow;")
        self.stack29.addPilot.clicked.connect(self.removePilot)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack29.addPilot)
        
        self.btpilotButton3 = QPushButton("Back to Pilot Menu")
        self.btpilotButton3.setFixedSize(200, 40)
        self.btpilotButton3.setStyleSheet("background-color: yellow;")
        buttonbox.addWidget(self.btpilotButton3)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack29.user)
        BIGbox.addWidget(self.stack29.nlabel)
        BIGbox.addLayout(hboxUN) 
        BIGbox.addLayout(buttonbox) 

        self.stack29.setLayout(BIGbox)

    def removePilot(self):

        try:
            username = self.stack29.usernameIN.text()
            with connection.cursor() as cursor:
                query = "call remove_pilot_role('{}')".format(username)
                cursor.execute(query, None)
                connection.commit()
            self.stack29.usernameIN.clear()
        except:
            error_dialog.showMessage('Remove Pilot Failed! Make sure you have all fields entered correctly.')


    def TakeoverDroneUI(self):
        self.stack30.resize(1000, 600)
        self.stack30.setWindowTitle("Restaurant Supply Express")
        self.stack30.BGcolor = 'aliceblue'
        self.stack30.setStyleSheet(f"background-color: {self.stack30.BGcolor};")

        self.stack30.nlabel= QLabel("If a value is null type 'null'")
        self.stack30.nlabel.setStyleSheet('font: bold 20px;')
        self.stack30.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack30.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack30.BGcolor = 'aliceblue'
        self.stack30.setStyleSheet(f"background-color: {self.stack30.BGcolor};")

        self.stack30.user = QLabel("Takeover Drone")
        self.stack30.user.setStyleSheet('font: bold 40px;')
        self.stack30.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack30.UN = QLabel("Username: ")
        self.stack30.UN.setFixedSize(200, 40)
        self.stack30.UN.setStyleSheet("font: 30px;")
        self.stack30.usernameIN = QLineEdit("")
        self.stack30.usernameIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack30.ID = QLabel("Drone ID: ")
        self.stack30.ID.setFixedSize(200, 40)
        self.stack30.ID.setStyleSheet("font: 30px;")
        self.stack30.IDIN = QLineEdit("")
        self.stack30.IDIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack30.tag = QLabel("Drone Tag: ")
        self.stack30.tag.setFixedSize(200, 40)
        self.stack30.tag.setStyleSheet("font: 30px;")
        self.stack30.tagIN = QLineEdit("")
        self.stack30.tagIN.setStyleSheet("background-color: white; border: 1px solid black;")

    
        #Horizontal Boxes
        hboxUN = QHBoxLayout()
        hbox2 = QHBoxLayout() 

        self.stack30.inputnum = [""]

        hboxUN.addWidget(self.stack30.UN)
        hboxUN.addWidget(self.stack30.usernameIN)

        hbox2.addWidget(self.stack30.ID)
        hbox2.addWidget(self.stack30.IDIN)
        hbox2.addWidget(self.stack30.tag)
        hbox2.addWidget(self.stack30.tagIN)

       
        #Add all Horizontal Boxes
        self.stack30.takeoverDrone = QPushButton("Takeover Drone", self.stack30)
        self.stack30.takeoverDrone.setFixedSize(200, 40)
        self.stack30.takeoverDrone.setStyleSheet("background-color: yellow;")
        self.stack30.takeoverDrone.clicked.connect(self.takeoverDrone)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack30.takeoverDrone)
        
        self.btpilotButton4 = QPushButton("Back to Pilot Menu")
        self.btpilotButton4.setFixedSize(200, 40)
        self.btpilotButton4.setStyleSheet("background-color: yellow;")
        buttonbox.addWidget(self.btpilotButton4)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack30.user) 
        BIGbox.addWidget(self.stack30.nlabel)
        BIGbox.addLayout(hboxUN)
        BIGbox.addLayout(hbox2) 
        BIGbox.addLayout(buttonbox) 

        self.stack30.setLayout(BIGbox)

    def takeoverDrone(self):

        try:
            username = self.stack30.usernameIN.text()
            ID = self.stack30.IDIN.text()
            tag = self.stack30.tagIN.text()
            with connection.cursor() as cursor:
                query = "call takeover_drone('{}','{}','{}')".format(username, ID, tag)
                cursor.execute(query, None)
                connection.commit()

            self.stack30.usernameIN.clear()
            self.stack30.IDIN.clear()
            self.stack30.tagIN.clear()
        
        except:
            error_dialog.showMessage('Takeover Drone Failed! Make sure you have all fields entered correctly.')

 
    def WorkerUI(self):
        self.stack24.resize(1000, 600)
        self.stack24.setWindowTitle("Restaurant Supply Express")
        self.stack24.BGcolor = 'aliceblue'
        self.stack24.setStyleSheet(f"background-color: {self.stack24.BGcolor};")

        box = QVBoxLayout()

        #Add Label
        self.stack24.workerLabel = QLabel("I want to ...")
        self.stack24.workerLabel.setStyleSheet("color: pink; font: bold 40px;")
        self.stack24.workerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack24.workerLabel.setGeometry(QtCore.QRect(437, 0, 200, 100))
        box.addWidget(self.stack24.workerLabel)

        self.addWorkerButton = QtWidgets.QPushButton(self.stack24)
        self.addWorkerButton.setText("Add Worker")
        self.addWorkerButton.setGeometry(QtCore.QRect(437, 50, 125, 50))
        self.addWorkerButton.setStyleSheet("background-color: yellow;")
        box.addWidget(self.addWorkerButton)

        #Return to the main window
        self.bteButton2 = QPushButton("Back to Employee")
        self.bteButton2.setGeometry(QtCore.QRect(10, 10, 200, 30))
        self.bteButton2.setStyleSheet("background-color: yellow;")
        box.addWidget(self.bteButton2)

        box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack24.setLayout(box)

    def AddWorkerUI(self):
        
        self.stack31.resize(1000, 600)
        self.stack31.setWindowTitle("Add Worker")
        
        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack31.BGcolor = 'aliceblue'
        self.stack31.setStyleSheet(f"background-color: {self.stack31.BGcolor};")

        #Title 
        self.stack31.user = QLabel("Worker")
        self.stack31.user.setStyleSheet('font: bold 40px;')
        self.stack31.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack31.nlabel= QLabel("If a value is null type 'null'")
        self.stack31.nlabel.setStyleSheet('font: bold 20px;')
        self.stack31.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack31.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack31.UN = QLabel("Username: ")
        self.stack31.UN.setFixedSize(200, 40)
        self.stack31.UN.setStyleSheet("font: 30px;")
        self.stack31.usernameIN = QLineEdit("")
        self.stack31.usernameIN.setStyleSheet("background-color: white; border: 1px solid black;")

        #Horizontal Boxes
        hboxUN = QHBoxLayout()

        self.stack31.inputnum = [""]

        hboxUN.addWidget(self.stack31.UN)
        hboxUN.addWidget(self.stack31.usernameIN)

        #Add all Horizontal Boxes
        self.stack31.addWorker = QPushButton("Add Worker", self.stack4)
        self.stack31.addWorker.setFixedSize(200, 40)
        self.stack31.addWorker.setStyleSheet("background-color: yellow;")
        self.stack31.addWorker.clicked.connect(self.addWorker)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack31.addWorker)
        
        self.btwButton1 = QPushButton("Back to Worker Menu")
        self.btwButton1.setFixedSize(200, 40)
        self.btwButton1.setStyleSheet("background-color: yellow;")
        buttonbox.addWidget(self.btwButton1)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack31.user) 
        BIGbox.addWidget(self.stack31.nlabel)
        BIGbox.addLayout(hboxUN) 
        BIGbox.addLayout(buttonbox) 

        self.stack31.setLayout(BIGbox)

    def addWorker(self):

        try:
            username = self.stack31.usernameIN.text()
            with connection.cursor() as cursor:
                query = "call add_worker_role('{}')".format(username)
                cursor.execute(query, None)
                connection.commit()
            self.stack31.usernameIN.clear()
        except:
            error_dialog.showMessage('Add Worker Failed! Make sure you have all fields entered correctly.')

    def dronesUI(self):
        self.stack32.resize(1000, 600)
        self.stack32.setWindowTitle("Restaurant Supply Express")
        self.stack32.BGcolor = 'white'
        self.stack32.setStyleSheet(f"background-color: {self.stack1.BGcolor};")

        dbox = QVBoxLayout()

        #Add Label
        self.stack32.drownLabel = QLabel("I wish to access...")
        self.stack32.drownLabel.setStyleSheet("color: pink; font: bold 40px;")
        self.stack32.drownLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack32.drownLabel.setGeometry(QtCore.QRect(437, 0, 200, 100))
        dbox.addWidget(self.stack32.drownLabel)

        #Add Drone
        self.addDroneButton = QtWidgets.QPushButton(self.stack32)
        self.addDroneButton.setText("Add Drone")
        self.addDroneButton.setGeometry(QtCore.QRect(437, 50, 125, 50))
        self.addDroneButton.setStyleSheet("background-color: yellow;")
        dbox.addWidget(self.addDroneButton)

        #Remove Drone
        self.removeDroneButton = QtWidgets.QPushButton(self.stack32)
        self.removeDroneButton.setText("Remove Drone")
        self.removeDroneButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.removeDroneButton.setStyleSheet("background-color: yellow;")
        dbox.addWidget(self.removeDroneButton)

        #Join Swarm
        self.joinSwarmButton = QtWidgets.QPushButton(self.stack32)
        self.joinSwarmButton.setText("Join Swarm")
        self.joinSwarmButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.joinSwarmButton.setStyleSheet("background-color: yellow;")
        dbox.addWidget(self.joinSwarmButton)

        #Leave Swarm
        self.LeaveSwarmButton = QtWidgets.QPushButton(self.stack32)
        self.LeaveSwarmButton.setText("Leave Swarm")
        self.LeaveSwarmButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.LeaveSwarmButton.setStyleSheet("background-color: yellow;")
        dbox.addWidget(self.LeaveSwarmButton)
        
        #Load Drone
        self.LoadDroneButton = QtWidgets.QPushButton(self.stack32)
        self.LoadDroneButton.setText("Load Drone")
        self.LoadDroneButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.LoadDroneButton.setStyleSheet("background-color: yellow;")
        dbox.addWidget(self.LoadDroneButton)

        #Refuel Drone
        self.RefuelDroneButton = QtWidgets.QPushButton(self.stack32)
        self.RefuelDroneButton.setText("Refuel Drone")
        self.RefuelDroneButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.RefuelDroneButton.setStyleSheet("background-color: yellow;")
        dbox.addWidget(self.RefuelDroneButton)

        #fly Drone
        self.flyDroneButton = QtWidgets.QPushButton(self.stack32)
        self.flyDroneButton.setText("Fly Drone")
        self.flyDroneButton.setGeometry(QtCore.QRect(437, 125, 125, 50))
        self.flyDroneButton.setStyleSheet("background-color: yellow;")
        dbox.addWidget(self.flyDroneButton)

        #Return to the main window
        self.menuButton7 = QPushButton("Back to Main Menu")
        self.menuButton7.setGeometry(QtCore.QRect(10, 10, 200, 30))
        self.menuButton7.setStyleSheet("background-color: yellow;")
        dbox.addWidget(self.menuButton7)

        dbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack32.setLayout(dbox)
    
    def addDronesUI(self):
        self.stack33.resize(1000, 600)
        self.stack33.setWindowTitle("Add Drone")

        BIGdbox = QVBoxLayout()

        #Background of the GUI
        self.stack33.BGcolor = 'aliceblue'
        self.stack33.setStyleSheet(f"background-color: {self.stack33.BGcolor};")

        #Title USER
        self.stack33.drone = QLabel("Drone")
        self.stack33.drone.setStyleSheet('font: bold 40px;')
        self.stack33.drone.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack33.nlabel= QLabel("If a value is null type 'null'")
        self.stack33.nlabel.setStyleSheet('font: bold 20px;')
        self.stack33.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack33.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack33.ID = QLabel("Drone ID: ")
        self.stack33.ID.setFixedSize(200, 40)
        self.stack33.ID.setStyleSheet("font: 30px;")
        self.stack33.IDIN = QLineEdit("")
        self.stack33.IDIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack33.TG = QLabel("Drone Tag: ")
        self.stack33.TG.setFixedSize(200, 40)
        self.stack33.TG.setStyleSheet("font: 30px;")
        self.stack33.TGIN = QLineEdit("")
        self.stack33.TGIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack33.FS = QLabel("Fuel Supply: ")
        self.stack33.FS.setFixedSize(200, 40)
        self.stack33.FS.setStyleSheet("font: 30px;")
        self.stack33.FSIN = QLineEdit("")
        self.stack33.FSIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack33.CP = QLabel("Capacity: ")
        self.stack33.CP.setFixedSize(200, 40)
        self.stack33.CP.setStyleSheet("font: 30px;")
        self.stack33.CPIN = QLineEdit("")
        self.stack33.CPIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack33.TS = QLabel("Sales: ")
        self.stack33.TS.setFixedSize(200, 40)
        self.stack33.TS.setStyleSheet("font: 30px;")
        self.stack33.TSIN = QLineEdit("")
        self.stack33.TSIN.setStyleSheet("background-color: white; border: 1px solid black;")
        
        self.stack33.FB = QLabel("Flown By: ")
        self.stack33.FB.setFixedSize(200, 40)
        self.stack33.FB.setStyleSheet("font: 30px;")
        self.stack33.FBIN = QLineEdit("")
        self.stack33.FBIN.setStyleSheet("background-color: white; border: 1px solid black;")

        #Horizontal Boxes
        hboxIT = QHBoxLayout()
        hboxFC = QHBoxLayout()
        hboxTP = QHBoxLayout()

        self.stack33.inputnum = [""]

        hboxIT.addWidget(self.stack33.ID)
        hboxIT.addWidget(self.stack33.IDIN)
        hboxIT.addWidget(self.stack33.TG)
        hboxIT.addWidget(self.stack33.TGIN)

        hboxFC.addWidget(self.stack33.FS)
        hboxFC.addWidget(self.stack33.FSIN)
        hboxFC.addWidget(self.stack33.CP)
        hboxFC.addWidget(self.stack33.CPIN)


        hboxTP.addWidget(self.stack33.TS)
        hboxTP.addWidget(self.stack33.TSIN)
        hboxTP.addWidget(self.stack33.FB)
        hboxTP.addWidget(self.stack33.FBIN)



        #Add all Horizontal Boxes
        self.stack33.addDrone = QPushButton("Add Drone", self.stack33)
        self.stack33.addDrone.setFixedSize(200, 40)
        self.stack33.addDrone.setStyleSheet("background-color: yellow;")
        self.stack33.addDrone.clicked.connect(self.addDrone)

        buttonboxd = QHBoxLayout()
        buttonboxd.addWidget(self.stack33.addDrone)
        
        self.btdButton1 = QPushButton("Back to Drone Menu")
        self.btdButton1.setFixedSize(200, 40)
        self.btdButton1.setStyleSheet("background-color: yellow;")
        buttonboxd.addWidget(self.btdButton1)
        buttonboxd.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGdbox.addWidget(self.stack33.drone) #this is the label that says USER
        BIGdbox.addWidget(self.stack33.nlabel)
        BIGdbox.addLayout(hboxIT) #this is the label that says 'username:' and the response box
        BIGdbox.addLayout(hboxFC) #same for first and last name
        BIGdbox.addLayout(hboxTP) #same for address and birthday
        BIGdbox.addLayout(buttonboxd) #same for the Add Owner button

        self.stack33.setLayout(BIGdbox)

    def addDrone(self):
    
        try:
            drone_id = self.stack33.IDIN.text()
            drone_tag = self.stack33.TGIN.text()
            fuel = self.stack33.FSIN.text()
            capacity = self.stack33.CPIN.text() 
            sales = self.stack33.TSIN.text()
            flown_by = self.stack33.FBIN.text()       

            with connection.cursor() as cursor:
                query = "call add_drone('{}', '{}', '{}', '{}', '{}', '{}')".format(drone_id, drone_tag, fuel, capacity, sales, flown_by)
                cursor.execute(query, None)
                connection.commit()

            self.stack33.IDIN.clear()
            self.stack33.TGIN.clear()
            self.stack33.FSIN.clear()
            self.stack33.CPIN.clear()
            self.stack33.TSIN.clear()
            self.stack33.FBIN.clear()
        except:
            error_dialog.showMessage('Add Drone Failed! Make sure you have all fields entered correctly.')
   

    def removeDroneUI(self):
        self.stack34.resize(1000, 600)
        self.stack34.setWindowTitle("Remove Drone")

        BIGrdbox = QVBoxLayout()

        #Background of the GUI
        self.stack34.BGcolor = 'aliceblue'
        self.stack34.setStyleSheet(f"background-color: {self.stack34.BGcolor};")

        #Title USER
        self.stack34.drone1 = QLabel("Remove Drone")
        self.stack34.drone1.setStyleSheet('font: bold 40px;')
        self.stack34.drone1.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack34.nlabel= QLabel("If a value is null type 'null'")
        self.stack34.nlabel.setStyleSheet('font: bold 20px;')
        self.stack34.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack34.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack34.ID1 = QLabel("Drone ID: ")
        self.stack34.ID1.setFixedSize(200, 40)
        self.stack34.ID1.setStyleSheet("font: 30px;")
        self.stack34.IDIN1 = QLineEdit("")
        self.stack34.IDIN1.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack34.TG1 = QLabel("Drone Tag: ")
        self.stack34.TG1.setFixedSize(200, 40)
        self.stack34.TG1.setStyleSheet("font: 30px;")
        self.stack34.TGIN1 = QLineEdit("")
        self.stack34.TGIN1.setStyleSheet("background-color: white; border: 1px solid black;")


        #Horizontal Boxes
        hboxIT1 = QHBoxLayout()

        self.stack34.inputnum = [""]

        hboxIT1.addWidget(self.stack34.ID1)
        hboxIT1.addWidget(self.stack34.IDIN1)
        hboxIT1.addWidget(self.stack34.TG1)
        hboxIT1.addWidget(self.stack34.TGIN1)




        #Add all Horizontal Boxes
        self.stack34.removeDrone = QPushButton("Remove Drone", self.stack34)
        self.stack34.removeDrone.setFixedSize(200, 40)
        self.stack34.removeDrone.setStyleSheet("background-color: yellow;")
        self.stack34.removeDrone.clicked.connect(self.removeDrone)

        buttonboxd1 = QHBoxLayout()
        buttonboxd1.addWidget(self.stack34.removeDrone)
        
        self.btdButton11 = QPushButton("Back to Drone Menu")
        self.btdButton11.setFixedSize(200, 40)
        self.btdButton11.setStyleSheet("background-color: yellow;")
        buttonboxd1.addWidget(self.btdButton11)
        buttonboxd1.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGrdbox.addWidget(self.stack34.drone1) #this is the label that says USER
        BIGrdbox.addWidget(self.stack34.nlabel)
        BIGrdbox.addLayout(hboxIT1) #this is the label that says 'username:' and the response box
        BIGrdbox.addLayout(buttonboxd1) #same for the Add Owner button

        self.stack34.setLayout(BIGrdbox)

    def removeDrone(self):
    

        try:
            drone_id = self.stack34.IDIN1.text()
            drone_tag = self.stack34.TGIN1.text()
            with connection.cursor() as cursor:
                query = "call remove_drone('{}', '{}')".format(drone_id, drone_tag)
                cursor.execute(query, None)
                connection.commit()

            self.stack34.IDIN1.clear()
            self.stack34.TGIN1.clear()
        except:
            error_dialog.showMessage('Remove Drone Failed! Make sure you have all fields entered correctly.')

    def leaveSwarmUI(self):

        self.stack35.resize(1000, 600)
        self.stack35.setWindowTitle("Leave Swarm")
        
        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack35.BGcolor = 'aliceblue'
        self.stack35.setStyleSheet(f"background-color: {self.stack35.BGcolor};")

        #Title 
        self.stack35.user = QLabel("Leave Swarm")
        self.stack35.user.setStyleSheet('font: bold 40px;')
        self.stack35.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack35.nlabel= QLabel("If a value is null type 'null'")
        self.stack35.nlabel.setStyleSheet('font: bold 20px;')
        self.stack35.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack35.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack35.ID = QLabel("ID: ")
        self.stack35.ID.setFixedSize(200, 40)
        self.stack35.ID.setStyleSheet("font: 30px;")
        self.stack35.IDIN = QLineEdit("")
        self.stack35.IDIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack35.tag1 = QLabel("Tag: ")
        self.stack35.tag1.setFixedSize(200, 40)
        self.stack35.tag1.setStyleSheet("font: 30px;")
        self.stack35.tagIN = QLineEdit("")
        self.stack35.tagIN.setStyleSheet("background-color: white; border: 1px solid black;")

        #Horizontal Boxes
        hboxUN = QHBoxLayout()
        hboxtag = QHBoxLayout()

        self.stack35.inputnum = [""]

        hboxUN.addWidget(self.stack35.ID)
        hboxUN.addWidget(self.stack35.IDIN)

        hboxtag.addWidget(self.stack35.tag1)
        hboxtag.addWidget(self.stack35.tagIN)

        #Add all Horizontal Boxes
        self.stack35.lswarm = QPushButton("Leave Swarm", self.stack35)
        self.stack35.lswarm.setFixedSize(200, 40)
        self.stack35.lswarm.setStyleSheet("background-color: yellow;")
        self.stack35.lswarm.clicked.connect(self.leaveSwarm)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack35.lswarm)
        
        self.btdButton4 = QPushButton("Back to Drone Menu")
        self.btdButton4.setFixedSize(200, 40)
        self.btdButton4.setStyleSheet("background-color: yellow;")
        buttonbox.addWidget(self.btdButton4)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack35.user)
        BIGbox.addWidget(self.stack35.nlabel) 
        BIGbox.addLayout(hboxUN) 
        BIGbox.addLayout(hboxtag)
        BIGbox.addLayout(buttonbox) 

        self.stack35.setLayout(BIGbox)

    def leaveSwarm(self):

        try:
            ID = self.stack35.IDIN.text()
            tag = self.stack35.tagIN.text()
            with connection.cursor() as cursor:
                query = "call leave_swarm('{}','{}')".format(ID, tag)
                cursor.execute(query, None)
                connection.commit()

            self.stack35.IDIN.clear()
            self.stack35.tagIN.clear()
        except:
            error_dialog.showMessage('Leave Swarm Failed! Make sure you have all fields entered correctly.')

    def loadDroneUI(self):
        #STACK 36
        self.stack36.resize(1000, 600)
        self.stack36.setWindowTitle("Load Drone")
        
        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack36.BGcolor = 'aliceblue'
        self.stack36.setStyleSheet(f"background-color: {self.stack36.BGcolor};")

        #Title 
        self.stack36.user = QLabel("Load Drone")
        self.stack36.user.setStyleSheet('font: bold 40px;')
        self.stack36.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack36.nlabel= QLabel("If a value is null type 'null'")
        self.stack36.nlabel.setStyleSheet('font: bold 20px;')
        self.stack36.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack36.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots
        self.stack36.UN = QLabel("ID: ")
        self.stack36.UN.setFixedSize(200, 40)
        self.stack36.UN.setStyleSheet("font: 30px;")
        self.stack36.usernameIN = QLineEdit("")
        self.stack36.usernameIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack36.FN = QLabel("Tag: ")
        self.stack36.FN.setFixedSize(200, 40)
        self.stack36.FN.setStyleSheet("font: 30px;")
        self.stack36.FNIN = QLineEdit("")
        self.stack36.FNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack36.LN = QLabel("Barcode: ")
        self.stack36.LN.setFixedSize(200, 40)
        self.stack36.LN.setStyleSheet("font: 30px;")
        self.stack36.LNIN = QLineEdit("")
        self.stack36.LNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack36.Address = QLabel("More \nPackages: ")
        self.stack36.Address.setFixedSize(200, 100)
        self.stack36.Address.setStyleSheet("font: 30px;")
        self.stack36.AddIN = QLineEdit("")
        self.stack36.AddIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack36.birthday = QLabel("Price: ")
        self.stack36.birthday.setFixedSize(200, 40)
        self.stack36.birthday.setStyleSheet("font: 30px;")
        self.stack36.bdIN = QLineEdit("")
        self.stack36.bdIN.setStyleSheet("background-color: white; border: 1px solid black;")

        #Horizontal Boxes

        hboxUN = QHBoxLayout()
        hboxname = QHBoxLayout()
        hboxAB = QHBoxLayout()
        

        self.stack36.inputnum = [""]

        hboxUN.addWidget(self.stack36.UN)
        hboxUN.addWidget(self.stack36.usernameIN)

        hboxUN.addWidget(self.stack36.FN)
        hboxUN.addWidget(self.stack36.FNIN)
        hboxname.addWidget(self.stack36.LN)
        hboxname.addWidget(self.stack36.LNIN)

        hboxAB.addWidget(self.stack36.Address)
        hboxAB.addWidget(self.stack36.AddIN)
        hboxAB.addWidget(self.stack36.birthday)
        hboxAB.addWidget(self.stack36.bdIN)

        #Add all Horizontal Boxes
        self.stack36.addEmployee = QPushButton("Load Drone", self.stack36)
        self.stack36.addEmployee.setFixedSize(200, 40)
        self.stack36.addEmployee.setStyleSheet("background-color: yellow;")
        self.stack36.addEmployee.clicked.connect(self.loadDrone)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack36.addEmployee)
        
        self.btdButton5 = QPushButton("Back to Drone Menu")
        self.btdButton5.setFixedSize(200, 40)
        self.btdButton5.setStyleSheet("background-color: yellow;")
        buttonbox.addWidget(self.btdButton5)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack36.user) #this is the label that says USER
        BIGbox.addWidget(self.stack36.nlabel)
        BIGbox.addLayout(hboxUN) #this is the label that says 'username:' and the response box
        BIGbox.addLayout(hboxname) #same for first and last name
        BIGbox.addLayout(hboxAB) 
        BIGbox.addLayout(buttonbox) 
        

        self.stack36.setLayout(BIGbox)

    def loadDrone(self):

        try:
            ID = self.stack36.usernameIN.text()
            tag = self.stack36.FNIN.text()
            barcode = self.stack36.LNIN.text()
            packages = self.stack36.AddIN.text()
            price = self.stack36.bdIN.text()
            with connection.cursor() as cursor:
                query = "call load_drone('{}','{}', '{}', '{}','{}')".format(ID, tag, barcode, packages, price)
                cursor.execute(query, None)
                connection.commit()

            self.stack36.usernameIN.clear()
            self.stack36.FNIN.clear()
            self.stack36.LNIN.clear()
            self.stack36.AddIN.clear()
            self.stack36.bdIN.clear()
        except:
            error_dialog.showMessage('Load Drone Failed! Make sure you have all fields entered correctly.')

    def refuelDroneUI(self):

        #STACK 37
        self.stack37.resize(1000, 600)
        self.stack37.setWindowTitle("Refuel Drone")
        
        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack37.BGcolor = 'aliceblue'
        self.stack37.setStyleSheet(f"background-color: {self.stack37.BGcolor};")

        #Title 
        self.stack37.user = QLabel("Refuel Drone")
        self.stack37.user.setStyleSheet('font: bold 40px;')
        self.stack37.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack37.nlabel= QLabel("If a value is null type 'null'")
        self.stack37.nlabel.setStyleSheet('font: bold 20px;')
        self.stack37.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack37.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots
        self.stack37.UN = QLabel("ID: ")
        self.stack37.UN.setFixedSize(200, 40)
        self.stack37.UN.setStyleSheet("font: 30px;")
        self.stack37.usernameIN = QLineEdit("")
        self.stack37.usernameIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack37.FN = QLabel("Tag: ")
        self.stack37.FN.setFixedSize(200, 40)
        self.stack37.FN.setStyleSheet("font: 30px;")
        self.stack37.FNIN = QLineEdit("")
        self.stack37.FNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack37.LN = QLabel("More Fuel: ")
        self.stack37.LN.setFixedSize(200, 40)
        self.stack37.LN.setStyleSheet("font: 30px;")
        self.stack37.LNIN = QLineEdit("")
        self.stack37.LNIN.setStyleSheet("background-color: white; border: 1px solid black;")



        #Horizontal Boxes

        hboxUN = QHBoxLayout()
        hboxname = QHBoxLayout()
        
        

        self.stack37.inputnum = [""]

        hboxUN.addWidget(self.stack37.UN)
        hboxUN.addWidget(self.stack37.usernameIN)

        hboxUN.addWidget(self.stack37.FN)
        hboxUN.addWidget(self.stack37.FNIN)
        hboxname.addWidget(self.stack37.LN)
        hboxname.addWidget(self.stack37.LNIN)

        

        #Add all Horizontal Boxes
        self.stack37.addEmployee = QPushButton("Refuel Drone", self.stack37)
        self.stack37.addEmployee.setFixedSize(200, 40)
        self.stack37.addEmployee.setStyleSheet("background-color: yellow;")
        self.stack37.addEmployee.clicked.connect(self.refuelDrone)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack37.addEmployee)
        
        self.btdButton6 = QPushButton("Back to Drone Menu")
        self.btdButton6.setFixedSize(200, 40)
        self.btdButton6.setStyleSheet("background-color: yellow;")
        buttonbox.addWidget(self.btdButton6)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack37.user) #this is the label that says USER
        BIGbox.addWidget(self.stack37.nlabel)
        BIGbox.addLayout(hboxUN) #this is the label that says 'username:' and the response box
        BIGbox.addLayout(hboxname) #same for first and last name
       
        BIGbox.addLayout(buttonbox) 
        

        self.stack37.setLayout(BIGbox)

    def refuelDrone(self):
        

        try:
            ID = self.stack37.usernameIN.text()
            tag = self.stack37.FNIN.text()
            morefuel = self.stack37.LNIN.text()
            with connection.cursor() as cursor:
                query = "call refuel_drone('{}','{}', '{}')".format(ID, tag, morefuel)
                cursor.execute(query, None)
                connection.commit()

            self.stack37.usernameIN.clear()
            self.stack37.FNIN.clear()
            self.stack37.LNIN.clear()
        except:
            error_dialog.showMessage('Refuel Drone Failed! Make sure you have all fields entered correctly.')

    def flyDroneUI(self):

        #STACK 38
        self.stack38.resize(1000, 600)
        self.stack38.setWindowTitle("Fly Drone")
        
        BIGbox = QVBoxLayout()

        #Background of the GUI
        self.stack38.BGcolor = 'aliceblue'
        self.stack38.setStyleSheet(f"background-color: {self.stack38.BGcolor};")

        #Title 
        self.stack38.user = QLabel("Fly Drone")
        self.stack38.user.setStyleSheet('font: bold 40px;')
        self.stack38.user.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack38.nlabel= QLabel("If a value is null type 'null'")
        self.stack38.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack38.nlabel.setStyleSheet('font: bold 20px;')
        self.stack38.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots
        self.stack38.UN = QLabel("ID: ")
        self.stack38.UN.setFixedSize(200, 40)
        self.stack38.UN.setStyleSheet("font: 30px;")
        self.stack38.usernameIN = QLineEdit("")
        self.stack38.usernameIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack38.FN = QLabel("Tag: ")
        self.stack38.FN.setFixedSize(200, 40)
        self.stack38.FN.setStyleSheet("font: 30px;")
        self.stack38.FNIN = QLineEdit("")
        self.stack38.FNIN.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack38.LN = QLabel("Destination: ")
        self.stack38.LN.setFixedSize(200, 40)
        self.stack38.LN.setStyleSheet("font: 30px;")
        self.stack38.LNIN = QLineEdit("")
        self.stack38.LNIN.setStyleSheet("background-color: white; border: 1px solid black;")



        #Horizontal Boxes

        hboxUN = QHBoxLayout()
        hboxname = QHBoxLayout()
        
        

        self.stack38.inputnum = [""]

        hboxUN.addWidget(self.stack38.UN)
        hboxUN.addWidget(self.stack38.usernameIN)

        hboxUN.addWidget(self.stack38.FN)
        hboxUN.addWidget(self.stack38.FNIN)
        hboxname.addWidget(self.stack38.LN)
        hboxname.addWidget(self.stack38.LNIN)

        

        #Add all Horizontal Boxes
        self.stack38.addEmployee = QPushButton("Fly Drone", self.stack38)
        self.stack38.addEmployee.setFixedSize(200, 40)
        self.stack38.addEmployee.setStyleSheet("background-color: yellow;")
        self.stack38.addEmployee.clicked.connect(self.flyDrone)

        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.stack38.addEmployee)
        
        self.btdButton7 = QPushButton("Back to Drone Menu")
        self.btdButton7.setFixedSize(200, 40)
        self.btdButton7.setStyleSheet("background-color: yellow;")
        buttonbox.addWidget(self.btdButton7)
        buttonbox.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGbox.addWidget(self.stack38.user) #this is the label that says USER
        BIGbox.addWidget(self.stack38.nlabel)
        BIGbox.addLayout(hboxUN) #this is the label that says 'username:' and the response box
        BIGbox.addLayout(hboxname) #same for first and last name
       
        BIGbox.addLayout(buttonbox) 
        

        self.stack38.setLayout(BIGbox)

    def flyDrone(self):
        

        try:
            ID = self.stack38.usernameIN.text()
            tag = self.stack38.FNIN.text()
            destination = self.stack38.LNIN.text()
            with connection.cursor() as cursor:
                query = "call fly_drone('{}','{}', '{}')".format(ID, tag, destination)
                cursor.execute(query, None)
                connection.commit()

            self.stack38.usernameIN.clear()
            self.stack38.FNIN.clear()
            self.stack38.LNIN.clear()
        except:
            error_dialog.showMessage('Fly Drone Failed! Make sure you have all fields entered correctly.')

    def joinSwarmUI(self):
        self.stack39.resize(1000, 600)
        self.stack39.setWindowTitle("Join Swarm")

        BIGboxjs = QVBoxLayout()

        #Background of the GUI
        self.stack39.BGcolor = 'aliceblue'
        self.stack39.setStyleSheet(f"background-color: {self.stack39.BGcolor};")

        #Title USER
        self.stack39.drone2 = QLabel("Join Swarm")
        self.stack39.drone2.setStyleSheet('font: bold 40px;')
        self.stack39.drone2.setAlignment(Qt.AlignmentFlag.AlignCenter)   # CHANGE THIS If USING PYQT5 TO "Qt.AlignCenter"

        self.stack39.nlabel= QLabel("If a value is null type 'null'")
        self.stack39.nlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stack39.nlabel.setStyleSheet('font: bold 20px;')
        self.stack39.nlabel.setGeometry(QtCore.QRect(437, 0, 200, 100))

        #Input Spots

        self.stack39.ID2 = QLabel("Drone ID: ")
        self.stack39.ID2.setFixedSize(200, 40)
        self.stack39.ID2.setStyleSheet("font: 30px;")
        self.stack39.IDIN2 = QLineEdit("")
        self.stack39.IDIN2.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack39.TG2 = QLabel("Drone Tag: ")
        self.stack39.TG2.setFixedSize(200, 40)
        self.stack39.TG2.setStyleSheet("font: 30px;")
        self.stack39.TGIN2 = QLineEdit("")
        self.stack39.TGIN2.setStyleSheet("background-color: white; border: 1px solid black;")

        self.stack39.ST = QLabel("Swarm Tag: ")
        self.stack39.ST.setFixedSize(200, 40)
        self.stack39.ST.setStyleSheet("font: 30px;")
        self.stack39.STIN = QLineEdit("")
        self.stack39.STIN.setStyleSheet("background-color: white; border: 1px solid black;")

        

        #Horizontal Boxes
        hboxID = QHBoxLayout()
        hboxST = QHBoxLayout()


        self.stack39.inputnum = [""]

        hboxID.addWidget(self.stack39.ID2)
        hboxID.addWidget(self.stack39.IDIN2)
        hboxST.addWidget(self.stack39.TG2)
        hboxST.addWidget(self.stack39.TGIN2)

        hboxST.addWidget(self.stack39.ST)
        hboxST.addWidget(self.stack39.STIN)
  



        #Add all Horizontal Boxes
        self.stack39.joinSwarm = QPushButton("Join Swarm", self.stack39)
        self.stack39.joinSwarm.setStyleSheet("background-color: yellow;")
        self.stack39.joinSwarm.setFixedSize(200, 40)
        self.stack39.joinSwarm.clicked.connect(self.joinSwarm)

        buttonboxjs = QHBoxLayout()
        buttonboxjs.addWidget(self.stack39.joinSwarm)
        
        self.btdButton1s = QPushButton("Back to Drone Menu")
        self.btdButton1s.setFixedSize(200, 40)
        buttonboxjs.addWidget(self.btdButton1s)
        self.btdButton1s.setStyleSheet("background-color: yellow;")
        buttonboxjs.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #Add all of our horizontal layouts :)

        BIGboxjs.addWidget(self.stack39.drone2) #this is the label that says USER
        BIGboxjs.addWidget(self.stack39.nlabel)
        BIGboxjs.addLayout(hboxID) #this is the label that says 'username:' and the response box
        BIGboxjs.addLayout(hboxST) #same for first and last name
        BIGboxjs.addLayout(buttonboxjs) #same for the Add Owner button

        self.stack39.setLayout(BIGboxjs)

    def joinSwarm(self):  

        try:
            drone_id = self.stack39.IDIN2.text()
            drone_tag = self.stack39.TGIN2.text()
            swarm_tag = self.stack39.STIN.text()    
            with connection.cursor() as cursor:
                query = "call join_swarm('{}', '{}', '{}')".format(drone_id, drone_tag, swarm_tag)
                cursor.execute(query, None)
                connection.commit()

            self.stack39.IDIN2.clear()
            self.stack39.TGIN2.clear()
            self.stack39.STIN.clear()
        except:
            error_dialog.showMessage('Join Swarm Failed! Make sure you have all fields entered correctly.')
   




class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.reload()

    def reload(self):
        self.setupUi(self)
        # Back to Menu Buttons
        self.menuButton1.clicked.connect(self.MainMenu)
        self.menuButton2.clicked.connect(self.MainMenu)
        self.menuButton3.clicked.connect(self.MainMenu)
        self.menuButton4.clicked.connect(self.MainMenu)
        self.menuButton5.clicked.connect(self.MainMenu)
        self.menuButton6.clicked.connect(self.MainMenu)
        self.menuButton7.clicked.connect(self.MainMenu)

        # Menu Buttons
        self.OwnersButton.clicked.connect(self.OpenOwner)
        self.DSButton.clicked.connect(self.OpenDeliveryService)
        self.IngredientsButton.clicked.connect(self.OpenIngredients)
        self.LocationsButton.clicked.connect(self.OpenLocation)
        self.RestaurantsButton.clicked.connect(self.OpenRest)
        self.EmployeeButton.clicked.connect(self.OpenEmployee)
        self.DronesButton.clicked.connect(self.OpenDrone)

        # Owner Buttons
        self.addOwnerButton.clicked.connect(self.OpenAddOwner)
        self.viewOwnerButton.clicked.connect(self.OpenViewOwner)
        self.viewFundingButton.clicked.connect(self.OpenStartFunding)

        # Back to Owner Buttons
        self.btoButton1.clicked.connect(self.reload)
        self.btoButton2.clicked.connect(self.reload)
        self.btoButton3.clicked.connect(self.reload)
        self.btoButton1.clicked.connect(self.OpenOwner)
        self.btoButton2.clicked.connect(self.OpenOwner)
        self.btoButton3.clicked.connect(self.OpenOwner)
        
        # DS Buttons
        self.addServiceButton.clicked.connect(self.OpenAddService)
        self.manageServiceButton.clicked.connect(self.OpenManageService)
        self.hireEmployeeButton.clicked.connect(self.OpenHireEmployee)
        self.fireEmployeeButton.clicked.connect(self.OpenFireEmployee)
        self.viewServiceButton.clicked.connect(self.OpenViewServices)

        # Back to DS Buttons
        self.btdsButton1.clicked.connect(self.reload)
        self.btdsButton2.clicked.connect(self.reload)
        self.btdsButton3.clicked.connect(self.reload)
        self.btdsButton4.clicked.connect(self.reload)
        self.btdsButton5.clicked.connect(self.reload)
        self.btdsButton1.clicked.connect(self.OpenDeliveryService)
        self.btdsButton2.clicked.connect(self.OpenDeliveryService)
        self.btdsButton3.clicked.connect(self.OpenDeliveryService)
        self.btdsButton4.clicked.connect(self.OpenDeliveryService)
        self.btdsButton5.clicked.connect(self.OpenDeliveryService)

        # Ingredient Buttons
        self.addIngButton.clicked.connect(self.OpenAddIng)
        self.viewIngButton.clicked.connect(self.OpenViewIng)
        self.removeIngButton.clicked.connect(self.OpenRemoveIng)

        # Back to Ingredient Buttons
        self.btiButton1.clicked.connect(self.reload)
        self.btiButton2.clicked.connect(self.reload)
        self.btiButton3.clicked.connect(self.reload)
        self.btiButton1.clicked.connect(self.OpenIngredients)
        self.btiButton2.clicked.connect(self.OpenIngredients)
        self.btiButton3.clicked.connect(self.OpenIngredients)

        # Location Buttons
        self.addlocButton.clicked.connect(self.OpenAddLoc)
        self.viewlocButton.clicked.connect(self.OpenViewLoc)

        # Back to Location Buttons
        self.btlButton1.clicked.connect(self.reload)
        self.btlButton2.clicked.connect(self.reload)
        self.btlButton1.clicked.connect(self.OpenLocation)
        self.btlButton2.clicked.connect(self.OpenLocation)

        # Restaurant Buttons
        self.addrestButton.clicked.connect(self.OpenAddRest)
        self.PurchaseIngButton.clicked.connect(self.OpenPurchaseIng)

        # Back to Rest Buttons
        self.btrButton1.clicked.connect(self.reload)
        self.btpiButton1.clicked.connect(self.reload)
        self.btrButton1.clicked.connect(self.OpenRest)
        self.btpiButton1.clicked.connect(self.OpenRest)

        # Back to Employee Buttons
        self.bteButton1.clicked.connect(self.reload)
        self.bteButton2.clicked.connect(self.reload)
        self.btempButton1.clicked.connect(self.reload)
        self.btempButton2.clicked.connect(self.reload)
        self.bteButton1.clicked.connect(self.OpenEmployee)
        self.bteButton2.clicked.connect(self.OpenEmployee)
        self.btempButton1.clicked.connect(self.OpenEmployee)
        self.btempButton2.clicked.connect(self.OpenEmployee)

        # Employee Buttons
        self.pilotPageButton.clicked.connect(self.OpenPilot)
        self.workerPageButton.clicked.connect(self.OpenWorker)
        self.addEmpButton.clicked.connect(self.OpenAddEmployee)
        self.viewEmpButton.clicked.connect(self.OpenViewEmployee)

        # Worker Buttons
        self.addWorkerButton.clicked.connect(self.OpenAddWorker)

        # Pilot Buttons
        self.addPilotButton.clicked.connect(self.OpenAddPilot)
        self.viewPilotButton.clicked.connect(self.OpenPilotView)
        self.takeoverDroneButton.clicked.connect(self.OpenTakeoverDrone)
        self.removePilotButton.clicked.connect(self.OpenRemovePilot)

        # Back to Worker Buttons
        self.btwButton1.clicked.connect(self.reload)
        self.btwButton1.clicked.connect(self.OpenWorker)

        # Back to Pilot Buttons
        self.btpilotButton1.clicked.connect(self.reload)
        self.btpilotButton2.clicked.connect(self.reload)
        self.btpilotButton3.clicked.connect(self.reload)
        self.btpilotButton4.clicked.connect(self.reload)
        self.btpilotButton1.clicked.connect(self.OpenPilot)
        self.btpilotButton2.clicked.connect(self.OpenPilot)
        self.btpilotButton3.clicked.connect(self.OpenPilot)
        self.btpilotButton4.clicked.connect(self.OpenPilot)

        # Drone Buttons
        self.LeaveSwarmButton.clicked.connect(self.OpenLeaveSwarm)
        self.LoadDroneButton.clicked.connect(self.OpenLoadDrone)
        self.RefuelDroneButton.clicked.connect(self.OpenRefuelDrone)
        self.flyDroneButton.clicked.connect(self.OpenFlyDrone)
        self.addDroneButton.clicked.connect(self.OpenAddDrone)
        self.removeDroneButton.clicked.connect(self.OpenRemoveDrone)
        self.joinSwarmButton.clicked.connect(self.OpenJoinSwarm)

        # Back to Drone Buttons
        self.btdButton1.clicked.connect(self.reload)
        self.btdButton11.clicked.connect(self.reload)
        self.btdButton1s.clicked.connect(self.reload)
        self.btdButton4.clicked.connect(self.reload)
        self.btdButton5.clicked.connect(self.reload)
        self.btdButton6.clicked.connect(self.reload)
        self.btdButton7.clicked.connect(self.reload)
        self.btdButton1.clicked.connect(self.OpenDrone)
        self.btdButton11.clicked.connect(self.OpenDrone)
        self.btdButton1s.clicked.connect(self.OpenDrone)
        self.btdButton4.clicked.connect(self.OpenDrone)
        self.btdButton5.clicked.connect(self.OpenDrone)
        self.btdButton6.clicked.connect(self.OpenDrone)
        self.btdButton7.clicked.connect(self.OpenDrone)
        
    def MainMenu(self):
        self.QtStack.setCurrentIndex(0)

    def OpenOwner(self):
        self.QtStack.setCurrentIndex(1)

    def OpenViewOwner(self):
        self.QtStack.setCurrentIndex(2)

    def OpenAddOwner(self):
        self.QtStack.setCurrentIndex(3)

    def OpenStartFunding(self):
        self.QtStack.setCurrentIndex(4)

    def OpenDeliveryService(self):
        self.QtStack.setCurrentIndex(5)

    def OpenAddService(self):
        self.QtStack.setCurrentIndex(6)

    def OpenManageService(self):
        self.QtStack.setCurrentIndex(7)

    def OpenHireEmployee(self):
        self.QtStack.setCurrentIndex(8)

    def OpenFireEmployee(self):
        self.QtStack.setCurrentIndex(9)

    def OpenViewServices(self):
        self.QtStack.setCurrentIndex(10)

    def OpenIngredients(self):
        self.QtStack.setCurrentIndex(11)

    def OpenAddIng(self):
        self.QtStack.setCurrentIndex(12)

    def OpenViewIng(self):
        self.QtStack.setCurrentIndex(13)

    def OpenRemoveIng(self):
        self.QtStack.setCurrentIndex(14)
        
    def OpenLocation(self):
        self.QtStack.setCurrentIndex(15)

    def OpenAddLoc(self):
        self.QtStack.setCurrentIndex(16)

    def OpenViewLoc(self):
        self.QtStack.setCurrentIndex(17)

    def OpenRest(self):
        self.QtStack.setCurrentIndex(18)

    def OpenAddRest(self):
        self.QtStack.setCurrentIndex(19)

    def OpenPurchaseIng(self):
        self.QtStack.setCurrentIndex(20)
    
    def OpenEmployee(self):
        self.QtStack.setCurrentIndex(21)

    def OpenPilot(self):
        self.QtStack.setCurrentIndex(22)

    def OpenWorker(self):
        self.QtStack.setCurrentIndex(23)

    def OpenAddEmployee(self):
        self.QtStack.setCurrentIndex(24)

    def OpenViewEmployee(self):
        self.QtStack.setCurrentIndex(25)

    def OpenAddPilot(self):
        self.QtStack.setCurrentIndex(26)

    def OpenPilotView(self):
        self.QtStack.setCurrentIndex(27)

    def OpenRemovePilot(self):
        self.QtStack.setCurrentIndex(28)

    def OpenTakeoverDrone(self):
        self.QtStack.setCurrentIndex(29)

    def OpenAddWorker(self):
        self.QtStack.setCurrentIndex(30)

    def OpenDrone(self):
        self.QtStack.setCurrentIndex(31)

    def OpenAddDrone(self):
        self.QtStack.setCurrentIndex(32)

    def OpenRemoveDrone(self):
        self.QtStack.setCurrentIndex(33)

    def OpenLeaveSwarm(self):
        self.QtStack.setCurrentIndex(34)

    def OpenLoadDrone(self):
        self.QtStack.setCurrentIndex(35)

    def OpenRefuelDrone(self):
        self.QtStack.setCurrentIndex(36)

    def OpenFlyDrone(self):
        self.QtStack.setCurrentIndex(37)

    def OpenJoinSwarm(self):
        self.QtStack.setCurrentIndex(38)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()
    error_dialog = QtWidgets.QErrorMessage()    # error messages
    sys.exit(app.exec())
