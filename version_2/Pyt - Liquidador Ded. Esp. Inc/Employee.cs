using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Policy;
using System.Text;
using System.Threading.Tasks;

namespace Employees
{
    internal class Employee
    {
        public int Legajo { get; }

        // Mes del empleado a liquidar con el que
        // se obtendran los datos
        public byte Mes { get; }

        // Anio a procesar
        public short Anio { get; }

        //Constructor
        public Employee(int legajo, byte mes, short anio)
        {
            this.Legajo = legajo;
            this.Mes = mes;
            this.Anio = anio;
        }
    }
    internal class EmployeeData
    {
        public int Legajo { get; }
        public long Cuil { get; }
        public string NombreApellido { get; }
        public DateTime FecIng { get; }

        public EmployeeData(int legajo, long cuil, string nombreApellido, DateTime fecIng)
        {
            this.Legajo = legajo;
            this.Cuil = cuil;
            this.NombreApellido = nombreApellido;
            this.FecIng = fecIng;
        }
    }

    internal sealed class EmployeeSalary
    {
        public int Legajo { get; }
        public string NombreApellido {get;}
        public byte Anio { get; }
        public byte Mes { get; }
        public decimal Importe { get; }

        public EmployeeSalary(int legajo, byte anio, byte mes)
        {

        }

        public EmployeeSalary(int legajo, string nombreApellido, byte anio, byte mes, decimal importe)
        {
            this.Legajo = legajo;
            this.NombreApellido = nombreApellido;
            this.Anio = anio;
            this.Mes = mes;
            this.Importe = importe;
        }
    }

    internal sealed class EmployeeFamily
    {
        public int Legajo { get; }
        public long Cuil { get; }
        public byte Anio { get; }
        public byte TipoDoc { get; }
        public long NroDoc { get; }
        public string Apellido { get; }
        public string Nombre { get; }
        public DateTime FecNac { get; }
        public byte MesDesde { get; }
        public byte MesHasta { get; }
        public byte Parentesco { get; }
        public byte Porcentaje { get; }

        public EmployeeFamily(int legajo, byte anio, byte mes)
        {

        }

        public EmployeeFamily(int legajo, long cuil, byte anio, byte tipoDoc, long nroDoc, string apellido, string nombre, DateTime fecNac, byte mesDesde, byte mesHasta, byte parentesco, byte porcentaje)
        {
            this.Legajo = legajo;
            this.Cuil = cuil;
            this.Anio = anio;
            this.TipoDoc = tipoDoc;
            this.NroDoc = nroDoc;
            this.Apellido = apellido;
            this.Nombre = nombre;
            this.FecNac = fecNac;
            this.MesDesde = mesDesde;
            this.MesHasta = mesHasta;
            this.Parentesco = parentesco;
            this.Porcentaje = porcentaje;
        }
    }

    internal sealed class EmployeeJobs
    {
        public int Legajo { get; }
        public byte Anio { get; }
        public long Cuil { get; }
        public long Cuit { get; }
        public string Denominacion { get; }
        public byte Mes { get; }
        public decimal ObraSocial { get; }
        public decimal SeguridadSocial { get; }
        public decimal Sindicato { get; }
        public decimal GananciaBruta { get; }
        public decimal RetencionGanancias { get; }
        public decimal RetNoHabituales { get; }
        public decimal Ajuste { get; }
        public decimal RemuneracionExenta { get; }
        public decimal Sac { get; }
        public decimal HsExtrasGravadas { get; }
        public decimal HsExtrasExentas { get; }
        public decimal MaterialDidactico { get; }
        public decimal MovilidadViaticos { get; }

        public EmployeeJobs(int legajo, byte anio, byte mes)
        {

        }

        public EmployeeJobs(int legajo, byte anio, long cuil, long cuit, string denominacion, byte mes,
            decimal obraSocial, decimal seguridadSocial, decimal sindicato, decimal gananciaBruta, decimal retencionGanancias,
            decimal retNoHabituales, decimal ajuste, decimal remuneracionExenta, decimal sac, decimal hsExtrasGravadas,
            decimal hsExtrasExentas, decimal materialDidactico, decimal movilidadViaticos)
        {
            this.Legajo = legajo;
            this.Anio = anio;
            this.Cuil = cuil;
            this.Cuit = cuit;
            this.Denominacion = denominacion;
            this.Mes = mes;
            this.ObraSocial = obraSocial;
            this.SeguridadSocial= seguridadSocial;
            this.Sindicato = sindicato;
            this.GananciaBruta = gananciaBruta;
            this.RetencionGanancias = retencionGanancias;
            this.RetNoHabituales = retNoHabituales;
            this.Ajuste= ajuste;
            this.RemuneracionExenta = remuneracionExenta;
            this.Sac = sac;
            this.HsExtrasGravadas = hsExtrasGravadas;
            this.HsExtrasExentas = hsExtrasExentas;
            this.MaterialDidactico = materialDidactico;
            this.MovilidadViaticos = movilidadViaticos;
        }

    }

    internal sealed class EmployeeDivision
    {
        public int Legajo { get; }
        public byte Anio { get; }
        public byte Mes { get; }
        public byte Divisor { get; }

        public EmployeeDivision(int legajo, byte anio, byte mes)
        {

        }

        public EmployeeDivision(int legajo, byte anio, byte mes, byte divisor)
        {
            this.Legajo = legajo;
            this.Anio = anio;
            this.Mes = mes;
            this.Divisor = divisor;
        }
    }
}
