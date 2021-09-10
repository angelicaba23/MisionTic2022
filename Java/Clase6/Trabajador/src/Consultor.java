public class Consultor extends Trabajador{
    
    private int diasLaborados;

    public Consultor(int id, String nombre, String apellido, int diasLaborados) {
        super(id, nombre, apellido);
        this.diasLaborados = diasLaborados;
    }

    public int getDiasLaborados() {
        return diasLaborados;
    }

    public void setDiasLaborados(int diasLaborados) {
        this.diasLaborados = diasLaborados;
    }

    @Override
    public String toString() {
        return "Consultor [diasLaborados=" + diasLaborados + "]";
    }

    public double pagarSalario(){
        return diasLaborados*3000;
    }
}
