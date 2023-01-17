#Modelo -> MVC

from pandas import DataFrame
from importacion import BaseDatos
from crud_bd import lee_promediobruto
from crud_bd import lee_primerparrafo
from crud_bd import lee_segundoparrafo
from crud_bd import lectura_bbdd_empleados
from crud_bd import lect_bbdd_rem_deduc
from crud_bd import lectura_carfam
from crud_bd import lectura_remoe

class Modelo():

    def __init__(self):
        pass


    def xlsx_promediobruto(self, archivo: str) -> bool:
        
        try:
            informacion = {'Legajo': [],
                    'Mes': [],
                    'Importe': []}

            query = BaseDatos.PromedioBruto.select(BaseDatos.PromedioBruto.legajo, BaseDatos.PromedioBruto.mes, 
                    BaseDatos.PromedioBruto.importe)

            for row in query:
                informacion['Legajo'].append(row.legajo) 
                informacion['Mes'].append(row.mes) 
                informacion['Importe'].append(row.importe)


            resultado = DataFrame(informacion, columns=['Legajo', 'Mes', 'Importe']) 

            resultado.to_excel(archivo, sheet_name='Hoja1')

            return True

        except:
            return False
        
        
    def xlsx_dedpparte(self, archivo: str) -> bool:

        try:       
         

            informacion = {'Legajo': [],
                           'Mes': [],
                           'Salario bruto': [],
                           'Deducciones': [],
                           'Deducción especial': [],
                           'Ganancia no imponible': [],
                           'Cargas de familia': [],
                           'Ded. primera parte': []}
        
            query = BaseDatos.PrimerParrafo.select(BaseDatos.PrimerParrafo.legajo, BaseDatos.PrimerParrafo.mes,
            BaseDatos.PrimerParrafo.sbruto, BaseDatos.PrimerParrafo.deducciones, BaseDatos.PrimerParrafo.ded_esp,
            BaseDatos.PrimerParrafo.min_no_imp, BaseDatos.PrimerParrafo.cargas_familia, BaseDatos.PrimerParrafo.ded_p_parrafo)


            for row in query:
                informacion['Legajo'].append(row.legajo) 
                informacion['Mes'].append(row.mes) 
                informacion['Salario bruto'].append(row.sbruto) 
                informacion['Deducciones'].append(row.deducciones) 
                informacion['Deducción especial'].append(row.ded_esp) 
                informacion['Ganancia no imponible'].append(row.min_no_imp) 
                informacion['Cargas de familia'].append(row.cargas_familia) 
                informacion['Ded. primera parte'].append(row.ded_p_parrafo) 

            resultado = DataFrame(informacion, columns=['Legajo', 'Mes', 'Salario bruto', 'Deducciones', 'Deducción especial',
                                                'Ganancia no imponible', 'Cargas de familia', 'Ded. primera parte'])

            resultado.to_excel(archivo, sheet_name='Hoja1')

            return True

        except:
            return False

    
    def xlsx_dedsparte(self, archivo: str) -> bool:

        try:

            informacion = {'Legajo': [],
                           'Mes': [],
                           'Ded. Segunda parte': []}

            query = BaseDatos.SegundoParrafo.select(BaseDatos.SegundoParrafo.legajo, BaseDatos.SegundoParrafo.mes, 
                    BaseDatos.SegundoParrafo.ded_s_parrafo)

            for row in query:
                informacion['Legajo'].append(row.legajo) 
                informacion['Mes'].append(row.mes) 
                informacion['Ded. Segunda parte'].append(row.ded_s_parrafo) 

            
            resultado = DataFrame(informacion, columns=['Legajo', 'Mes', 'Ded. Segunda parte'])

            resultado.to_excel(archivo, sheet_name='Hoja1')

            return True

        except:
            return False

