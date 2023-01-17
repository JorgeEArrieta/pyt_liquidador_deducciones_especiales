#Módulo que contiene las funciones correspondientes a la lectura, modificación,
#y borrado de registros de la BBDD.

from importacion import BaseDatos 
from importacion import RangoSegundoParrafo
from importacion import DeduccionesPersonales
from peewee import InterfaceError
from peewee import OperationalError


#Lectura de deducciones para formulario el formulario de configuración.
################################################################################################################
def carga_ded_personales(year):

    """
    Obtiene, de la base de datos config.db, los valores correspondientes a la tabla deducciones personales. 
    El parametro year, de la función, determina de que año se obtendrán los valores.
    """

    try:

        listado = list()

        query = DeduccionesPersonales.select(DeduccionesPersonales.importe).where(DeduccionesPersonales.year == year)

        for row in query:
            listado.append(row.importe)

        return listado

    except:
        pass

def actualizar_ded_personales(year, tipo, importe):

    try:

        valor = DeduccionesPersonales.update(importe = importe).where(
            DeduccionesPersonales. year == year, DeduccionesPersonales.tipo == tipo)

        valor.execute()

    except OperationalError:
        print('Base de datos en uso por otro programa. No puede accederse a la misma.')



#Lectura de la tabla rango segundo párrafo
################################################################################################################

def lee_dedsegundoparrafo(resolucion: str) -> list:
    
    """
    Lee los registros de la tabla rangosegundoparrafo, del esquema usuario, y devuelve los valores.
    """
    
    try:
        resultado = list()

        query = RangoSegundoParrafo.select(RangoSegundoParrafo.id, RangoSegundoParrafo.resolucion, RangoSegundoParrafo.val_min, 
            RangoSegundoParrafo.val_max, RangoSegundoParrafo.deduccion).where(
            RangoSegundoParrafo.resolucion == resolucion)
    
        for row in query:
            lista = list()
            lista.append(row.id)
            lista.append(row.resolucion)
            lista.append(row.val_min)
            lista.append(row.val_max)
            lista.append(row.deduccion)
            resultado.append(lista)

        return resultado

    except InterfaceError:
        print('Problema en bbdd.')

    
def registro_dedsegundoparrafo(id: str) -> list:

    try:
        
        query = RangoSegundoParrafo.select(RangoSegundoParrafo.resolucion, RangoSegundoParrafo.val_min, 
                RangoSegundoParrafo.val_max, RangoSegundoParrafo.deduccion).where(
                RangoSegundoParrafo.id == id)
    
        for row in query:
            resolucion = row.resolucion
            val_min = row.val_min
            val_max = row.val_max
            deduccion = row.deduccion
            
        return resolucion, val_min, val_max, deduccion

    except InterfaceError:
        print('Problema en bbdd.')

    except Exception as error:
        print(error)
    
        
def actualiza_dedsegundoparrafo(id: int, min: float, max: float, deduc: float) -> bool:

    try:

        query = RangoSegundoParrafo.update(val_min = min, val_max = max, deduccion = deduc).where(
                RangoSegundoParrafo.id == id)
        query.execute()

        return True

    except Exception as error:
        print(error)
        return False


def elimina_dedsegundoparrafo(id: int) -> bool:

    try:
        query = RangoSegundoParrafo.delete().where(RangoSegundoParrafo.id == id)
        query.execute()

        return True

    except Exception as error:
        print(error)
        return False

    

#Funciones del esquema usuario
################################################################################################################
def lee_promediobruto(month: list, year: list) -> list:
    
    """
    Obtiene los datos que se encuentran en la tabla promediobruto, del esquema usario.
    """
    
    try:
        if year[0] == '*':
            year = ['2021', '2022']

        if month[0] == '*':
            month = ['1', '2', '3', '4' , '5', '6', '7', '8', '9', '10', '11', '12']

        resultado = list()

        query = BaseDatos.PromedioBruto.select(BaseDatos.PromedioBruto.legajo, BaseDatos.PromedioBruto.ann, BaseDatos.PromedioBruto.mes,
        BaseDatos.PromedioBruto.importe).where(BaseDatos.PromedioBruto.ann.in_(year), BaseDatos.PromedioBruto.mes.in_(month))

        for row in query:
            listado = list()
            listado.append(row.legajo)
            listado.append(row.ann)
            listado.append(row.mes)
            listado.append(row.importe)
            resultado.append(listado)

        return resultado

    except InterfaceError:
        print('No se abrio la base de datos')

    except Exception as error:
        print(error)

    
