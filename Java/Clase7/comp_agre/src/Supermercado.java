public class Supermercado {
    
    private String nombreSupermercado;
    private Empleado empleado;

    public Supermercado(String nombreSupermercado, Empleado empleado) {
        this.nombreSupermercado = nombreSupermercado;
        this.empleado = empleado;
    }

    public String getNombreSupermercado() {
        return nombreSupermercado;
    }

    public Empleado getEmpleado() {
        return empleado;
    }

    @Override
    public String toString() {
        return "Supermercado [empleado=" + empleado + ", nombreSupermercado=" + nombreSupermercado + "]";
    }

    public void mostrarPuntosCliente(Cliente cliente){
        System.out.println(cliente);
    }
    
}
