#Módulo perteneciente al modelo. 
#Contiene todas las funciones de creación de base de datos e importación de información 
#desde archivos ".xlsx" o ".xml"

from pandas import read_excel
from pandas import DataFrame
from peewee import SqliteDatabase
from peewee import Model
from peewee import CharField
from peewee import DateField
from peewee import IntegerField
from peewee import FloatField
from peewee import TextField
from peewee import IntegrityError
from xml.dom import minidom
from errores import ExisteFamiliar 
from errores import ExisteLegajo
from errores import ExisteRegistro
from errores import NoExisteLegajo
import os
import time

###########################################################################################################
#Bases de datos propias del sistema.

try:
    
    config = SqliteDatabase('bbdd/config.db')

    class BaseModel(Model):
    
        class Meta:
    
            database = config

    class DeduccionesPersonales(BaseModel):
        year = IntegerField()
        tipo = TextField()
        importe = FloatField()

    class RangoSegundoParrafo (BaseModel):
        resolucion = TextField()
        val_min = FloatField()
        val_max = FloatField()
        deduccion = FloatField()

    class ParametrosGananciasOE(BaseModel):
        
        """
        1 = True.
        2 = False.
        """
        
        item = TextField()
        valor = IntegerField()

    config.connect()
    config.create_tables([DeduccionesPersonales, RangoSegundoParrafo, ParametrosGananciasOE])
    
except:
    pass


###########################################################################################################
#Funciones para configurar los parametros correspondientes a otras deducciones.

def lee_par_gananoe(item: str) -> int:
    
    query = ParametrosGananciasOE.select(ParametrosGananciasOE.valor).where(ParametrosGananciasOE.item == item)

    for row in query:
        valor = row.valor

    return valor


def actualiza_par_gananoe(item: str, valor: int):

    query = ParametrosGananciasOE.update(valor = valor).where(ParametrosGananciasOE.item == item)
    query.execute()


###########################################################################################################
#Actualiza los valores de la tabla RangoSegundoParrafo 
def lee_rangosegundoparrafo(archivo: str) -> bool:

    try:

        excel_file = read_excel(archivo)

        _resolucion = excel_file['resolucion'].values
        _val_min = excel_file['valor minimo'].values
        _val_max = excel_file['valor maximo'].values
        _deduccion = excel_file['deduccion'].values

        diccionario = {'Resolución': [],
                   'Valor mínimo': [],
                   'Valor máximo': [],
                   'Deducción': []}

        diccionario['Resolución'] = _resolucion
        diccionario['Valor mínimo'] = _val_min
        diccionario['Valor máximo'] = _val_max
        diccionario['Deducción'] = _deduccion

        datos = DataFrame(diccionario, columns=['Resolución', 'Valor mínimo', 'Valor máximo', 'Deducción'])

        return datos

    except:
        pass

def borra_dedsparrafo(resolucion: str):

    query = RangoSegundoParrafo.delete().where(RangoSegundoParrafo.resolucion == resolucion)
    query.execute()


def guarda_dedsparrafo(*args):

    rango = RangoSegundoParrafo()
    rango.resolucion = args[0]
    rango.val_min = args[1]
    rango.val_max = args[2]
    rango.deduccion = args[3]
    rango.save()
    

###########################################################################################################
#Bases de datos correspondientes al procedimiento de liquidación

base_datos = SqliteDatabase(None)

class BaseDatos():

    def __init__ (self, directorio):
        self.directorio = directorio  

    def arbir_bbdd(self):    
        global base_datos
        base_datos.init(self.directorio, pragmas={'foreign_keys': 1})
        base_datos.connect()
        
    def nueva_bbdd(self):
        global base_datos
        base_datos.init(self.directorio, pragmas={'foreign_keys': 1})
        base_datos.connect()
        base_datos.create_tables([BaseDatos.Empleados, BaseDatos.SueldosBrutos, BaseDatos.Deducciones,
        BaseDatos.CargasFamilia, BaseDatos.GananciasOE, BaseDatos.PromedioBruto, BaseDatos.PrimerParrafo,
        BaseDatos.SegundoParrafo, BaseDatos.Divisor])

    class BaseModel(Model):
    
        class Meta:
            global base_datos
            database = base_datos

    class Empleados (BaseModel):
        legajo =  IntegerField()
        cuil = IntegerField()
        nombre_apellido = TextField()
        fecha_ingreso = DateField()

    class SueldosBrutos(BaseModel):
        legajo = IntegerField()
        nombre_apellido = TextField()
        ann = IntegerField()
        mes = IntegerField()
        importe = FloatField()
        
    class Deducciones(BaseModel):
        legajo = IntegerField()
        nombre_apellido = TextField()
        ann = IntegerField()
        mes = IntegerField()
        importe = FloatField()
        
    class CargasFamilia(BaseModel):
        legajo = IntegerField()
        ann = IntegerField()
        cuil_empleado = IntegerField()
        tipo_doc = IntegerField()
        nro_doc = IntegerField()
        apellido = TextField()
        nombre = TextField()
        fecha_nac = DateField()
        mes_desde = CharField()
        mes_hasta = CharField()
        parentesco = CharField()
        porcentaje_deduccion = CharField()

    class GananciasOE(BaseModel):
        legajo = IntegerField()
        ann = IntegerField()
        cuil = IntegerField()
        cuit = IntegerField()
        denominacion = TextField()
        mes = IntegerField()
        obra_soc = FloatField()
        seg_soc = FloatField()
        sind = FloatField()
        gan_brut = FloatField()
        ret_gan = FloatField()
        retrib_nohab = FloatField()
        ajuste = FloatField()
        exe_noalc = FloatField()
        sac = FloatField()
        horas_extgr = FloatField()
        horas_extex = FloatField()
        mat_did = FloatField()
        gastos_movviat = FloatField()

    class PromedioBruto(BaseModel):
        legajo = IntegerField()
        ann = IntegerField()
        mes = IntegerField()
        importe = FloatField()

    class PrimerParrafo(BaseModel):
        legajo = IntegerField()
        ann = IntegerField()
        mes = IntegerField()
        sbruto = FloatField()
        deducciones = FloatField()
        ded_esp = FloatField()
        min_no_imp = FloatField()
        cargas_familia = FloatField()
        ded_p_parrafo = FloatField()

    class SegundoParrafo(BaseModel):
        legajo = IntegerField()
        ann = IntegerField()
        mes = IntegerField()
        ded_s_parrafo = FloatField()

    class Divisor(BaseModel):
        legajo = IntegerField()
        ann = IntegerField()
        mes = IntegerField()
        divisor = IntegerField()