def lee_primerparrafo(month: list, year: list) -> list:
    
    try:

        resultado = list()

        if year[0] == '*':
            year = ['2021', '2022']
        if month[0] == '*':
            month = ['1', '2', '3', '4' , '5', '6', '7', '8', '9', '10', '11', '12']

        query = BaseDatos.PrimerParrafo.select(BaseDatos.PrimerParrafo.legajo, BaseDatos.PrimerParrafo.ann, BaseDatos.PrimerParrafo.mes,
        BaseDatos.PrimerParrafo.sbruto, BaseDatos.PrimerParrafo.deducciones, BaseDatos.PrimerParrafo.ded_esp,
        BaseDatos.PrimerParrafo.min_no_imp, BaseDatos.PrimerParrafo.cargas_familia, BaseDatos.PrimerParrafo.ded_p_parrafo).where(
        BaseDatos.PrimerParrafo.ann.in_(year), BaseDatos.PrimerParrafo.mes.in_(month))

        for row in query:
            listado = list()
            listado.append(row.legajo)
            listado.append(row.ann)
            listado.append(row.mes)
            listado.append(row.sbruto)
            listado.append(row.deducciones)
            listado.append(row.ded_esp)
            listado.append(row.min_no_imp)
            listado.append(row.cargas_familia)
            listado.append(row.ded_p_parrafo)
            resultado.append(listado)

        return resultado

    except InterfaceError:
        print('No se abrio la base de datos')

    except Exception as error:
        print(error)


def lee_segundoparrafo(month: list, year: list) -> list:
    
    try:
        resultado = list()

        if year[0] == '*':
            year = ['2021', '2022']
        
        if month[0] == '*':
            month = ['1', '2', '3', '4' , '5', '6', '7', '8', '9', '10', '11', '12']

        query = BaseDatos.SegundoParrafo.select(BaseDatos.SegundoParrafo.legajo, BaseDatos.SegundoParrafo.ann, 
        BaseDatos.SegundoParrafo.mes, BaseDatos.SegundoParrafo.ded_s_parrafo).where(
        BaseDatos.SegundoParrafo.ann.in_(year), BaseDatos.SegundoParrafo.mes.in_(month))

        for row in query:
            listado = list()
            listado.append(row.legajo)
            listado.append(row.ann)
            listado.append(row.mes)
            listado.append(row.ded_s_parrafo)
            resultado.append(listado)

        return resultado

    except InterfaceError:
        print('No se abrio la base de datos')

    except Exception as error:
        print(error)


def lista_empleados():

    """
    Obtiene el listado de legajos de la tabla empleados de la bbdd.
    """
    try:

        #Declaración variables
        lista_legajo = list()

        empleado = BaseDatos.Empleados()

        #Se leen los datos de la tabla empleado de la bbdd.
        legajos = empleado.select(BaseDatos.Empleados.legajo)

        for legajo in legajos:
            lista_legajo.append(legajo.legajo)

        return lista_legajo

    except InterfaceError:
        print('No se abrio la base de datos')
    
    except Exception as error:
        print(error)


def lectura_bbdd_empleados() -> list:

    """
    Lee los registros que estan cargados en la tabla de empleados de la bbdd.
    """
    try:

        listado = lista_empleados()
        datos = list()

        for legajo in listado:

            consulta = BaseDatos.Empleados.select(BaseDatos.Empleados.legajo, BaseDatos.Empleados.cuil, 
            BaseDatos.Empleados.nombre_apellido, BaseDatos.Empleados.fecha_ingreso).where(
            BaseDatos.Empleados.legajo == legajo)

            for row in consulta:
                lista = list()
                lista.append(row.legajo)
                lista.append(row.cuil)
                lista.append(row.nombre_apellido)
                lista.append(row.fecha_ingreso)
                datos.append(lista)

        return datos

    except InterfaceError:
        print('No se abrio la base de datos.')

    except TypeError:
        print('Error en datos.')

    except Exception as error:
        print(error)


