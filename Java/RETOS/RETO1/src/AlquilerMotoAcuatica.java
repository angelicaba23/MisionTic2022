public class AlquilerMotoAcuatica {

    private int Id;
    private String CedulaCliente;
    private int AnoNacimientoCliente;
    private  String IdentificadorMoto;
    private int HorasAlquiler;


    //CONSTRUCTOR: para inicializar la clase
    public AlquilerMotoAcuatica(int _Id, String _Cedula,int _AnoNacimiento,String _Identificador,int _Horas){
        this.Id = _Id;
        this.CedulaCliente = _Cedula;
        this.AnoNacimientoCliente = _AnoNacimiento;
        this.IdentificadorMoto = _Identificador;
        this.HorasAlquiler = _Horas;
    }


    public double TerminarAlquiler(int cantidadHoras){
        
        if (cantidadHoras <= 0){
            return 0;
        }
        else if (cantidadHoras <= HorasAlquiler){
            return 40000*cantidadHoras;
        }
        else if (cantidadHoras > HorasAlquiler){
            if (cantidadHoras < HorasAlquiler+3){
                return (40000*cantidadHoras)+(40000*cantidadHoras*0.15);
            }
            else{
                return (40000*cantidadHoras)+(40000*cantidadHoras*0.30);
            }
        }
        else{
            return 0000;
        }
    }
}