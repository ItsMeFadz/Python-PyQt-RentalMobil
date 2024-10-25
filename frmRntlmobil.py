import sys
from PyQt5 import QtWidgets, uic
import psycopg2 as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from rntlMobil import rentalmobil

qtcreator_file  = "Rentalmobil.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class RentalmobilWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtNoktp.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox noktp
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    #def select_data(self):
        #try:
            #rntl = rentalmobil()

            # Get all 
            #result = rntl.getAllData()

            #self.gridMahasiswa.setHorizontalHeaderLabels(['ID', 'noktp', 'Nama', 'Jenis Kelamin', 'Prodi'])
            #elf.gridMahasiswa.setRowCount(0)
            

            #for row_number, row_data in enumerate(result):
                #print(row_number)
                #self.gridMahasiswa.insertRow(row_number)
                #for column_number, data in enumerate(row_data):
                    #print(column_number)
                    #self.gridMahasiswa.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        #except mc.Error as e:
            #self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            noktp=self.txtNoktp.text()           
            rntl = rentalmobil()

            # search process
            result = rntl.getBynoktp(noktp)
            a = rntl.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data Anda tidak ditemukan")
                self.txtNama.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            rntl = rentalmobil()
            noktp=self.txtNoktp.text()
            nama=self.txtNama.text()
            if self.optLaki.isChecked():
                jk="L"
            
            if self.optPerempuan.isChecked():
                jk="P"
            
            nowa=self.txtNowa.text()
            jenis=self.cboJenis.currentText()
            pilihan=self.cboPilihan.currentText()
            peminjaman=self.txtPeminjaman.text()
            pengembalian=self.txtPengembalian.text()
            
            if(self.edit_mode==False):   
                rntl.noktp = noktp
                rntl.nama = nama
                rntl.jk = jk
                rntl.nowa = nowa
                rntl.jenis = jenis
                rntl.pilihan = pilihan
                rntl.peminjaman = peminjaman
                rntl.pengembalian = pengembalian
                a = rntl.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Anda Tersimpan")
                    self.messagebox("TERIMA KASIH", "Silahkan Menuju Kasir Untuk Melakukan Pembayaran")
                else:
                    self.messagebox("GAGAL", "Data Anda Gagal Tersimpan")
                
                self.clear_entry(self) # Clear Entry Form
                #self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                rntl.nama = nama
                rntl.jk = jk
                rntl.nowa = nowa
                rntl.jenis = jenis
                rntl.pilihan = pilihan
                rntl.peminjaman = peminjaman
                rntl.pengembalian = pengembalian
                a = rntl.updateBynoktp(noktp)
                if(a>0):
                    self.messagebox("SUKSES", "Data Anda Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Anda Gagal Diperbarui")
                
                self.clear_entry(self) # Clear Entry Form
                #self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def delete_data(self, MainWindow):
        try:
            rntl = rentalmobil()
            noktp=self.txtNoktp.text()
                       
            if(self.edit_mode==True):
                a = rntl.deleteBynoktp(noktp)
                if(a>0):
                    self.messagebox("SUKSES", "Data Anda Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Anda Gagal Dihapus")
                
                self.clear_entry(self) # Clear Entry Form
                #self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def TampilData(self,result):
        self.txtNoktp.setText(result[1])
        self.txtNama.setText(result[2])
        if(result[3]=="L"):
            self.optLaki.setChecked(True)
            self.optPerempuan.setChecked(False)
        else:
            self.optLaki.setChecked(False)
            self.optPerempuan.setChecked(True)

        self.txtNowa.setText(result[4])
        self.cboJenis.setCurrentText(result[5])
        self.cboPilihan.setCurrentText(result[6])
        self.txtPeminjaman.setText(result[7])
        self.txtPengembalian.setText(result[8])
        self.btnSimpan.setText("Update")
        self.edit_mode=True
        self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
        self.btnHapus.setStyleSheet("background-color : red")

    def clear_entry(self, MainWindow):
        self.txtNoktp.setText("")
        self.txtNama.setText("")
        self.optLaki.setChecked(False)
        self.optPerempuan.setChecked(False)
        self.txtNowa.setText("")
        self.cboJenis.setCurrentText("")
        self.cboPilihan.setCurrentText("")
        self.txtPeminjaman.setText("")
        self.txtPengembalian.setText("")
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : blue")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RentalmobilWindow()
    window.show()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = RentalmobilWindow()