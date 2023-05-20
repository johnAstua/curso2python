import pymysql

class estudiante_base:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'sql863.main-hosting.eu',
            user = 'u484426513_apireact',
            password = 'i:![VW:3S#',
            db = 'u484426513_apireact'
        )
        self.cursor = self.connection.cursor()
        
    def getEstudiante(self):
        sql = "SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idCarreras, usuario FROM estudiante"

        try:
            self.cursor.execute(sql)

            estudiante = self.cursor.fetchall()

            for item in estudiante:
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
                print("id carreras", item [12])
                print("usuario:", item [13])
                print('-----------------\n')

        except Exception as e:
            print('Error: ', e )
            raise    

    def getEstudiante_Id(self, id):
        sql = "SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idCarreras, usuario FROM estudiante WHERE=id {}".format(id)

        try:
            self.cursor.execute(sql)

            estudiante = self.cursor.fetchone()

            
            print('-----------------\n')
            print("id:", estudiante[0])
            print("cedula:", estudiante[1])
            print("correo electronico:", estudiante [2])
            print("telefono:", estudiante [3])
            print("telefono celular:", estudiante [4])
            print("fecha de nacimiento:", estudiante[5])
            print("sexo:", estudiante [6])
            print("direccion:", estudiante [7])
            print("nombre:", estudiante [8])
            print("apellido paterno:", estudiante[9])
            print("apellido materno:", estudiante [10])
            print("nacionalidad:", estudiante [11])
            print("id carreras", estudiante [12])
            print("usuario:", estudiante [13])
            print('-----------------\n')

        except Exception as e:
            print('Error: ', e )
            raise    

    def updateEstudiante_cedula(self, id, cedula):
        sql = "UPDATE estudiante SET cedula='{}' WHERE  id='{}'".format(cedula, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  


    def updateEstudiante_correo(self, id, correoelectronico):
        sql = "UPDATE estudiante SET correoelectronico='{}' WHERE  id='{}'".format(correoelectronico, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  


    def updateEstudiante_telefono(self, id, telefono):
        sql = "UPDATE estudiante SET telefono='{}' WHERE  id='{}'".format(telefono, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  
    
    def updateEstudiante_telefono_celular(self, id, telefonocelular):
        sql = "UPDATE estudiante SET telefonocelular='{}' WHERE  id='{}'".format(telefonocelular, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  
    
    def updateEstudiante_fecha_nacimiento(self, id, fechanacimiento):
        sql = "UPDATE estudiante SET fechanacimiento='{}' WHERE  id='{}'".format(fechanacimiento, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateEstudiante_sexo(self, id, sexo):
        sql = "UPDATE estudiante SET sexo='{}' WHERE  id='{}'".format(sexo, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateEstudiante_direccion(self, id, direccion):
        sql = "UPDATE estudiante SET direccion='{}' WHERE  id='{}'".format(direccion, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    
    def updateEstudiante_nombre(self, id, nombre):
        sql = "UPDATE estudiante SET nombre='{}' WHERE  id='{}'".format(nombre, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  


    def updateEstudiante_apellido_paterno(self, id, apellidopaterno):
        sql = "UPDATE estudiante SET apellidopaterno='{}' WHERE  id='{}'".format(apellidopaterno, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateEstudiante_apellido_materno(self, id, apellidomaterno):
        sql = "UPDATE estudiante SET apellidomaterno='{}' WHERE  id='{}'".format(apellidomaterno, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateEstudiante_nacionalidad(self, id, nacionalidad):
        sql = "UPDATE estudiante SET nacionalidad='{}' WHERE  id='{}'".format(nacionalidad, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateEstudiante_id_carreras(self, id, idcarreras):
        sql = "UPDATE estudiante SET  idCarreras='{}' WHERE  id='{}'".format(idcarreras, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def updateEstudiante_usuario(self, id, usuario):
        sql = "UPDATE estudiante SET usuario='{}' WHERE  id='{}'".format(usuario, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  


    def updateEstudiante_total(self, id,  cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idcarreras, usuario):
        sql = "UPDATE estudiante SET cedula='{}',correoelectronico='{}',telefono='{}',telefonocelular='{}',fechanacimiento='{}',sexo='{}',direccion='{}',nombre='{}',apellidopaterno='{}',apellidomaterno='{}',nacionalidad='{}',idcarreras='{}', usuario='{}' WHERE id='{}'".format( cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idcarreras, usuario, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  

    def crearEstudiante(self, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idcarreras, usuario):
        sql = "INSERT INTO estudiante(id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idCarreras, usuario) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(0, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idcarreras, usuario )


        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  


    def borrarEstudiante( self, id):
        sql= "DELETE FROM `estudiante`WHERE id='{}'".format(id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

            
        except Exception as e:
            print('Error: ', e )
            raise






    def verificar_cambios_estudiante(self, id):
            sql = "SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idCarreras, usuario FROM estudiante WHERE id={}".format(id)

            try:
                self.cursor.execute(sql)

                estudiante = self.cursor.fetchone()

                if estudiante is None:
                     print("Error, la id {} no existe, cambio no realizado".format(id))
                
                else:
                    print('-----------------\n')                  
                    print("id:", estudiante[0])
                    print("cedula:", estudiante[1])
                    print("correo electronico:", estudiante [2])
                    print("telefono:", estudiante [3])
                    print("telefono celular:", estudiante [4])
                    print("fecha de nacimiento:", estudiante[5])
                    print("sexo:", estudiante [6])
                    print("direccion:", estudiante [7])
                    print("nombre:", estudiante [8])
                    print("apellido paterno:", estudiante[9])
                    print("apellido materno:", estudiante [10])
                    print("nacionalidad:", estudiante [11])
                    print("id carreras", estudiante [12])
                    print("usuario:", estudiante [13])       
                    print('-----------------\n')
                    print("Cambio realizado")
            except Exception as e:
                print('Error: ', e )
                raise  



    def verificar_borrar_estudiante(self, id):
            sql = "SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idCarreras, usuario FROM estudiante WHERE id={}".format(id)

            try:
                self.cursor.execute(sql)

                estudiante = self.cursor.fetchone()

                if estudiante is None:
                    print("Error, la id {} no existe, no borrado".format(id))
                
                else:
                    print("Registro eliminado")
            except Exception as e:
                print('Error: ', e )
                raise  


















    def verificar_id_estudiante(self, id):
            sql = "SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idCarreras, usuario FROM estudiante WHERE id={}".format(id)


            try:
                self.cursor.execute(sql)

                estudiante = self.cursor.fetchone()

                if estudiante is None:
                     print("Error, la id {} no existe".format(id))
                
                else: 
                    print('-----------------\n')
                    print("id:", estudiante[0])
                    print("cedula:", estudiante[1])
                    print("correo electronico:", estudiante [2])
                    print("telefono:", estudiante [3])
                    print("telefono celular:", estudiante [4])
                    print("fecha de nacimiento:", estudiante[5])
                    print("sexo:", estudiante [6])
                    print("direccion:", estudiante [7])
                    print("nombre:", estudiante [8])
                    print("apellido paterno:", estudiante[9])
                    print("apellido materno:", estudiante [10])
                    print("nacionalidad:", estudiante [11])
                    print("id carreras",estudiante[12])
                    print("usuario:", estudiante [13])
                    print('-----------------\n')

            except Exception as e:
                print('Error: ', e )
                raise  

    def usuaraio_existente_estudiante(self, usuario):
        sql = "SELECT COUNT(*) FROM estudiante WHERE usuario = %s"
        try:
            self.cursor.execute(sql, (usuario,))
            count = self.cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print('Error: ', e)
            raise


    def cedula_existente_estudiante(self, cedula):
        sql = "SELECT COUNT(*) FROM estudiante WHERE cedula = %s"
        try:
            self.cursor.execute(sql, (cedula,))
            count = self.cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print('Error: ', e)
            raise

    
    def correo_electronico_existente_estudiante(self, correoelectronico):
        sql = "SELECT COUNT(*) FROM estudiante WHERE correoelectronico = %s"
        try:
            self.cursor.execute(sql, (correoelectronico,))
            count = self.cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print('Error: ', e)
            raise

 

    def telefono_celular_existente_estudiante(self, telefonocelular):
        sql = "SELECT COUNT(*) FROM estudiante WHERE telefonocelular = %s"
        try:
            self.cursor.execute(sql, (telefonocelular,))
            count = self.cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print('Error: ', e)
            raise

Estudiantes = estudiante_base()