import pymysql

class Usuario_base:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'sql863.main-hosting.eu',
            user = 'u484426513_apireact',
            password = 'i:![VW:3S#',
            db = 'u484426513_apireact'
        )
        self.cursor = self.connection.cursor()
    
    def getUsuario(self):
        sql = "SELECT id, name, email, password FROM user"
        
        try:
            self.cursor.execute(sql)

            user = self.cursor.fetchall()
         
            for item in user:
                print('-----------------\n')
                print('id:', item[0])
                print('nombre:',item[1])
                print('correo electronico:',item[2])
                print('contraseña:',item[3])
                print('-----------------\n')

        except Exception as e:
            print('Error: ', e )
            raise

    def verificar_id_usuario (self, id):
        sql = "SELECT id, name, email, password FROM user WHERE id={}".format(id)

        

        try:
            self.cursor.execute(sql)

            user = self.cursor.fetchone()
            if user is None:
                print("Error, la id {} no existe".format(id))
     
            else:
                print('-----------------\n')
                print('id:', user[0])
                print('nombre:',user[1])
                print('correo electronico:',user[2])
                print('contraseña:',user[3])
                print('-----------------\n')

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateUsuario_nombre(self, id, name):
        sql = "UPDATE user SET name='{}' WHERE  id='{}'".format(name, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   


    def verificar_cambios_usuario (self, id):
        sql = "SELECT id, name, email, password FROM user WHERE id={}".format(id)

        try:
            self.cursor.execute(sql)

            user = self.cursor.fetchone()

            if user is None:
                     print("Error, la id {} no existe, cambio no realizado".format(id))
                
            else:
                print('-----------------\n')
                print('id:', user[0])
                print('nombre:',user[1])
                print('correo electronico:',user[2])
                print('contraseña:',user[3])
                print('-----------------\n')
                print("Cambio realizado")
        except Exception as e:
            print('Error: ', e )
            raise  

    def updateUsuario_correo_electronico(self, id, email):
        sql = "UPDATE user SET email='{}' WHERE  id='{}'".format(email, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   

    
    def updateUsuario_paswword(self, id, password):
        sql = "UPDATE user SET password='{}' WHERE  id='{}'".format(password, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   

    def updateUsuario_total(self, id, name, email, password):
        sql = "UPDATE user SET name='{}',email='{}',password='{}' WHERE  id='{}'".format(name, email, password, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   

    def crear_Usuario(self, name, email, password):
        sql = "INSERT INTO user(id, name, email, password) VALUES ('{}','{}','{}','{}')".format(0, name, email, password)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   

    def borrar_Usuario(self, id):
        sql ="DELETE FROM `user` WHERE  id ={}".format(id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   
    
    def verificar_borrar_usuario (self, id):
        sql = "SELECT id, name, email, password FROM user WHERE id={}".format(id)

        try:
            self.cursor.execute(sql)

            user = self.cursor.fetchone()

            if user is None:
                print("Error, la id {} no existe, no borrado".format(id))
                
            else:
                print("Registro eliminado")

        except Exception as e:
            print('Error: ', e )
            raise



    def correo_existe_usuario(self, email):
        sql = "SELECT COUNT(*) FROM user WHERE email = %s"
        try:
            self.cursor.execute(sql, (email,))
            count = self.cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print('Error: ', e)
            raise


                

usuarios = Usuario_base()