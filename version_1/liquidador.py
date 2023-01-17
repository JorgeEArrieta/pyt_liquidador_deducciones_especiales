
from datetime import datetime
from lib2to3.pytree import Base
from importacion import BaseDatos
from importacion import DeduccionesPersonales
from importacion import RangoSegundoParrafo
from importacion import lee_par_gananoe
from errores import LegajoInactivo
from errores import ErrorBruto
import calendar

#Procesos para el liquidador de promedio
#########################################################################################################

def verifica_ingreso(legajo, mes_actual, y):

    query = BaseDatos.Empleados.select(BaseDatos.Empleados.fecha_ingreso).where(BaseDatos.Empleados.legajo == legajo)

    for row in query:
        fecha = row.fecha_ingreso
    
    year = int(datetime.strftime(fecha, '%Y'))
    mes = int(datetime.strftime(fecha, '%m'))
    
    if year < y:
        return True

    elif (year == y) & (mes <= mes_actual):
        return True

    else:
        return False 

def legajos_activos(leg_incial, leg_final, y, mes):
    
    listado = list()
    
    y = int(y)
    mes = int(mes)

    day = calendar.monthrange(y, mes)[1]

    f = f'{day}/{mes}/{y}'

    fecha = datetime.strptime(f, '%d/%m/%Y')
    
    query_empleados = BaseDatos.Empleados.select(BaseDatos.Empleados.legajo).where(
                      BaseDatos.Empleados.legajo.between(leg_incial, leg_final),
                      BaseDatos.Empleados.fecha_ingreso <= fecha)
                

    for row in query_empleados:
        listado.append(row.legajo)

    return listado


#Funciones para el liquidador de promedios brutos
########################################################################################################
def divisor_promedio(legajo, mes_actual, y):

    """
    Función para calcular el divisor para el promedio variable. 
    """

    query = BaseDatos.Empleados.select(BaseDatos.Empleados.fecha_ingreso).where(BaseDatos.Empleados.legajo == legajo)

    for row in query:
        fecha = row.fecha_ingreso

    year = int(datetime.strftime(fecha, '%Y'))
    mes = int(datetime.strftime(fecha, '%m'))
   
   #Calculo para el divisor para el promedio bruto.

   #Año 2021
    if y == 2021:

        if year < y:

            if mes_actual <= 8:

                resultado = mes_actual

            else:

                resultado = mes_actual - 9 + 1

        if year == y:

            if mes <= 8:

                if mes_actual <= 8:
                
                    resultado = mes_actual - mes + 1
            
                else:

                    resultado = mes_actual - 9 + 1

            else:

                resultado = mes_actual - mes + 1


    #Busca un divisor cargado por el usuario.
    query = BaseDatos.Divisor.select(BaseDatos.Divisor.divisor).where(BaseDatos.Divisor.legajo == legajo,
            BaseDatos.Divisor.ann == y, BaseDatos.Divisor.mes == mes_actual)

    divisor = None

    for row in query:
        divisor = row.divisor

    if divisor != None:
        resultado = divisor

    return resultado


