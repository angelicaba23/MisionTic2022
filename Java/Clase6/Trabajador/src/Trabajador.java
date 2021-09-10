public class Trabajador {

    //atributos
    private int id;
    private String nombre;
    private String apellido;

    //constructor
    public Trabajador(int id, String nombre, String apellido) {
    this.id = id;
    this.nombre = nombre;
    this.apellido = apellido;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    @Override
    public String toString() {
        return "Trabajador [apellido=" + apellido + ", id=" + id + ", nombre=" + nombre + "]";
    }
    
    public double pagarSalario(){
        return 0;
    }

}