###########################################################################################################
#Obtiene la hora actual del sistema.
def obtiene_fecha():

    return time.strftime('%Y-%m-%d', time.localtime())

###########################################################################################################
#Validación de errores.
def existe_legajo(legajo):

    """
    Busca el legajo en la tabla empleados. Retorna una variable de tipo boolean-
    """
    
    resultado = None

    query = BaseDatos.Empleados.select(BaseDatos.Empleados.legajo).where(BaseDatos.Empleados.legajo == legajo)

    for row in query:

        resultado = row.legajo

    if resultado != None:
        return True

    else:
        return False

def existe_registro(legajo, mes, y, tabla):

    """
    Busca el legajo en la tabla de deducciones o remuneraciones (segín lo indicado en parámetro tabla).
    Retorna una variable de tipo boolean
    """
    resultado = None

    if tabla == 'deduc':
        
        query = BaseDatos.Deducciones.select(BaseDatos.Deducciones.legajo).where(
                BaseDatos.Deducciones.legajo == legajo, BaseDatos.Deducciones.mes == mes,
                BaseDatos.Deducciones.ann == y)

        for row in query:

            resultado = row.legajo

        if resultado != None:
            return True

        else:
            return False

    if tabla == 'remu':
    
        query = BaseDatos.SueldosBrutos.select(BaseDatos.SueldosBrutos.legajo).where(
            BaseDatos.SueldosBrutos.legajo == legajo, BaseDatos.SueldosBrutos.mes == mes, 
            BaseDatos.SueldosBrutos.ann == y)
        
        for row in query:
            resultado = row.legajo

        if resultado != None:
            return True

        else:
            return False

def existe_familiar(legajo, documento):
    
    """
    Verifica si un familiar existe en la tabla de cargas familiares.
    """

    resultado = None

    query = BaseDatos.CargasFamilia.select(BaseDatos.CargasFamilia.nro_doc).where(
            BaseDatos.CargasFamilia.legajo == legajo, BaseDatos.CargasFamilia.nro_doc == documento)

    for row in query:
        resultado = row.nro_doc

    if resultado != None:
        return True

    else:
        return False 

def existe_ganancia(legajo, cuit, mes, y):

    """
    Verifica si existe un registro en la tabla de gananciasoe, para un mes y cuit determinado. 
    Arroja resultado de tipo boolean.
    """

    resultado = None

    query = BaseDatos.GananciasOE.select(BaseDatos.GananciasOE.legajo).where(BaseDatos.GananciasOE.legajo == legajo,
    BaseDatos.GananciasOE.cuit == cuit, BaseDatos.GananciasOE.mes == mes, BaseDatos.GananciasOE.ann == y)

    for row in query:
        resultado = row.legajo

    if resultado != None:
        return True

    else:
        return False


#Comienzo de las funciones para importar información al sistema.
##############################################################################################################


#Importación de empleados.
##############################################################################################################
def lee_empleados(archivo):

    """
    Función que importa, desde un archivo ".xlsx", los datos para la tabla empleados.
    """
    
    try:

        #Lee el archivo xlsx.
        excel_file = read_excel(archivo)

        _legajo = excel_file['legajo'].values
        _cuil = excel_file['cuil'].values
        _nombre_apellido = excel_file['nombre y apellido'].values
        _fecha_ingreso = excel_file['fecha ingreso'].values

        #Diccionario para el Dataframe
        diccionario_empleado = {
            'Legajo' : [],
            'CUIL' : [],
            'Nombre y apellido' : [],
            'Fecha de ingreso' : []
        }

        #Guarda los datos en el diccionario.
        diccionario_empleado['Legajo'] = _legajo
        diccionario_empleado['CUIL'] = _cuil
        diccionario_empleado['Nombre y apellido'] = _nombre_apellido
        diccionario_empleado['Fecha de ingreso'] = _fecha_ingreso

        #Genera el Dataframe.
        array_empleado = DataFrame(diccionario_empleado, 
                                   columns=['Legajo', 'CUIL', 'Nombre y apellido', 'Fecha de ingreso'])  

        return array_empleado     
    
    except Exception as error:
        print(error)


def guarda_empleado(*args):

    """Guarda los datos en la tabla empleados."""

    try:

        if existe_legajo(args[0]) == True:
            raise ExisteLegajo

        empleado = BaseDatos.Empleados()
        empleado.legajo = args[0]
        empleado.cuil = args[1]
        empleado.nombre_apellido = args[2]
        empleado.fecha_ingreso = args[3]
        empleado.save()

    except ExisteLegajo:
        txt = open('logs/update_empleado.txt', 'a')
        txt.write(f'El legajo {args[0]} ya existe en la base de datos. No se realiza el insert.\n')
        txt.close()


#Funciones para leer el archivo de remuneraciones y deducciones y guardar los datos en un archivo
##############################################################################################################
def sueldos_brutos_deducciones(archivo):
    
    """
    Carga, desde un archivo con extensión ".xlsx", los datos a la tabla remuneraciones (o deducciones). 
    La variable archivo contiene la información correspondiente al archivo con extensión ".xlsx".
    """

    #Lee la información desde el archivo seleccionado.
    excel_file = read_excel(archivo)

    _legajo = excel_file['legajo'].values
    _nombre_apellido = excel_file['nombre y apellido'].values
    _ann = excel_file['año'].values
    _mes = excel_file['mes'].values
    _importe = excel_file['importe'].values

    #Genera el diccionario para el Dataframe.
    diccionario_import = {
        'Legajo' : [],
        'Nombre y apellido' : [],
        'Año': [],
        'Mes' : [],
        'Importe' : [],
    }

    diccionario_import['Legajo'] = _legajo
    diccionario_import['Nombre y apellido'] = _nombre_apellido
    diccionario_import['Año'] = _ann
    diccionario_import['Mes'] = _mes
    diccionario_import['Importe'] = _importe

    #Dataframe.
    array_empleado = DataFrame(diccionario_import, columns=['Legajo', 'Nombre y apellido', 'Año', 'Mes', 'Importe'])

    return array_empleado
    

#Sueldo bruto
##############################################################################################################
def guarda_sbruto(*args):

    """
    Guarda en la base de datos (tabla sueldobrutos) los registros enviados mediante el parametro *args.
    """
    try:

        hora = str(obtiene_fecha())

        # Valida que exista el legajo en la base de datos.
        if existe_legajo(args[0]) == False:
            raise NoExisteLegajo

        # Valida que no exista un registro en la tabla sueldosbruto 
        # para el legajo a cargar.
        if existe_registro(args[0], args[3], args[2], 'remu')   == True:
            raise ExisteRegistro

        # Valida que los campos sean números.
        float(args[4])
        
        #Guarda los datos en la base.
        sueldo_bruto = BaseDatos.SueldosBrutos()
        sueldo_bruto.legajo = args[0]
        sueldo_bruto.nombre_apellido = args[1]
        sueldo_bruto.mes = args[3]
        sueldo_bruto.ann = args[2]
        sueldo_bruto.importe = args[4]
        sueldo_bruto.save()
        
    #Manejo de excepciones.
    except NoExisteLegajo:
        txt = open(f'logs/insert_sueldobruto {hora}.txt', 'a')
        txt.write(f'El legajo {args[0]} no existe dentro de la tabla de empleados. No se realiza el insert.\n')
        txt.close()

    except ExisteRegistro:
        txt = open(f'logs/insert_sueldobruto {hora}.txt', 'a')
        txt.write(f'Ya existe un registro para el legajo {args[0]}. No se realiza el insert.\n')
        txt.close()

    except TypeError:
        txt = open(f'logs/insert_sueldobruto {hora}.txt', 'a')
        txt.write(f'El legajo {args[0]} contiene en sus filas valores no numericos. No se realiza el insert.\n')
        txt.close()

    except IntegrityError:
        txt = open(f'logs/insert_sueldobruto {hora}.txt', 'a')
        txt.write(f'El legajo {args[0]} no posee todos los campos requeridos. No se realiza el insert.\n')
        txt.close()


#Deducciones    
##############################################################################################################
def guarda_deducciones(*args):

    """
    Guarda en la base de datos (tabla sueldobrutos) los registros enviados mediante el parametro *args.
    """

    try:
        hora = str(obtiene_fecha())
        
        # Valida que exista el legajo en la base de datos.
        if existe_legajo(args[0]) == False:
            raise NoExisteLegajo
        
        # Valida que no exista un registro en la tabla sueldosbru
        # para el legajo a cargar.
        if existe_registro(args[0], args[3], args[2], 'deduc') == True:
            raise ExisteRegistro

        #Guarda los datos en la base.
        deducciones = BaseDatos.Deducciones()
        deducciones.legajo = args[0]
        deducciones.nombre_apellido = args[1]
        deducciones.mes = args[3]
        deducciones.ann = args[2]
        deducciones.importe = args[4]
        deducciones.save()

    #Manejo de excepciones.
    except NoExisteLegajo:
        txt = open(f'logs/insert_deducciones {hora}.txt', 'a')
        txt.write(f'El legajo {args[0]} no existe dentro de la tabla de empleados. No se realiza el insert.\n')
        txt.close()

    except ExisteRegistro:
        txt = open(f'logs/insert_deducciones {hora}.txt', 'a')
        txt.write(f'Ya existe un registro para el legajo {args[0]}. No se realiza el insert.\n')
        txt.close()

    except TypeError:
        txt = open(f'logs/insert_deducciones {hora}.txt', 'a')
        txt.write(f'El legajo {args[0]} contiene en sus filas valores no numericos. No se realiza el insert.\n')
        txt.close()

    except IntegrityError:
        txt = open(f'logs/insert_sueldobruto {hora}.txt', 'a')
        txt.write(f'El legajo {args[0]} no posee todos los campos requeridos. No se realiza el insert.\n')
        txt.close()


#Funciones para las tablas cargas familiares y ganancias otros empleos.
##############################################################################################################
def leer_directorio(directorio):
    
    """
    Lee los archivos xml existentes en un directorio.
    """
    archivos = os.scandir(directorio)

    xml_file = []

    for i in archivos:
        if i.name.endswith('.xml'):
            xml_file.append(i.path)

    return xml_file


#Lectura de formularios 572 del item cargas de familia.
##############################################################################################################
def lee_familiares_xml(archivo):

    """
    Lee un archivo, con extensión xml y retorno la información obtendia mediante un array.
    """
    hora = obtiene_fecha()

    try:
        documento_xml = minidom.parse(archivo)
        presentacion = documento_xml.getElementsByTagName('presentacion')
        carga_familia = documento_xml.getElementsByTagName('cargaFamilia')

        array_presentacion = list()
        resultado = list()

    
        for child_node in presentacion:
            
            #Inicia las variables.
            periodo = ''
            cuit = '' 

            if child_node.getElementsByTagName('periodo'):
                periodo = child_node.getElementsByTagName('periodo')

            if child_node.getElementsByTagName('empleado'):
            
                for child in child_node.getElementsByTagName('empleado'):
                
                    if child.getElementsByTagName('cuit'):
                        cuit = child.getElementsByTagName('cuit')

            if cuit!="":
                array_presentacion.append(cuit[0].childNodes[0].data)
            else:
                array_presentacion.append(" ") 

            if periodo!="":
                array_presentacion.append(periodo[0].childNodes[0].data)
            else:
                array_presentacion.append(" ")

        for child_node in carga_familia:

            new_array = list()

            tipo_doc=''
            nro_doc=''
            apellido=''
            nombre=''
            fecha_nac=''
            mes_desde=''
            mes_hasta=''
            parentesco=''
            porcentaje_deduccion=''

            if child_node.getElementsByTagName('tipoDoc'):
                tipo_doc = child_node.getElementsByTagName('tipoDoc')
           
            if child_node.getElementsByTagName('nroDoc'):
                nro_doc = child_node.getElementsByTagName('nroDoc')
           
            if child_node.getElementsByTagName('apellido'):
                apellido = child_node.getElementsByTagName('apellido')
           
            if child_node.getElementsByTagName('nombre'):
                nombre = child_node.getElementsByTagName('nombre')
           
            if child_node.getElementsByTagName('fechaNac'):
                fecha_nac = child_node.getElementsByTagName('fechaNac')
           
            if child_node.getElementsByTagName('mesDesde'):
                mes_desde = child_node.getElementsByTagName('mesDesde')
           
            if child_node.getElementsByTagName('mesHasta'):
                mes_hasta = child_node.getElementsByTagName('mesHasta')
           
            if child_node.getElementsByTagName('parentesco'):
                parentesco = child_node.getElementsByTagName('parentesco')
        
            if child_node.getElementsByTagName('porcentajeDeduccion'):
                porcentaje_deduccion = child_node.getElementsByTagName('porcentajeDeduccion')
        
            for i in array_presentacion:
                new_array.append(i)

            if len(str(tipo_doc)) > 1:
                new_array.append(tipo_doc[0].childNodes[0].data)
            else:
                new_array.append(' ')
            
            if len(str(nro_doc)) > 1:
                new_array.append(nro_doc[0].childNodes[0].data)
            else:
                new_array.append(' ')
            
            if len(str(apellido)) > 1:
                new_array.append(apellido[0].childNodes[0].data)
            else:
                new_array.append(' ')
            
            try:
                if len(str(nombre)) > 1 :
                    new_array.append(nombre[0].childNodes[0].data)
            except: 
                new_array.append(' ')

            if len(str(fecha_nac)) > 1:
                new_array.append(fecha_nac[0].childNodes[0].data)
            else:
                new_array.append(' ')
            
            if mes_desde!='':
                new_array.append(mes_desde[0].childNodes[0].data)
            else:
                new_array.append(' ')
            
            if mes_hasta != '':
                new_array.append(mes_hasta[0].childNodes[0].data)
            else:
                new_array.append(' ')
            
            if parentesco!='':
                new_array.append(parentesco[0].childNodes[0].data)
            else:
                new_array.append(' ')
            
            if len(str(porcentaje_deduccion)) > 1:
                new_array.append(porcentaje_deduccion[0].childNodes[0].data)
            else:
                new_array.append(' ')

            legajos = BaseDatos.Empleados.select(BaseDatos.Empleados.legajo).where(BaseDatos.Empleados.cuil == new_array[0])

            for leg in legajos:
                legajo = leg.legajo

                if existe_legajo(legajo) == False:
                    raise NoExisteLegajo
                else:
                    new_array.append(legajo)

            resultado.append(new_array)

        return resultado 

    except NoExisteLegajo:

        txt = open(f'logs/insert_cargasfam {hora}.txt', 'a')
        txt.write(f'No existe legajo para el cuil {new_array[0]} dentro de la tabla de empleados. No se realiza el insert.\n')
        txt.close()
        