def xlsx_empleados(archivo: str):
    
    try:
        registros = lectura_bbdd_empleados()

        informacion = {'Legajo': [],
                       'CUIL': [],
                       'Nombre y Apellido': [],
                       'Fecha de ingreso': []}

        for registro in registros:
            informacion['Legajo'].append(registro[0])
            informacion['CUIL'].append(registro[1])
            informacion['Nombre y Apellido'].append(registro[2])
            informacion['Fecha de ingreso'].append(registro[3])

        resultado = DataFrame(informacion, columns=['Legajo', 'CUIL', 'Nombre y Apellido',
                    'Fecha de ingreso'])

        resultado.to_excel(archivo)

        return True

    except:
        return False


def xlsx_remuneraciones(legajo: list, month: list, year: list, archivo: str):

    try:
        registros = lect_bbdd_rem_deduc('remu', legajo, month, year)

        informacion = {'Legajo': [],
                       'Nombre y Apellido': [],
                       'Año': [],
                       'Mes': [],
                       'Importe': []}

        for registro in registros:
            informacion['Legajo'].append(registro[0])
            informacion['Nombre y Apellido'].append(registro[1])
            informacion['Año'].append(registro[2])
            informacion['Mes'].append(registro[3])
            informacion['Importe'].append(registro[4])
    
        resultado = DataFrame(informacion, columns=['Legajo', 'Nombre y Apellido', 'Año', 'Mes', 'Importe'])
    
        resultado.to_excel(archivo)

        return True
    
    except:
        return False
    


def xlsx_deducciones(legajo: list, month: list, year: list, archivo: str):

    try:
        registros = lect_bbdd_rem_deduc('deduc', legajo, month, year)
        informacion = {'Legajo': [],
                       'Nombre y Apellido': [],
                       'Año': [],
                       'Mes': [],
                       'Importe': []}
    
        for registro in registros:
            informacion['Legajo'].append(registro[0])
            informacion['Nombre y Apellido'].append(registro[1])
            informacion['Año'].append(registro[2])
            informacion['Mes'].append(registro[3])
            informacion['Importe'].append(registro[4])
    
        resultado = DataFrame(informacion, columns=['Legajo', 'Nombre y Apellido', 'Año', 'Mes', 'Importe'])
    
        resultado.to_excel(archivo)
        
        return True

    except:
        return False

def xlsx_cargasfam(legajo: list, year: list, month: list, archivo: str):

    try:
        registros = lectura_carfam(legajo, year, month)
        informacion = {'Legajo': [],
                       'Año': [],
                       'CUIL': [],
                       'Número documento': [],
                       'Apellido': [],
                       'Nombre': [],
                       'Mes desde': [],
                       'Mes hasta': [],
                       'Parentesco': [],
                       'Porcentaje': []
        }
                       
        for registro in registros:
            informacion['Legajo'].append(registro[1])
            informacion['Año'].append(registro[2])
            informacion['CUIL'].append(registro[3])
            informacion['Número documento'].append(registro[4])
            informacion['Apellido'].append(registro[5])
            informacion['Nombre'].append(registro[6])
            informacion['Mes desde'].append(registro[7])
            informacion['Mes hasta'].append(registro[8])
            informacion['Parentesco'].append(registro[9])
            informacion['Porcentaje'].append(registro[10])
    
        resultado = DataFrame(informacion, columns=['Legajo', 'Año', 'CUIL', 'Número documento', 'Apellido',
        'Nombre', 'Mes desde', 'Mes hasta', 'Parentesco', 'Porcentaje'])
    
        resultado.to_excel(archivo)

        return True

    except:
        return False


