import pymysql

class curso_base:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'sql863.main-hosting.eu',
            user = 'u484426513_apireact',
            password = 'i:![VW:3S#',
            db = 'u484426513_apireact'
        )
        self.cursor = self.connection.cursor()
        

    def getCurso(self):
        sql = 'SELECT id, nombre, descripcion, tiempo, usuario FROM curso'

        try:
            self.cursor.execute(sql)

            curso = self.cursor.fetchall()
          
           
            for item in curso:
                print('-----------------\n')
                print('id:', item[0])
                print('nombre:',item[1])
                print('descripcion:',item[2])
                print('tiempo:',item[3])
                print('usuario:',item[4])
                print('-----------------\n')

        except Exception as e:
            print('Error: ', e )
            raise

    def getCurso_Id(self, id):
            sql = 'SELECT id, nombre, descripcion, tiempo, usuario FROM curso WHERE id={}'.format(id)

            try:
                self.cursor.execute(sql)

                curso = self.cursor.fetchone()
                print('-----------------\n')
                print('id:', curso[0])
                print('nombre:',curso[1])
                print('descripcion:',curso[2])
                print('tiempo:',curso[3])
                print('usuario:',curso[4])
                print('-----------------\n')

            except Exception as e:
                print('Error: ', e )
                raise  

    def updateCurso_nombre(self, id, nombre):
        sql = "UPDATE curso SET nombre='{}' WHERE id='{}'".format(nombre, id)
         
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e )
            raise   





    def updateCurso_descripcion(self, id, descripcion):
        sql = "UPDATE curso SET descripcion='{}' WHERE id='{}'".format(descripcion, id)
         
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e )
            raise   

    def updateCurso_tiempo(self, id, tiempo):
        sql = "UPDATE curso SET tiempo='{}' WHERE id='{}'".format(tiempo, id)
         
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e )
            raise   


    def updateCurso_usuario(self, id, usuario):
        sql = "UPDATE curso SET usuario='{}' WHERE id='{}'".format(usuario, id)
         
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e )
            raise   



    def updateCurso_total(self, id, nombre, descripcion, tiempo, usuario ):
        sql = "UPDATE curso SET nombre='{}', descripcion='{}', tiempo='{}', usuario='{}' WHERE id='{}'".format(nombre, descripcion, tiempo, usuario, id)
         
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e )
            raise   


    def crearCurso(self, nombre, descripcion, tiempo, usuario):
        
        sql = "INSERT INTO curso(id, nombre, descripcion, tiempo, usuario) VALUES ('{}','{}','{}','{}','{}')".format(0, nombre, descripcion, tiempo, usuario)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  



    def borrarCurso(self, id):
        
        sql = "DELETE FROM `curso`WHERE id='{}'".format(id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
           
        except Exception as e:
            print('Error: ', e )
            raise






    def verificar_id_curso(self, id):
            sql = 'SELECT id, nombre, descripcion, tiempo, usuario FROM curso WHERE id={}'.format(id)


            try:
                self.cursor.execute(sql)

                curso = self.cursor.fetchone()

                if curso is None:
                     print("Error, la id {} no existe".format(id))
                
                else:
                    print('-----------------\n')
                    print('id:', curso[0])
                    print('nombre:',curso[1])
                    print('descripcion:',curso[2])
                    print('tiempo:',curso[3])
                    print('usuario:',curso[4])
                    print('-----------------\n')

            except Exception as e:
                print('Error: ', e )
                raise  

    def verificar_cambios_curso(self, id):
            sql = 'SELECT id, nombre, descripcion, tiempo, usuario FROM curso WHERE id={}'.format(id)


            try:
                self.cursor.execute(sql)

                curso = self.cursor.fetchone()

                if curso is None:
                     print("Error, la id {} no existe, cambio no realizado".format(id))
                
                else:
                    print('-----------------\n')
                    print('id:', curso[0])
                    print('nombre:',curso[1])
                    print('descripcion:',curso[2])
                    print('tiempo:',curso[3])
                    print('usuario:',curso[4])
                    print('-----------------\n')
                    print("Cambio realizado")
            except Exception as e:
                print('Error: ', e )
                raise  


    def verificar_curso_borrado(self, id):
            sql = 'SELECT id, nombre, descripcion, tiempo, usuario FROM curso WHERE id={}'.format(id)


            try:
                self.cursor.execute(sql)

                curso = self.cursor.fetchone()

                if curso is None:
                     print("Error, la id {} no existe, no borrado".format(id))
                
                else:    
                    print("Registro eliminado")
                    
            except Exception as e:
                print('Error: ', e )
                raise  
    


    def usuaraio_existente_curso(self, usuario):
        sql = "SELECT COUNT(*) FROM curso WHERE usuario = %s"
        try:
            self.cursor.execute(sql, (usuario,))
            count = self.cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print('Error: ', e)
            raise



Cursos = curso_base()
