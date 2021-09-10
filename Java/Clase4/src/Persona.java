public class Persona {

    private String nombre;
    private int edad;
    private  String correoElectronico;

    //CONSTRUCTOR: para inicializar la clase
    public Persona(String nombre, int edad, String correoElectronico){
        this.nombre = nombre;
        this.edad =edad;
        this.correoElectronico = correoElectronico;
    }

    public String registrarHoras(int n){
        return "Las horas trabajadas fueron" + n;
    }
    
    public void validar(){
        System.out.println("Estamos validando..");
    }

    public String toString(){
        return 
            " \n" +
            " \n Nombre: " + nombre +
            " \n Edad: " + edad +
            " \n email: " + correoElectronico
        ;
    }
}