def promedio_bruto(year, legajo ,mes_liquidacion):
    
    try:
        #Inicia variable.
        sueldo_actual = 0
        
        if verifica_ingreso(legajo, mes_liquidacion, year) == False:
            raise LegajoInactivo
    
        divisor = divisor_promedio(legajo, mes_liquidacion, year)

        if year == 2021:
        
            if mes_liquidacion <= 8:  
                #Obtiene el promedio
                query_promedio = BaseDatos.SueldosBrutos.select(BaseDatos.SueldosBrutos.importe).where(
                                 BaseDatos.SueldosBrutos.legajo == legajo, 
                                 BaseDatos.SueldosBrutos.mes <= mes_liquidacion,
                                 BaseDatos.SueldosBrutos.ann == year)

                query_remoe = BaseDatos.GananciasOE.select(BaseDatos.GananciasOE.gan_brut, BaseDatos.GananciasOE.retrib_nohab, BaseDatos.GananciasOE.ajuste, BaseDatos.GananciasOE.exe_noalc,
                              BaseDatos.GananciasOE.horas_extgr, BaseDatos.GananciasOE.horas_extex, BaseDatos.GananciasOE.mat_did, BaseDatos.GananciasOE.ret_gan, BaseDatos.GananciasOE.sac,
                              BaseDatos.GananciasOE.gastos_movviat).where(BaseDatos.GananciasOE.legajo == legajo, 
                              BaseDatos.GananciasOE.mes <= mes_liquidacion, BaseDatos.GananciasOE.ann == year)

            else:
                #Obtiene el promedio
                query_promedio = BaseDatos.SueldosBrutos.select(BaseDatos.SueldosBrutos.importe).where(
                                 BaseDatos.SueldosBrutos.legajo == legajo, BaseDatos.SueldosBrutos.ann== year,
                                 (BaseDatos.SueldosBrutos.mes >= 9) & (BaseDatos.SueldosBrutos.mes <= mes_liquidacion))


                query_remoe = BaseDatos.GananciasOE.select(BaseDatos.GananciasOE.gan_brut, BaseDatos.GananciasOE.retrib_nohab, BaseDatos.GananciasOE.ajuste, BaseDatos.GananciasOE.exe_noalc,
                              BaseDatos.GananciasOE.horas_extgr, BaseDatos.GananciasOE.horas_extex, BaseDatos.GananciasOE.mat_did, BaseDatos.GananciasOE.ret_gan, BaseDatos.GananciasOE.sac,
                              BaseDatos.GananciasOE.gastos_movviat).where(BaseDatos.GananciasOE.legajo == legajo, BaseDatos.GananciasOE.ann == year,
                              (BaseDatos.GananciasOE.mes >= 9) & (BaseDatos.GananciasOE.mes <= mes_liquidacion))    
            
            acumulado = 0
        
            for row in query_promedio:
                acumulado += row.importe

            for row in query_remoe:
                if lee_par_gananoe('gan_brut') == 1:
                    acumulado += row.gan_brut
                    
                if lee_par_gananoe('ret_gan') == 1:
                    acumulado += row.ret_gan
                    
                if lee_par_gananoe('retrib_nohab') == 1:
                    acumulado += row.retrib_nohab 
                    
                if lee_par_gananoe('ajuste') == 1:  
                    acumulado += row.ajuste 
                   
                if lee_par_gananoe('exe_noalc') == 1:
                    acumulado += row.exe_noalc
                   
                if lee_par_gananoe('sac') == 1:
                    acumulado += row.sac
                   
                if lee_par_gananoe('horas_extgr') == 1:
                    acumulado += row.horas_extgr
                   
                if lee_par_gananoe('horas_extex') == 1:
                    acumulado += row.horas_extex
                   
                if lee_par_gananoe('mat_did') == 1:
                    acumulado += row.mat_did
                    
                if lee_par_gananoe('gastos_movviat') == 1:
                    acumulado += row.gastos_movviat
                         
            #Obtiene el ultimo sueldo.
            query_sueldo = BaseDatos.SueldosBrutos.select(BaseDatos.SueldosBrutos.importe).where(
                           BaseDatos.SueldosBrutos.legajo == legajo, BaseDatos.SueldosBrutos.mes == mes_liquidacion, BaseDatos.SueldosBrutos.ann == year)

            query_remoe_ac = BaseDatos.GananciasOE.select(BaseDatos.GananciasOE.gan_brut, BaseDatos.GananciasOE.retrib_nohab, BaseDatos.GananciasOE.ajuste, BaseDatos.GananciasOE.exe_noalc,
                             BaseDatos.GananciasOE.horas_extgr, BaseDatos.GananciasOE.horas_extex, BaseDatos.GananciasOE.mat_did, BaseDatos.GananciasOE.ret_gan, BaseDatos.GananciasOE.sac,
                             BaseDatos.GananciasOE.gastos_movviat).where(BaseDatos.GananciasOE.legajo == legajo, BaseDatos.GananciasOE.ann == year,
                             BaseDatos.GananciasOE.mes == mes_liquidacion)
        
            for row in query_sueldo:
                sueldo_actual = row.importe

            for row in query_remoe_ac:
                if lee_par_gananoe('gan_brut') == 1:
                    sueldo_actual += row.gan_brut
                if lee_par_gananoe('ret_gan') == 1:
                    sueldo_actual += row.ret_gan
                if lee_par_gananoe('retrib_nohab') == 1:
                    sueldo_actual += row.retrib_nohab 
                if lee_par_gananoe('ajuste') == 1:  
                    sueldo_actual += row.ajuste 
                if lee_par_gananoe('exe_noalc') == 1:
                    sueldo_actual += row.exe_noalc
                if lee_par_gananoe('sac') == 1:
                    sueldo_actual += row.sac
                if lee_par_gananoe('horas_extgr') == 1:
                    sueldo_actual += row.horas_extgr
                if lee_par_gananoe('horas_extex') == 1:
                    sueldo_actual += row.horas_extex
                if lee_par_gananoe('mat_did') == 1:
                    sueldo_actual += row.mat_did
                if lee_par_gananoe('gastos_movviat') == 1:
                    sueldo_actual += row.gastos_movviat
            
            #Calcula el promedio bruto
            promedio = acumulado / divisor

            #Verifica si corresponde el valor mensual o el promedio bruto.
            if sueldo_actual > 0:

                if sueldo_actual > promedio:
                    return legajo, year, mes_liquidacion, round(promedio, 2)
                else:
                    return legajo, year, mes_liquidacion, round(sueldo_actual, 2)  
            
            else:
                return legajo, year, mes_liquidacion, round(promedio, 2)
            
            
        if year != 2021:

            #Obtiene el promedio
            query_promedio = BaseDatos.SueldosBrutos.select(BaseDatos.SueldosBrutos.importe).where(
                             BaseDatos.SueldosBrutos.legajo == legajo, BaseDatos.SueldosBrutos.mes <= mes_liquidacion,
                             BaseDatos.SueldosBrutos.ann == year)

            query_remoe = BaseDatos.GananciasOE.select(BaseDatos.GananciasOE.gan_brut, BaseDatos.GananciasOE.retrib_nohab, BaseDatos.GananciasOE.ajuste, BaseDatos.GananciasOE.exe_noalc,
                          BaseDatos.GananciasOE.horas_extgr, BaseDatos.GananciasOE.horas_extex, BaseDatos.GananciasOE.mat_did, BaseDatos.GananciasOE.ret_gan, BaseDatos.GananciasOE.sac,
                          BaseDatos.GananciasOE.gastos_movviat).where(BaseDatos.GananciasOE.legajo == legajo, BaseDatos.GananciasOE.ann == year,
                          BaseDatos.GananciasOE.mes <= mes_liquidacion)

            acumulado = 0
        
            for row in query_promedio:
                acumulado += row.importe

            for row in query_remoe:
                if lee_par_gananoe('gan_brut') == 1:
                    acumulado += row.gan_brut
                if lee_par_gananoe('ret_gan') == 1:
                    acumulado += row.ret_gan
                if lee_par_gananoe('retrib_nohab') == 1:
                    acumulado += row.retrib_nohab 
                if lee_par_gananoe('ajuste') == 1:  
                    acumulado += row.ajuste 
                if lee_par_gananoe('exe_noalc') == 1:
                    acumulado += row.exe_noalc
                if lee_par_gananoe('sac') == 1:
                    acumulado += row.sac
                if lee_par_gananoe('horas_extgr') == 1:
                    acumulado += row.horas_extgr
                if lee_par_gananoe('horas_extex') == 1:
                    acumulado += row.horas_extex
                if lee_par_gananoe('mat_did') == 1:
                    acumulado += row.mat_did
                if lee_par_gananoe('gastos_movviat') == 1:
                    acumulado += row.gastos_movviat
            
            #Obtiene el ultimo sueldo.
            query_sueldo = BaseDatos.SueldosBrutos.select(BaseDatos.SueldosBrutos.importe).where(
                           BaseDatos.SueldosBrutos.legajo == legajo, BaseDatos.SueldosBrutos.mes == mes_liquidacion,
                           BaseDatos.SueldosBrutos.ann == year)

            query_remoe_ac = BaseDatos.GananciasOE.select(BaseDatos.GananciasOE.gan_brut, BaseDatos.GananciasOE.retrib_nohab, BaseDatos.GananciasOE.ajuste, BaseDatos.GananciasOE.exe_noalc,
                             BaseDatos.GananciasOE.horas_extgr, BaseDatos.GananciasOE.horas_extex, BaseDatos.GananciasOE.mat_did, BaseDatos.GananciasOE.ret_gan, BaseDatos.GananciasOE.sac,
                             BaseDatos.GananciasOE.gastos_movviat).where(BaseDatos.GananciasOE.legajo == legajo, BaseDatos.GananciasOE.ann == year,
                             BaseDatos.GananciasOE.mes == mes_liquidacion)

            for row in query_sueldo:
                sueldo_actual = row.importe

            for row in query_remoe_ac:

                if lee_par_gananoe('gan_brut') == 1:
                    sueldo_actual += row.gan_brut
                if lee_par_gananoe('ret_gan') == 1:
                    sueldo_actual += row.ret_gan
                if lee_par_gananoe('retrib_nohab') == 1:
                    sueldo_actual += row.retrib_nohab 
                if lee_par_gananoe('ajuste') == 1:  
                    sueldo_actual += row.ajuste 
                if lee_par_gananoe('exe_noalc') == 1:
                    sueldo_actual += row.exe_noalc
                if lee_par_gananoe('sac') == 1:
                    sueldo_actual += row.sac
                if lee_par_gananoe('horas_extgr') == 1:
                    sueldo_actual += row.horas_extgr
                if lee_par_gananoe('horas_extex') == 1:
                    sueldo_actual += row.horas_extex
                if lee_par_gananoe('mat_did') == 1:
                    sueldo_actual += row.mat_did
                if lee_par_gananoe('gastos_movviat') == 1:
                    sueldo_actual += row.gastos_movviat
               
            #Calcula el promedio bruto   
            promedio = acumulado / divisor  

            #Verifica si corresponde el sueldo mensual o el promedio bruto.
            if sueldo_actual > 0:

                if sueldo_actual > promedio:
                    return legajo, year, mes_liquidacion, round(promedio, 2)
                
                elif sueldo_actual < promedio:
                    return legajo, year, mes_liquidacion, round(sueldo_actual, 2)  

            else:
                return legajo, year, mes_liquidacion, round(promedio, 2)

    except LegajoInactivo:
        print('Error')
                     
                     
def elimina_promedio(legajo, ann, mes):

    try:
        query = BaseDatos.PromedioBruto.delete().where(BaseDatos.PromedioBruto.legajo == legajo,
                BaseDatos.PromedioBruto.ann == ann, BaseDatos.PromedioBruto.mes == mes)

        query.execute()

    except:
        pass

def guarda_promedio(*args):
    
    try:
        promedio_empleado = BaseDatos.PromedioBruto()
        promedio_empleado.legajo = args[0]
        promedio_empleado.ann = args[1]
        promedio_empleado.mes = args[2]
        promedio_empleado.importe = args[3]
        promedio_empleado.save()

    except:
        pass


#Liquidador del primer párrafo
##############################################################################################################

def obtiene_remoe(legajo, mes, year):

    """
    Devuelve la sumatoria de las remuneraciones brutas existentes para un legajo, en un mes determinado.
    """

    acumulado = 0

    query_remoe = BaseDatos.GananciasOE.select(BaseDatos.GananciasOE.gan_brut, BaseDatos.GananciasOE.ajuste, BaseDatos.GananciasOE.exe_noalc, BaseDatos.GananciasOE.retrib_nohab,
                  BaseDatos.GananciasOE.horas_extgr, BaseDatos.GananciasOE.horas_extex, BaseDatos.GananciasOE.mat_did, BaseDatos.GananciasOE.ret_gan, 
                  BaseDatos.GananciasOE.sac, BaseDatos.GananciasOE.gastos_movviat).where(BaseDatos.GananciasOE.legajo == legajo, 
                  BaseDatos.GananciasOE.mes == mes, BaseDatos.GananciasOE.ann == year)

    for row in query_remoe:
        if lee_par_gananoe('gan_brut') == 1:
            acumulado += row.gan_brut
        if lee_par_gananoe('ret_gan') == 1:
            acumulado += row.ret_gan
        if lee_par_gananoe('retrib_nohab') == 1:
            acumulado += row.retrib_nohab 
        if lee_par_gananoe('ajuste') == 1:  
            acumulado += row.ajuste 
        if lee_par_gananoe('exe_noalc') == 1:
            acumulado += row.exe_noalc
        if lee_par_gananoe('sac') == 1:
            acumulado += row.sac
        if lee_par_gananoe('horas_extgr') == 1:
            acumulado += row.horas_extgr
        if lee_par_gananoe('horas_extex') == 1:
            acumulado += row.horas_extex
        if lee_par_gananoe('mat_did') == 1:
            acumulado += row.mat_did
        if lee_par_gananoe('gastos_movviat') == 1:
            acumulado += row.gastos_movviat
    
    return round(acumulado, 2)

def obtiene_dedoe(legajo, mes, year):

    """
    Devuelve la sumatoria de las remuneraciones brutas existentes para un legajo, en un mes determinado.
    """

    resultado = 0

    query_dedoe = BaseDatos.GananciasOE.select(BaseDatos.GananciasOE.obra_soc, BaseDatos.GananciasOE.seg_soc, BaseDatos.GananciasOE.sind).where(
                  BaseDatos.GananciasOE.legajo == legajo, BaseDatos.GananciasOE.mes == mes, BaseDatos.GananciasOE.ann == year)

    for row in query_dedoe:
        resultado += row.obra_soc
        resultado += row.seg_soc
        resultado += row.sind

    return round(resultado, 2)

def obtiene_cargas_familia(legajo, mes, year):

    """
    Obtiene el importe total a tomar en cuenta para el calculo de cargas familiares para la deducción del 
    primer párrafo.
    """
    
    #Inicialización de variables.
    resultado = 0
    v_hijo = 0
    v_hijo_inc = 0
    v_conyuge = 0

    #Obtiene el valor de la deducción hijo.
    query_hijo = DeduccionesPersonales.select(DeduccionesPersonales.importe).where(
                 DeduccionesPersonales.tipo == 'hijo', DeduccionesPersonales.year == year)

    for row in query_hijo:
        if row.importe != None:
            v_hijo += row.importe

    #Obtiene el valor de la deducción hijo incapacitado.
    query_hijo_inc = DeduccionesPersonales.select(DeduccionesPersonales.importe).where(
                 DeduccionesPersonales.tipo == 'hijo_inca', DeduccionesPersonales.year == year)
    
    for row in query_hijo_inc:
        if row.importe != None:
            v_hijo_inc += row.importe
    
    #Obtiene el valor de la deducción hijo incapacitado.
    query_cony = DeduccionesPersonales.select(DeduccionesPersonales.importe).where(
                     DeduccionesPersonales.tipo == 'conyuge', DeduccionesPersonales.year == year)
    
    for row in query_cony:
        if row.importe != None:
            v_conyuge += row.importe

    #Genera un array para buscar los valores correspondientes a mes hasta.
    
    mes_h = mes
    mes_d = mes
    lista_mes_h = list()
    lista_mes_d = list()
    
    while mes_h <= 12:
        lista_mes_h.append(str(mes_h))
        mes_h += 1

    while mes_d >= 1:
        lista_mes_d.append(str(mes_d))
        mes_d -= 1

    hijos_incapacitado = BaseDatos.CargasFamilia.select(BaseDatos.CargasFamilia.porcentaje_deduccion).where(
                         BaseDatos.CargasFamilia.legajo == legajo, BaseDatos.CargasFamilia.mes_desde.in_(lista_mes_d), 
                         BaseDatos.CargasFamilia.mes_hasta.in_(lista_mes_h), BaseDatos.CargasFamilia.parentesco.in_(['31', '32']),
                         BaseDatos.CargasFamilia.ann == year)

    for row in hijos_incapacitado:
        try:
            valor = float(row.porcentaje_deduccion)
            resultado += valor * v_hijo_inc / 100
            
        except:
            pass

    hijos = BaseDatos.CargasFamilia.select(BaseDatos.CargasFamilia.porcentaje_deduccion).where(
            BaseDatos.CargasFamilia.legajo == legajo, BaseDatos.CargasFamilia.mes_desde.in_(lista_mes_d), 
            BaseDatos.CargasFamilia.mes_hasta.in_(lista_mes_h), BaseDatos.CargasFamilia.parentesco.in_(['3', '30']),
            BaseDatos.CargasFamilia.ann == year)

    for row in hijos:
        try:
            valor = float(row.porcentaje_deduccion)
            resultado += valor * v_hijo / 100
        except:
            pass

    conyuge = BaseDatos.CargasFamilia.select(BaseDatos.CargasFamilia.cuil_empleado).where(
              BaseDatos.CargasFamilia.legajo == legajo, BaseDatos.CargasFamilia.mes_desde.in_(lista_mes_d), 
              BaseDatos.CargasFamilia.mes_hasta.in_(lista_mes_h), BaseDatos.CargasFamilia.parentesco == '1', 
              BaseDatos.CargasFamilia.ann == year)

    for row in conyuge:
            resultado += v_conyuge     

    return round(resultado, 2)


