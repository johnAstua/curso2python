import pymysql

class Profesor_base:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'sql863.main-hosting.eu',
            user = 'u484426513_apireact',
            password = 'i:![VW:3S#',
            db = 'u484426513_apireact'
        )
        self.cursor = self.connection.cursor()

    def getProfesor(self):
        sql = "SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras FROM profesor"

        try:
            self.cursor.execute(sql)

            profesor = self.cursor.fetchall()

            for item in profesor:
                print('-----------------\n')
                print("id:", item[0])
                print("cedula:", item[1])
                print("correo electronico:", item [2])
                print("telefono:", item [3])
                print("telefono celular:", item [4])
                print("fecha de nacimiento:", item[5])
                print("sexo:", item [6])
                print("direccion:", item [7])
                print("nombre:", item [8])
                print("apellido paterno:", item[9])
                print("apellido materno:", item [10])
                print("nacionalidad:", item [11])
                print("usuario:", item [12])
                print("id carreras", item [13])
                print('-----------------\n')

        except Exception as e:
            print('Error: ', e )
            raise    


    def verificar_profesor_id(self, id):
        sql = "SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras FROM profesor WHERE id={}".format(id)

        try:
            self.cursor.execute(sql)

            profesor = self.cursor.fetchone()
               
            if profesor is None:
                     print("Error, la id {} no existe".format(id))
            
            else:
                print('-----------------\n')
                print("id:", profesor[0])
                print("cedula:", profesor[1])
                print("correo electronico:", profesor [2])
                print("telefono:", profesor [3])
                print("telefono celular:", profesor [4])
                print("fecha de nacimiento:", profesor[5])
                print("sexo:", profesor [6])
                print("direccion:", profesor [7])
                print("nombre:", profesor [8])
                print("apellido paterno:", profesor[9])
                print("apellido materno:", profesor [10])
                print("nacionalidad:", profesor [11])
                print("usuario:", profesor [12])
                print("id carreras", profesor [13])
                print('-----------------\n')

        except Exception as e:
            print('Error: ', e )
            raise    

    def updateProfesor_cedula(self, id, cedula):
        sql = "UPDATE profesor SET cedula='{}' WHERE id='{}'".format(cedula, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  



    def verificar_cambios_profesor(self, id):
            sql = "SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras FROM profesor WHERE id={}".format(id)

            try:
                self.cursor.execute(sql)

                profesor = self.cursor.fetchone()

                if profesor is None:
                     print("Error, la id {} no existe, cambio no realizado".format(id))
                
                else:
                    print('-----------------\n')
                    print("id:", profesor[0])
                    print("cedula:", profesor[1])
                    print("correo electronico:", profesor [2])
                    print("telefono:", profesor [3])
                    print("telefono celular:", profesor [4])
                    print("fecha de nacimiento:", profesor[5])
                    print("sexo:", profesor [6])
                    print("direccion:", profesor [7])
                    print("nombre:", profesor [8])
                    print("apellido paterno:", profesor[9])
                    print("apellido materno:", profesor [10])
                    print("nacionalidad:", profesor [11])
                    print("usuario:", profesor [12])
                    print("id carreras", profesor [13])
                    print('-----------------\n')
                    print("Cambio realizado")
            except Exception as e:
                print('Error: ', e )
                raise  






    def updateProfesor_correo_electronico(self, id, correoelectronico):
        sql = "UPDATE profesor SET correoelectronico='{}' WHERE id='{}'".format(correoelectronico, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateProfesor_telefono(self, id, telefono):
        sql = "UPDATE profesor SET telefono='{}' WHERE id='{}'".format(telefono, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  
    
    def updateProfesor_telefono_celular(self, id, telefonocelular):
        sql = "UPDATE profesor SET telefonocelular='{}' WHERE id='{}'".format(telefonocelular, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateProfesor_fecha_nacimiento(self, id, fechanacimiento):
        sql = "UPDATE profesor SET fechanacimiento='{}' WHERE id='{}'".format(fechanacimiento, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateProfesor_sexo(self, id, sexo):
        sql = "UPDATE profesor SET sexo='{}' WHERE id='{}'".format(sexo, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateProfesor_direccion(self, id, direccion):
        sql = "UPDATE profesor SET direccion='{}' WHERE id='{}'".format(direccion, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateProfesor_nombre(self, id, nombre):
        sql = "UPDATE profesor SET nombre='{}' WHERE id='{}'".format(nombre, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateProfesor_apellido_paterno(self, id, apellidopaterno):
        sql = "UPDATE profesor SET apellidopaterno='{}' WHERE id='{}'".format(apellidopaterno, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  
    
    def updateProfesor_apellido_materno(self, id, apellidomaterno):
        sql = "UPDATE profesor SET apellidomaterno='{}' WHERE id='{}'".format(apellidomaterno, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateProfesor_nacionalidad(self, id, nacionalidad):
        sql = "UPDATE profesor SET nacionalidad='{}' WHERE id='{}'".format(nacionalidad, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  
    
    def updateProfesor_usuario(self, id, usuario):
        sql = "UPDATE profesor SET usuario='{}' WHERE id='{}'".format(usuario, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateProfesor_id_carreras(self, id, idcarreras):
        sql = "UPDATE profesor SET idcarreras='{}' WHERE id='{}'".format(idcarreras, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateProfesor_total(self, id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras):
        sql = "UPDATE profesor SET cedula='{}',correoelectronico='{}',telefono='{}',telefonocelular='{}',fechanacimiento='{}',sexo='{}',direccion='{}',nombre='{}',apellidopaterno='{}',apellidomaterno='{}',nacionalidad='{}',usuario='{}',idcarreras='{}' WHERE id='{}'".format( cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  


    def crear_profesor(self, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras):
        sql = "INSERT INTO profesor(id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(0, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  


    def borrar_profesor(self, id):
        
        sql = "DELETE FROM `profesor`WHERE id='{}'".format(id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
           
        except Exception as e:
            print('Error: ', e )
            raise


    def verificar_borrar_profesor(self, id):
            sql = "SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras FROM profesor WHERE id={}".format(id)

            try:
                self.cursor.execute(sql)

                profesor = self.cursor.fetchone()

                if profesor is None:
                    print("Error, la id {} no existe, no borrado".format(id))
                
                else:
                    print("Registro eliminado")
            except Exception as e:
                print('Error: ', e )
                raise  

            
    def cedula_existente_profesor(self, cedula):
        sql = "SELECT COUNT(*) FROM profesor WHERE cedula = %s"
        try:
            self.cursor.execute(sql, (cedula,))
            count = self.cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print('Error: ', e)
            raise

    def correo_electronico_existente_profesor(self, correoelectronico):
        sql = "SELECT COUNT(*) FROM profesor WHERE correoelectronico = %s"
        try:
            self.cursor.execute(sql, (correoelectronico,))
            count = self.cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print('Error: ', e)
            raise


    def telefono_celular_existente_profesor(self, telefonocelular):
        sql = "SELECT COUNT(*) FROM profesor WHERE telefonocelular = %s"
        try:
            self.cursor.execute(sql, (telefonocelular,))
            count = self.cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print('Error: ', e)
            raise

    def usuaraio_existente_profesor(self, usuario):
        sql = "SELECT COUNT(*) FROM profesor WHERE usuario = %s"
        try:
            self.cursor.execute(sql, (usuario,))
            count = self.cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print('Error: ', e)
            raise


Profesores = Profesor_base()






















Profesores = Profesor_base()


    