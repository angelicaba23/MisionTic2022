public class Cliente {

    private String cedula;
    private String nombre;
    private int puntos;

    public Cliente(String cedula, String nombre, int puntos) {
        this.cedula = cedula;
        this.nombre = nombre;
        this.puntos = puntos;
    }

    public String getCedula() {
        return cedula;
    }

    public void setCedula(String cedula) {
        this.cedula = cedula;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getPuntos() {
        return puntos;
    }

    public void setPuntos(int puntos) {
        this.puntos = puntos;
    }

    @Override
    public String toString() {
        return "Cliente [cedula=" + cedula + ", nombre=" + nombre + ", puntos=" + puntos + "]";
    }

    
}