def primer_parrafo(legajo, mes, year):

    """
    Calcula la deducción especial correspondiente al primer párrafo de ganancias.
    """

    try:
    
        #Inicializa las variables.
        sbruto = 0
        ded = 0
        min_no_imp = 0
        ded_especial = 0
        cargas_familia = 0
        resultado = 0
        
        listado = list()

        #Obtiene el sueldo bruto.
        sueldo_bruto = BaseDatos.SueldosBrutos.select(BaseDatos.SueldosBrutos.importe).where(BaseDatos.SueldosBrutos.legajo == legajo,
                       BaseDatos.SueldosBrutos.mes == mes, BaseDatos.SueldosBrutos.ann == year)

        for row in sueldo_bruto:
            if row.importe != None:
                sbruto += round(row.importe, 2)

        sbruto += obtiene_remoe(legajo, mes, year)

        #Obtiene las deducciones.
        deduccion = BaseDatos.Deducciones.select(BaseDatos.Deducciones.importe).where(BaseDatos.Deducciones.legajo == legajo,
                    BaseDatos.Deducciones.mes == mes, BaseDatos.Deducciones.ann == year)

        for row in deduccion:
            if row.importe != None:
                ded += round(row.importe, 2)

        ded += obtiene_dedoe(legajo, mes, year)

        #Obtiene el importe total para cargas de familia 
        cargas_familia += obtiene_cargas_familia(legajo, mes, year)

        #Obtiene el valor de la deducción especial
        ded_esp = DeduccionesPersonales.select(DeduccionesPersonales.importe).where(
                  DeduccionesPersonales.tipo == 'ded_esp', DeduccionesPersonales.year == year)

        for row in ded_esp:
            if row.importe != None:
                ded_especial += row.importe

        #Obtiene el valor del minimo no imponible
        ganan_noimp = DeduccionesPersonales.select(DeduccionesPersonales.importe).where(
                      DeduccionesPersonales.tipo == 'ganan_no_imp', DeduccionesPersonales.year == year)
    
        for row in ganan_noimp:
            if row.importe != None:
                min_no_imp += row.importe

        resultado = sbruto - ded - ded_especial - min_no_imp - cargas_familia

        #Verifica que no haya importe negativo 
        
        if resultado < 0:
            resultado = 0
        else:
            resultado = round(resultado, 2)

        #Guarda los valores en un array.
        listado.append(legajo)
        listado.append(year)
        listado.append(mes)
        listado.append(sbruto)
        listado.append(ded)
        listado.append(ded_especial)
        listado.append(min_no_imp)
        listado.append(cargas_familia)
        listado.append(resultado)

        return listado

    except ErrorBruto:

        listado.append(legajo)
        listado.append(year)
        listado.append(mes)
        listado.append(0)
        listado.append(0)
        listado.append(0)
        listado.append(0)
        listado.append(0)
        listado.append(0)

        return listado


