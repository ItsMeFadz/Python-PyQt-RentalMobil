from db import DBConnection as mydb

class Napi:

    def __init__(self):
        self.__no=None
        self.__id=None
        self.__nama=None
        self.__umur=None
        self.__jk=None
        self.__kasus=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "id:" + self.__id + "\n" + "Nama:" + self.__nama + "\n" + "Umur"+ self.__umur + "\n" + "Jk" + self.__jk + "\n" + "kasus:" + self.__kasus
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def no(self):
        return self.__no


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value


    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value


    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, value):
        self.__umur = value
    

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value
    

    @property
    def kasus(self):
        return self.__kasus

    @kasus.setter
    def kasus(self, value):
        self.__kasus = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__id, self.__nama, self.__umur, self.__jk, self.__kasus)
        sql="INSERT INTO napi (id, nama, umur, jk, kasus) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, no):
        self.conn = mydb()
        val = (self.__id, self.__nama, self.__umur, self.__jk, self.__kasus, no)
        sql="UPDATE napi SET id = %s, nama = %s, umur=%s, jk=%s, kasus=%s WHERE no=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByid(self, id):
        self.conn = mydb()
        val = (self.__nama, self.__umur, self.__jk, self.__kasus, id)
        sql="UPDATE napi SET nama = %s, umur=%s, jk=%s, kasus=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, no):
        self.conn = mydb()
        sql="DELETE FROM napi WHERE no='" + str(no) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByid(self, id):
        self.conn = mydb()
        sql="DELETE FROM napi WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByno(self, no):
        self.conn = mydb()
        sql="SELECT * FROM napi WHERE no='" + str(no) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[1]
        self.__nama = self.result[2]
        self.__umur = self.result[3]
        self.__jk = self.result[4]
        self.__kasus = self.result[5]
        self.conn.disconnect
        return self.result

    def getByid(self, id):
        self.conn = mydb()
        sql="SELECT * FROM napi WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__id = self.result[1]
            self.__nama = self.result[2]
            self.__umur = self.result[3]
            self.__jk = self.result[4]
            self.__kasus = self.result[5]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__id = ''
            self.__nama = ''
            self.__umur = ''
            self.__jk = ''
            self.__kasus = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM napi limit 100"
        self.result = self.conn.findAll(sql)
        return self.result
