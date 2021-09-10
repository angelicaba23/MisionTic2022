import java.util.HashMap;

public class Alquiler {

    private int Id;
    private Persona Cliente;
    private MotoAcuatica Moto;

    public Alquiler(int id, Persona cliente, MotoAcuatica moto) {
        Id = id;
        Cliente = cliente;
        Moto = moto;
    }

    public Persona getCliente() {
        return Cliente;
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

    public static HashMap<String, Integer> AnalizarAlquileres(Alquiler[] historial){
        HashMap<String, Integer> resume = new HashMap<String, Integer>();

        int menor18 = 0;
        int entre18_30 = 0;
        int entre31_40 = 0;
        int entre41_50 = 0;
        int mayor50 = 0;

        for (int i = historial.length -1; i >= 0; i--){
            if(historial[i].Cliente.getEdad() <= 18){
                menor18++;
                resume.put("18 o menos", menor18);
            }
            if(historial[i].Cliente.getEdad() > 18 && historial[i].Cliente.getEdad() <= 30){
                entre18_30++;
                resume.put("18 –30", entre18_30);
            }
            if(historial[i].Cliente.getEdad() > 30 && historial[i].Cliente.getEdad() <= 40){
                entre31_40++;
                resume.put("31 –40", entre31_40);
            }
            if(historial[i].Cliente.getEdad() > 40 && historial[i].Cliente.getEdad() <= 50){
                entre41_50++;
                resume.put("31 –40", entre41_50);
            }
            if(historial[i].Cliente.getEdad() > 50){
                mayor50++;
                resume.put("51 o más", mayor50);
            }

        }
        return resume;
    }

    
    @Override
    public String toString() {
        return Cliente.getNombre() + " con cédula " + Cliente.getCedula() + " renta la moto " + Moto.getId() + " modelo " + Moto.getModelo() + "." ;
    }
}