#Liquidador del segundo párrafo
##############################################################################################################
def segundo_parrafo(bruto, mes, y):

    rango = list() 
    resultado = 0 

    if y == 2022:

        query_deducciones = RangoSegundoParrafo.select(RangoSegundoParrafo.val_min, 
                            RangoSegundoParrafo.val_max, RangoSegundoParrafo.deduccion).where(
                            RangoSegundoParrafo.resolucion == 'RIPTE_2022')

        for row in query_deducciones:
            listado = list()
            listado.append(row.val_min)
            listado.append(row.val_max)
            listado.append(row.deduccion)
            rango.append(listado)

    if y == 2021 and mes < 9:
        
        query_deducciones = RangoSegundoParrafo.select(RangoSegundoParrafo.val_min, 
                            RangoSegundoParrafo.val_max, RangoSegundoParrafo.deduccion).where(
                            RangoSegundoParrafo.resolucion == 'RG_5008')
        
        for row in query_deducciones:
            listado = list()
            listado.append(row.val_min)
            listado.append(row.val_max)
            listado.append(row.deduccion)
            rango.append(listado)

    if y == 2021 and mes >= 9:
    
        query_deducciones = RangoSegundoParrafo.select(RangoSegundoParrafo.val_min, 
                            RangoSegundoParrafo.val_max, RangoSegundoParrafo.deduccion).where(
                            RangoSegundoParrafo.resolucion == 'RG_5076')
    
        for row in query_deducciones:
            listado = list()
            listado.append(row.val_min)
            listado.append(row.val_max)
            listado.append(row.deduccion)
            rango.append(listado)

    for valor in rango:
        if bruto > valor[0] and bruto <= valor[1]:
            resultado = valor[2]
            break

    return resultado


