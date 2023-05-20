from curso import Cursos
from limpiar_consola import limpiar_consola
from Estudiante import Estudiantes
from profesor import Profesores
from grupo import grupos
from usuario import usuarios
from fechas import validar_fecha


eleccion  = 0 

while eleccion != 6:
    limpiar_consola()
    print("""
    Base de datos

Eliga una de las secciones:

    1-Curso
    2-Estudiante
    3-Profesor
    4-Grupo
    5-Usuario
    6-Salir
    """)

    error_elecion = False
    eleccion_input = input("Numero de la seccion:")
    while True:
        if not eleccion_input:
            eleccion_input = input("(Error, no puede estar vacio)Numero de la seccion:")
            error_elecion = True
        elif not eleccion_input.isdigit():
            eleccion_input = input("(Error, solo se permiten numeros)Numero de la seccion:")
            error_elecion = True     

        elif int(eleccion_input) not in range (1, 7):
            eleccion_input = input("(Error, numero no valido)Numero de la seccion:")
            error_elecion = True  

        else:
            break
    eleccion = int(eleccion_input)
    if eleccion == 1:
        limpiar_consola()
        opcion = 0
        while opcion != 6:
            print("""   
    Seccion Curso

Eliga una de las siguientes opciones:

    1-Consultar datos generales          
    2-Consultar datos individuales       
    3-Actualizar un registro        
    4-Crear un registro         
    5-Eliminar un registro           
    6-Volver al menu principal            
                    """)
            error_opcion = False

            opcion_input =input("Numero de la opcion:")

            while True:
                if not opcion_input:
                    opcion_input =input("(Error, no puede estar vacio)Numero de la opcion:")
                    error_opcion = True

                elif not opcion_input.isdigit():
                    opcion_input =input("(Error, solo se permiten numeros)Numero de la opcion:")    
                    error_opcion = True

                elif int(opcion_input) not in range(1, 7):
                    opcion_input =input("(Error, numero no valido)Numero de la opcion:")
                    error_opcion = True
                else:
                    break
            

            opcion = int(opcion_input)            
                     
            if opcion ==1:
                Cursos.getCurso()
                menu_volver = input("Ingrese una (s) para volver a la seccion Curso o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Curso o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break
                
            if opcion == 2:
                id_curso_error = False
                id_curso_buscar= input("Ingrese la id del curso:")
                while True:
                    if not id_curso_buscar:
                        id_curso_buscar= input("(Error, no puede estar vacio)Ingrese la id del curso:")
                        id_curso_error = True

                    elif not id_curso_buscar.isdigit():
                        id_curso_buscar= input("(Error, solo se permite numeros)Ingrese la id del curso:")
                        id_curso_error = True
                    
                    else:
                        break
                Cursos.verificar_id_curso(id_curso_buscar)
                menu_volver = input("Ingrese una (s) para volver a la seccion Curso o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Curso o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break
            
            if opcion ==3:
                limpiar_consola()
                opciones = 0
                while opciones != 6:
                    print("""
    Actualizar  registro en la seccion Curso

Eliga lo que quiere actualizar:
    
    1-Actualizar nombre
    2-Actualizar descripcion
    3-Actualizar tiempo
    4-Actualizar usuario 
    5-Actualizar todo                         
    6-Salir                                     
                          """)
                    error_opciones = False 
                    opciones_input =input("Ingrese el numero de la opcion:")

                    while True:

                        if not opciones_input:
                            opciones_input =input("(Error, no puede estar vacio)Ingrese el numero de la opcion:")
                            error_opciones = True

                        elif not opciones_input.isdigit():
                            opciones_input =input("(Error, solo se permiten numeros)Ingrese el numero de la opcion:")   
                            error_opciones = True

                        elif int(opciones_input) not in range (1, 7):
                            opciones_input =input("(Error, numero no valido)Ingrese el numero de la opcion:")
                            error_opciones = True

                        else:
                            break

                    opciones = int(opciones_input)   
            
            
                    
                    if opciones == 1:
                        id_curso_error = False
                        id_curso_buscar= input("Ingrese la id del curso:")
                        while True:
                            if not id_curso_buscar:
                                id_curso_buscar= input("(Error, no puede estar vacio)Ingrese la id del curso:")
                                id_curso_error = True

                            elif not id_curso_buscar.isdigit():
                                id_curso_buscar= input("(Error, solo se permite numeros)Ingrese la id del curso:")
                                id_curso_error = True
                    
                            else:
                                break
                        nombre_error_curso = False
                        nombre_curso = input("Ingrese el nombre nuevo del curso:")
                        while True:
                            if not nombre_curso:
                                nombre_curso = input("(Error, no puede estar vacio)Ingrese el nombre nuevo del curso:")
                                nombre_error_curso = True

                            elif not all(letra.isalpha() or letra.isspace() for letra in nombre_curso):
                                nombre_curso = input("(Error, solo se permiten letras)Ingrese el nombre nuevo del curso:")
                                nombre_error_curso = True
                            else:
                                break
                        Cursos.updateCurso_nombre(id_curso_buscar, nombre_curso)
                        Cursos.verificar_cambios_curso(id_curso_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Curso:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Curso:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                    
                    if opciones ==2:
                        id_curso_error = False
                        id_curso_buscar= input("Ingrese la id del curso:")
                        while True:
                            if not id_curso_buscar:
                                id_curso_buscar= input("(Error, no puede estar vacio)Ingrese la id del curso:")
                                id_curso_error = True

                            elif not id_curso_buscar.isdigit():
                                id_curso_buscar= input("(Error, solo se permite numeros)Ingrese la id del curso:")
                                id_curso_error = True
                    
                            else:
                                break
                        descripcion_curso = input("Ingrese la descripcion nueva:")
                        while not descripcion_curso:
                            descripcion_curso= input("(Error, no puede estar vacio)Ingrese la descripcion nueva:")
                        Cursos.updateCurso_descripcion(id_curso_buscar, descripcion_curso)
                        Cursos.verificar_cambios_curso(id_curso_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Curso:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Curso:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break




                    if opciones ==3:
                        id_curso_error = False
                        id_curso_buscar= input("Ingrese la id del curso:")
                        while True:
                            if not id_curso_buscar:
                                id_curso_buscar= input("(Error, no puede estar vacio)Ingrese la id del curso:")
                                id_curso_error = True

                            elif not id_curso_buscar.isdigit():
                                id_curso_buscar= input("(Error, solo se permite numeros)Ingrese la id del curso:")
                                id_curso_error = True
                    
                            else:
                                break
                        tiempo_curso = input("Ingrese el tiempo nuevo del curso:")
                        while not tiempo_curso:
                            tiempo_curso= input("(Error, no puede estar vacio)Ingrese el tiempo nuevo del curso:")
                        Cursos.updateCurso_tiempo(id_curso_buscar, tiempo_curso)
                        Cursos.verificar_cambios_curso(id_curso_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Curso:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Curso:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones ==4:
                        id_curso_error = False
                        id_curso_buscar= input("Ingrese la id del curso:")
                        while True:
                            if not id_curso_buscar:
                                id_curso_buscar= input("(Error, no puede estar vacio)Ingrese la id del curso:")
                                id_curso_error = True

                            elif not id_curso_buscar.isdigit():
                                id_curso_buscar= input("(Error, solo se permite numeros)Ingrese la id del curso:")
                                id_curso_error = True
                    
                            else:
                                break
                        usuario_error_curso = False
                        usuario_curso = input("Ingrese el nuevo usuario:")
                        while True:
                            if not usuario_curso:
                                usuario_curso= input("(Error, no puede estar vacio)Ingrese el nuevo uusario:")
                                usuario_error_curso = True

                            elif Cursos.usuaraio_existente_curso(usuario_curso):
                                usuario_curso= input("(Error, el usuario ya existe)Ingrese el nuevo usuario:")
                                usuario_error_curso = True
                            else:
                                break
                        Cursos.updateCurso_usuario(id_curso_buscar, usuario_curso)
                        Cursos.verificar_cambios_curso(id_curso_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Curso:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Curso:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones ==5:
                        id_curso_error = False
                        id_curso_buscar= input("Ingrese la id del curso:")
                        while True:
                            if not id_curso_buscar:
                                id_curso_buscar= input("(Error, no puede estar vacio)Ingrese la id del curso:")
                                id_curso_error = True

                            elif not id_curso_buscar.isdigit():
                                id_curso_buscar= input("(Error, solo se permite numeros)Ingrese la id del curso:")
                                id_curso_error = True
                    
                            else:
                                break
                        nombre_error_curso = False
                        nombre_curso = input("Ingrese el nombre nuevo del curso:")
                        while True:
                            if not nombre_curso:
                                nombre_curso = input("(Error, no puede estar vacio)Ingrese el nombre nuevo del curso:")
                                nombre_error_curso = True

                            elif not all(letra.isalpha() or letra.isspace() for letra in nombre_curso):
                                nombre_curso = input("(Error, solo se permiten letras)Ingrese el nombre nuevo del curso:")
                                nombre_error_curso = True
                            else:
                                break
                        descripcion_curso = input("Ingrese la descripcion nueva:")
                        while not descripcion_curso:
                            descripcion_curso= input("(Error, no puede estar vacio)Ingrese la descripcion nueva:")
                        tiempo_curso = input("Ingrese el tiempo nuevo del curso:")
                        while not tiempo_curso:
                            tiempo_curso= input("(Error, no puede estar vacio)Ingrese el tiempo nuevo del curso:")
                        usuario_error_curso = False
                        usuario_curso = input("Ingrese el nuevo usuario:")
                        while True:
                            if not usuario_curso:
                                usuario_curso= input("(Error, no puede estar vacio)Ingrese el nuevo uusario:")
                                usuario_error_curso = True

                            elif Cursos.usuaraio_existente_curso(usuario_curso):
                                usuario_curso= input("(Error, el usuario ya existe)Ingrese el nuevo usuario:")
                                usuario_error_curso = True
                            else:
                                break
                        Cursos.updateCurso_total(id_curso_buscar, nombre_curso, descripcion_curso, tiempo_curso, usuario_curso)
                        Cursos.verificar_cambios_curso(id_curso_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Curso:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Curso:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                    
                    if opciones ==6:
                        limpiar_consola()
                        break
            
            if opcion == 4:
                nombre_error_curso = False
                nombre_curso = input("Ingrese el nombre del curso:")
                while True:
                    if not nombre_curso:
                        nombre_curso = input("(Error, no puede estar vacio)Ingrese el nombre del curso:")
                        nombre_error_curso = True

                    elif not all(letra.isalpha() or letra.isspace() for letra in nombre_curso):
                        nombre_curso = input("(Error, solo se permiten letras)Ingrese el nombre del curso:")
                        nombre_error_curso = True
                    else:
                        break
                descripcion_curso = input("Ingrese la descripcion:")
                while not descripcion_curso:
                    descripcion_curso = input("(Error, no puede estar vacio)Ingrese la descripcion:")
                tiempo_curso = input("Ingrese el tiempo del curso:")
                while not tiempo_curso:
                    tiempo_curso = input("(Error, no puede estar vacio)Ingrese el tiempo del curso:")
                usuario_error_curso = False
                usuario_curso = input("Ingrese el usuario:")
                while True:
                    if not usuario_curso:
                        usuario_curso= input("(Error, no puede estar vacio)Ingrese el uusario:")
                        usuario_error_curso = True

                    elif Cursos.usuaraio_existente_curso(usuario_curso):
                        usuario_curso= input("(Error, el usuario ya existe)Ingrese el usuario:")
                        usuario_error_curso = True
                    else:
                        break
                Cursos.crearCurso(nombre_curso, descripcion_curso, tiempo_curso, usuario_curso)
                print("Se creo un nuevo registro")
                menu_volver = input("Ingrese una (s) para volver a la seccion curso o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion curso o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break
            
            if opcion ==5:
                id_curso_error = False
                id_borrar_curso = input("Ingrese la id a borrar:")
                while True:
                    if not id_borrar_curso:
                        id_borrar_curso= input("(Error, no puede estar vacio)Ingrese la id a borrar:")
                        id_curso_error = True

                    elif not id_borrar_curso.isdigit():
                        id_borrar_curso= input("(Error, solo se permite numeros)Ingrese la id a borrar:")
                        id_curso_error = True
                    
                    else:
                        break
                Cursos.verificar_curso_borrado(id_borrar_curso)
                Cursos.borrarCurso(id_borrar_curso)
                menu_volver = input("Ingrese una (s) para volver a la seccion curso o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion curso o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break
            
            if opcion ==6:
                limpiar_consola()
                break  
    


    if eleccion == 2:
        limpiar_consola()
        opcion = 0
        while opcion != 6:
            print("""   
    Seccion Estudiante

Eliga una de las siguientes opciones:

    1-Consultar datos generales          
    2-Consultar datos individuales       
    3-Actualizar un registro        
    4-Crear un registro         
    5-Eliminar un registro           
    6-Volver al menu principal            
                    """)
            
            error_opcion = False

            opcion_input =input("Numero de la opcion:")

            while True:
                if not opcion_input:
                    opcion_input =input("(Error, no puede estar vacio)Numero de la opcion:")
                    error_opcion = True

                elif not opcion_input.isdigit():
                    opcion_input =input("(Error, solo se permiten numeros)Numero de la opcion:")    
                    error_opcion = True

                elif int(opcion_input) not in range(1, 7):
                    opcion_input =input("(Error, numero no valido)Numero de la opcion:")
                    error_opcion = True
                else:
                    break
            

            opcion = int(opcion_input)     
    

            if opcion == 1:
                Estudiantes.getEstudiante()
                menu_volver = input("Ingrese una (s) para volver a la seccion Estudiante o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Estudiante o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break

            if opcion == 2:
                id_error_estudiante = False
                id_estudiante_buscar = input("Ingrese la id del estudiante:")
                while True:
                    if not id_estudiante_buscar:
                        id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                        id_error_estudiante = True
                    elif not id_estudiante_buscar.isdigit():
                        id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                        id_error_estudiante = True
                    else:
                        break    
                Estudiantes.verificar_id_estudiante(id_estudiante_buscar)
                menu_volver = input("Ingrese una (s) para volver a la seccion Estudiante o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Estudiante o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break

            
            if opcion == 3:
                limpiar_consola()
                opciones = 0
                while opciones != 15:
                    print("""
    Actualizar  registro en la seccion Estudiante

Eliga lo que quiere actualizar:
    
    1-Actualizar cedula
    2-Actualizar correo electronico
    3-Actualizar telefono
    4-Actualizar telefono celular
    5-Actualizar fecha de nacimiento
    6-Actualizar sexo
    7-Actualizar direccion
    8-Actualizar nombre
    9-Actualizar apellido paterno
    10-Actualizar apellido materno
    11-Actualizar nacionalidad
    12-Actualizar id carreras 
    13-Actualizar usuario
    14-Actualizar todo                         
    15-Salir                                     
                          """)
                   
                    error_opciones = False 
                    opciones_input =input("Ingrese el numero de la opcion:")

                    while True:

                        if not opciones_input:
                            opciones_input =input("(Error, no puede estar vacio)Ingrese el numero de la opcion:")
                            error_opciones = True

                        elif not opciones_input.isdigit():
                            opciones_input =input("(Error, solo se permiten numeros)Ingrese el numero de la opcion:")   
                            error_opciones = True

                        elif int(opciones_input) not in range (1, 16):
                            opciones_input =input("(Error, numero no valido)Ingrese el numero de la opcion:")
                            error_opciones = True

                        else:
                            break

                    opciones = int(opciones_input)        
           

                    if opciones == 1:
                        id_error_estudiante = False
                        id_estudiante_buscar = input("Ingrese la id del estudiante:")
                        while True:
                            if not id_estudiante_buscar:
                                id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            elif not id_estudiante_buscar.isdigit():
                                id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            else:
                                break  
                        cedula_error_estudiante = False  
                        estudiante_cedula = input("Ingrese la cedula nueva:")
                        while True:
                            if not estudiante_cedula:
                                estudiante_cedula= input("(Error, no puede estar vacio)Ingrese la cedula nueva:")
                                cedula_error_estudiante = True
                            elif not estudiante_cedula.isdigit():
                                estudiante_cedula= input("(Error, solo se permite numeros)Ingrese la cedula nueva:")
                                cedula_error_estudiante = True
                            elif Estudiantes.cedula_existente_estudiante(estudiante_cedula):
                                estudiante_cedula= input("(Error, la cedula ya esta registrada)Ingrese la cedula nueva:")     
                                cedula_error_estudiante = True
                            else:
                                break                
                        Estudiantes.updateEstudiante_cedula(id_estudiante_buscar, estudiante_cedula)
                        Estudiantes.verificar_cambios_estudiante(id_estudiante_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones == 2:
                        id_error_estudiante = False
                        id_estudiante_buscar = input("Ingrese la id del estudiante:")
                        while True:
                            if not id_estudiante_buscar:
                                id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            elif not id_estudiante_buscar.isdigit():
                                id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            else:
                                break  
                        correo_error_estudiante = False
                        correo_electronico_estudiante = input("Ingrese el correo electronico nuevo:")
                        while True:
                            if not correo_electronico_estudiante:
                                correo_electronico_estudiante= input("(Error, no puede estar vacio)Ingrese el correo electronico nuevo:")
                                correo_error_estudiante = True
                            elif "@" not in correo_electronico_estudiante or ".com" not in correo_electronico_estudiante:
                                correo_electronico_estudiante= input("(Error, tiene que llevar @ y .com)Ingrese el correo electronico nuevo:")
                                correo_error_estudiante = True
                            elif Estudiantes.correo_electronico_existente_estudiante(correo_electronico_estudiante):
                                correo_electronico_estudiante= input("(Error, el correo ya esta registrado)Ingrese el correo electronico nuevo:")
                                correo_error_estudiante = True
                            else:
                                break
                        Estudiantes.updateEstudiante_correo(id_estudiante_buscar, correo_electronico_estudiante)
                        Estudiantes.verificar_cambios_estudiante(id_estudiante_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones == 3:
                        id_error_estudiante = False
                        id_estudiante_buscar = input("Ingrese la id del estudiante:")
                        while True:
                            if not id_estudiante_buscar:
                                id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            elif not id_estudiante_buscar.isdigit():
                                id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            else:
                                break  
                        telefono_error_estudiante = False
                        telefono_estudiante = input("Ingrese el telefono nuevo:")
                        while True:
                            if not telefono_estudiante:
                                telefono_estudiante= input("(Error, no puede estar vacio)Ingrese el telefono nuevo:")
                                telefono_error_estudiante =True
                            elif len(telefono_estudiante) != 8 or not telefono_estudiante.isdigit():
                                telefono_estudiante = input("(Error, debe de tener 8 numeros)Ingrese el telefono nuevo:")
                                telefono_error_estudiante =True
                            else:
                                break   
                        Estudiantes.updateEstudiante_telefono(id_estudiante_buscar, telefono_estudiante)
                        Estudiantes.verificar_cambios_estudiante(id_estudiante_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones == 4:
                        id_error_estudiante = False
                        id_estudiante_buscar = input("Ingrese la id del estudiante:")
                        while True:
                            if not id_estudiante_buscar:
                                id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            elif not id_estudiante_buscar.isdigit():
                                id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            else:
                                break  
                        celular_error_estudiante = False
                        celular_estudiante = input("Ingrese el nuevo numero de telefono celular:")
                        while True:
                            if not celular_estudiante:
                                celular_estudiante= input("(Error, no puede estar vacio)Ingrese el nuevo numero de telefono celular:")
                                celular_error_estudiante =True
                            elif len(celular_estudiante) != 8 or not celular_estudiante.isdigit():
                                celular_estudiante = input("(Error, debe de tener 8 numeros)Ingrese el nuevo numero de telefono celular:")
                                celular_error_estudiante =True
                            elif Estudiantes.telefono_celular_existente_estudiante(celular_estudiante):
                                celular_estudiante = input("(Error, el numero ya esta registrado)Ingrese el nuevo numero de telefono celular:")
                                celular_error_estudiante =True
                            else:
                                break
                        Estudiantes.updateEstudiante_telefono_celular(id_estudiante_buscar, celular_estudiante)
                        Estudiantes.verificar_cambios_estudiante(id_estudiante_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones == 5:
                        id_error_estudiante = False
                        id_estudiante_buscar = input("Ingrese la id del estudiante:")
                        while True:
                            if not id_estudiante_buscar:
                                id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            elif not id_estudiante_buscar.isdigit():
                                id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            else:
                                break  
                        error_fecha_estudiante = False
                        fecha_nacimiento_estudiante = input("Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                        while True:
                            if not fecha_nacimiento_estudiante:
                                fecha_nacimiento_estudiante= input("(Error, no puede estar vacio)Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                                error_fecha_estudiante = True
                            elif not validar_fecha(fecha_nacimiento_estudiante):
                                fecha_nacimiento_estudiante= input("(Error, formato no valido)Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                                error_fecha_estudiante = True
                            else:
                                break
                        Estudiantes.updateEstudiante_fecha_nacimiento(id_estudiante_buscar, fecha_nacimiento_estudiante)
                        Estudiantes.verificar_cambios_estudiante(id_estudiante_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones == 6:
                        id_error_estudiante = False
                        id_estudiante_buscar = input("Ingrese la id del estudiante:")
                        while True:
                            if not id_estudiante_buscar:
                                id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            elif not id_estudiante_buscar.isdigit():
                                id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            else:
                                break  
                        sexo_error_estudiante = False
                        sexo_estudiante = input("Ingrese el nuevo sexo:")
                        while True: 
                            if not sexo_estudiante:
                                sexo_estudiante= input("(Error, no puede estar vacio)Ingrese el nuevo sexo:")
                                sexo_error_estudiante = True
                            elif not sexo_estudiante.isalpha():
                                sexo_estudiante= input("(Error, solo se permite letras)Ingrese el nuevo sexo:")
                                sexo_error_estudiante = True
                            else:
                                break   
                        Estudiantes.updateEstudiante_sexo(id_estudiante_buscar, sexo_estudiante)
                        Estudiantes.verificar_cambios_estudiante(id_estudiante_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                            

                    if opciones == 7:
                        id_error_estudiante = False
                        id_estudiante_buscar = input("Ingrese la id del estudiante:")
                        while True:
                            if not id_estudiante_buscar:
                                id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            elif not id_estudiante_buscar.isdigit():
                                id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            else:
                                break  
                        direccion_estudiante = input("Ingrese la nueva direccion:")
                        while not direccion_estudiante:
                            direccion_estudiante= input("(Error, no puede estar vacio)Ingrese la nueva direccion:")
                        Estudiantes.updateEstudiante_direccion(id_estudiante_buscar, direccion_estudiante)
                        Estudiantes.verificar_cambios_estudiante(id_estudiante_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break



                    if opciones == 8:
                        id_error_estudiante = False
                        id_estudiante_buscar = input("Ingrese la id del estudiante:")
                        while True:
                            if not id_estudiante_buscar:
                                id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            elif not id_estudiante_buscar.isdigit():
                                id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            else:
                                break  
                        nombre_error_estudiante = False
                        nombre_estudiante = input("Ingresar el nuevo nombre:")
                        while True:
                            if not nombre_estudiante:
                                nombre_estudiante= input("(Error, no puede estar vacio)Ingresar el nuevo nombre:")
                                nombre_error_curso = True
                            elif not all(letra.isalpha() or letra.isspace() for letra in nombre_estudiante):
                                nombre_estudiante= input("(Error, solo se permiten letras)Ingresar el nuevo nombre:")
                                nombre_error_curso = True
                            else:
                                break
                        Estudiantes.updateEstudiante_nombre(id_estudiante_buscar, nombre_estudiante)
                        Estudiantes.verificar_cambios_estudiante(id_estudiante_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                    
                    if opciones == 9:
                        id_error_estudiante = False
                        id_estudiante_buscar = input("Ingrese la id del estudiante:")
                        while True:
                            if not id_estudiante_buscar:
                                id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            elif not id_estudiante_buscar.isdigit():
                                id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            else:
                                break  
                        apellido_p_estudiante = False
                        apellido_paterno_estudiante = input("Ingrese el nuvo apellido paterno:")
                        while True:
                            if not apellido_paterno_estudiante:
                                apellido_paterno_estudiante= input("(Error, no puede estar vacio)Ingrese el nuvo apellido paterno:")
                                apellido_p_estudiante = True
                            elif not apellido_paterno_estudiante.isalpha():
                                apellido_paterno_estudiante= input("(Error, solo se permite letras)Ingrese el nuvo apellido paterno:")
                                apellido_p_estudiante = True
                            else:
                                break
                        Estudiantes.updateEstudiante_apellido_paterno(id_estudiante_buscar, apellido_paterno_estudiante)
                        Estudiantes.verificar_cambios_estudiante(id_estudiante_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                    
                    if opciones == 10 :
                        id_error_estudiante = False
                        id_estudiante_buscar = input("Ingrese la id del estudiante:")
                        while True:
                            if not id_estudiante_buscar:
                                id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            elif not id_estudiante_buscar.isdigit():
                                id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            else:
                                break  
                        apellido_m_estudiante = False
                        apellido_materno_estudiante = input("Ingrese el nuevo apellido materno:")
                        while True:
                            if not apellido_materno_estudiante:
                                apellido_materno_estudiante= input("(Error, no puede estar vacio)Ingrese el nuevo apellido materno:")
                                apellido_m_estudiante = True
                            elif not apellido_materno_estudiante.isalpha():
                                apellido_materno_estudiante= input("(Error, solo se permite letras)Ingrese el nuevo apellido materno:")
                                apellido_m_estudiante = True
                            else:
                                break
                        Estudiantes.updateEstudiante_apellido_materno(id_estudiante_buscar, apellido_materno_estudiante)
                        Estudiantes.verificar_cambios_estudiante(id_estudiante_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                            



                    if opciones == 11:
                        id_error_estudiante = False
                        id_estudiante_buscar = input("Ingrese la id del estudiante:")
                        while True:
                            if not id_estudiante_buscar:
                                id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            elif not id_estudiante_buscar.isdigit():
                                id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            else:
                                break  
                        nacionalidad_error_estudiante = False
                        nacionalidad_estudiante = input("Ingrese la nueva nacionalidad:")
                        while True:
                            if not nacionalidad_estudiante:
                                nacionalidad_estudiante= input("(Error, no puede estar vacio)Ingrese la nueva nacionalidad:")
                                nacionalidad_error_estudiante = True
                            elif not nacionalidad_estudiante.isalpha():
                                nacionalidad_estudiante= input("(Error, solo se permite letras)Ingrese la nueva nacionalidad:")
                                nacionalidad_error_estudiante = True
                            else:
                                break
                        Estudiantes.updateEstudiante_nacionalidad(id_estudiante_buscar, nacionalidad_estudiante)
                        Estudiantes.verificar_cambios_estudiante(id_estudiante_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break


                    if opciones == 12:
                        id_error_estudiante = False
                        id_estudiante_buscar = input("Ingrese la id del estudiante:")
                        while True:
                            if not id_estudiante_buscar:
                                id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            elif not id_estudiante_buscar.isdigit():
                                id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            else:
                                break  
                        id_c_estudiante = False
                        idcarreras_estudiante = input ("Ingrese el nuevo id de carreras:")
                        while True:
                            if not idcarreras_estudiante:
                                idcarreras_estudiante= input("(Error, no puede estar vacio)Ingrese el nuevo id de carreras:")
                                id_c_estudiante = True
                            elif not idcarreras_estudiante.isdigit():
                                idcarreras_estudiante= input("(Error, solo se permite numeros)Ingrese el nuevo id de carreras:")
                                id_c_estudiante = True
                            else:
                                break
                        Estudiantes.updateEstudiante_id_carreras(id_estudiante_buscar, idcarreras_estudiante)
                        Estudiantes.verificar_cambios_estudiante(id_estudiante_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                    
                    if opciones == 13:
                        id_error_estudiante = False
                        id_estudiante_buscar = input("Ingrese la id del estudiante:")
                        while True:
                            if not id_estudiante_buscar:
                                id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            elif not id_estudiante_buscar.isdigit():
                                id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            else:
                                break  
                        usuario_error_estudiante = False
                        usuario_estudiante = input("Ingrese el nuevo usuario:")
                        while True:
                            if not usuario_estudiante:
                                usuario_estudiante= input("(Error, no puede estar vacio)Ingrese el nuevo usuario:")
                                usuario_error_estudiante = True
                            elif Estudiantes.usuaraio_existente_estudiante(usuario_estudiante):
                                usuario_estudiante= input("(Error, el usuario ya existe)Ingrese el nuevo usuario:")
                                usuario_error_estudiante = True
                            else:
                                break
                        Estudiantes.updateEstudiante_usuario(id_estudiante_buscar, usuario_estudiante)
                        Estudiantes.verificar_cambios_estudiante(id_estudiante_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones == 14:
                        id_error_estudiante = False
                        id_estudiante_buscar = input("Ingrese la id del estudiante:")
                        while True:
                            if not id_estudiante_buscar:
                                id_estudiante_buscar= input("(Error, no puede estar vacio)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            elif not id_estudiante_buscar.isdigit():
                                id_estudiante_buscar= input("(Error, solo se permite numeros)Ingrese la id del estudiante:")
                                id_error_estudiante = True
                            else:
                                break  
                        cedula_error_estudiante = False  
                        estudiante_cedula = input("Ingrese la cedula nueva:")
                        while True:
                            if not estudiante_cedula:
                                estudiante_cedula= input("(Error, no puede estar vacio)Ingrese la cedula nueva:")
                                cedula_error_estudiante = True
                            elif not estudiante_cedula.isdigit():
                                estudiante_cedula= input("(Error, solo se permite numeros)Ingrese la cedula nueva:")
                                cedula_error_estudiante = True
                            elif Estudiantes.cedula_existente_estudiante(estudiante_cedula):
                                estudiante_cedula= input("(Error, la cedula ya esta registrada)Ingrese la cedula nueva:")     
                                cedula_error_estudiante = True
                            else:
                                break       
                        correo_error_estudiante = False
                        correo_electronico_estudiante = input("Ingrese el correo electronico nuevo:")
                        while True:
                            if not correo_electronico_estudiante:
                                correo_electronico_estudiante= input("(Error, no puede estar vacio)Ingrese el correo electronico nuevo:")
                                correo_error_estudiante = True
                            elif "@" not in correo_electronico_estudiante or ".com" not in correo_electronico_estudiante:
                                correo_electronico_estudiante= input("(Error, tiene que llevar @ y .com)Ingrese el correo electronico nuevo:")
                                correo_error_estudiante = True
                            elif Estudiantes.correo_electronico_existente_estudiante(correo_electronico_estudiante):
                                correo_electronico_estudiante= input("(Error, el correo ya esta registrado)Ingrese el correo electronico nuevo:")
                                correo_error_estudiante = True
                            else:
                                break
                        telefono_error_estudiante = False
                        telefono_estudiante = input("Ingrese el telefono nuevo:")
                        while True:
                            if not telefono_estudiante:
                                telefono_estudiante= input("(Error, no puede estar vacio)Ingrese el telefono nuevo:")
                                telefono_error_estudiante =True
                            elif len(telefono_estudiante) != 8 or not telefono_estudiante.isdigit():
                                telefono_estudiante = input("(Error, debe de tener 8 numeros)Ingrese el telefono nuevo:")
                                telefono_error_estudiante =True
                            else:
                                break   
                        celular_error_estudiante = False
                        celular_estudiante = input("Ingrese el nuevo numero de telefono celular:")
                        while True:
                            if not celular_estudiante:
                                celular_estudiante= input("(Error, no puede estar vacio)Ingrese el nuevo numero de telefono celular:")
                                celular_error_estudiante =True
                            elif len(celular_estudiante) != 8 or not celular_estudiante.isdigit():
                                celular_estudiante = input("(Error, debe de tener 8 numeros)Ingrese el nuevo numero de telefono celular:")
                                celular_error_estudiante =True
                            elif Estudiantes.telefono_celular_existente_estudiante(celular_estudiante):
                                celular_estudiante = input("(Error, el numero ya esta registrado)Ingrese el nuevo numero de telefono celular:")
                                celular_error_estudiante =True
                            else:
                                break
                        error_fecha_estudiante = False
                        fecha_nacimiento_estudiante = input("Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                        while True:
                            if not fecha_nacimiento_estudiante:
                                fecha_nacimiento_estudiante= input("(Error, no puede estar vacio)Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                                error_fecha_estudiante = True
                            elif not validar_fecha(fecha_nacimiento_estudiante):
                                fecha_nacimiento_estudiante= input("(Error, formato no valido)Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                                error_fecha_estudiante = True
                            else:
                                break
                        sexo_error_estudiante = False
                        sexo_estudiante = input("Ingrese el nuevo sexo:")
                        while True: 
                            if not sexo_estudiante:
                                sexo_estudiante= input("(Error, no puede estar vacio)Ingrese el nuevo sexo:")
                                sexo_error_estudiante = True
                            elif not sexo_estudiante.isalpha():
                                sexo_estudiante= input("(Error, solo se permite letras)Ingrese el nuevo sexo:")
                                sexo_error_estudiante = True
                            else:
                                break   
                        direccion_estudiante = input("Ingrese la nueva direccion:")
                        while not direccion_estudiante:
                            direccion_estudiante= input("(Error, no puede estar vacio)Ingrese la nueva direccion:")
                        nombre_error_estudiante = False
                        nombre_estudiante = input("Ingresar el nuevo nombre:")
                        while True:
                            if not nombre_estudiante:
                                nombre_estudiante= input("(Error, no puede estar vacio)Ingresar el nuevo nombre:")
                                nombre_error_curso = True
                            elif not all(letra.isalpha() or letra.isspace() for letra in nombre_estudiante):
                                nombre_estudiante= input("(Error, solo se permiten letras)Ingresar el nuevo nombre:")
                                nombre_error_curso = True
                            else:
                                break
                        apellido_p_estudiante = False
                        apellido_paterno_estudiante = input("Ingrese el nuvo apellido paterno:")
                        while True:
                            if not apellido_paterno_estudiante:
                                apellido_paterno_estudiante= input("(Error, no puede estar vacio)Ingrese el nuvo apellido paterno:")
                                apellido_p_estudiante = True
                            elif not apellido_paterno_estudiante.isalpha():
                                apellido_paterno_estudiante= input("(Error, solo se permite letras)Ingrese el nuvo apellido paterno:")
                                apellido_p_estudiante = True
                            else:
                                break
                        apellido_m_estudiante = False
                        apellido_materno_estudiante = input("Ingrese el nuevo apellido materno:")
                        while True:
                            if not apellido_materno_estudiante:
                                apellido_materno_estudiante= input("(Error, no puede estar vacio)Ingrese el nuevo apellido materno:")
                                apellido_m_estudiante = True
                            elif not apellido_materno_estudiante.isalpha():
                                apellido_materno_estudiante= input("(Error, solo se permite letras)Ingrese el nuevo apellido materno:")
                                apellido_m_estudiante = True
                            else:
                                break
                        nacionalidad_error_estudiante = False
                        nacionalidad_estudiante = input("Ingrese la nueva nacionalidad:")
                        while True:
                            if not nacionalidad_estudiante:
                                nacionalidad_estudiante= input("(Error, no puede estar vacio)Ingrese la nueva nacionalidad:")
                                nacionalidad_error_estudiante = True
                            elif not nacionalidad_estudiante.isalpha():
                                nacionalidad_estudiante= input("(Error, solo se permite letras)Ingrese la nueva nacionalidad:")
                                nacionalidad_error_estudiante = True
                            else:
                                break
                        id_c_estudiante = False
                        idcarreras_estudiante = input ("Ingrese el nuevo id de carreras:")
                        while True:
                            if not idcarreras_estudiante:
                                idcarreras_estudiante= input("(Error, no puede estar vacio)Ingrese el nuevo id de carreras:")
                                id_c_estudiante = True
                            elif not idcarreras_estudiante.isdigit():
                                idcarreras_estudiante= input("(Error, solo se permite numeros)Ingrese el nuevo id de carreras:")
                                id_c_estudiante = True
                            else:
                                break
                        usuario_error_estudiante = False
                        usuario_estudiante = input("Ingrese el nuevo usuario:")
                        while True:
                            if not usuario_estudiante:
                                usuario_estudiante= input("(Error, no puede estar vacio)Ingrese el nuevo usuario:")
                                usuario_error_estudiante = True
                            elif Estudiantes.usuaraio_existente_estudiante(usuario_estudiante):
                                usuario_estudiante= input("(Error, el usuario ya existe)Ingrese el nuevo usuario:")
                                usuario_error_estudiante = True
                            else:
                                break
                        Estudiantes.updateEstudiante_total(id_estudiante_buscar, estudiante_cedula, correo_electronico_estudiante, telefono_estudiante, celular_estudiante, fecha_nacimiento_estudiante, sexo_estudiante, direccion_estudiante, nombre_estudiante, apellido_paterno_estudiante, apellido_materno_estudiante, nacionalidad_estudiante, idcarreras_estudiante, usuario_estudiante)
                        Estudiantes.verificar_cambios_estudiante(id_estudiante_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Estudiante:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break



                    if opciones == 15 :
                        limpiar_consola()
                        break
            

            if opcion == 4:
                cedula_error_estudiante = False  
                estudiante_cedula = input("Ingrese la cedula:")
                while True:
                    if not estudiante_cedula:
                        estudiante_cedula= input("(Error, no puede estar vacio)Ingrese la cedula:")
                        cedula_error_estudiante = True
                    elif not estudiante_cedula.isdigit():
                        estudiante_cedula= input("(Error, solo se permite numeros)Ingrese la cedula:")
                        cedula_error_estudiante = True
                    elif Estudiantes.cedula_existente_estudiante(estudiante_cedula):
                        estudiante_cedula= input("(Error, la cedula ya esta registrada)Ingrese la cedula:")     
                        cedula_error_estudiante = True
                    else:
                        break       
                correo_error_estudiante = False
                correo_electronico_estudiante = input("Ingrese el correo electronico nuevo:")
                while True:
                    if not correo_electronico_estudiante:
                        correo_electronico_estudiante= input("(Error, no puede estar vacio)Ingrese el correo electronico:")
                        correo_error_estudiante = True
                    elif "@" not in correo_electronico_estudiante or ".com" not in correo_electronico_estudiante:
                        correo_electronico_estudiante= input("(Error, tiene que llevar @ y .com)Ingrese el correo electronico:")
                        correo_error_estudiante = True
                    elif Estudiantes.correo_electronico_existente_estudiante(correo_electronico_estudiante):
                        correo_electronico_estudiante= input("(Error, el correo ya esta registrado)Ingrese el correo electronico:")
                        correo_error_estudiante = True
                    else:
                        break
                telefono_error_estudiante = False
                telefono_estudiante = input("Ingrese el telefono:")
                while True:
                    if not telefono_estudiante:
                        telefono_estudiante= input("(Error, no puede estar vacio)Ingrese el telefono:")
                        telefono_error_estudiante =True
                    elif len(telefono_estudiante) != 8 or not telefono_estudiante.isdigit():
                        telefono_estudiante = input("(Error, debe de tener 8 numeros)Ingrese el telefono:")
                        telefono_error_estudiante =True
                    else:
                        break   
                celular_error_estudiante = False
                celular_estudiante = input("Ingrese el numero de telefono celular:")
                while True:
                    if not celular_estudiante:
                        celular_estudiante= input("(Error, no puede estar vacio)Ingrese el numero de telefono celular:")
                        celular_error_estudiante =True
                    elif len(celular_estudiante) != 8 or not celular_estudiante.isdigit():
                        celular_estudiante = input("(Error, debe de tener 8 numeros)Ingrese el numero de telefono celular:")
                        celular_error_estudiante =True
                    elif Estudiantes.telefono_celular_existente_estudiante(celular_estudiante):
                        celular_estudiante = input("(Error, el numero ya esta registrado)Ingrese el numero de telefono celular:")
                        celular_error_estudiante =True
                    else:
                        break
                error_fecha_estudiante = False
                fecha_nacimiento_estudiante = input("Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                while True:
                    if not fecha_nacimiento_estudiante:
                        fecha_nacimiento_estudiante= input("(Error, no puede estar vacio)Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                        error_fecha_estudiante = True
                    elif not validar_fecha(fecha_nacimiento_estudiante):
                        fecha_nacimiento_estudiante= input("(Error, formato no valido)Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                        error_fecha_estudiante = True
                    else:
                        break
                sexo_error_estudiante = False
                sexo_estudiante = input("Ingrese el sexo:")
                while True: 
                    if not sexo_estudiante:
                        sexo_estudiante= input("(Error, no puede estar vacio)Ingrese el sexo:")
                        sexo_error_estudiante = True
                    elif not sexo_estudiante.isalpha():
                        sexo_estudiante= input("(Error, solo se permite letras)Ingrese el sexo:")
                        sexo_error_estudiante = True
                    else:
                        break   
                direccion_estudiante = input("Ingrese la direccion:")
                while not direccion_estudiante:
                    direccion_estudiante= input("(Error, no puede estar vacio)Ingrese la direccion:")
                nombre_error_estudiante = False
                nombre_estudiante = input("Ingresar el nombre:")
                while True:
                    if not nombre_estudiante:
                        nombre_estudiante= input("(Error, no puede estar vacio)Ingresar el nombre:")
                        nombre_error_curso = True
                    elif not all(letra.isalpha() or letra.isspace() for letra in nombre_estudiante):
                        nombre_estudiante= input("(Error, solo se permiten letras)Ingresar el nombre:")
                        nombre_error_curso = True
                    else:
                        break
                apellido_p_estudiante = False
                apellido_paterno_estudiante = input("Ingrese el apellido paterno:")
                while True:
                    if not apellido_paterno_estudiante:
                        apellido_paterno_estudiante= input("(Error, no puede estar vacio)Ingrese el apellido paterno:")
                        apellido_p_estudiante = True
                    elif not apellido_paterno_estudiante.isalpha():
                        apellido_paterno_estudiante= input("(Error, solo se permite letras)Ingrese el apellido paterno:")
                        apellido_p_estudiante = True
                    else:
                        break
                apellido_m_estudiante = False
                apellido_materno_estudiante = input("Ingrese el apellido materno:")
                while True:
                    if not apellido_materno_estudiante:
                        apellido_materno_estudiante= input("(Error, no puede estar vacio)Ingrese el apellido materno:")
                        apellido_m_estudiante = True
                    elif not apellido_materno_estudiante.isalpha():
                        apellido_materno_estudiante= input("(Error, solo se permite letras)Ingrese el apellido materno:")
                        apellido_m_estudiante = True
                    else:
                        break
                nacionalidad_error_estudiante = False
                nacionalidad_estudiante = input("Ingrese la nacionalidad:")
                while True:
                    if not nacionalidad_estudiante:
                        nacionalidad_estudiante= input("(Error, no puede estar vacio)Ingrese la nacionalidad:")
                        nacionalidad_error_estudiante = True
                    elif not nacionalidad_estudiante.isalpha():
                        nacionalidad_estudiante= input("(Error, solo se permite letras)Ingrese la nacionalidad:")
                        nacionalidad_error_estudiante = True
                    else:
                        break
                id_c_estudiante = False
                idcarreras_estudiante = input ("Ingrese el id de carreras:")
                while True:
                    if not idcarreras_estudiante:
                        idcarreras_estudiante= input("(Error, no puede estar vacio)Ingrese el id de carreras:")
                        id_c_estudiante = True
                    elif not idcarreras_estudiante.isdigit():
                        idcarreras_estudiante= input("(Error, solo se permite numeros)Ingrese el id de carreras:")
                        id_c_estudiante = True
                    else:
                        break
                usuario_error_estudiante = False
                usuario_estudiante = input("Ingrese el usuario:")
                while True:
                    if not usuario_estudiante:
                        usuario_estudiante= input("(Error, no puede estar vacio)Ingrese el usuario:")
                        usuario_error_estudiante = True
                    elif Estudiantes.usuaraio_existente_estudiante(usuario_estudiante):
                        usuario_estudiante= input("(Error, el usuario ya existe)Ingrese el usuario:")
                        usuario_error_estudiante = True
                    else:
                        break
                Estudiantes.crearEstudiante(estudiante_cedula, correo_electronico_estudiante, telefono_estudiante, celular_estudiante, fecha_nacimiento_estudiante, sexo_estudiante, direccion_estudiante, nombre_estudiante, apellido_paterno_estudiante, apellido_materno_estudiante, nacionalidad_estudiante, idcarreras_estudiante, usuario_estudiante)
                print("Se creo un nuevo registro")
                menu_volver = input("Ingrese una (s) para volver a la seccion Estudiante o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Estudiante o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break

            if opcion == 5:
                id_borrar_esudiante_error = False
                id_estudiante_borrar = input("Ingrese la id que quiere borrar:")
                while True:
                    if not id_estudiante_borrar:
                        id_estudiante_borrar= input("(Error, no puede estar vacio)Ingrese la id que quiere borrar:")
                        id_borrar_esudiante_error = True                
                    elif not id_estudiante_borrar.isdigit():
                        id_estudiante_borrar= input("(Error, solo se permite numeros)Ingrese la id que quiere borrar:")
                        id_borrar_esudiante_error = True   
                    else:
                        break
                Estudiantes.verificar_borrar_estudiante(id_estudiante_borrar)
                Estudiantes.borrarEstudiante(id_estudiante_borrar)
                menu_volver = input("Ingrese una (s) para volver a la seccion Estudiante o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Estudiante o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break

            if opcion == 6:
                limpiar_consola()
                break




    if eleccion ==3:
        limpiar_consola()
        opcion = 0
        while opcion != 6:
            print("""   
    Seccion Profesor

Eliga una de las siguientes opciones:

    1-Consultar datos generales          
    2-Consultar datos individuales       
    3-Actualizar un registro        
    4-Crear un registro         
    5-Eliminar un registro           
    6-Volver al menu principal            
                    """)
          
            error_opcion = False

            opcion_input =input("Numero de la opcion:")

            while True:
                if not opcion_input:
                    opcion_input =input("(Error, no puede estar vacio)Numero de la opcion:")
                    error_opcion = True

                elif not opcion_input.isdigit():
                    opcion_input =input("(Error, solo se permiten numeros)Numero de la opcion:")    
                    error_opcion = True

                elif int(opcion_input) not in range(1, 7):
                    opcion_input =input("(Error, numero no valido)Numero de la opcion:")
                    error_opcion = True
                else:
                    break
            

            opcion = int(opcion_input)     

            if opcion == 1:
                Profesores.getProfesor()
                menu_volver = input("Ingrese una (s) para volver a la seccion Profesor o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Profesor o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break

            if opcion == 2:
                id_error_profesor = False
                id_buscar_profesor = input("Ingrese la id del profesor:")
                while  True:
                    if not id_buscar_profesor:
                        id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                        id_error_profesor = True
                    elif not id_buscar_profesor.isdigit():
                        id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                        id_error_profesor = True
                    else:
                        break
                Profesores.verificar_profesor_id(id_buscar_profesor)
                menu_volver = input("Ingrese una (s) para volver a la seccion Profesor o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Profesor o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break


            if opcion == 3:
                limpiar_consola()
                opciones = 0
                while opciones != 15:
                    print(""""
    Actualizar  registro en la seccion Profesor

Eliga lo que quiere actualizar:
    
    1-Actualizar cedula
    2-Actualizar correo electronico
    3-Actualizar telefono
    4-Actualizar telefono celular
    5-Actualizar fecha de nacimiento
    6-Actualizar sexo
    7-Actualizar direccion
    8-Actualizar nombre
    9-Actualizar apellido paterno
    10-Actualizar apellido materno
    11-Actualizar nacionalidad
    12-Actualizar usuario 
    13-Actualizar id carreras   
    14-Actualizar todo                      
    15-Salir                                     
                          """)
                    
                    error_opciones = False 
                    opciones_input =input("Ingrese el numero de la opcion:")

                    while True:

                        if not opciones_input:
                            opciones_input =input("(Error, no puede estar vacio)Ingrese el numero de la opcion:")
                            error_opciones = True

                        elif not opciones_input.isdigit():
                            opciones_input =input("(Error, solo se permiten numeros)Ingrese el numero de la opcion:")   
                            error_opciones = True

                        elif int(opciones_input) not in range (1, 16):
                            opciones_input =input("(Error, numero no valido)Ingrese el numero de la opcion:")
                            error_opciones = True

                        else:
                            break

                    opciones = int(opciones_input)       
            

                    if opciones == 1:
                        id_error_profesor = False
                        id_buscar_profesor = input("Ingrese la id del profesor:")
                        while  True:
                            if not id_buscar_profesor:
                                id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                                id_error_profesor = True
                            elif not id_buscar_profesor.isdigit():
                                id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                                id_error_profesor = True
                            else:
                                break
                        error_cedula_profesor = False
                        profesor_cedula = input("Ingrese la nueva cedula:")
                        while True:
                            if not profesor_cedula:
                                profesor_cedula= input("(Error, no puede estar vacio)Ingrese la nueva cedula:")
                                error_cedula_profesor = True
                            elif not profesor_cedula.isdigit():
                                profesor_cedula= input("(Error, solo se permite numeros)Ingrese la nueva cedula:") 
                                error_cedula_profesor = True
                            elif Profesores.cedula_existente_profesor(profesor_cedula):
                                profesor_cedula= input("(Error, la cedula ya esta registrada)Ingrese la nueva cedula:") 
                                error_cedula_profesor = True
                            else:
                                break
                        Profesores.updateProfesor_cedula(id_buscar_profesor, profesor_cedula)
                        Profesores.verificar_cambios_profesor(id_buscar_profesor)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones ==2:
                        id_error_profesor = False
                        id_buscar_profesor = input("Ingrese la id del profesor:")
                        while  True:
                            if not id_buscar_profesor:
                                id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                                id_error_profesor = True
                            elif not id_buscar_profesor.isdigit():
                                id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                                id_error_profesor = True
                            else:
                                break 
                        error_correo_profesor = False
                        correo_electronico_profesor = input("Ingrese el correo electronico nuevo:")
                        while True:
                            if not correo_electronico_profesor:
                                correo_electronico_profesor= input("(Error, no puede estar vacio)Ingrese el correo electronico nuevo:")
                                error_correo_profesor =True
                            elif "@" not in correo_electronico_profesor or ".com" not in correo_electronico_profesor:
                                correo_electronico_profesor= input("(Error, tiene que llevar @ y .com)Ingrese el correo electronico nuevo:")
                                error_correo_profesor =True
                            elif Profesores.correo_electronico_existente_profesor(correo_electronico_profesor):
                                correo_electronico_profesor= input("(Error, el correo ya esta registrado)Ingrese el correo electronico nuevo:")
                                error_correo_profesor =True
                            else:
                                break
                        Profesores.updateProfesor_correo_electronico(id_buscar_profesor, correo_electronico_profesor)
                        Profesores.verificar_cambios_profesor(id_buscar_profesor)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones == 3:
                        id_error_profesor = False
                        id_buscar_profesor = input("Ingrese la id del profesor:")
                        while  True:
                            if not id_buscar_profesor:
                                id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                                id_error_profesor = True
                            elif not id_buscar_profesor.isdigit():
                                id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                                id_error_profesor = True
                            else:
                                break
                        telefono_error_profesor = False
                        profesor_telefono = input("Ingrese el telefono nuevo:")
                        while True:
                            if not profesor_telefono:
                                profesor_telefono= input("(Error, no puede estar vacio)Ingrese el telefono nuevo:")
                                telefono_error_profesor = True
                            elif len(profesor_telefono) != 8 or not profesor_telefono.isdigit():
                                profesor_telefono = input("(Error, debe de tener 8 numeros)Ingrese el telefono nuevo:")
                                telefono_error_profesor = True
                            else:
                                break
                        Profesores.updateProfesor_telefono(id_buscar_profesor, profesor_telefono)
                        Profesores.verificar_cambios_profesor(id_buscar_profesor)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                    
                    if opciones == 4:
                        id_error_profesor = False
                        id_buscar_profesor = input("Ingrese la id del profesor:")
                        while  True:
                            if not id_buscar_profesor:
                                id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                                id_error_profesor = True
                            elif not id_buscar_profesor.isdigit():
                                id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                                id_error_profesor = True
                            else:
                                break 
                        celular_error_profesor = False
                        profesor_telefono_celular = input("Ingrese el nuevo numero de telefono celular:")
                        while True:
                            if not profesor_telefono_celular:
                                profesor_telefono_celular= input("(Error, no puede estar vacio)Ingrese el nuevo numero de telefono celular:")
                                celular_error_profesor = True
                            elif len(profesor_telefono_celular) != 8 or not profesor_telefono_celular.isdigit():
                                profesor_telefono_celular = input("(Error, debe de tener 8 numeros)Ingrese el nuevo numero de telefono celular:")
                                celular_error_profesor = True
                            elif Profesores.telefono_celular_existente_profesor(profesor_telefono_celular):
                                profesor_telefono_celular = input("(Error, el numero ya esta registrado)Ingrese el nuevo numero de telefono celular:")
                                celular_error_profesor = True
                            else:
                                break
                        Profesores.updateProfesor_telefono_celular(id_buscar_profesor, profesor_telefono_celular)
                        Profesores.verificar_cambios_profesor(id_buscar_profesor)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                    
                    if opciones ==5:
                        id_error_profesor = False
                        id_buscar_profesor = input("Ingrese la id del profesor:")
                        while  True:
                            if not id_buscar_profesor:
                                id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                                id_error_profesor = True
                            elif not id_buscar_profesor.isdigit():
                                id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                                id_error_profesor = True
                            else:
                                break
                        error_fecha_profesor = False
                        fecha_nacimiento_profesor = input("Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                        while True:
                            if not fecha_nacimiento_profesor:
                                fecha_nacimiento_profesor= input("(Error, no puede estar vacio)Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                                error_fecha_profesor = True
                            elif not validar_fecha(fecha_nacimiento_profesor):
                                fecha_nacimiento_profesor= input("(Error, formato no valido)Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                                error_fecha_profesor = True
                            else:
                                break   
                        Profesores.updateProfesor_fecha_nacimiento(id_buscar_profesor, fecha_nacimiento_profesor)
                        Profesores.verificar_cambios_profesor(id_buscar_profesor)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones ==6:
                        id_error_profesor = False
                        id_buscar_profesor = input("Ingrese la id del profesor:")
                        while  True:
                            if not id_buscar_profesor:
                                id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                                id_error_profesor = True
                            elif not id_buscar_profesor.isdigit():
                                id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                                id_error_profesor = True
                            else:
                                break
                        sexo_error_profesor = False
                        sexo_profesor = input("Ingrese el nuevo sexo:")
                        while True:
                            if not sexo_profesor:
                                sexo_profesor= input("(Error, no puede estar vacio)Ingrese el nuevo sexo:")
                                sexo_error_profesor = True
                            elif not sexo_profesor.isalpha():
                                sexo_profesor= input("(Error, solo se permite letras)Ingrese el nuevo sexo:")
                                sexo_error_profesor = True
                            else:
                                break
                        Profesores.updateProfesor_sexo(id_buscar_profesor, sexo_profesor)
                        Profesores.verificar_cambios_profesor(id_buscar_profesor)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                    
                    if opciones ==7:
                        id_error_profesor = False
                        id_buscar_profesor = input("Ingrese la id del profesor:")
                        while  True:
                            if not id_buscar_profesor:
                                id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                                id_error_profesor = True
                            elif not id_buscar_profesor.isdigit():
                                id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                                id_error_profesor = True
                            else:
                                break
                        direccion_profesor = input("Ingrese la nueva direccion:")
                        while not direccion_profesor:
                            direccion_profesor= input("(Error, no puede estar vacio)Ingrese la nueva direccion:")
                        Profesores.updateProfesor_direccion(id_buscar_profesor, direccion_profesor)
                        Profesores.verificar_cambios_profesor(id_buscar_profesor)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones ==8:
                        id_error_profesor = False
                        id_buscar_profesor = input("Ingrese la id del profesor:")
                        while  True:
                            if not id_buscar_profesor:
                                id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                                id_error_profesor = True
                            elif not id_buscar_profesor.isdigit():
                                id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                                id_error_profesor = True
                            else:
                                break
                        error_nombre_profesor = False
                        nombre_profesor = input("Ingresar el nuevo nombre:")
                        while True:
                            if not nombre_profesor:
                                nombre_profesor= input("(Error, no puede estar vacio)Ingresar el nuevo nombre:")
                                error_nombre_profesor = True
                            elif not all(letra.isalpha() or letra.isspace() for letra in nombre_profesor):
                                nombre_profesor= input("(Error, solo se permiten letras)Ingresar el nuevo nombre:")
                                error_nombre_profesor = True
                            else:
                                break
                        Profesores.updateProfesor_nombre(id_buscar_profesor, nombre_profesor)
                        Profesores.verificar_cambios_profesor(id_buscar_profesor)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones ==9:
                        id_error_profesor = False
                        id_buscar_profesor = input("Ingrese la id del profesor:")
                        while  True:
                            if not id_buscar_profesor:
                                id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                                id_error_profesor = True
                            elif not id_buscar_profesor.isdigit():
                                id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                                id_error_profesor = True
                            else:
                                break
                        apellido_p_profesor = False
                        apellido_paterno_profesor = input("Ingrese el nuvo apellido paterno:")
                        while True:
                            if not apellido_paterno_profesor:
                                apellido_paterno_profesor= input("(Error, no puede estar vacio)Ingrese el nuvo apellido paterno:")
                                apellido_p_profesor = True
                            elif not apellido_paterno_profesor.isalpha():
                                apellido_paterno_profesor= input("(Error, solo se permite letras)Ingrese el nuvo apellido paterno:")
                                apellido_p_profesor = True
                            else:
                                break
                        Profesores.updateProfesor_apellido_paterno(id_buscar_profesor, apellido_paterno_profesor)
                        Profesores.verificar_cambios_profesor(id_buscar_profesor)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones ==10:
                        id_error_profesor = False
                        id_buscar_profesor = input("Ingrese la id del profesor:")
                        while  True:
                            if not id_buscar_profesor:
                                id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                                id_error_profesor = True
                            elif not id_buscar_profesor.isdigit():
                                id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                                id_error_profesor = True
                            else:
                                break 
                        apellido_m_profesor = False
                        apellido_materno_profesor = input("Ingrese el nuevo apellido materno:")
                        while True:
                            if not apellido_materno_profesor:
                                apellido_materno_profesor= input("(Error, no puede estar vacio)Ingrese el nuevo apellido materno:")
                                apellido_m_profesor = True
                            elif not apellido_materno_profesor.isalpha():
                                apellido_materno_profesor= input("(Error, solo se permite letras)Ingrese el nuevo apellido materno:")
                                apellido_m_profesor = True
                            else:
                                break
                        Profesores.updateProfesor_apellido_materno(id_buscar_profesor, apellido_materno_profesor)
                        Profesores.verificar_cambios_profesor(id_buscar_profesor)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones ==11:
                        id_error_profesor = False
                        id_buscar_profesor = input("Ingrese la id del profesor:")
                        while  True:
                            if not id_buscar_profesor:
                                id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                                id_error_profesor = True
                            elif not id_buscar_profesor.isdigit():
                                id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                                id_error_profesor = True
                            else:
                                break
                        nacionalidad_error_profesor = False
                        nacionalidad_profesor = input("Ingrese la nueva nacionalidad:")
                        while True:
                            if not nacionalidad_profesor:
                                nacionalidad_profesor= input("(Error, no puede estar vacio)Ingrese la nueva nacionalidad:")
                                nacionalidad_error_profesor = True
                            elif not nacionalidad_profesor.isalpha():
                                nacionalidad_profesor= input("(Error, solo se permite letras)Ingrese la nueva nacionalidad:")
                                nacionalidad_error_profesor = True
                            else:
                                break
                        Profesores.updateProfesor_nacionalidad(id_buscar_profesor, nacionalidad_profesor)
                        Profesores.verificar_cambios_profesor(id_buscar_profesor)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones ==12:
                        id_error_profesor = False
                        id_buscar_profesor = input("Ingrese la id del profesor:")
                        while  True:
                            if not id_buscar_profesor:
                                id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                                id_error_profesor = True
                            elif not id_buscar_profesor.isdigit():
                                id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                                id_error_profesor = True
                            else:
                                break
                        usuario_error_profesor =False
                        usuario_profesor = input("Ingrese el nuevo usuario:")
                        while True:
                            if not usuario_profesor:
                                usuario_profesor= input("(Error, no puede estar vacio)Ingrese el nuevo usuario:")
                                usuario_error_profesor = True
                            elif Profesores.usuaraio_existente_profesor(usuario_profesor):
                                usuario_profesor= input("(Error, el usuario ya esta registrado)Ingrese el nuevo usuario:")
                                usuario_error_profesor = True
                            else:
                                break
                        Profesores.updateProfesor_usuario(id_buscar_profesor, usuario_profesor)
                        Profesores.verificar_cambios_profesor(id_buscar_profesor)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones ==13:
                        id_error_profesor = False
                        id_buscar_profesor = input("Ingrese la id del profesor:")
                        while  True:
                            if not id_buscar_profesor:
                                id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                                id_error_profesor = True
                            elif not id_buscar_profesor.isdigit():
                                id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                                id_error_profesor = True
                            else:
                                break 
                        id_c_profesor = False
                        idcarreras_profesor = input ("Ingrese el nuevo id de carreras:")
                        while True:
                            if not idcarreras_profesor:
                                idcarreras_profesor= input("(Error, no puede estar vacio)Ingrese el nuevo id de carreras:")
                                id_c_profesor = True
                            elif not idcarreras_profesor.isdigit():
                                idcarreras_profesor= input("(Error, solo se permite numeros)Ingrese el nuevo id de carreras:")
                                id_c_profesor = True
                            else:
                                break
                        Profesores.updateProfesor_id_carreras(id_buscar_profesor, idcarreras_profesor)
                        Profesores.verificar_cambios_profesor(id_buscar_profesor)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                            
                    if opciones ==14:
                        id_error_profesor = False
                        id_buscar_profesor = input("Ingrese la id del profesor:")
                        while  True:
                            if not id_buscar_profesor:
                                id_buscar_profesor= input("(Error, no puede estar vacio)Ingrese la id del profesor:")
                                id_error_profesor = True
                            elif not id_buscar_profesor.isdigit():
                                id_buscar_profesor= input("(Error, solo se permite numeros)Ingrese la id del profesor:") 
                                id_error_profesor = True
                            else:
                                break
                        error_cedula_profesor = False
                        profesor_cedula = input("Ingrese la nueva cedula:")
                        while True:
                            if not profesor_cedula:
                                profesor_cedula= input("(Error, no puede estar vacio)Ingrese la nueva cedula:")
                                error_cedula_profesor = True
                            elif not profesor_cedula.isdigit():
                                profesor_cedula= input("(Error, solo se permite numeros)Ingrese la nueva cedula:") 
                                error_cedula_profesor = True
                            elif Profesores.cedula_existente_profesor(profesor_cedula):
                                profesor_cedula= input("(Error, la cedula ya esta registrada)Ingrese la nueva cedula:") 
                                error_cedula_profesor = True
                            else:
                                break
                        error_correo_profesor = False
                        correo_electronico_profesor = input("Ingrese el correo electronico nuevo:")
                        while True:
                            if not correo_electronico_profesor:
                                correo_electronico_profesor= input("(Error, no puede estar vacio)Ingrese el correo electronico nuevo:")
                                error_correo_profesor =True
                            elif "@" not in correo_electronico_profesor or ".com" not in correo_electronico_profesor:
                                correo_electronico_profesor= input("(Error, tiene que llevar @ y .com)Ingrese el correo electronico nuevo:")
                                error_correo_profesor =True
                            elif Profesores.correo_electronico_existente_profesor(correo_electronico_profesor):
                                correo_electronico_profesor= input("(Error, el correo ya esta registrado)Ingrese el correo electronico nuevo:")
                                error_correo_profesor =True
                            else:
                                break
                        telefono_error_profesor = False
                        profesor_telefono = input("Ingrese el telefono nuevo:")
                        while True:
                            if not profesor_telefono:
                                profesor_telefono= input("(Error, no puede estar vacio)Ingrese el telefono nuevo:")
                                telefono_error_profesor = True
                            elif len(profesor_telefono) != 8 or not profesor_telefono.isdigit():
                                profesor_telefono = input("(Error, debe de tener 8 numeros)Ingrese el telefono nuevo:")
                                telefono_error_profesor = True
                            else:
                                break
                        celular_error_profesor = False
                        profesor_telefono_celular = input("Ingrese el nuevo numero de telefono celular:")
                        while True:
                            if not profesor_telefono_celular:
                                profesor_telefono_celular= input("(Error, no puede estar vacio)Ingrese el nuevo numero de telefono celular:")
                                celular_error_profesor = True
                            elif len(profesor_telefono_celular) != 8 or not profesor_telefono_celular.isdigit():
                                profesor_telefono_celular = input("(Error, debe de tener 8 numeros)Ingrese el nuevo numero de telefono celular:")
                                celular_error_profesor = True
                            elif Profesores.telefono_celular_existente_profesor(profesor_telefono_celular):
                                profesor_telefono_celular = input("(Error, el numero ya esta registrado)Ingrese el nuevo numero de telefono celular:")
                                celular_error_profesor = True
                            else:
                                break
                        error_fecha_profesor = False
                        fecha_nacimiento_profesor = input("Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                        while True:
                            if not fecha_nacimiento_profesor:
                                fecha_nacimiento_profesor= input("(Error, no puede estar vacio)Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                                error_fecha_profesor = True
                            elif not validar_fecha(fecha_nacimiento_profesor):
                                fecha_nacimiento_profesor= input("(Error, formato no valido)Ingrese la nueva fecha de nacimiento (año-mes-dia):")
                                error_fecha_profesor = True
                            else:
                                break   
                        sexo_error_profesor = False
                        sexo_profesor = input("Ingrese el nuevo sexo:")
                        while True:
                            if not sexo_profesor:
                                sexo_profesor= input("(Error, no puede estar vacio)Ingrese el nuevo sexo:")
                                sexo_error_profesor = True
                            elif not sexo_profesor.isalpha():
                                sexo_profesor= input("(Error, solo se permite letras)Ingrese el nuevo sexo:")
                                sexo_error_profesor = True
                            else:
                                break
                        direccion_profesor = input("Ingrese la nueva direccion:")
                        while not direccion_profesor:
                            direccion_profesor= input("(Error, no puede estar vacio)Ingrese la nueva direccion:")
                        error_nombre_profesor = False
                        nombre_profesor = input("Ingresar el nuevo nombre:")
                        while True:
                            if not nombre_profesor:
                                nombre_profesor= input("(Error, no puede estar vacio)Ingresar el nuevo nombre:")
                                error_nombre_profesor = True
                            elif not all(letra.isalpha() or letra.isspace() for letra in nombre_profesor):
                                nombre_profesor= input("(Error, solo se permiten letras)Ingresar el nuevo nombre:")
                                error_nombre_profesor = True
                            else:
                                break
                        apellido_p_profesor = False
                        apellido_paterno_profesor = input("Ingrese el nuvo apellido paterno:")
                        while True:
                            if not apellido_paterno_profesor:
                                apellido_paterno_profesor= input("(Error, no puede estar vacio)Ingrese el nuvo apellido paterno:")
                                apellido_p_profesor = True
                            elif not apellido_paterno_profesor.isalpha():
                                apellido_paterno_profesor= input("(Error, solo se permite letras)Ingrese el nuvo apellido paterno:")
                                apellido_p_profesor = True
                            else:
                                break
                        apellido_m_profesor = False
                        apellido_materno_profesor = input("Ingrese el nuevo apellido materno:")
                        while True:
                            if not apellido_materno_profesor:
                                apellido_materno_profesor= input("(Error, no puede estar vacio)Ingrese el nuevo apellido materno:")
                                apellido_m_profesor = True
                            elif not apellido_materno_profesor.isalpha():
                                apellido_materno_profesor= input("(Error, solo se permite letras)Ingrese el nuevo apellido materno:")
                                apellido_m_profesor = True
                            else:
                                break
                        nacionalidad_error_profesor = False
                        nacionalidad_profesor = input("Ingrese la nueva nacionalidad:")
                        while True:
                            if not nacionalidad_profesor:
                                nacionalidad_profesor= input("(Error, no puede estar vacio)Ingrese la nueva nacionalidad:")
                                nacionalidad_error_profesor = True
                            elif not nacionalidad_profesor.isalpha():
                                nacionalidad_profesor= input("(Error, solo se permite letras)Ingrese la nueva nacionalidad:")
                                nacionalidad_error_profesor = True
                            else:
                                break
                        usuario_error_profesor =False
                        usuario_profesor = input("Ingrese el nuevo usuario:")
                        while True:
                            if not usuario_profesor:
                                usuario_profesor= input("(Error, no puede estar vacio)Ingrese el nuevo usuario:")
                                usuario_error_profesor = True
                            elif Profesores.usuaraio_existente_profesor(usuario_profesor):
                                usuario_profesor= input("(Error, el usuario ya esta registrado)Ingrese el nuevo usuario:")
                                usuario_error_profesor = True
                            else:
                                break 
                        id_c_profesor = False
                        idcarreras_profesor = input ("Ingrese el nuevo id de carreras:")
                        while True:
                            if not idcarreras_profesor:
                                idcarreras_profesor= input("(Error, no puede estar vacio)Ingrese el nuevo id de carreras:")
                                id_c_profesor = True
                            elif not idcarreras_profesor.isdigit():
                                idcarreras_profesor= input("(Error, solo se permite numeros)Ingrese el nuevo id de carreras:")
                                id_c_profesor = True
                            else:
                                break                   
                        Profesores.updateProfesor_total(id_buscar_profesor, profesor_cedula, correo_electronico_profesor, profesor_telefono, profesor_telefono_celular, fecha_nacimiento_profesor, sexo_profesor, direccion_profesor, nombre_profesor, apellido_paterno_profesor, apellido_materno_profesor, nacionalidad_profesor, usuario_profesor, idcarreras_profesor)
                        Profesores.verificar_cambios_profesor(id_buscar_profesor)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Profesor:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                    
                    if opciones == 15:
                        limpiar_consola()
                        break

            if opcion == 4:
                error_cedula_profesor = False
                profesor_cedula = input("Ingrese la cedula:")
                while True:
                    if not profesor_cedula:
                        profesor_cedula= input("(Error, no puede estar vacio)Ingrese la cedula:")
                        error_cedula_profesor = True
                    elif not profesor_cedula.isdigit():
                        profesor_cedula= input("(Error, solo se permite numeros)Ingrese la cedula:") 
                        error_cedula_profesor = True
                    elif Profesores.cedula_existente_profesor(profesor_cedula):
                        profesor_cedula= input("(Error, la cedula ya esta registrada)Ingrese la cedula:") 
                        error_cedula_profesor = True
                    else:
                        break
                error_correo_profesor = False
                correo_electronico_profesor = input("Ingrese el correo electronico:")
                while True:
                    if not correo_electronico_profesor:
                        correo_electronico_profesor= input("(Error, no puede estar vacio)Ingrese el correo electronico:")
                        error_correo_profesor =True
                    elif "@" not in correo_electronico_profesor or ".com" not in correo_electronico_profesor:
                        correo_electronico_profesor= input("(Error, tiene que llevar @ y .com)Ingrese el correo electronico:")
                        error_correo_profesor =True
                    elif Profesores.correo_electronico_existente_profesor(correo_electronico_profesor):
                        correo_electronico_profesor= input("(Error, el correo ya esta registrado)Ingrese el correo electronico:")
                        error_correo_profesor =True
                    else:
                         break
                telefono_error_profesor = False
                profesor_telefono = input("Ingrese el telefono:")
                while True:
                    if not profesor_telefono:
                        profesor_telefono= input("(Error, no puede estar vacio)Ingrese el telefono:")
                        telefono_error_profesor = True
                    elif len(profesor_telefono) != 8 or not profesor_telefono.isdigit():
                        profesor_telefono = input("(Error, debe de tener 8 numeros)Ingrese el telefono:")
                        telefono_error_profesor = True
                    else:
                        break
                celular_error_profesor = False
                profesor_telefono_celular = input("Ingrese el numero de telefono celular:")
                while True:
                    if not profesor_telefono_celular:
                        profesor_telefono_celular= input("(Error, no puede estar vacio)Ingrese el numero de telefono celular:")
                        celular_error_profesor = True
                    elif len(profesor_telefono_celular) != 8 or not profesor_telefono_celular.isdigit():
                        profesor_telefono_celular = input("(Error, debe de tener 8 numeros)Ingrese el numero de telefono celular:")
                        celular_error_profesor = True
                    elif Profesores.telefono_celular_existente_profesor(profesor_telefono_celular):
                        profesor_telefono_celular = input("(Error, el numero ya esta registrado)Ingrese el numero de telefono celular:")
                        celular_error_profesor = True
                    else:
                        break
                error_fecha_profesor = False
                fecha_nacimiento_profesor = input("Ingrese la fecha de nacimiento (año-mes-dia):")
                while True:
                    if not fecha_nacimiento_profesor:
                        fecha_nacimiento_profesor= input("(Error, no puede estar vacio)Ingrese la fecha de nacimiento (año-mes-dia):")
                        error_fecha_profesor = True
                    elif not validar_fecha(fecha_nacimiento_profesor):
                        fecha_nacimiento_profesor= input("(Error, formato no valido)Ingrese la fecha de nacimiento (año-mes-dia):")
                        error_fecha_profesor = True
                    else:
                        break   
                sexo_error_profesor = False
                sexo_profesor = input("Ingrese el sexo:")
                while True:
                    if not sexo_profesor:
                        sexo_profesor= input("(Error, no puede estar vacio)Ingrese el sexo:")
                        sexo_error_profesor = True
                    elif not sexo_profesor.isalpha():
                        sexo_profesor= input("(Error, solo se permite letras)Ingrese el sexo:")
                        sexo_error_profesor = True
                    else:
                        break
                direccion_profesor = input("Ingrese la direccion:")
                while not direccion_profesor:
                    direccion_profesor= input("(Error, no puede estar vacio)Ingrese la direccion:")
                error_nombre_profesor = False
                nombre_profesor = input("Ingresar el nombre:")
                while True:
                    if not nombre_profesor:
                        nombre_profesor= input("(Error, no puede estar vacio)Ingresar el nombre:")
                        error_nombre_profesor = True
                    elif not all(letra.isalpha() or letra.isspace() for letra in nombre_profesor):
                        nombre_profesor= input("(Error, solo se permiten letras)Ingresar el nombre:")
                        error_nombre_profesor = True
                    else:
                        break
                apellido_p_profesor = False
                apellido_paterno_profesor = input("Ingrese el apellido paterno:")
                while True:
                    if not apellido_paterno_profesor:
                        apellido_paterno_profesor= input("(Error, no puede estar vacio)Ingrese el apellido paterno:")
                        apellido_p_profesor = True
                    elif not apellido_paterno_profesor.isalpha():
                        apellido_paterno_profesor= input("(Error, solo se permite letras)Ingrese el apellido paterno:")
                        apellido_p_profesor = True
                    else:
                        break
                apellido_m_profesor = False
                apellido_materno_profesor = input("Ingrese el apellido materno:")
                while True:
                    if not apellido_materno_profesor:
                        apellido_materno_profesor= input("(Error, no puede estar vacio)Ingrese el apellido materno:")
                        apellido_m_profesor = True
                    elif not apellido_materno_profesor.isalpha():
                        apellido_materno_profesor= input("(Error, solo se permite letras)Ingrese el apellido materno:")
                        apellido_m_profesor = True
                    else:
                         break
                nacionalidad_error_profesor = False
                nacionalidad_profesor = input("Ingrese la nacionalidad:")
                while True:
                    if not nacionalidad_profesor:
                        nacionalidad_profesor= input("(Error, no puede estar vacio)Ingrese la nacionalidad:")
                        nacionalidad_error_profesor = True
                    elif not nacionalidad_profesor.isalpha():
                        nacionalidad_profesor= input("(Error, solo se permite letras)Ingrese la nacionalidad:")
                        nacionalidad_error_profesor = True
                    else:
                        break
                usuario_error_profesor =False
                usuario_profesor = input("Ingrese el usuario:")
                while True:
                    if not usuario_profesor:
                        usuario_profesor= input("(Error, no puede estar vacio)Ingrese el usuario:")
                        usuario_error_profesor = True
                    elif Profesores.usuaraio_existente_profesor(usuario_profesor):
                        usuario_profesor= input("(Error, el usuario ya esta registrado)Ingrese el usuario:")
                        usuario_error_profesor = True
                    else:
                        break 
                id_c_profesor = False
                idcarreras_profesor = input ("Ingrese el id de carreras:")
                while True:
                    if not idcarreras_profesor:
                        idcarreras_profesor= input("(Error, no puede estar vacio)Ingrese el id de carreras:")
                        id_c_profesor = True
                    elif not idcarreras_profesor.isdigit():
                        idcarreras_profesor= input("(Error, solo se permite numeros)Ingrese el id de carreras:")
                        id_c_profesor = True
                    else:
                        break                 
                Profesores.crear_profesor( profesor_cedula, correo_electronico_profesor, profesor_telefono, profesor_telefono_celular, fecha_nacimiento_profesor, sexo_profesor, direccion_profesor, nombre_profesor, apellido_paterno_profesor, apellido_materno_profesor, nacionalidad_profesor, usuario_profesor, idcarreras_profesor)
                print("Se creo un nuevo registro")
                menu_volver = input("Ingrese una (s) para volver a la seccion Profesor o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Profesor o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break


            if opcion == 5:
                id_error_profesor_borrar = False
                id_profesor_borrar = input("Ingrese la id que quiere borrar:")
                while True:
                    if not id_profesor_borrar:
                        id_profesor_borrar= input("(Error, no puede estar vacio)Ingrese la id que quiere borrar:")
                        
                    elif not id_profesor_borrar.isdigit():
                        id_profesor_borrar= input("(Error, solo se permite numeros)Ingrese la id que quiere borrar:")
                        id_error_profesor_borrar = True
                    else:
                        break
                Profesores.verificar_borrar_profesor(id_profesor_borrar)
                Profesores.borrar_profesor(id_profesor_borrar)
                menu_volver = input("Ingrese una (s) para volver a la seccion Profesor o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Profesor o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break

            if opcion == 6:
                limpiar_consola()
                break
 
    if eleccion ==4 :
        limpiar_consola()
        opcion = 0
        while opcion != 6:
            print("""   
    Seccion Grupo

Eliga una de las siguientes opciones:

    1-Consultar datos generales          
    2-Consultar datos individuales       
    3-Actualizar un registro        
    4-Crear un registro         
    5-Eliminar un registro           
    6-Volver al menu principal            
                    """)
            
            error_opcion = False

            opcion_input =input("Numero de la opcion:")

            while True:
                if not opcion_input:
                    opcion_input =input("(Error, no puede estar vacio)Numero de la opcion:")
                    error_opcion = True

                elif not opcion_input.isdigit():
                    opcion_input =input("(Error, solo se permiten numeros)Numero de la opcion:")    
                    error_opcion = True

                elif int(opcion_input) not in range(1, 7):
                    opcion_input =input("(Error, numero no valido)Numero de la opcion:")
                    error_opcion = True
                else:
                    break
            

            opcion = int(opcion_input)     

            if opcion ==1:
                grupos.getGrupo()
                menu_volver = input("Ingrese una (s) para volver a la seccion Grupo o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Grupo o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break

            if opcion == 2:
                id_error_grupo = False
                id_grupo_buscar= input("Ingrese la id del grupo:")
                while True:
                    if not id_grupo_buscar:
                        id_grupo_buscar= input("(Error, no puede estar vacio)Ingrese la id del grupo:")
                        id_error_grupo = True
                    elif not id_grupo_buscar.isdigit():
                        id_grupo_buscar= input("(Error, solo se permite numeros)Ingrese la id del grupo:")
                        id_error_grupo = True
                    else:
                        break
                grupos.verificar_id_grupo(id_grupo_buscar)
                menu_volver = input("Ingrese una (s) para volver a la seccion Grupo o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Grupo o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break

            if opcion ==3:
                limpiar_consola()
                opciones = 0
                while opciones != 2:
                    print("""
    Actualizar  registro en la seccion Grupo

Eliga lo que quiere actualizar:
    
    1-Actualizar nombre                      
    2-Salir                                     
                          """)
                    
                    error_opciones = False 
                    opciones_input =input("Ingrese el numero de la opcion:")

                    while True:

                        if not opciones_input:
                            opciones_input =input("(Error, no puede estar vacio)Ingrese el numero de la opcion:")
                            error_opciones = True

                        elif not opciones_input.isdigit():
                            opciones_input =input("(Error, solo se permiten numeros)Ingrese el numero de la opcion:")   
                            error_opciones = True

                        elif int(opciones_input) not in range (1, 3):
                            opciones_input =input("(Error, numero no valido)Ingrese el numero de la opcion:")
                            error_opciones = True

                        else:
                            break

                    opciones = int(opciones_input)                    
                    
                    if opciones ==1:
                        id_error_grupo = False
                        id_grupo_buscar= input("Ingrese la id del grupo:")
                        while True:
                            if not id_grupo_buscar:
                                id_grupo_buscar= input("(Error, no puede estar vacio)Ingrese la id del grupo:")
                                id_error_grupo = True
                            elif not id_grupo_buscar.isdigit():
                                id_grupo_buscar= input("(Error, solo se permite numeros)Ingrese la id del grupo:")
                                id_error_grupo = True
                            else:
                                break
                        nombre_grupo = input("Ingrese el nombre nuevo:")
                        while not nombre_grupo:
                            nombre_grupo = input("(Error, no puede estar vacio)Ingrese el nombre nuevo:")
                        grupos.updateGrupo_nombre(id_grupo_buscar, nombre_grupo)
                        grupos.verificar_cambios_grupo(id_grupo_buscar)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Grupo:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Grupo:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                        
                    if opciones ==2:
                        limpiar_consola()
                        break

                
            if opcion ==4:
                nombre_grupo = input("Ingrese el nombre del grupo:")
                while not nombre_grupo:
                    nombre_grupo = input("(Error, no puede estar vacio)Ingrese el nombre del grupo:")
                grupos.crearGrupo(nombre_grupo)
                print("Se creo un nuevo registro")
                menu_volver = input("Ingrese una (s) para volver a la seccion Grupo o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Grupo o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break
            
            if opcion ==5:
                id_error_eliminar_gurpo = False
                id_grupo_eliminar= input("Ingrese la id del grupo:")
                while True:
                    if not id_grupo_eliminar:
                        id_grupo_eliminar= input("(Error, no puede estar vacio)Ingrese la id del grupo:")
                        id_error_eliminar_gurpo = True
                    elif not id_grupo_eliminar.isdigit():
                        id_grupo_eliminar= input("(Error, solo se permite numeros)Ingrese la id del grupo:")
                        id_error_eliminar_gurpo = True
                    else:
                        break
                grupos.verificar_borrado_grupo(id_grupo_eliminar)
                grupos.borrar_grupo(id_grupo_eliminar)
                menu_volver = input("Ingrese una (s) para volver a la seccion Grupo o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Grupo o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break


            if opcion ==6:
                limpiar_consola()
                break

    if eleccion ==5:
        limpiar_consola()
        opcion = 0
        while opcion != 6:
            print("""   
    Seccion usuario

Eliga una de las siguientes opciones:

    1-Consultar datos generales          
    2-Consultar datos individuales       
    3-Actualizar un registro        
    4-Crear un registro         
    5-Eliminar un registro           
    6-Volver al menu principal            
                    """)
           
            error_opcion = False

            opcion_input =input("Numero de la opcion:")

            while True:
                if not opcion_input:
                    opcion_input =input("(Error, no puede estar vacio)Numero de la opcion:")
                    error_opcion = True

                elif not opcion_input.isdigit():
                    opcion_input =input("(Error, solo se permiten numeros)Numero de la opcion:")    
                    error_opcion = True

                elif int(opcion_input) not in range(1, 7):
                    opcion_input =input("(Error, numero no valido)Numero de la opcion:")
                    error_opcion = True
                else:
                    break
            

            opcion = int(opcion_input)     

            if opcion ==1:
                usuarios.getUsuario()
                menu_volver = input("Ingrese una (s) para volver a la seccion Usuario o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Usuario o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break

            if opcion ==2:
                id_error_usuario = False
                id_buscar_usuario = input("Ingrese la id del usuario:")
                while True:
                    if not id_buscar_usuario:
                        id_buscar_usuario= input("(Error, no puede estar vacio)Ingrese la id del usuario:")
                        id_error_usuario = True
                    elif not id_buscar_usuario.isdigit():
                        id_buscar_usuario= input("(Error, solo se permite numeros)Ingrese la id del usuario:")
                        id_error_usuario = True
                    else:
                        break
                usuarios.verificar_id_usuario(id_buscar_usuario)
                menu_volver = input("Ingrese una (s) para volver a la seccion Usuario o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Usuario o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break

            if opcion ==3:
                limpiar_consola()
                opciones = 0
                while opciones != 6:
                    print("""
    Actualizar  registro en la seccion Usuario

Eliga lo que quiere actualizar:
    
    1-Actualizar nombre
    2-Actualizar correo electronico
    3-Actualizar contraseña   
    4-Actualizar todo                   
    5-Salir                                     
                          """)

                    error_opciones = False 
                    opciones_input =input("Ingrese el numero de la opcion:")

                    while True:

                        if not opciones_input:
                            opciones_input =input("(Error, no puede estar vacio)Ingrese el numero de la opcion:")
                            error_opciones = True

                        elif not opciones_input.isdigit():
                            opciones_input =input("(Error, solo se permiten numeros)Ingrese el numero de la opcion:")   
                            error_opciones = True

                        elif int(opciones_input) not in range (1, 6):
                            opciones_input =input("(Error, numero no valido)Ingrese el numero de la opcion:")
                            error_opciones = True

                        else:
                            break

                    opciones = int(opciones_input)       
            

                    if opciones ==1:
                        id_error_usuario = False
                        id_buscar_usuario = input("Ingrese la id del usuario:")
                        while True:
                            if not id_buscar_usuario:
                                id_buscar_usuario= input("(Error, no puede estar vacio)Ingrese la id del usuario:")
                                id_error_usuario = True
                            elif not id_buscar_usuario.isdigit():
                                id_buscar_usuario= input("(Error, solo se permite numeros)Ingrese la id del usuario:")
                                id_error_usuario = True
                            else:
                                break
                        error_nombre_usuario = False
                        nombre_usuario = input("Ingrese el nuevo nombre:")
                        while True:
                            if not nombre_usuario:
                                nombre_usuario = input("(Error, no puede estar vacio)Ingrese el nombre nuevo:")
                                error_nombre_usuario = True
                            elif not nombre_usuario.isalpha():
                                nombre_usuario = input("(Error, solo se permiten letras)Ingrese el nombre nuevo:")
                                error_nombre_usuario = True
                            else:
                                break
                        usuarios.updateUsuario_nombre(id_buscar_usuario, nombre_usuario)
                        usuarios.verificar_cambios_usuario(id_buscar_usuario)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Usuario:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Usuario:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                        
                    if opciones ==2:
                        id_error_usuario = False
                        id_buscar_usuario = input("Ingrese la id del usuario:")
                        while True:
                            if not id_buscar_usuario:
                                id_buscar_usuario= input("(Error, no puede estar vacio)Ingrese la id del usuario:")
                                id_error_usuario = True
                            elif not id_buscar_usuario.isdigit():
                                id_buscar_usuario= input("(Error, solo se permite numeros)Ingrese la id del usuario:")
                                id_error_usuario = True
                            else:
                                break
                        correo_error_usuario = False
                        correo_electronico_usuario = input("Ingrese el correo electronico nuevo:")
                        while True:
                            if not correo_electronico_usuario:
                                correo_electronico_usuario= input("(Error, no puede estar vacio)Ingrese el correo electronico nuevo:")
                                correo_error_usuario = True
                            elif "@" not in correo_electronico_usuario or ".com" not in correo_electronico_usuario:
                                correo_electronico_usuario= input("(Error, tiene que llevar @ y .com)Ingrese el correo electronico nuevo:")   
                                correo_error_usuario = True
                            elif usuarios.correo_existe_usuario(correo_electronico_usuario):
                                correo_electronico_usuario= input("(Error, el correo ya esta registrado)Ingrese el correo electronico nuevo:")
                                correo_error_usuario = True
                            else:
                                break
                        usuarios.updateUsuario_correo_electronico(id_buscar_usuario, correo_electronico_usuario)
                        usuarios.verificar_cambios_usuario(id_buscar_usuario)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Usuario:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Usuario:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones ==3:
                        id_error_usuario = False
                        id_buscar_usuario = input("Ingrese la id del usuario:")
                        while True:
                            if not id_buscar_usuario:
                                id_buscar_usuario= input("(Error, no puede estar vacio)Ingrese la id del usuario:")
                                id_error_usuario = True
                            elif not id_buscar_usuario.isdigit():
                                id_buscar_usuario= input("(Error, solo se permite numeros)Ingrese la id del usuario:")
                                id_error_usuario = True
                            else:
                                break
                        password_usuario = input("Ingrese la nueva contraseña:")
                        while not password_usuario:
                            password_usuario= input("(Error, no puede estar vacio)Ingrese la nueva contraseña:")
                        usuarios.updateUsuario_paswword(id_buscar_usuario, password_usuario)
                        usuarios.verificar_cambios_usuario(id_buscar_usuario)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Usuario:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Usuario:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break

                    if opciones ==4:
                        id_error_usuario = False
                        id_buscar_usuario = input("Ingrese la id del usuario:")
                        while True:
                            if not id_buscar_usuario:
                                id_buscar_usuario= input("(Error, no puede estar vacio)Ingrese la id del usuario:")
                                id_error_usuario = True
                            elif not id_buscar_usuario.isdigit():
                                id_buscar_usuario= input("(Error, solo se permite numeros)Ingrese la id del usuario:")
                                id_error_usuario = True
                            else:
                                break
                        error_nombre_usuario = False
                        nombre_usuario = input("Ingrese el nuevo nombre:")
                        while True:
                            if not nombre_usuario:
                                nombre_usuario = input("(Error, no puede estar vacio)Ingrese el nombre nuevo:")
                                error_nombre_usuario = True
                            elif not nombre_usuario.isalpha():
                                nombre_usuario = input("(Error, solo se permiten letras)Ingrese el nombre nuevo:")
                                error_nombre_usuario = True
                            else:
                                break
                        correo_error_usuario = False
                        correo_electronico_usuario = input("Ingrese el correo electronico nuevo:")
                        while True:
                            if not correo_electronico_usuario:
                                correo_electronico_usuario= input("(Error, no puede estar vacio)Ingrese el correo electronico nuevo:")
                                correo_error_usuario = True
                            elif "@" not in correo_electronico_usuario or ".com" not in correo_electronico_usuario:
                                correo_electronico_usuario= input("(Error, tiene que llevar @ y .com)Ingrese el correo electronico nuevo:")   
                                correo_error_usuario = True
                            elif usuarios.correo_existe_usuario(correo_electronico_usuario):
                                correo_electronico_usuario= input("(Error, el correo ya esta registrado)Ingrese el correo electronico nuevo:")
                                correo_error_usuario = True
                            else:
                                break
                        password_usuario = input("Ingrese la nueva contraseña:")
                        while not password_usuario:
                            password_usuario= input("(Error, no puede estar vacio)Ingrese la nueva contraseña:")
                        usuarios.updateUsuario_total(id_buscar_usuario, nombre_usuario, correo_electronico_usuario, password_usuario)
                        usuarios.verificar_cambios_usuario(id_buscar_usuario)
                        menu_volver = input("Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Usuario:")
                        while menu_volver not in ["s", "n"]:
                            menu_volver = input("(Error)Ingrese una (s) para realizar otro cambio o (n) para volver a la seccion Usuario:")
                        if menu_volver == "s":
                            limpiar_consola()
                            continue
                        if menu_volver == "n":
                            limpiar_consola()
                            break
                        
                    if opciones ==5:
                        limpiar_consola()
                        break
            
            if opcion ==4:
                error_nombre_usuario = False
                nombre_usuario = input("Ingrese el nombre:")
                while True:
                    if not nombre_usuario:
                        nombre_usuario = input("(Error, no puede estar vacio)Ingrese el nombre:")
                        error_nombre_usuario = True
                    elif not nombre_usuario.isalpha():
                        nombre_usuario = input("(Error, solo se permiten letras)Ingrese el nombre:")
                        error_nombre_usuario = True
                    else:
                        break
                correo_error_usuario = False
                correo_electronico_usuario = input("Ingrese el correo electronico nuevo:")
                while True:
                    if not correo_electronico_usuario:
                        correo_electronico_usuario= input("(Error, no puede estar vacio)Ingrese el correo electronico:")
                        correo_error_usuario = True
                    elif "@" not in correo_electronico_usuario or ".com" not in correo_electronico_usuario:
                        correo_electronico_usuario= input("(Error, tiene que llevar @ y .com)Ingrese el correo electronico:")   
                        correo_error_usuario = True
                    elif usuarios.correo_existe_usuario(correo_electronico_usuario):
                        correo_electronico_usuario= input("(Error, el correo ya esta registrado)Ingrese el correo electronico:")
                        correo_error_usuario = True
                    else:
                        break
                password_usuario = input("Ingrese la contraseña:")
                while not password_usuario:
                    password_usuario= input("(Error, no puede estar vacio)Ingrese la contraseña:")
                usuarios.crear_Usuario(nombre_usuario, correo_electronico_usuario, password_usuario)
                print("Se creo un nuevo registro")
                menu_volver = input("Ingrese una (s) para volver a la seccion Usuario o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Usuario o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break

            if opcion ==5:
                id_error_eliminar_usuario = False
                id_eliminar_usuario = input("Ingrese la id del usuario:")
                while True: 
                    if not id_eliminar_usuario:
                        id_eliminar_usuario= input("(Error, no puede estar vacio)Ingrese la id del usuario:")
                        id_error_eliminar_usuario = True
                    elif not id_eliminar_usuario.isdigit():
                        id_eliminar_usuario= input("(Error, solo se permite numeros)Ingrese la id del usuario:")
                        id_error_eliminar_usuario = True
                    else:
                        break
                usuarios.verificar_borrar_usuario(id_eliminar_usuario)
                usuarios.borrar_Usuario(id_eliminar_usuario)
                menu_volver = input("Ingrese una (s) para volver a la seccion Usuario o (n) para volver al menu principal:")
                while menu_volver not in ["s", "n"]:
                    menu_volver = input("(Error)Ingrese una (s) para volver a la seccion Usuario o (n) para volver al menu principal:")
                if menu_volver == "s":
                    limpiar_consola()
                    continue
                if menu_volver == "n":
                    limpiar_consola()
                    break
            
            if opcion ==6:
                limpiar_consola()
                break



    if eleccion == 6:
        limpiar_consola()
        print("Desconectado")
        break