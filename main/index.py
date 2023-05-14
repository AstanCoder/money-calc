# coding=<UTF-8>


from PyQt5.QtWidgets import *

from PyQt5 import QtGui, QtCore

from PyQt5.QtSql import *

from PyQt5 import uic

from MainWindow import *

from about_window import *

from CalculateWindow import Ui_calculateForm

from CalculateWindow import *

import sqlite3




import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

class otherApps_form(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('resources\otherApps_form.ui', self)

class calculate_form(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('resources\CalculateWindow.ui', self)
        
class about_form(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('resources\About_window.ui', self)

class help_form(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('resources\help_window.ui', self)
        
class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    db_name = 'database.db'
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        super().__init__()
        self.setupUi(self)
        self.db_query = db_query()
        self.c_table = Ui_calculateForm()
        
        #Main Wind Declarations
        self.setWindowTitle('Money Calculator')
        self.setFixedHeight(750)
        self.setFixedWidth(750)
        self.setWindowIcon(QtGui.QIcon('resources\icon.png'))
        
        #about wind Declarations
        self.aboutWind = about_form()
        self.aboutWind.setWindowTitle('Acerca De: ')
        self.aboutWind.setWindowIcon(QtGui.QIcon('resources\icon.png'))
        self.aboutWind.setFixedHeight(230)
        self.aboutWind.setFixedWidth(420)
        
        #Help Wind Declarations
        self.helpWind = help_form()
        self.helpWind.setWindowTitle('Ayuda')
        self.helpWind.setWindowIcon(QtGui.QIcon('resources\help_icon.png'))
        self.helpWind.setFixedSize(600, 450)
        
        #Calculate Wind declarations
        self.cWind = calculate_form()
        self.cWind.setWindowTitle('Calculate')
        self.cWind.setFixedHeight(500)
        self.cWind.setFixedWidth(600)
        self.cWind.setWindowIcon(QtGui.QIcon('resources\icon.png'))
        
        #Other apps wind declarations
        self.otherAppsWind = otherApps_form()
        self.otherAppsWind.setWindowTitle('Other Apps')
        self.otherAppsWind.setWindowIcon(QtGui.QIcon('resources\other.png'))
        self.otherAppsWind.setFixedHeight(250)
        self.otherAppsWind.setFixedWidth(400)
        
        #Botones MainWindow
        self.getRecords_Button.clicked.connect(self.history_query)    
        self.about_Button.clicked.connect(self.show_about)
        self.calculate_Button.clicked.connect(self.show_calculate)
        self.help_Button.clicked.connect(self.show_help)
        self.otherApps_Button.clicked.connect(self.show_otherApps)
        
        
        #Botones CalculateWindow
        self.cWind.cCalculate_button.clicked.connect(self.calc_method)
        self.cWind.cDelete_button.clicked.connect(self.cDel_method)
        # self.cWind.cSave_button.clicked.connect(self.save)
        
        
    #About Form Call    
    def show_about(self):
        self.aboutWind.exec_()
 
    
    #Calculate Form Call
    def show_calculate(self):
        self.cWind.exec_()
 
    #Help Form Call
    def show_help(self):
        self.helpWind.exec_()
        
    #Other apps form call
    
    def show_otherApps(self):
        self.otherAppsWind.exec_()    
    
    
    #Calc method 
    def calc_method(self):
        
        bill = []
        try:
            
            
            
            for i in range(0, 11):
                bill.append(self.cWind.cTable.item(i, 0).text())
                print(bill[i])
                
            total = int(bill[1])*1 + int(bill[2])*3  + int(bill[3])*5  + int(bill[4])*10 + int(bill[5]) *20  + int(bill[6]) *50  + int(bill[7]) *100  + int(bill[8]) *200  + int(bill[9]) *500  + int(bill[10]) *1000
        
            self.cWind.cTable.setItem(1, 1, QTableWidgetItem(str(int(bill[1])*1)))
            self.cWind.cTable.setItem(2, 1, QTableWidgetItem(str(int(bill[2])*3)))
            self.cWind.cTable.setItem(3, 1, QTableWidgetItem(str(int(bill[3])*5)))
            self.cWind.cTable.setItem(4, 1, QTableWidgetItem(str(int(bill[4])*10)))
            self.cWind.cTable.setItem(5, 1, QTableWidgetItem(str(int(bill[5])*20)))
            self.cWind.cTable.setItem(6, 1, QTableWidgetItem(str(int(bill[6])*50)))
            self.cWind.cTable.setItem(7, 1, QTableWidgetItem(str(int(bill[7])*100)))
            self.cWind.cTable.setItem(8, 1, QTableWidgetItem(str(int(bill[8])*200)))
            self.cWind.cTable.setItem(9, 1, QTableWidgetItem(str(int(bill[9])*500)))
            self.cWind.cTable.setItem(10, 1, QTableWidgetItem(str(int(bill[10])*1000)))
            self.cWind.cTotal_table.setItem(0, 0, QTableWidgetItem(str(total)))
                
        except AttributeError:
            QMessageBox.critical(None, 'Filling error', 'Llena todos los campos' ,QMessageBox.Cancel)
        bill = []
        self.save()
        self.history_query()
        
        
    #Calculate Wind table clear
    def cDel_method(self):
        
        index = 0
        
        
        for rows in range(1, 10):
            test = self.cWind.cTable.item(rows, index).text()
            print(test)
            
            
        self.cWind.cTable.clearContents()
        self.cWind.cTotal_table.clearContents()
        
        for rows in range(0, 11):
            self.cWind.cTable.setItem(rows, 0, QTableWidgetItem(str(0)))
        
            self.cWind.cTable.setItem(rows, 1, QTableWidgetItem(str(0)))
        
        
        self.cWind.cTotal_table.setItem(0, 0, QTableWidgetItem(str(0)))
    
        
    #Calculate record saving
    def run_query(self, query, parameters = ()): 
        with sqlite3.connect(self.db_name) as conn: 
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result 
    
        
    #Save exec
    def save(self):
        
        #1
        Coin_ID = '1$'
        Coin_amount = self.cWind.cTable.item(1, 0).text()
        Coin_total = self.cWind.cTable.item(1, 1).text()
        self.save_query(Coin_amount, Coin_total, Coin_ID)
        
        #3
        Coin_ID = '3$'
        Coin_amount = self.cWind.cTable.item(2, 0).text()
        Coin_total = self.cWind.cTable.item(2, 1).text()
        self.save_query(Coin_amount, Coin_total, Coin_ID)
        
        #5
        Coin_ID = '5$'
        Coin_amount = self.cWind.cTable.item(3, 0).text()
        Coin_total = self.cWind.cTable.item(3, 1).text()
        self.save_query(Coin_amount, Coin_total, Coin_ID)
        
        #10
        Coin_ID = '10$'
        Coin_amount = self.cWind.cTable.item(4, 0).text()
        Coin_total = self.cWind.cTable.item(4, 1).text()
        self.save_query(Coin_amount, Coin_total, Coin_ID)
        
        #20
        Coin_ID = '20$'
        Coin_amount = self.cWind.cTable.item(5, 0).text()
        Coin_total = self.cWind.cTable.item(5, 1).text()
        self.save_query(Coin_amount, Coin_total, Coin_ID)
        
        #50
        Coin_ID = '50$'
        Coin_amount = self.cWind.cTable.item(6, 0).text()
        Coin_total = self.cWind.cTable.item(6, 1).text()
        self.save_query(Coin_amount, Coin_total, Coin_ID)
        
        #100
        Coin_ID = '100$'
        Coin_amount = self.cWind.cTable.item(7, 0).text()
        Coin_total = self.cWind.cTable.item(7, 1).text()
        self.save_query(Coin_amount, Coin_total, Coin_ID)
        
        #200
        Coin_ID = '200$'
        Coin_amount = self.cWind.cTable.item(8, 0).text()
        Coin_total = self.cWind.cTable.item(8, 1).text()
        self.save_query(Coin_amount, Coin_total, Coin_ID)
        
        #500
        Coin_ID = '500$'
        Coin_amount = self.cWind.cTable.item(9, 0).text()
        Coin_total = self.cWind.cTable.item(9, 1).text()
        self.save_query(Coin_amount, Coin_total, Coin_ID)
        
        #1000
        Coin_ID = '1000$'
        Coin_amount = self.cWind.cTable.item(10, 0).text()
        Coin_total = self.cWind.cTable.item(10, 1).text()
        self.save_query(Coin_amount, Coin_total, Coin_ID)
        
        #Total
        Total = self.cWind.cTotal_table.item(0, 0).text()
        ID = 1
        self.total_query(Total, ID)
    
    
    #SAVE QUERY
    def save_query(self, Coin_amount, Coin_total, Coin_ID):
        query = 'UPDATE currency SET Coin_amount = ?, Coin_total = ? WHERE Coin_ID = ?'
        parameters = (Coin_amount, Coin_total, Coin_ID)
        self.run_query(query, parameters)
 
 
    #Record Query
    def history_query(self): 
        order = 'SELECT * FROM currency'
        index = 0
        query = QSqlQuery()
        query.exec_(order)
        
        while query.next():
            moneda = query.value(0)
            cantidad = query.value(1)
            totalPorBilletes = query.value(2)
            
            
            self.records_table.setRowCount(index + 1)
            self.records_table.setItem(index, 0, QTableWidgetItem(str(moneda)))
            self.records_table.setItem(index, 1, QTableWidgetItem(str(cantidad)))
            self.records_table.setItem(index, 2, QTableWidgetItem(str(totalPorBilletes)))
            
            
            
            index += 1    
            
            
        order_2 = 'SELECT * FROM currency_total'
        index = 0
        query = QSqlQuery()
        query.exec_(order_2)
        
        while query.next():
            total = query.value(1)
            
            self.total_table.setItem(index, 0, QTableWidgetItem(str(total)))    
   
   
    #Total query
    def total_query(self, Total, ID):
        query = 'UPDATE currency_total SET Total = ? WHERE ID = ?'
        parameters = (Total, ID)
        self.run_query(query, parameters)
        
 
            
   
#Conector Global        
class db_query():
    def __init__(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database.db')
        
        if not self.db.open():
            QMessageBox.critical(None, 'Database error', 'No se pudo abrir la base de datos', QMessageBox.Cancel)        
        
        
        
         
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainApp()
    window.show()
    window.history_query()                            
    app.exec_()
    main_wind = Ui_MainWindow()
    
    
    
    
        


    