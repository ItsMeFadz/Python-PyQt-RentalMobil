import os, sys; sys.path.insert(0,os.path.dirname(os.path.realpath(__name__)))
import sys
from PyQt5 import QtWidgets, uic
import psycopg2 as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from rental import Rental

qtcreator_file  = "rental.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowRental(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtNops.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox nops
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")
        self.select_data()

    def select_data(self):
        try:
            rntl = Rental()

            # Get all 
            result = rntl.getAllData()

            self.gridRental.setHorizontalHeaderLabels(['ID', 'nops', 'nama', 'nowa'])
            self.gridRental.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridRental.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridRental.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            no_ps=self.txtNops.text()           
            rntl = Rental()
            # search process
            result = rntl.getByno_ps(no_ps)           
            a = rntl.affected
            if(a!=0):
                self.txtNama.setText(rntl.nama_lengkap.strip())
                self.txtWa.setText(rntl.nomor_whatsapp.strip())
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
                self.btnHapus.setStyleSheet("background-color : red")
            else:
                self.messagebox("INFORMASI PENTING ", "Data tidak ditemukan")
                self.txtNops.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            rntl = Rental()
            nops = self.txtNops.text()
            nama=self.txtNama.text()
            nowa=self.txtWa.text()
            
            if(self.edit_mode==False):   
                rntl.no_ps = nops
                rntl.nama_lengkap = nama
                rntl.nomor_whatsapp = nowa
                a = rntl.simpan()
                if(a>0):
                    self.messagebox("SELAMAT", "Data Rental Tersimpan")
                else:
                    self.messagebox("MAAF", "Data Rental Gagal Tersimpan")
                
                self.clear_entry(MainWindow) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                rntl.no_ps = nops
                rntl.nama_lengkap = nama
                rntl.nomor_whatsapp = nowa
                a = rntl.updateByno_ps(nops)
                if(a>0):
                    self.messagebox("SUKSES", "Data Rental Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Rental Gagal Diperbarui")
                
                self.clear_entry(MainWindow) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self, MainWindow):
        try:
            rntl = Rental()
            no_ps = self.txtNops.text()
                       
            if(self.edit_mode==True):
                a = rntl.deleteByno_ps(no_ps)
                if(a>0):
                    self.messagebox("SELAMAT", "Data Rental Dihapus")
                    self.txtNops.setFocus()
                else:
                    self.messagebox("MAAF", "Data Rental Gagal Dihapus")
                    self.txtNops.setFocus()
                
                self.clear_entry(MainWindow) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self, MainWindow):
        self.txtNops.setText("")
        self.txtNama.setText("")
        self.txtWa.setText("")
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowRental()
    window.show()
    window.select_data()
    sys.exit(app.exec_())