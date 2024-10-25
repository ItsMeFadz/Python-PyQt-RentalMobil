import psycopg2 as mc
class DBConnection:
    def __init__(self):
        self.name = 'pajri'
        self.port = 5432
        self.user = 'fazhri'
        self.password = '123'
        self.host = 'localhost'
        self.conn = None
        self.cursor = None
        self.result = None
        self.connected = False
        self.affected = 0
        self.connect()
        
    @property
    def connection_status(self):
        return self.connected

    @property
    def info(self):
        if(self.connected==True):
            self.cursor.execute('SELECT version();')
            # fetch result
            record = self.cursor.fetchone()
            a='PostgreSQL version = {}'.format(record)
            return a + "\n" + "Server is running on " + self.host + ' using port ' + str(self.port)
        else:
            return "Server is offline."

    
    def connect(self):
        try:           
            self.conn = mc.connect(host = self.host,
                                    port = self.port,
                                    database = self.name,
                                    user = self.user,
                                    password = self.password)

            self.connected = True
            self.cursor=self.conn.cursor()
        except mc.Error as e:
            self.connected = False
        return self.conn

    def disconnect(self):
        if(self.connected==True):
            self.conn.close
        else:
            self.conn = None

    def findOne(self, sql):
        self.connect()
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        a = self.cursor.rowcount
        if(a>0):
            self.result = res
        else:
            self.result = None
        return self.result

    def findAll(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        return self.result

    def insert(self, sql):
        self.connect()  
        self.cursor.execute(sql)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected

    def update(self, sql, val):
        self.connect()  
        self.cursor.execute(sql, val)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected

    def delete(self, sql):
        self.connect()  
        self.cursor.execute(sql)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected

mydb = DBConnection()
print(mydb.info)