def lee_familiares_xlsx(archivo):
    
    """
    Lee la información obtenida desde un archivo, con extensión xlsx, y devuelve la información en un array. 
    La variable archivo contiene la información correspondiente al archivo con extensión ".xlsx".
    """
    try:

        hora = obtiene_fecha()

        #Lee la información desde el archivo seleccionado.
        excel_file = read_excel(archivo)

        _legajo = excel_file['legajo'].values
        _cuil_empleado = excel_file['cuil empleado'].values
        _ann = excel_file['año'].values
        _tipo_doc = excel_file['tipo doc'].values
        _nro_doc = excel_file['nro doc'].values
        _apellido = excel_file['apellido'].values
        _nombre = excel_file['nombre'].values
        _fecha_nac = excel_file['fecha nac'].values
        _mes_desde = excel_file['mes desde'].values
        _mes_hasta = excel_file['mes hasta'].values
        _parentesco = excel_file['parentesco'].values
        _porcentaje_deduccion = excel_file['porcentaje deduccion'].values
    
        #Genera el diccionario para el Dataframe.
        diccionario_import = {
            'Cuil empleado' : [],
            'Año' : [],
            'Tipo doc' : [],
            'Nro doc' : [],
            'Apellido' : [],
            'Nombre' : [],
            'Fecha nac' : [],
            'Mes desde' : [],
            'Mes hasta' : [],
            'Parentesco' : [],
		    'Porcentaje deduccion' : [],
            'Legajo' : []
        }

        diccionario_import['Legajo'] = _legajo
        diccionario_import['Cuil empleado'] = _cuil_empleado
        diccionario_import['Año'] = _ann
        diccionario_import['Tipo doc'] = _tipo_doc
        diccionario_import['Nro doc'] = _nro_doc
        diccionario_import['Apellido'] = _apellido
        diccionario_import['Nombre'] = _nombre
        diccionario_import['Fecha nac'] = _fecha_nac
        diccionario_import['Mes desde'] = _mes_desde
        diccionario_import['Mes hasta'] = _mes_hasta
        diccionario_import['Parentesco'] = _parentesco
        diccionario_import['Porcentaje deduccion'] = _porcentaje_deduccion
    
        #Dataframe.
        array_empleado = DataFrame(diccionario_import, columns=['Cuil empleado', 'Año', 'Tipo doc', 'Nro doc',
                        'Apellido', 'Nombre', 'Fecha nac', 'Mes desde', 'Mes hasta', 'Parentesco', 
                        'Porcentaje deduccion', 'Legajo'])

        return array_empleado

    except KeyError:
        txt = open(f'logs/insert_cargasfam {hora}.txt', 'a')
        txt.write(f'Error en lectura de archivo xlsx. No se realiza el insert.\n')
        txt.close()


def guarda_familiar(*args):

    """
    Guarda los registros obtenidos, a partir del parametro *args, dentro de la tabla cargasfamilia 
    """
    
    try:

        hora = obtiene_fecha()

        if existe_legajo(args[11]) == False:
            raise NoExisteLegajo

        if existe_familiar(args[11], args[3]) == True:
            raise ExisteFamiliar

        if len(args) != 12:
            raise IndexError

        carga_familia = BaseDatos.CargasFamilia()
        carga_familia.legajo = args[11]
        carga_familia.cuil_empleado = args[0]
        carga_familia.ann = args[1]
        carga_familia.tipo_doc = args[2]
        carga_familia.nro_doc = args[3]
        carga_familia.apellido = args[4]
        carga_familia.nombre = args[5]
        carga_familia.fecha_nac = args[6]
        carga_familia.mes_desde = args[7]
        carga_familia.mes_hasta = args[8]
        carga_familia.parentesco = args[9]
        carga_familia.porcentaje_deduccion = args[10]
        carga_familia.save()
        
    except NoExisteLegajo:

        txt = open(f'logs/insert_cargasfam {hora}.txt', 'a')
        txt.write(f'El legajo {args[11]} no existe dentro de la tabla de empleados. No se realiza el insert.\n')
        txt.close()

    except ExisteFamiliar:
        txt = open(f'logs/insert_cargasfam {hora}.txt', 'a')
        txt.write(f'El legajo {args[11]} ya contiene un familiar con el numero de documento {args[3]}. No se realiza el insert.\n')
        txt.close()
    
    except IndexError:
        txt = open(f'logs/insert_cargasfam {hora}.txt', 'a')
        txt.write(f'Error en la lectura del xml {args[0]}. Revisar que exista un legajo asociado para el número de cuil.\n')
        txt.close()

    except IntegrityError:
        txt = open(f'logs/insert_cargasfam {hora}.txt', 'a')
        txt.write(f'Faltan campos obligatorios en legajo {args[11]}. No se realiza el insert.\n')
        txt.close()
    


