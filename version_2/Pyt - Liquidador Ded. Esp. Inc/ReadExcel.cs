using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DocumentFormat.OpenXml.Drawing.Diagrams;
using DocumentFormat.OpenXml.Office2013.Drawing.ChartStyle;
using DocumentFormat.OpenXml.Spreadsheet;
using DocumentFormat.OpenXml.Wordprocessing;
using Employees;
using SpreadsheetLight;

namespace ExcelFiles
{
    internal static class ReadExcel
    {
        public static List<EmployeeData> ImportEmployeesData(string file)
        {
            List<EmployeeData> employees = new List<EmployeeData>();

            SLDocument excelFile = new SLDocument(file);

            int column = 1;
            int row = 2;

            while (string.IsNullOrEmpty(excelFile.GetCellValueAsString(row, column)) == false)
            {
                // Declaración de variables.
                int legajo;
                long cuil;
                string apynom;
                DateTime fecing;

                // Lectura de archivo excel.
                string data = excelFile.GetCellValueAsString(row, 1);
                legajo = int.Parse(data);

                data = excelFile.GetCellValueAsString(row, 2);
                cuil = long.Parse(data);

                apynom = excelFile.GetCellValueAsString(row, 3);

                fecing = excelFile.GetCellValueAsDateTime(row, 4);

                employees.Add(new EmployeeData(legajo, cuil, apynom, fecing));

                // Verificación de existencia de datos en el archivo.
                if (string.IsNullOrEmpty(excelFile.GetCellValueAsString(row + 1, column)) == false)
                {
                    column = 1;
                    row++;
                }
                else
                {
                    break;
                }
            }

            return employees;
        }

        public static List<EmployeeSalary> ImportEmployeeSalary(string file)
        {
            List<EmployeeSalary> employeesalary = new List<EmployeeSalary>();

            SLDocument excelFile = new SLDocument(file);

            int column = 1;
            int row = 2;

            while(string.IsNullOrEmpty(excelFile.GetCellValueAsString(row, column)) == false) 
            {
                // Declaración de variables.
                int legajo;
                string apynom;
                byte anio;
                byte mes;
                decimal importe;

                // Lectura de archivo excel.
                string data = excelFile.GetCellValueAsString(row, 1);
                legajo = int.Parse(data);

                apynom = excelFile.GetCellValueAsString(row, 2);

                data = excelFile.GetCellValueAsString(row, 3);
                anio = byte.Parse(data);

                data = excelFile.GetCellValueAsString(row, 4);
                mes = byte.Parse(data);

                data = excelFile.GetCellValueAsString(row, 5);
                importe = decimal.Parse(data);

                employeesalary.Add(new EmployeeSalary(legajo, apynom, anio, mes, importe));

                // Verificación de existencia de datos en el archivo.
                if (string.IsNullOrEmpty(excelFile.GetCellValueAsString(row + 1, column)) == false)
                {
                    column = 1;
                    row++;
                }
                else
                {
                    break;
                }
            }

            return employeesalary;
        }

        public static List<EmployeeFamily> ImportEmployeeFamily(string file)
        {
            List<EmployeeFamily> employeeFamily = new List<EmployeeFamily>();

            SLDocument excelFile = new SLDocument(file);

            int column = 1;
            int row = 2;

            while (string.IsNullOrEmpty(excelFile.GetCellValueAsString(row, column)) == false)
            {
                // Declaración de variables.
                int legajo;
                long cuil;
                byte anio;
                byte tipdoc;
                long nrodoc;
                string apellido;
                string nombre;
                DateTime fecnac;
                byte mesdesde;
                byte meshasta;
                byte parentesco;
                byte porcentaje;

                // Lectura de archivo excel.
                string data = excelFile.GetCellValueAsString(row, 1);
                legajo = int.Parse(data);

                data = excelFile.GetCellValueAsString(row, 2);
                cuil = long.Parse(data);

                data = excelFile.GetCellValueAsString(row, 3);
                anio = byte.Parse(data);

                data = excelFile.GetCellValueAsString(row, 4);
                tipdoc = byte.Parse(data);

                data = excelFile.GetCellValueAsString(row, 5);
                nrodoc = long.Parse(data);

                apellido = excelFile.GetCellValueAsString(row, 6);
                nombre = excelFile.GetCellValueAsString(row, 7);

                data = excelFile.GetCellValueAsString(row, 8);
                fecnac = DateTime.Parse(data);

                data = excelFile.GetCellValueAsString(row, 9);
                mesdesde = byte.Parse(data);

                data = excelFile.GetCellValueAsString(row, 10);
                meshasta = byte.Parse(data);

                data = excelFile.GetCellValueAsString(row, 11);
                parentesco= byte.Parse(data);

                data = excelFile.GetCellValueAsString(row, 12);
                porcentaje = byte.Parse(data);

                employeeFamily.Add(new EmployeeFamily(legajo, cuil, anio, tipdoc, nrodoc,
                    apellido, nombre, fecnac, mesdesde, meshasta, parentesco, porcentaje));
                // Verificación de existencia de datos en el archivo.
                if (string.IsNullOrEmpty(excelFile.GetCellValueAsString(row + 1, column)) == false)
                {
                    column = 1;
                    row++;
                }
                else
                {
                    break;
                }
            }
            return employeeFamily;
        }

