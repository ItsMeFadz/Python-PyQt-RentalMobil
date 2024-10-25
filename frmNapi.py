import sys
from PyQt5 import QtWidgets, uic
import psycopg2 as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from napi import Napi

qtcreator_file  = "napi.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class NapiWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtID.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox id
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def select_data(self):
        try:
            mhs = Napi()

            # Get all 
            result = mhs.getAllData()

            self.gridNapi.setHorizontalHeaderLabels(['Data Ke-', 'Id', 'Nama Lengkap', 'Umur', 'Jenis Kelamin', 'Kasus'])
            self.gridNapi.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridNapi.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridNapi.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            id=self.txtID.text()           
            mhs = Napi()

            # search process
            result = mhs.getByid(id)
            a = mhs.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNama.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            mhs = Napi()
            id=self.txtID.text()
            nama=self.txtNama.text()
            umur=self.txtUmur.text()
            if self.optLaki.isChecked():
                jk="L"
            
            if self.optPerempuan.isChecked():
                jk="P"
    
            kasus=self.txtKasus.text()
            
            if(self.edit_mode==False):   
                mhs.id = id
                mhs.nama = nama
                mhs.jk = jk
                mhs.umur = umur
                mhs.kasus = kasus
                a = mhs.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data napi Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data napi Gagal Tersimpan")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                mhs.nama = nama
                mhs.jk = jk
                mhs.umur = umur
                mhs.kasus = kasus
                a = mhs.updateByid(id)
                if(a>0):
                    self.messagebox("SUKSES", "Data napi Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data napi Gagal Diperbarui")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def delete_data(self, MainWindow):
        try:
            mhs = Napi()
            id=self.txtID.text()
                       
            if(self.edit_mode==True):
                a = mhs.deleteByid(id)
                if(a>0):
                    self.messagebox("SUKSES", "Data napi Dihapus")
                else:
                    self.messagebox("GAGAL", "Data napi Gagal Dihapus")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def TampilData(self,result):
        self.txtID.setText(result[1])
        self.txtNama.setText(result[2])
        self.txtUmur.setText(result[3])
        if(result[4]=="L"):
            self.optLaki.setChecked(True)
            self.optPerempuan.setChecked(False)
        else:
            self.optLaki.setChecked(False)
            self.optPerempuan.setChecked(True)

        self.txtKasus.setText(result[5])
        self.btnSimpan.setText("Update")
        self.edit_mode=True
        self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
        self.btnHapus.setStyleSheet("background-color : red")

    def clear_entry(self, MainWindow):
        self.txtID.setText("")
        self.txtNama.setText("")
        self.txtUmur.setText("")
        self.optLaki.setChecked(False)
        self.optPerempuan.setChecked(False)
        self.txtKasus.setText("")
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
    window = NapiWindow()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = NapiWindow()