#Ganancias otros empleadores.
##############################################################################################################
def lee_gananoe_xml(archivo):

    """
    Lee la información, correspondiente al campo, ganancias otros empleos del formulario 572.
    """
    hora = obtiene_fecha()
    
    try:
        documento_xml = minidom.parse(archivo)
        presentacion = documento_xml.getElementsByTagName('presentacion')
        otros_empleos = documento_xml.getElementsByTagName('empEnt')

        array_presentacion = list()
        resultado = list()
    
        #Lee los datos de la presentación del formulario 572.
        for child_node in presentacion:
            
            #Inicialización de variables.
            periodo=''
            cuit = '' 

            if child_node.getElementsByTagName('periodo'):
                periodo = child_node.getElementsByTagName('periodo')

            if child_node.getElementsByTagName('empleado'):
            
                for child in child_node.getElementsByTagName('empleado'):
                
                    if child.getElementsByTagName('cuit'):
                        cuit = child.getElementsByTagName('cuit')

            if cuit!="":
                array_presentacion.append(cuit[0].childNodes[0].data)
            else:
                array_presentacion.append(" ") 
            
            if periodo!="":
                array_presentacion.append(periodo[0].childNodes[0].data)
            else:
                array_presentacion.append(" ")
                
        #Primer bucle.
        for child_node in otros_empleos:

            array_titulo = list()
            
            cuit=''
            denominacion=''
            mes=''
            obraSoc=''
            segSoc=''
            sind=''
            ganBrut=''
            retGan=''
            retribNoHab=''
            ajuste=''
            exeNoAlc=''
            sac=''
            horasExtGr=''
            horasExtEx=''
            matDid=''
            gastosMovViat=''
    
            if child_node.getElementsByTagName('cuit'):
                cuit = child_node.getElementsByTagName('cuit')
                
            if child_node.getElementsByTagName('denominacion'):
                denominacion = child_node.getElementsByTagName('denominacion')
            
            if len(str(cuit)) > 1:
                array_titulo.append(cuit[0].childNodes[0].data)
            else:
                array_titulo.append('-')
                
            if len(str(denominacion)) > 1:
                array_titulo.append(denominacion[0].childNodes[0].data)
            else:
                array_titulo.append('-')

            #Bucle para recorrer los valores mensuales
        
            for c_child in child_node.getElementsByTagName('ingAp'):

                array_mes = list()
                
                if c_child.getAttribute('mes'):
                    mes = c_child.getAttribute('mes')
                                   
                if c_child.getElementsByTagName('obraSoc'):
                    obraSoc = c_child.getElementsByTagName('obraSoc')
                       
                if c_child.getElementsByTagName('segSoc'):
                    segSoc = c_child.getElementsByTagName('segSoc')
                       
                if c_child.getElementsByTagName('sind'):
                    sind = c_child.getElementsByTagName('sind')   
                       
                if c_child.getElementsByTagName('ganBrut'):
                    ganBrut = c_child.getElementsByTagName('ganBrut')
                       
                if c_child.getElementsByTagName('retGan'):
                    retGan = c_child.getElementsByTagName('retGan')  
                       
                if c_child.getElementsByTagName('retribNoHab'):
                    retribNoHab = c_child.getElementsByTagName('retribNoHab')   
                    
                if c_child.getElementsByTagName('ajuste'):
                    ajuste = c_child.getElementsByTagName('ajuste')   
                       
                if c_child.getElementsByTagName('exeNoAlc'):
                    exeNoAlc = c_child.getElementsByTagName('exeNoAlc')  
                       
                if c_child.getElementsByTagName('sac'):
                    sac = c_child.getElementsByTagName('sac')
                       
                if c_child.getElementsByTagName('horasExtGr'):
                    horasExtGr = c_child.getElementsByTagName('horasExtGr')
                       
                if c_child.getElementsByTagName('horasExtEx'):
                    horasExtEx = c_child.getElementsByTagName('horasExtEx') 
                       
                if c_child.getElementsByTagName('matDid'):
                    matDid = c_child.getElementsByTagName('matDid')
                       
                if c_child.getElementsByTagName('gastosMovViat'):
                    gastosMovViat = c_child.getElementsByTagName('gastosMovViat')   

                for i in array_presentacion:
                    array_mes.append(i)

                for i in array_titulo:
                    array_mes.append(i)

                if mes != '':
                    array_mes.append(mes)
                else:
                    array_mes.append('error')
                    
                if len(str(obraSoc)) > 1:
                    array_mes.append(obraSoc[0].childNodes[0].data) 
                else:
                    array_mes.append(0)
                    
                if len(str(segSoc)) > 1:
                    array_mes.append(segSoc[0].childNodes[0].data) 
                else:
                    array_mes.append(0)
                    
                if len(str(sind)) > 1:
                    array_mes.append(sind[0].childNodes[0].data) 
                else:
                    array_mes.append(0)  
                    
                if len(str(ganBrut)) > 1:
                    array_mes.append(ganBrut[0].childNodes[0].data) 
                else:
                    array_mes.append(0)
                    
                if len(str(retGan)) > 1:
                    array_mes.append(retGan[0].childNodes[0].data) 
                else:
                    array_mes.append(0)
                    
                if len(str(retribNoHab)) > 1:
                    array_mes.append(retribNoHab[0].childNodes[0].data) 
                else:
                    array_mes.append(0)
                    
                if len(str(ajuste)) > 1:
                    array_mes.append(ajuste[0].childNodes[0].data) 
                else:
                    array_mes.append(0)
                    
                if len(str(exeNoAlc)) > 1:
                    array_mes.append(exeNoAlc[0].childNodes[0].data) 
                else:
                    array_mes.append(0)
                    
                if len(str(sac)) > 1:
                    array_mes.append(sac[0].childNodes[0].data) 
                else:
                    array_mes.append(0)
                    
                if len(str(horasExtGr)) > 1:
                    array_mes.append(horasExtGr[0].childNodes[0].data) 
                else:
                    array_mes.append(0)
                    
                if len(str(horasExtEx)) > 1:
                    array_mes.append(horasExtEx[0].childNodes[0].data) 
                else:
                    array_mes.append(0) 
                    
                if len(str(matDid)) > 1:
                    array_mes.append(matDid[0].childNodes[0].data) 
                else:
                    array_mes.append(0)
                    
                if len(str(gastosMovViat)) > 1:
                    array_mes.append(gastosMovViat[0].childNodes[0].data) 
                else:
                    array_mes.append(0)
                
                legajo = BaseDatos.Empleados.select(BaseDatos.Empleados.legajo).where(BaseDatos.Empleados.cuil == array_mes[0])

                for row in legajo:
                    
                    if existe_legajo(row.legajo) == False:
                        raise NoExisteLegajo
                    else:
                        array_mes.append(row.legajo)
                
                resultado.append(array_mes)
       
        return resultado

    except NoExisteLegajo:
        txt = open(f'logs/insert_gananoe {hora}.txt', 'a')
        txt.write(f'No existe legajo para el cuil {array_mes[0]} dentro de la tabla de empleados. No se realiza el insert.\n')
        txt.close()