def lect_bbdd_rem_deduc(tabla: str, legajo: list, month: list, year: list) -> list:
    
    """
    Lee los registros de las tablas de deducciones o, remuneraciones brutas, y obtiene los datos de
    la tabla seleccionada.
    """
    
    try:

        #Declaración de variables
        datos = list()

        if legajo[0] == '*':
            legajo = lista_empleados()
            
        if year[0] == '*':
            year = ['2021', '2022']

        if month[0] == '*':
            month = ['1', '2', '3', '4' , '5', '6', '7', '8', '9', '10', '11', '12']

        #Lectura de la tabla remuneraciones
        if tabla == 'remu':

            consulta = BaseDatos.SueldosBrutos.select(BaseDatos.SueldosBrutos.legajo, BaseDatos.SueldosBrutos.nombre_apellido,
                        BaseDatos.SueldosBrutos.ann, BaseDatos.SueldosBrutos.mes, BaseDatos.SueldosBrutos.importe).where(
                        BaseDatos.SueldosBrutos.legajo.in_(legajo), BaseDatos.SueldosBrutos.ann.in_(year), BaseDatos.SueldosBrutos.mes.in_(month))
        
            for row in consulta:
                lista = list()
                lista.append(row.legajo)
                lista.append(row.nombre_apellido)
                lista.append(row.ann)
                lista.append(row.mes)
                lista.append(row.importe)
                datos.append(lista)
    
        #Lectura de la tabla deducciones.
        elif tabla == 'deduc':

            consulta = BaseDatos.Deducciones.select(BaseDatos.Deducciones.legajo, BaseDatos.Deducciones.nombre_apellido,
            BaseDatos.Deducciones.ann, BaseDatos.Deducciones.mes, BaseDatos.Deducciones.importe).where(
            BaseDatos.Deducciones.legajo.in_(legajo), BaseDatos.Deducciones.ann.in_(year), BaseDatos.Deducciones.mes.in_(month))
        
            for row in consulta:
                lista = list()
                lista.append(row.legajo)
                lista.append(row.nombre_apellido)
                lista.append(row.ann)
                lista.append(row.mes)
                lista.append(row.importe)
                datos.append(lista)

        return datos

    except InterfaceError:
        print('No se abrio la base de datos.')

    except Exception as error:
        print(error)


def lectura_carfam(legajo: list, year: list, mes: list) -> list:

    """
    Lee los registros de la tabla cargasfamilia y los guarda en un array.
    """

    try:

        datos = list()

        if legajo[0] == '*':
            legajo = lista_empleados()

        if year[0] == '*':
            year = ['2021', '2022']

        if mes[0] != '*':
            
            mes_d = int(mes[0])
            mes_h = int(mes[0])
            
            lista_mes_d = list()
            lista_mes_h = list()

            while mes_h <= 12:
                lista_mes_h.append(str(mes_h))
                mes_h += 1

            while mes_d >= 1:
                lista_mes_d.append(str(mes_d))
                mes_d -= 1
            
            consulta = BaseDatos.CargasFamilia.select(BaseDatos.CargasFamilia.id, BaseDatos.CargasFamilia.legajo, BaseDatos.CargasFamilia.ann, 
            BaseDatos.CargasFamilia.cuil_empleado, BaseDatos.CargasFamilia.nro_doc, BaseDatos.CargasFamilia.apellido, BaseDatos.CargasFamilia.nombre, 
            BaseDatos.CargasFamilia.mes_desde, BaseDatos.CargasFamilia.mes_hasta, BaseDatos.CargasFamilia.porcentaje_deduccion, BaseDatos.CargasFamilia.parentesco).where(
            BaseDatos.CargasFamilia.legajo.in_(legajo), BaseDatos.CargasFamilia.ann.in_(year), 
            BaseDatos.CargasFamilia.mes_desde.in_(lista_mes_d), BaseDatos.CargasFamilia.mes_hasta.in_(lista_mes_h))

        else:
            consulta = BaseDatos.CargasFamilia.select(BaseDatos.CargasFamilia.id, BaseDatos.CargasFamilia.legajo, BaseDatos.CargasFamilia.ann, 
            BaseDatos.CargasFamilia.cuil_empleado, BaseDatos.CargasFamilia.nro_doc, BaseDatos.CargasFamilia.apellido, BaseDatos.CargasFamilia.nombre, 
            BaseDatos.CargasFamilia.mes_desde, BaseDatos.CargasFamilia.mes_hasta, BaseDatos.CargasFamilia.porcentaje_deduccion, BaseDatos.CargasFamilia.parentesco).where(
            BaseDatos.CargasFamilia.legajo.in_(legajo), BaseDatos.CargasFamilia.ann.in_(year)) 

        for row in consulta:
            lista = list()
            lista.append(row.id)
            lista.append(row.legajo)
            lista.append(row.ann)
            lista.append(row.cuil_empleado)
            lista.append(row.nro_doc)
            lista.append(row.apellido)
            lista.append(row.nombre)
            lista.append(row.mes_desde)
            lista.append(row.mes_hasta)
            lista.append(row.porcentaje_deduccion)
            lista.append(row.parentesco)
            datos.append(lista)
                
        return datos

    except InterfaceError:
        print('No se abrio la base de datos.')
    
    except Exception as error:
        print(error)