        public static List<EmployeeJobs> ImporteEmployeeJobs(string file)
        {
            List<EmployeeJobs> employeeJobs = new List<EmployeeJobs>();
            SLDocument excelFile = new SLDocument(file);

            int column = 1;
            int row = 2;
            
            while (string.IsNullOrEmpty(excelFile.GetCellValueAsString(row, column)) == false)
            {
                // Declaración de variables.
                int legajo;
                byte anio;
                long cuil;
                long cuit;
                string denominacion;
                byte mes;
                decimal obraSocial;
                decimal seguridadSocial;
                decimal sindicato;
                decimal gananciaBruta;
                decimal retencionGanancias;
                decimal retNoHabituales;
                decimal ajuste;
                decimal remuneracionExenta;
                decimal sac;
                decimal hsExtrasGravadas;
                decimal hsExtrasExentas;
                decimal materialDidactico;
                decimal movilidadViaticos;

                // Lectura de archivo excel.
                string data = excelFile.GetCellValueAsString(row, 1);
                legajo = int.Parse(data);

                data = excelFile.GetCellValueAsString(row, 2);
                anio = byte.Parse(data);

                data = excelFile.GetCellValueAsString(row, 3);
                cuil = long.Parse(data);

                data = excelFile.GetCellValueAsString(row, 4);
                cuit = long.Parse(data);

                denominacion = excelFile.GetCellValueAsString(row, 5);

                data = excelFile.GetCellValueAsString(row, 6);
                mes = byte.Parse(data);

                data = excelFile.GetCellValueAsString(row, 7);
                obraSocial = decimal.Parse(data);

                data = excelFile.GetCellValueAsString(row, 8);
                seguridadSocial= decimal.Parse(data);

                data = excelFile.GetCellValueAsString(row, 9);
                sindicato = decimal.Parse(data);

                data = excelFile.GetCellValueAsString(row, 10);
                gananciaBruta = decimal.Parse(data);

                data = excelFile.GetCellValueAsString(row, 11);
                retencionGanancias = decimal.Parse(data);

                data = excelFile.GetCellValueAsString(row, 12);
                retNoHabituales= decimal.Parse(data);

                data = excelFile.GetCellValueAsString(row, 13);
                ajuste = decimal.Parse(data);

                data = excelFile.GetCellValueAsString(row, 14);
                remuneracionExenta = decimal.Parse(data);

                data = excelFile.GetCellValueAsString(row, 15);
                sac = decimal.Parse(data);

                data = excelFile.GetCellValueAsString(row, 16);
                hsExtrasGravadas = decimal.Parse(data);

                data = excelFile.GetCellValueAsString(row, 17);
                hsExtrasExentas= decimal.Parse(data);

                data = excelFile.GetCellValueAsString(row, 18);
                materialDidactico= decimal.Parse(data);

                data = excelFile.GetCellValueAsString(row, 19);
                movilidadViaticos= decimal.Parse(data);

                employeeJobs.Add(new EmployeeJobs(
                    legajo,
                    anio, 
                    cuil, 
                    cuit, 
                    denominacion, 
                    mes, 
                    obraSocial,
                    seguridadSocial, 
                    sindicato,
                    gananciaBruta, 
                    retencionGanancias,
                    retNoHabituales,
                    ajuste, 
                    remuneracionExenta, 
                    sac, 
                    hsExtrasGravadas, 
                    hsExtrasExentas, 
                    materialDidactico, 
                    movilidadViaticos));
                
                // Verificación de existencia de datos en el archivo.
                if (string.IsNullOrEmpty(excelFile.GetCellValueAsString(row + 1, column)) == false)
                {
                    column = 1;
                    row++;
                }
                else
                {
                    break;
                }
            }
            return employeeJobs;
        }

        public static List<EmployeeDivision> ImportEmployeeDivisions(string file)
        {
            List <EmployeeDivision> employeeDivisions = new List<EmployeeDivision>();
            SLDocument excelFile = new SLDocument(file);

            int column = 1;
            int row = 2;

            while(string.IsNullOrEmpty(excelFile.GetCellValueAsString(row,column)) == false)
            {
                // Declaración de variables.
                int legajo;
                byte anio;
                byte mes;
                byte divisor;

                // Lectura de archivo excel.
                string data = excelFile.GetCellValueAsString(row, 1);
                legajo = int.Parse(data);

                data = excelFile.GetCellValueAsString(row, 2);
                anio = byte.Parse(data);

                data = excelFile.GetCellValueAsString(row, 3);
                mes = byte.Parse(data);

                data = excelFile.GetCellValueAsString(row, 4);
                divisor = byte.Parse(data);

                employeeDivisions.Add(new EmployeeDivision(legajo, anio, mes, divisor));

                // Verificación de existencia de datos en el archivo.
                if (string.IsNullOrEmpty(excelFile.GetCellValueAsString(row + 1, column)) == false)
                {
                    column = 1;
                    row++;
                }
                else
                {
                    break;
                }
            }
            return employeeDivisions;
        }
    }
}
