from db import DBConnection as mydb

class Bengkel:

    def __init__(self):
        self.__no=None
        self.__id=None
        self.__nama=None
        self.__jk=None
        self.__jm=None
        self.__kerusakan=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "id:" + self.__id + "\n" + "Nama:" + self.__nama + "\n" + "Jk" + self.__jk + "\n" + "Jenis Mobil"+ self.__jm + "\n" + "Kerusakan:" + self.__kerusakan
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
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value
    
    @property
    def jm(self):
        return self.__jm

    @jk.setter
    def jm(self, value):
        self.__jm = value

    @property
    def kerusakan(self):
        return self.__kerusakan

    @kerusakan.setter
    def kerusakan(self, value):
        self.__kerusakan = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__id, self.__nama, self.__jk, self.__jm, self.__kerusakan)
        sql="INSERT INTO bengkel (id, nama, jk, jm, kerusakan) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, no):
        self.conn = mydb()
        val = (self.__id, self.__nama, self.__jk, self.__jm,self.__kerusakan, no)
        sql="UPDATE bengkel SET id = %s, nama = %s, jk=%s, jm=%s, kerusakan=%s WHERE nomhs=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByid(self, id):
        self.conn = mydb()
        val = (self.__nama, self.__jk, self.__jm, self.__kerusakan, id)
        sql="UPDATE bengkel SET nama = %s, jk=%s, jm=%s,kerusakan=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, no):
        self.conn = mydb()
        sql="DELETE FROM bengkel WHERE nomhs='" + str(no) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByid(self, id):
        self.conn = mydb()
        sql="DELETE FROM bengkel WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByno(self, no):
        self.conn = mydb()
        sql="SELECT * FROM bengkel WHERE nomhs='" + str(no) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.__jm = self.result[4]
        self.__kerusakan = self.result[5]
        self.conn.disconnect
        return self.result

    def getByid(self, id):
        self.conn = mydb()
        sql="SELECT * FROM bengkel WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__id = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.__jm = self.result[4]
            self.__kerusakan = self.result[5]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__id = ''
            self.__nama = ''
            self.__jk = ''
            self.__jm = ''
            self.__kerusakan = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM bengkel limit 100"
        self.result = self.conn.findAll(sql)
        return self.result