def lee_gananoe_xlsx(archivo):
    
    """
    Lee la información obtenida desde un archivo, con extensión xlsx, y devuelve la información en un array. 
    La variable archivo contiene la información correspondiente al archivo con extensión ".xlsx".
    """

    try:

        hora = obtiene_fecha()

        #Lee la información desde el archivo seleccionado.
        excel_file = read_excel(archivo)

        _legajo = excel_file['legajo'].values
        _ann = excel_file['año'].values
        _cuil = excel_file['CUIL'].values
        _cuit = excel_file['CUIT'].values
        _denominacion = excel_file['denominacion'].values
        _mes = excel_file['mes'].values
        _obra_soc = excel_file['obra social'].values
        _seg_soc = excel_file['seguridad social'].values
        _sind = excel_file['sindicato'].values
        _gan_brut = excel_file['ganancia bruta'].values
        _ret_gan = excel_file['retencion ganancias'].values
        _retrib_nohab = excel_file['retribuciones no habituales'].values
        _ajuste = excel_file['ajuste'].values
        _exe_noalc = excel_file['remuneracion exenta'].values
        _sac = excel_file['SAC'].values
        _horas_extgr = excel_file['hs. extras gravadas'].values
        _horas_extex = excel_file['hs. extras exentas'].values
        _mat_did = excel_file['material didactico'].values
        _gastos_movviat = excel_file['movilidad y viaticos'].values

        #Genera el diccionario para el Dataframe.
        diccionario_import = {
            'CUIL' : [],
            'Año' : [],
            'CUIT' : [],
            'Denominación' : [],
            'Mes' : [],
            'Obra social' : [],
            'Seguridad social' : [],
            'Sindicato' : [],
            'Ganancia bruta' : [],
            'Retención ganancias' : [],
            'Retribuciones no habituales': [],
		    'Ajuste' : [],
		    'Remuneración exenta' : [],
		    'SAC' : [],
		    'Hs. Extras gravadas' : [],
		    'Hs. Extras exentas' : [],
		    'Material didactico' : [],
		    'Movilidad y viaticos' : [],
            'Legajo' : []
        }

        diccionario_import['CUIL'] = _cuil
        diccionario_import['Año'] = _ann 
        diccionario_import['CUIT'] = _cuit
        diccionario_import['Denominación'] = _denominacion
        diccionario_import['Mes'] = _mes
        diccionario_import['Obra social'] = _obra_soc
        diccionario_import['Seguridad social'] = _seg_soc
        diccionario_import['Sindicato'] = _sind
        diccionario_import['Ganancia bruta'] = _gan_brut
        diccionario_import['Retención ganancias'] = _ret_gan
        diccionario_import['Retribuciones no habituales'] = _retrib_nohab
        diccionario_import['Ajuste'] = _ajuste
        diccionario_import['Remuneración exenta'] = _exe_noalc
        diccionario_import['SAC'] = _sac
        diccionario_import['Hs. Extras gravadas'] = _horas_extgr
        diccionario_import['Hs. Extras exentas'] = _horas_extex
        diccionario_import['Material didactico'] = _mat_did 
        diccionario_import['Movilidad y viaticos'] = _gastos_movviat
        diccionario_import['Legajo'] = _legajo

        #Dataframe.
        array_empleado = DataFrame(diccionario_import, columns=['CUIL', 'Año', 'CUIT', 'Denominación', 'Mes', 'Obra social', 'Seguridad social', 
					    'Sindicato', 'Ganancia bruta', 'Retención ganancias', 'Retribuciones no habituales', 'Ajuste', 'Remuneración exenta', 'SAC', 'Hs. Extras gravadas', 
					    'Hs. Extras exentas', 'Material didactico', 'Movilidad y viaticos', 'Legajo'])

        return array_empleado

    except KeyError:
        txt = open(f'logs/insert_gananoe {hora}.txt', 'a')
        txt.write(f'Error en lectura de archivo xlsx. No se realiza el insert.\n')
        txt.close()