def lectura_remoe(legajo: list, month: list, year: list) -> list:

    """
    Lee los registros en la tabla gananciasoe y los guarda en un array.
    """
    try:

        datos = list()

        if legajo[0] == '*':
            legajo = lista_empleados()
        
        if year[0] == '*':
            year = ['2021', '2022']
        
        if month[0] == '*':
            month = ['1', '2', '3', '4' , '5', '6', '7', '8', '9', '10', '11', '12']
    

        consulta = BaseDatos.GananciasOE.select(BaseDatos.GananciasOE.id, BaseDatos.GananciasOE.legajo, BaseDatos.GananciasOE.ann, 
        BaseDatos.GananciasOE.cuil, BaseDatos.GananciasOE.denominacion, BaseDatos.GananciasOE.mes, BaseDatos.GananciasOE.gan_brut, 
        BaseDatos.GananciasOE.retrib_nohab, BaseDatos.GananciasOE.ajuste, BaseDatos.GananciasOE.exe_noalc, BaseDatos.GananciasOE.horas_extgr, 
        BaseDatos.GananciasOE.horas_extex, BaseDatos.GananciasOE.mat_did, BaseDatos.GananciasOE.gastos_movviat, 
        BaseDatos.GananciasOE.obra_soc, BaseDatos.GananciasOE.seg_soc, BaseDatos.GananciasOE.sind).where(
        BaseDatos.GananciasOE.legajo.in_(legajo), BaseDatos.GananciasOE.ann.in_(year), BaseDatos.GananciasOE.mes.in_(month))

        for row in consulta:
            lista = list()
            lista.append(row.id)
            lista.append(row.legajo)
            lista.append(row.ann)
            lista.append(row.cuil)
            lista.append(row.denominacion)
            lista.append(row.mes)
            lista.append(row.gan_brut)
            lista.append(row.retrib_nohab)
            lista.append(row.ajuste)
            lista.append(row.exe_noalc)
            lista.append(row.horas_extgr)
            lista.append(row.horas_extex)
            lista.append(row.mat_did)
            lista.append(row.gastos_movviat)
            lista.append(row.obra_soc)
            lista.append(row.seg_soc)
            lista.append(row.sind)
            datos.append(lista)

        return datos
    
    except InterfaceError:
        print('No se abrio la base de datos.')


    except Exception as error:
        print(error)


def visualiza_empleado(legajo: str) -> list:

    try:
        query = BaseDatos.Empleados.select(BaseDatos.Empleados.cuil, BaseDatos.Empleados.nombre_apellido, 
            BaseDatos.Empleados.fecha_ingreso).where(BaseDatos.Empleados.legajo == legajo)

        datos = list()

        for row in query:
            datos.append(legajo)
            datos.append(row.cuil)
            datos.append(row.nombre_apellido)
            datos.append(row.fecha_ingreso)

        return datos

    except InterfaceError:
        print('No se abrio la bbdd.')

    except TypeError:
        
        print('Posible error en bbdd.')
        
    except Exception as error:
        print(error)


def visualiza_rembruta(legajo, mes):
    
    try:
        query = BaseDatos.SueldosBrutos.select(BaseDatos.SueldosBrutos.importe).where(
                BaseDatos.SueldosBrutos.legajo == legajo, BaseDatos.SueldosBrutos.mes == mes)

        for row in query:
            importe = row.importe
    
        return importe

    except Exception as error:
        print(error)
        return 0



