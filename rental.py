from db import DBConnection as mydb

class Rental:
    def __init__(self):
        self.__idps= None
        self.__no_ps= None
        self.__nama_lengkap= None
        self.__nomor_whatsapp= None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def info(self):
        if(self.__info==None):
            return "Kode rental :" + self.__no_ps + "\n" + "nama lengkap:" + self.__nama_lengkap + "\n" + "nomor whatsapp" + self.__nomor_whatsapp
        else:
            return self.__info

    @property
    def id(self):
        return self.__idps
    
    @property
    def no_ps(self):
        return self.__no_ps

    @no_ps.setter
    def no_ps(self, value):
        self.__no_ps = value
    
    @property
    def nama_lengkap(self):
        return self.__nama_lengkap

    @nama_lengkap.setter
    def nama_lengkap(self, value):
        self.__nama_lengkap = value
    
    @property
    def nomor_whatsapp(self):
        return self.__nomor_whatsapp

    @nomor_whatsapp.setter
    def nomor_whatsapp(self, value):
        self.__nomor_whatsapp = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__no_ps,self.__nama_lengkap,self.__nomor_whatsapp)
        sql="INSERT INTO rental (no_ps,nama_lengkap,nomor_whatsapp) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__no_ps,self.__nama_lengkap,self.__nomor_whatsapp, id)
        sql="UPDATE rental SET no_ps=%s, nama_lengkap=%s, nomor_whatsapp=%s WHERE idps=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateByno_ps(self, no_ps):
        self.conn = mydb()
        val = (self.__no_ps,self.__nama_lengkap,self.__nomor_whatsapp, no_ps)
        sql="UPDATE rental SET no_ps=%s, nama_lengkap=%s, nomor_whatsapp=%s WHERE no_ps=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM rental WHERE idps='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteByno_ps(self, no_ps):
        self.conn = mydb()
        sql="DELETE FROM rental WHERE no_ps='" + str(no_ps) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM rental WHERE idps='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__no_ps = self.result[1]                   
        self.__nama_lengkap = self.result[2]                   
        self.__nomor_whatsapp = (self.result[3])                                     
        self.conn.disconnect
        return self.result
        
    def getByno_ps(self, no_ps):
        a=str(no_ps)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM rental WHERE no_ps='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__no_ps = self.result[1]                   
            self.__nama_lengkap = self.result[2]                   
            self.__nomor_whatsapp = (self.result[3])                   
            self.affected = self.conn.cursor.rowcount
        else:
            self.__no_ps = ''                  
            self.__nama_lengkap = ''                  
            self.__nomor_whatsapp = ''                  
            self.affected = 0
            self.conn.disconnect
            return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM rental"
        self.result = self.conn.findAll(sql)
        return self.result

'''mk = Mahasiswa()
result = mk.getAllData()
print(result)'''