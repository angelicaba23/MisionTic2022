public class Persona {

    //private final static String NOMBRE = "Jhon"; //Declaración de una Constante en Java

    //Atributos de la clase
    private String nombre;
    private int edad;
    private String correoElectronico;

    //Constructor de la clase
    public Persona(String nombre, int edad, String correoElectronico){
        this.nombre = nombre;
        this.edad = edad;
        this.correoElectronico = correoElectronico;
    }

    //Métodos de la clase

    
    /**
     * Registra las horas del trabajador por jornada laboral
     */
    public String registrarHoras(int n){
        return "Las horas trabajadas fueron " + n;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getCorreoElectronico() {
        return correoElectronico;
    }

    public void setCorreoElectronico(String correoElectronico) {
        this.correoElectronico = correoElectronico;
    }

    public void validar(){
        System.out.println(nombre + ".......Estamos validando...");
    }

    //Método para obtener la tabla de multiplicar de un número que se pasa como parámetro del método (Estructura for).
    public String tablaMultiplicarFor(int numero){
        String cadena = "";        
        for(int i = 0; i <= 10; i++){
            cadena += (numero + " X " + i + " = " + (numero*i) + "\n");
        }
        return cadena;  
    }

    //Método para obtener la tabla de multiplicar de un número que se pasa como parámetro del método (Estructura for).
    public String tablaMultiplicarWhile(int numero){  
        String cadena = "";
        int i = 0;  
        while(i <= 10){
            cadena += (numero + " X " + i + " = " + (numero*i) + "\n");
            i++;
        }
        return cadena;  
    }

    @Override
    public String toString() {
        return "Persona [Correo Electrónico=" + correoElectronico + ", edad=" + edad + ", nombre=" + nombre + "]";
    }

/*    public String toString(){
        return "Nombre: " + nombre + " Edad: " + edad + " Correo Electrónico: " + correoElectronico;
    }
*/
}