#Funciones para eliminar y guardar los registros de la primer y segunda deduccion en BBDD.
##############################################################################################################

def elimina_registro(legajo, ann, mes):
    
    query_pparrafo = BaseDatos.PrimerParrafo.delete().where(BaseDatos.PrimerParrafo.legajo == legajo,
                     BaseDatos.PrimerParrafo.ann == ann, BaseDatos.PrimerParrafo.mes == mes)

    query_pparrafo.execute()

    query_sparrafo = BaseDatos.SegundoParrafo.delete().where(BaseDatos.SegundoParrafo.legajo == legajo,
                     BaseDatos.SegundoParrafo.ann == ann, BaseDatos.SegundoParrafo.mes == mes)

    query_sparrafo.execute()

def guarda_p_parrafo(*args):
    
    p_parrafo = BaseDatos.PrimerParrafo()
    p_parrafo.legajo = args[0]
    p_parrafo.ann = args[1]
    p_parrafo.mes = args[2]
    p_parrafo.sbruto = args[3]
    p_parrafo.deducciones = args[4]
    p_parrafo.ded_esp = args[5]
    p_parrafo.min_no_imp = args[6]
    p_parrafo.cargas_familia = args[7]
    p_parrafo.ded_p_parrafo = args[8]
    p_parrafo.save()

