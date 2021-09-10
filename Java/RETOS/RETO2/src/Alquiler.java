public class Alquiler {

    private int Id;
    private Persona Cliente;
    private MotoAcuatica Moto;

    public Alquiler(int id, Persona cliente, MotoAcuatica moto) {
        Id = id;
        Cliente = cliente;
        Moto = moto;
    }



    @Override
    public String toString() {
        return Cliente.getNombre() + " con cédula " + Cliente.getCedula() + " renta la moto " + Moto.getId() + " modelo " + Moto.getModelo() + "." ;
    }



    public double TerminarAlquiler(int cantidadHoras){
        int age = 1;
        int costoPorHora = 0;
        if (Cliente.getEdad() < 18){
            age = 2;
        }
        if (Moto.getMarca() == "Yamaha"){
            costoPorHora = 50000;
        }
        else if (Moto.getMarca() == "Kawasaki"){
            costoPorHora = 60000;
        }
        else if (Moto.getMarca() == "Sea-Doo"){
            costoPorHora = 60000;
        }
        return age*costoPorHora*cantidadHoras;
    }
}