public class Operario extends Trabajador {

    private int horasTrabajadas;


    public Operario(int id, String nombre, String apellido, int horasTrabajadas) {
        super(id, nombre, apellido);
        this.horasTrabajadas = horasTrabajadas;
    }


    public int getHorasTrabajadas() {
        return horasTrabajadas;
    }


    public void setHorasTrabajadas(int horasTrabajadas) {
        this.horasTrabajadas = horasTrabajadas;
    }


    @Override
    public String toString() {
        return "Operario [horasTrabajadas=" + horasTrabajadas + "]";
    }


    public double pagarSalario(){
        return horasTrabajadas*2000;
    }
    
}