def guarda_s_parrafo(*args):

    s_parrafo = BaseDatos.SegundoParrafo()
    s_parrafo.legajo = args[0]
    s_parrafo.ann = args[1]
    s_parrafo.mes = args[2]
    s_parrafo.ded_s_parrafo = args[3]
    s_parrafo.save()

#Liquidador
##############################################################################################################

def liquida(legajo, mes, year):

    try:
    
        #Inicialización de variables
        empleados = list()

        #Obtiene el listado de legajos a liquidar.

        query_promedios = BaseDatos.PromedioBruto.select(BaseDatos.PromedioBruto.legajo, BaseDatos.PromedioBruto.mes, 
                          BaseDatos.PromedioBruto.importe).where(BaseDatos.PromedioBruto.legajo == legajo, 
                          BaseDatos.PromedioBruto.ann == year, BaseDatos.PromedioBruto.mes == mes)

        for row in query_promedios:
            lista = list()
            lista.append(row.legajo)
            lista.append(row.mes)
            lista.append(row.importe)
            empleados.append(lista)

        for empleado in empleados:

            elimina_registro(empleado[0], year, mes)
            
            if empleado[2] > 0:
                
                if mes < 9 and year == 2021:

                    if empleado[2] < 150000:
                       pparrafo = primer_parrafo(empleado[0], mes, year)
                       guarda_p_parrafo(pparrafo[0], pparrafo[1], pparrafo[2], pparrafo[3], pparrafo[4], pparrafo[5],
                                        pparrafo[6], pparrafo[7], pparrafo[8])
                    else:
                        sparrafo = list()
                        sparrafo.append(empleado[0])
                        sparrafo.append(year)
                        sparrafo.append(empleado[1])
                        sparrafo.append(segundo_parrafo(empleado[2], mes, year))
                        guarda_s_parrafo(sparrafo[0], sparrafo[1], sparrafo[2], sparrafo[3])
                    
                if mes >= 9 and year == 2021:
        
                    if empleado[2] < 175000:
                        pparrafo = primer_parrafo(empleado[0], mes, year)
                        guarda_p_parrafo(pparrafo[0], pparrafo[1], pparrafo[2], pparrafo[3], pparrafo[4], pparrafo[5],
                                         pparrafo[6], pparrafo[7], pparrafo[8])
                    else:
                        sparrafo = list()
                        sparrafo.append(empleado[0])
                        sparrafo.append(year)
                        sparrafo.append(empleado[1])
                        sparrafo.append(segundo_parrafo(empleado[2], mes, year))
                        guarda_s_parrafo(sparrafo[0], sparrafo[1], sparrafo[2], sparrafo[3])
                
                if year == 2022:
    
                    if empleado[2] < 225937:
                        guarda_p_parrafo(pparrafo[0], pparrafo[1], pparrafo[2], pparrafo[3], pparrafo[4], pparrafo[5],
                                         pparrafo[6], pparrafo[7], pparrafo[8])
                    else:
                        sparrafo = list()
                        sparrafo.append(empleado[0])
                        sparrafo.append(year)
                        sparrafo.append(empleado[1])
                        sparrafo.append(segundo_parrafo(empleado[2], mes, year))
                        guarda_s_parrafo(sparrafo[0], sparrafo[1], sparrafo[2], sparrafo[3])

    except IndexError:
        pass