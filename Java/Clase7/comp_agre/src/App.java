public class App {
    public static void main(String[] args) throws Exception {
        Cliente cliente = new Cliente("112231", "Juancho", 20100);
        Empleado empleado = new Empleado("21211","Jesu");
        Supermercado surtimax = new Supermercado("Surtimax", empleado);
        
        System.out.println(surtimax);
        surtimax.mostrarPuntosCliente(cliente);
    }
}
