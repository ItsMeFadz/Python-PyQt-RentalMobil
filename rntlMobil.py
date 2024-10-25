from db import DBConnection as mydb

class rentalmobil:

    def __init__(self):
        self.__id=None
        self.__noktp=None
        self.__nama=None
        self.__jk=None
        self.__nowa=None
        self.__jenis=None
        self.__pilihan=None
        self.__peminjaman=None
        self.__pengembalian=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "noktp:" + self.__noktp + "\n" + "nama:" + self.__nama + "\n" + "Jk" + self.__jk + "\n" + "Nowa" + self.__nowa + "\n" + "jenis:" + self.__jenis + "\n" + "Pilihan" + self.__pilihan + "\n" + "Peminjaman" + self.__peminjaman + "\n" + "Pengembalian" + self.__pengembalian 
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__id

    @property
    def noktp(self):
        return self.__noktp

    @noktp.setter
    def noktp(self, value):
        self.__noktp = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def nowa(self):
        return self.__nowa

    @nowa.setter
    def nowa(self, value):
        self.__nowa = value

    @property
    def jenis(self):
        return self.__jenis

    @jenis.setter
    def jenis(self, value):
        self.__jenis = value

    @property
    def pilihan(self):
        return self.__pilihan

    @pilihan.setter
    def pilihan(self, value):
        self.__pilihan = value

    @property
    def peminjaman(self):
        return self.__peminjaman

    @peminjaman.setter
    def peminjaman(self, value):
        self.__peminjaman = value

    @property
    def pengembalian(self):
        return self.__pengembalian

    @pengembalian.setter
    def pengembalian(self, value):
        self.__pengembalian = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__noktp, self.__nama, self.__jk, self.__nowa, self.__jenis, self.__pilihan, self.__peminjaman, self.__pengembalian)
        sql="INSERT INTO rentalmobil (noktp, nama, jk, nowa, jenis, pilihan, peminjaman, pengembalian) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__noktp, self.__nama, self.__jk, self.__nowa, self.__jenis, self.__pilihan, self.__peminjaman, self.__pengembalian, id)
        sql="UPDATE rentalmobil SET noktp = %s, nama = %s, jk=%s, nowa=%s, jenis=%s, pilihan=%s, peminjaman=%s, pengembalian=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBynoktp(self, noktp):
        self.conn = mydb()
        val = (self.__nama, self.__jk, self.__nowa, self.__jenis, self.__pilihan, self.__peminjaman, self.__pengembalian, noktp)
        sql="UPDATE rentalmobil SET nama = %s, jk=%s, nowa=%s, jenis=%s, pilihan=%s, peminjaman=%s, pengembalian=%s WHERE noktp=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM rentalmobil WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBynoktp(self, noktp):
        self.conn = mydb()
        sql="DELETE FROM rentalmobil WHERE noktp='" + str(noktp) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM rentalmobil WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__noktp = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.__jenis = self.result[4]
        self.conn.disconnect
        return self.result

    def getBynoktp(self, noktp):
        self.conn = mydb()
        sql="SELECT * FROM rentalmobil WHERE noktp='" + str(noktp) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__noktp = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.__nowa = self.result[4]
            self.__jenis = self.result[5]
            self.__pilihan = self.result[6]
            self.__peminjaman = self.result[7]
            self.__pengembalian = self.result[8]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__noktp = ''
            self.__nama = ''
            self.__jk = ''
            self.__nowa = ''
            self.__jenis = ''
            self.__pilihan = ''
            self.__peminjaman = ''
            self.__pengembalian = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM rentalmobil limit 100"
        self.result = self.conn.findAll(sql)
        return self.result