def guarda_oe(*args):

    try:
        
        hora = obtiene_fecha()
        
        if existe_ganancia(args[18], args[2], args[4], args[1]) == True:
            raise ExisteRegistro

        if existe_legajo(args[18]) == False:
            raise NoExisteLegajo
          
        if len(args) != 19:
            raise IndexError

        ingresos_oe = BaseDatos.GananciasOE()
        ingresos_oe.legajo = args[18]
        ingresos_oe.cuil = args[0]
        ingresos_oe.ann = args[1]
        ingresos_oe.cuit = args[2]
        ingresos_oe.denominacion = args[3]
        ingresos_oe.mes = args[4]
        ingresos_oe.obra_soc = args[5]
        ingresos_oe.seg_soc = args[6]
        ingresos_oe.sind = args[7]
        ingresos_oe.gan_brut = args[8]
        ingresos_oe.ret_gan = args[9]
        ingresos_oe.retrib_nohab = args[10]
        ingresos_oe.ajuste = args[11]
        ingresos_oe.exe_noalc = args[12]
        ingresos_oe.sac = args[13]
        ingresos_oe.horas_extgr = args[14]
        ingresos_oe.horas_extex = args[15]
        ingresos_oe.mat_did = args[16]
        ingresos_oe.gastos_movviat = args[17]
        ingresos_oe.save()
    
    except NoExisteLegajo:
        txt = open(f'logs/insert_gananoe {hora}.txt', 'a')
        txt.write(f'El legajo {args[18]} no existe dentro de la tabla de empleados. No se realiza el insert.\n')
        txt.close()
    
    except ExisteRegistro:
        txt = open(f'logs/insert_gananoe {hora}.txt', 'a')
        txt.write(f'El legajo {args[18]} ya contiene un registro para el cuit {args[1]}, mes {args[3]}. No se realiza el insert.\n')
        txt.close()

  
    except IndexError:
        txt = open(f'logs/insert_gananoe {hora}.txt', 'a')
        txt.write(f'Error en la lectura del xml {args[0]}. Revisar que exista un legajo asociado para el número de cuil.\n')
        txt.close()

    except IntegrityError:
        txt = open(f'logs/insert_gananoe {hora}.txt', 'a')
        txt.write(f'Faltan campos obligatorios en legajo {args[0]}. No se realiza el insert.\n')
        txt.close()

    except:
        pass

#Divisor.
##############################################################################################################

def existe_divisor(legajo: int, ann: int, mes: int) -> bool:
    
    """
    Verifica si ya existe un registro para el mes y año especificado.
    """
    
    try:
        
        query = BaseDatos.Divisor.select().where(BaseDatos.Divisor.legajo == legajo, BaseDatos.Divisor.ann == ann,
        BaseDatos.Divisor.mes == mes)

        for row in query:
            resultado = row.legajo
            
        if resultado != None:
            return True
        else:
            return False
    
    except:
        return False



def lee_archivo_divisor(archivo: str) -> DataFrame:

    """
    Lee la información que contiene el archivo y devuelve los datos en un dataframe.
    """

    try:

        hora = obtiene_fecha()

        excel_file = read_excel(archivo)

        _legajo = excel_file['legajo'].values
        _ann = excel_file['año'].values
        _mes = excel_file['mes'].values
        _divisor = excel_file['divisor'].values

        diccionario = {
            'Legajo':[],
            'Año': [],
            'Mes':[],
            'Divisor': []
        }

        diccionario['Legajo'] = _legajo
        diccionario['Año'] = _ann
        diccionario['Mes'] = _mes
        diccionario['Divisor'] = _divisor

        resultado = DataFrame(diccionario, columns=['Legajo', 'Año', 'Mes', 'Divisor'])

        return resultado
    
    except KeyError:
        txt = open(f'logs/insert_divisor {hora}.txt', 'a')
        txt.write(f'Error en lectura de archivo xlsx. No se realiza el insert.\n')
        txt.close()


def guarda_divisor(*args):
    
    """
    Guarda registros en la tabla divisor.
    """
    
    try:
        hora = obtiene_fecha()

        if existe_divisor(args[0], args[1], args[2]) == True:
            raise ExisteRegistro
        
        divisor = BaseDatos.Divisor()
        divisor.legajo = args[0]
        divisor.ann = args[1]
        divisor.mes = args[2]
        divisor.divisor = args[3]
        divisor.save()

    except NoExisteLegajo:
        txt = open(f'logs/insert_divisor {hora}.txt', 'a')
        txt.write(f'El legajo {args[0]} no existe dentro de la tabla de empleados. No se realiza el insert.\n')
        txt.close()

    except IndexError:
        txt = open(f'logs/insert_divisor {hora}.txt', 'a')
        txt.write(f'Error en la lectura del xlsx {args[0]}. Revisar que exista un legajo asociado para el número de cuil.\n')
        txt.close()

    except IntegrityError:
        txt = open(f'logs/insert_divisor {hora}.txt', 'a')
        txt.write(f'Faltan campos obligatorios en legajo {args[0]}. No se realiza el insert.\n')
        txt.close()

    except ExisteRegistro:
        txt = open(f'logs/insert_divisor {hora}.txt', 'a')
        txt.write(f'Ya existe un registro para el legajo {args[0]} para el año {args[1]}, mes {args[2]}. No se realiza el insert.\n')
        txt.close()

    except:
        pass