#Función que obtiene los datos para el formulario ver_deducciones.py
def visualiza_deducciones(legajo, mes):

    """
    Obtiene la información de un registro determinado desde el valor de la variable legajo.
    """
    try:
        query = BaseDatos.Deducciones.select(BaseDatos.Deducciones.importe).where(
                BaseDatos.Deducciones.legajo == legajo, BaseDatos.Deducciones.mes == mes)

        for row in query:
        
            importe = row.importe
    
        return importe

    except Exception as error:
        print(error)
        return 0

#Función que obtiene los datos para el formulario ver_carga_familia.py
def visualiza_cfam(id):

    """
    Obtiene la información de un registro determinado, de la tabla cargasfamilia, desde el valor de la variable id.
    """
    try:
        datos = list()

        query = BaseDatos.CargasFamilia.select(BaseDatos.CargasFamilia.legajo,BaseDatos.CargasFamilia.nro_doc, BaseDatos.CargasFamilia.apellido,
        BaseDatos.CargasFamilia.nombre, BaseDatos.CargasFamilia.mes_desde, BaseDatos.CargasFamilia.mes_hasta, BaseDatos.CargasFamilia.porcentaje_deduccion,
        BaseDatos.CargasFamilia.parentesco).where(BaseDatos.CargasFamilia.id == id)

        for row in query:
            datos.append(str(row.legajo))
            datos.append(str(row.nro_doc))
            datos.append(str(row.apellido))
            datos.append(str(row.nombre))
            datos.append(str(row.mes_desde))
            datos.append(str(row.mes_hasta))
            datos.append(str(row.porcentaje_deduccion))
            datos.append(str(row.parentesco))
    
        return datos
    
    except InterfaceError:
        print('Error en bbdd.')

    except Exception as error:
        print(error)
    
#Función que obtiene los datos para el formulario ver_ganancias_oe.py
def visualiza_ganoe(id):

    """
    Obtiene la información de un registro determinado, de la tabla gananciasoe, desde el valor de la variable id.
    """

    try:
        datos = list()

        query = BaseDatos.GananciasOE.select(BaseDatos.GananciasOE.legajo, BaseDatos.GananciasOE.denominacion, BaseDatos.GananciasOE.mes, BaseDatos.GananciasOE.gan_brut, BaseDatos.GananciasOE.retrib_nohab,
        BaseDatos.GananciasOE.ajuste, BaseDatos.GananciasOE.exe_noalc, BaseDatos.GananciasOE.horas_extgr, BaseDatos.GananciasOE.horas_extex, BaseDatos.GananciasOE.mat_did,
        BaseDatos.GananciasOE.gastos_movviat, BaseDatos.GananciasOE.obra_soc, BaseDatos.GananciasOE.seg_soc, BaseDatos.GananciasOE.sind).where(BaseDatos.GananciasOE.id == id)

        for row in query:
            datos.append(str(row.legajo))
            datos.append(str(row.denominacion))
            datos.append(str(row.mes))
            datos.append(str(row.gan_brut))
            datos.append(str(row.retrib_nohab))
            datos.append(str(row.ajuste))
            datos.append(str(row.exe_noalc))
            datos.append(str(row.horas_extgr))
            datos.append(str(row.horas_extex))
            datos.append(str(row.mat_did))
            datos.append(str(row.gastos_movviat))
            datos.append(str(row.obra_soc))
            datos.append(str(row.seg_soc))
            datos.append(str(row.sind))
    
        return datos
    
    except InterfaceError:
        print('Error en bbdd.')

    except Exception as error:
        print(error)

        
#Funciones para actualizar y eliminar registros de la tabla de empleados.
def actualiza_empleado(legajo, cuil, nom_ap, fec_ing):
    
    """
    Actualiza los datos de un empleado en la tabla. 
    legajo actualiza el campo legajo de la tabla empleados, cuil el campo cuil de la tabla empleados,
    nom_ap actualiza nombre_apellido y fec_ing actualiza fec_ing. 
    Si el procediemiento se realiza sin errores, devuelve True. Caso contrario, False.
    """

    try:
        actualizar  = BaseDatos.Empleados.update(cuil = cuil, nombre_apellido = nom_ap, 
                      fecha_ingreso = fec_ing).where(BaseDatos.Empleados.legajo == legajo)

        actualizar.execute()

        return True

    except Exception as error:
        print(error)
        return False
    

