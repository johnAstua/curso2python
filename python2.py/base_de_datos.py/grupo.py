import pymysql

class Grupo_base:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'sql863.main-hosting.eu',
            user = 'u484426513_apireact',
            password = 'i:![VW:3S#',
            db = 'u484426513_apireact'
        )
        self.cursor = self.connection.cursor()

    def getGrupo (self):
        sql = "SELECT id, nombre FROM grupo"

        try:
            self.cursor.execute(sql)

            grupo = self.cursor.fetchall()
          
            for item in grupo:
                print('-----------------\n')
                print('id:', item[0])
                print('nombre:',item[1])
                print('-----------------\n')

        except Exception as e:
            print('Error: ', e )
            raise

        
    def getGrupoID(self, id):
        sql = "SELECT id, nombre FROM grupo WHERE id={}".format(id)

        try:
            self.cursor.execute(sql)

            grupo = self.cursor.fetchall()
          
           
            print('-----------------\n')
            print('id:', grupo[0])
            print('nombre:',grupo[1])
            print('-----------------\n')

        except Exception as e:
            print('Error: ', e )
            raise

    def verificar_id_grupo(self, id):
            sql ="SELECT id, nombre FROM grupo WHERE id={}".format(id)


            try:
                self.cursor.execute(sql)

                grupo = self.cursor.fetchone()

                if grupo is None:
                     print("Error, la id {} no existe".format(id))
                
                else:
                    print('-----------------\n')
                    print('id:', grupo[0])
                    print('nombre:',grupo[1])
                    print('-----------------\n')

            except Exception as e:
                print('Error: ', e )
                raise  
 

    def updateGrupo_nombre(self, id, nombre):
        sql = "UPDATE grupo SET nombre='{}' WHERE id='{}'".format(nombre, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   


    def verificar_cambios_grupo(self, id):
            sql ="SELECT id, nombre FROM grupo WHERE id={}".format(id)


            try:
                self.cursor.execute(sql)

                grupo = self.cursor.fetchone()

                if grupo is None:
                     print("Error, la id {} no existe, cambio no realizado".format(id))
                
                else:
                    print('-----------------\n')
                    print('id:', grupo[0])
                    print('nombre:',grupo[1])
                    print('-----------------\n')
                    print("Cambio realizado")
            except Exception as e:
                print('Error: ', e )
                raise  
 
    def crearGrupo (self, nombre):
        sql = " INSERT INTO grupo(id, nombre) VALUES ('{}','{}')".format(0, nombre)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   


    def borrar_grupo (self, id):
        sql = "DELETE FROM `grupo` WHERE  id ={}".format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

            
        except Exception as e:
            print('Error: ', e )
            raise


    def verificar_borrado_grupo (self, id):
        sql = "SELECT id, nombre FROM grupo WHERE id={}".format(id)

        try:
            self.cursor.execute(sql)

            grupo = self.cursor.fetchall()
          
            if grupo is None:
                    print("Error, la id {} no existe, no borrado".format(id))
                
            else:
                print("Registro eliminado")
          
        except Exception as e:
            print('Error: ', e )
            raise  


grupos = Grupo_base()