def xlsx_gananciasoe(legajo: list, month: list, year: list, archivo: str):

    try:
        registros = lectura_remoe(legajo, month, year)
        
        informacion = {'Legajo': [],
                       'Año': [],
                       'CUIL': [],
                       'Denominación': [],
                       'Mes': [],
                       'Obra social': [],
                       'Seguridad social': [],
                       'Sindicato': [],
                       'Ganancia bruta': [],
                       'Retribuciones no habituales': [],
                       'Ajuste': [],
                       'Remuneración exenta': [],
                       'SAC': [],
                       'Hs. extras gravadas': [],
                       'Hs. extras exentas': [],
                       'Material didactico': [],
                       'Gastos mov. y viaticos': []
                      }
                   
        for registro in registros:
            informacion['Legajo'].append(registro[1])
            informacion['Año'].append(registro[2])
            informacion['CUIL'].append(registro[3])
            informacion['Denominación'].append(registro[4])
            informacion['Mes'].append(registro[5])
            informacion['Obra social'].append(registro[6])
            informacion['Seguridad social'].append(registro[7])
            informacion['Sindicato'].append(registro[8])
            informacion['Ganancia bruta'].append(registro[9])
            informacion['Retribuciones no habituales'].append(registro[10])
            informacion['Ajuste'].append(registro[11])
            informacion['Remuneración exenta'].append(registro[12])
            informacion['Hs. extras gravadas'].append(registro[13])
            informacion['Hs. extras exentas'].append(registro[14])
            informacion['Material didactico'].append(registro[15])
            informacion['Gastos mov. y viaticos'].append(registro[16])
            
    
        resultado = DataFrame(informacion, columns=['Legajo', 'Año', 'CUIL', 'CUIT', 'Denominación', 'Mes', 'Obra social', 'Seguridad social', 
        'Sindicato', 'Ganancia bruta', 'Retribuciones no habituales', 'Ajuste', 'Remuneración exenta', 
        'Hs. extras gravadas', 'Hs. extras exentas', 'Material didactico', 'Gastos mov. y viaticos'])
    
        resultado.to_excel(archivo)
    
        return True

    except:
        return False



def xlsx_promediobruto(month: list, year: list, archivo: str):

    try:
        registros = lee_promediobruto(month, year)
        informacion = {'Legajo': [],
                       'Año': [],
                       'Mes': [],
                       'Importe': []}
    
        for registro in registros:
            informacion['Legajo'].append(registro[0])
            informacion['Año'].append(registro[1])
            informacion['Mes'].append(registro[2])
            informacion['Importe'].append(registro[3])
    
        resultado = DataFrame(informacion, columns=['Legajo', 'Año', 'Mes', 'Importe'])
    
        resultado.to_excel(archivo)
    
        return True

    except:
        return False



def xlsx_dedpparte(month: list, year: list, archivo: str):
    

    try:
        registros = lee_primerparrafo(month, year)
        informacion = {'Legajo': [],
                       'Año': [],
                       'Mes': [],
                       'Salario bruto': [],
                       'Deducciones': [],
                       'Deducción especial': [],
                       'Ganancia no imponible': [],
                       'Cargas de familia': [],
                       'Deducción primera parte': []
                       }
    
        for registro in registros:
            informacion['Legajo'].append(registro[0])
            informacion['Año'].append(registro[1])
            informacion['Mes'].append(registro[2])
            informacion['Salario bruto'].append(registro[3])
            informacion['Deducciones'].append(registro[4])
            informacion['Deducción especial'].append(registro[5])
            informacion['Ganancia no imponible'].append(registro[6])
            informacion['Cargas de familia'].append(registro[7])
            informacion['Deducción primera parte'].append(registro[8])
    
        resultado = DataFrame(informacion, columns=['Legajo', 'Año', 'Mes', 'Salario bruto', 'Deducciones', 
        'Deducción especial', 'Ganancia no imponible', 'Cargas de familia', 'Deducción primera parte'])
    
        resultado.to_excel(archivo)
    
        return True

    except:
        return False


def xlsx_dedsparte(month: list, year: list, archivo: str):

    try:
        registros = lee_segundoparrafo(month, year)
        informacion = {'Legajo': [],
                       'Año': [],
                       'Mes': [],
                       'Deducción segunda parte': []}
    
        for registro in registros:
            informacion['Legajo'].append(registro[0])
            informacion['Año'].append(registro[1])
            informacion['Mes'].append(registro[2])
            informacion['Deducción segunda parte'].append(registro[3])
    
        resultado = DataFrame(informacion, columns=['Legajo', 'Año', 'Mes', 'Deducción segunda parte'])
    
        resultado.to_excel(archivo)
    
        return True

    except:
        return False