def elimina_empleado(legajo):

    """
    Elimina el registro seleccionado. Al realizar esta tarea, tambien se borran los registros relacionados 
    de las demas tablas. 
    Si el procediemiento se realiza sin errores, devuelve True. Caso contrario, False.
    """
    try:
        
        

        #Elimina el registro de la tabla empleados.
        elimina_emp = BaseDatos.Empleados.get(BaseDatos.Empleados.legajo == legajo)
        elimina_emp.delete_instance()
    
        #Elimina el registro de la tabla sueldosbrutos.
        query_rem = BaseDatos.SueldosBrutos.select(BaseDatos.SueldosBrutos.legajo == legajo)
        
        #Verifica que exista información en la query. 
        dato = None

        for row in query_rem:
            dato = row.legajo

        if dato != None:
            elimina_rem = BaseDatos.SueldosBrutos.get(BaseDatos.SueldosBrutos.legajo == legajo)
            elimina_rem.delete_instance()
    
        #Elimina el registro de la tabla deducciones.
        query_ded = BaseDatos.Deducciones.select(BaseDatos.Deducciones.legajo == legajo)
        
        #Verifica que exista información en la query. 
        dato = None
        
        for row in query_ded:
            dato = row.legajo
        
        if dato != None:
            elimina_ded = BaseDatos.Deducciones.get(BaseDatos.Deducciones.legajo == legajo)
            elimina_ded.delete_instance()
    
        #Elimina el registro de la tabla cargasfamilia.
        query_cfam = BaseDatos.CargasFamilia.select(BaseDatos.CargasFamilia.legajo == legajo)
        
        #Verifica que exista información en la query. 
        dato = None
        
        for row in query_cfam:
            dato = row.legajo
        
        if dato != None:
            elimina_cfam = BaseDatos.CargasFamilia.get(BaseDatos.CargasFamilia.legajo == legajo)
            elimina_cfam.delete_instance()
    
        #Elimina el registro de la tabla gananciasoe
        query_cfam = BaseDatos.GananciasOE.select(BaseDatos.GananciasOE.legajo == legajo)
        
        #Verifica que exista información en la query. 
        dato = None
        
        for row in query_cfam:
            dato = row.legajo
        
        if dato != None:
            elimina_gananoe = BaseDatos.GananciasOE.get(BaseDatos.GananciasOE.legajo == legajo)
            elimina_gananoe.delete_instance()

        return True

    except Exception as error:
        print(error)
        return False

    
#Funciones para actualizar y eliminar registros de la tabla de sueldosbrutos.
#############################################################################################################
def actualiza_sbruto(legajo, month, year, imp):

    """
    Realiza un update sobre la tabla sueldosbrutos. El primer campo es el legajo, por el cual se identifica
    el update. Luego recibe una lista con los valores a actualizar.
    Si el procediemiento se realiza sin errores, devuelve True. Caso contrario, False.
    """
    
    try:
        
        verifica = None

        query = BaseDatos.SueldosBrutos.select(BaseDatos.SueldosBrutos.importe).where(
                BaseDatos.SueldosBrutos.legajo == legajo, BaseDatos.SueldosBrutos.mes == month,
                BaseDatos.SueldosBrutos.ann == year)

        for row in query:
            verifica = row.importe

        if verifica == None:
        
            query_nombre = BaseDatos.Empleados.select(BaseDatos.Empleados.nombre_apellido).where(BaseDatos.Empleados.legajo == legajo)

            for row in query_nombre:
                nombre = row.nombre_apellido

            nuevo_registro = BaseDatos.SueldosBrutos()
            nuevo_registro.legajo = legajo
            nuevo_registro.nombre_apellido = nombre
            nuevo_registro.ann = year
            nuevo_registro.mes = month
            nuevo_registro.importe = imp
            nuevo_registro.save()

        else:
            actualizacion = BaseDatos.SueldosBrutos.update(importe = imp).where(
                            BaseDatos.SueldosBrutos.legajo == legajo, BaseDatos.SueldosBrutos.mes == month,
                            BaseDatos.SueldosBrutos.ann == year)

            actualizacion.execute()

        return True

    except Exception as error:
        print(error)
        return False
    
    
def elimina_sbruto(legajo, year):
    """
    Elimina un registro de la tabla sueldosbrutos.
    Si el procediemiento se realiza sin errores, devuelve True. Caso contrario, False.
    """

    try:

        registro = BaseDatos.SueldosBrutos.delete().where(BaseDatos.SueldosBrutos.legajo == legajo,
        BaseDatos.SueldosBrutos.ann == year)
        registro.execute()
        
        return True
    
    except Exception as error:
        print(error)
        return False


