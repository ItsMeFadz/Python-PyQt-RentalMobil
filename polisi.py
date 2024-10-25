from db import DBConnection as mydb

class Polisi:

    def __init__(self):
        self.__id=None
        self.__no_seri=None
        self.__nama=None
        self.__jk=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "no_seri:" + self.__no_seri + "\n" + "Nama:" + self.__nama + "\n" + "Jk" + self.__jk
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__id

    @property
    def no_seri(self):
        return self.__no_seri

    @no_seri.setter
    def no_seri(self, value):
        self.__no_seri = value

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

    def simpan(self):
        self.conn = mydb()
        val = (self.__no_seri, self.__nama, self.__jk)
        sql="INSERT INTO polisi (no_seri, nama, jk) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__no_seri, self.__nama, self.__jk, id)
        sql="UPDATE polisi SET no_seri= %s, nama = %s, jk=%s WHERE idmhs=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByno_seri(self, no_seri):
        self.conn = mydb()
        val = (self.__nama, self.__jk , no_seri)
        sql="UPDATE polisi SET nama = %s, jk=%s WHERE no_seri=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM polisi WHERE idmhs='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByno_seri(self, no_seri):
        self.conn = mydb()
        sql="DELETE FROM polisi WHERE no_seri='" + str(no_seri) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM polisi WHERE idmhs='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__no_seri = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.conn.disconnect
        return self.result

    def getByno_seri(self, no_seri):
        self.conn = mydb()
        sql="SELECT * FROM polisi WHERE no_seri='" + str(no_seri) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__no_seri = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__no_seri = ''
            self.__nama = ''
            self.__jk = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM polisi limit 100"
        self.result = self.conn.findAll(sql)
        return self.result