#Funciones para actualizar y eliminar registros de la tabla de deducciones.
#############################################################################################################
def actualiza_deducciones(legajo: str, month: str, year: str, imp: str) -> bool:

    """
    Realiza un update sobre la tabla deducciones. El primer campo es el legajo, por el cual se identifica
    el update. Luego recibe una lista con los valores a actualizar.
    Si el procediemiento se realiza sin errores, devuelve True. Caso contrario, False.
    """
    try:
    
        verifica = None

        query = BaseDatos.Deducciones.select(BaseDatos.Deducciones.importe).where(
                BaseDatos.Deducciones.legajo == legajo, BaseDatos.Deducciones.mes == month,
                BaseDatos.Deducciones.ann == year)
        
        for row in query:
            verifica = row.importe
        
        if verifica == None:

            query_nombre = BaseDatos.Empleados.select(BaseDatos.Empleados.nombre_apellido).where(
                           BaseDatos.Empleados.legajo == legajo)
            
            for row in query_nombre:
                nombre = row.nombre_apellido
        
            nuevo_registro = BaseDatos.Deducciones()
            nuevo_registro.legajo = legajo
            nuevo_registro.nombre_apellido = nombre
            nuevo_registro.ann = year
            nuevo_registro.mes = month
            nuevo_registro.importe = imp
            nuevo_registro.save()
        
        else:

            actualizacion = BaseDatos.Deducciones.update(importe = imp).where(
                            BaseDatos.Deducciones.legajo == legajo, BaseDatos.Deducciones.mes == month,
                            BaseDatos.Deducciones.ann == year)
            actualizacion.execute()

        return True
    
    except Exception as error:
        print(error)
        return False


def elimina_deducciones(legajo, year):
    """
    Elimina un registro de la tabla deducciones.
    Si el procediemiento se realiza sin errores, devuelve True. Caso contrario, False.
    """

    try:

        registro = BaseDatos.Deducciones.delete().where(BaseDatos.Deducciones.legajo == legajo, 
        BaseDatos.Deducciones.ann == year)
        registro.execute()
        
        return True
    
    except Exception as error:
        print(error)
        return False


#Funciones para actualizar y eliminar registros de la tabla de cargasfamilia.
def actualiza_cfam(id, *args):

    """
    Realiza un update sobre la tabla cargasfamilia. El primer campo es el id, por el cual se identifica
    el update. Luego recibe una lista con los valores a actualizar.
    Si el procediemiento se realiza sin errores, devuelve True. Caso contrario, False.
    """
    
    try:
        actualizacion = BaseDatos.CargasFamilia.update(nro_doc = args[0], apellido = args[1], nombre = args[2],
                        mes_desde = args[3], mes_hasta = args[4], porcentaje_deduccion = args[5],
                        parentesco = args[6]).where(BaseDatos.CargasFamilia.id == id)

        actualizacion.execute()

        return True
    
    
    except Exception as error:
        print(error)
        return False

    
    
def elimina_cfam(id):
    """
    Elimina un registro de la tabla cargasfamilia.
    Si el procediemiento se realiza sin errores, devuelve True. Caso contrario, False.
    """

    try:

        registro = BaseDatos.CargasFamilia.get(BaseDatos.CargasFamilia.id == id)
        registro.delete_instance()
        
        return True
    
    except Exception as error:
        print(error)
        return False


#Funciones para actualizar y eliminar registros de la tabla de gananciasoe.
def actualiza_ganoe(id, *args):

    """
    Realiza un update sobre la tabla gananciasoe. El primer campo es el id, por el cual se identifica
    el update. Luego recibe una lista con los valores a actualizar.
    Si el procediemiento se realiza sin errores, devuelve True. Caso contrario, False.
    """
    
    try:
        actualizacion = BaseDatos.GananciasOE.update(denominacion = args[0], gan_brut = args[1], retrib_nohab = args[2],
        ajuste = args[3], exe_noalc = args[4], horas_extgr = args[5], horas_extex = args[6], mat_did = args[7],
        gastos_movviat = args[8], obra_soc = args[9], seg_soc = args[10], sind = args[11]).where(BaseDatos.GananciasOE.id == id)
        
        actualizacion.execute()

        return True
    
    
    except Exception as error:
        print(error)
        return False
    
    
def elimina_ganoe(id):
    
    """
    Elimina un registro de la tabla cargasfamilia.
    Si el procediemiento se realiza sin errores, devuelve True. Caso contrario, False.
    """

    try:

        registro = BaseDatos.GananciasOE.get(BaseDatos.GananciasOE.id == id)
        registro.delete_instance()
        
        return True
    
    except Exception as error:
        print(error)
        return False



def borra_contenido(tabla: str, month: list, year: list) -> bool:
    
    try:

        if year[0] == '*':
            year = ['2021', '2022']
        
        if month[0] == '*':
            month = ['1', '2', '3', '4' , '5', '6', '7', '8', '9', '10', '11', '12']

        if tabla == 'Remuneraciones':

            query = BaseDatos.SueldosBrutos.delete().where(BaseDatos.SueldosBrutos.mes.in_(month),
                    BaseDatos.SueldosBrutos.ann.in_(year))

            query.execute()

            return True

        if tabla == 'Deducciones':
            
            query = BaseDatos.Deducciones.delete().where(BaseDatos.Deducciones.mes.in_(month),
                    BaseDatos.Deducciones.ann.in_(year))
            
            query.execute()

            return True

        if tabla == 'Cargas de familia':

            query = BaseDatos.CargasFamilia.delete().where(BaseDatos.CargasFamilia.ann.in_(year))
            
            query.execute()
            
            return True

        if tabla == 'Ganancias otros empleadores':
            
            query = BaseDatos.GananciasOE.delete().where(BaseDatos.GananciasOE.mes.in_(month),
            BaseDatos.GananciasOE.ann.in_(year))
            
            query.execute()
            
            return True

        if tabla == 'Promedio bruto':
    
            query = BaseDatos.PromedioBruto.delete().where(BaseDatos.PromedioBruto.mes.in_(month),
                    BaseDatos.PromedioBruto.ann.in_(year))
    
            query.execute()
    
            return True

        if tabla == 'Ded. Esp. Inc. Primera parte':
    
            query = BaseDatos.PrimerParrafo.delete().where(BaseDatos.PrimerParrafo.mes.in_(month),
                    BaseDatos.PrimerParrafo.ann.in_(year))
    
            query.execute()
    
            return True

        if tabla == 'Ded. Esp. Inc. Segunda parte':
    
            query = BaseDatos.SegundoParrafo.delete().where(BaseDatos.SegundoParrafo.mes.in_(month),
                    BaseDatos.SegundoParrafo.ann.in_(year))
            
            query.execute()
    
            return True

    except Exception as error:
        print(error)
        return False


#Lectura de la tabla divisor
################################################################################################################

def lectura_divisor() -> list:

    try:
        resultado = list()
        query = BaseDatos.Divisor.select(BaseDatos.Divisor.id, BaseDatos.Divisor.legajo, BaseDatos.Divisor.ann,
                BaseDatos.Divisor.mes, BaseDatos.Divisor.divisor)

        for row in query:
            lista = list()
            lista.append(row.id)
            lista.append(row.legajo)
            lista.append(row.ann)
            lista.append(row.mes)
            lista.append(row.divisor)
            resultado.append(lista)

        return resultado

    except Exception as error:
        print(error)


def leer_reg_divisor(id: int) -> list:

   try:

       resultado = list()
        
       query = BaseDatos.Divisor.select(BaseDatos.Divisor.legajo, BaseDatos.Divisor.ann,
               BaseDatos.Divisor.mes, BaseDatos.Divisor.divisor).where(BaseDatos.Divisor.id == id)
        
       for row in query:
            resultado.append(row.legajo)
            resultado.append(row.ann)
            resultado.append(row.mes)
            resultado.append(row.divisor)
        
       return resultado
    
   except Exception as error:
        print(error)


def actualizar_divisor(id: int, legajo: int, ann: int, mes: int, divisor: int) -> bool:

    try:

        query = BaseDatos.Divisor.update(legajo = legajo, ann = ann, mes = mes, divisor = divisor).where(
                BaseDatos.Divisor.id == id)
        query.execute()

        return True

    except Exception as error:
        print(error)
        return False


def elimina_divisor(id: int) -> bool:

    try:

        query = BaseDatos.Divisor.delete().where(BaseDatos.Divisor.id == id)
        query.execute()

        return True

    except Exception as error:
        print(error)
        return False
