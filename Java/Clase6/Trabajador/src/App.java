public class App {
    public static void main(String[] args) throws Exception {
        Trabajador objT1 = new Consultor(111, "AngelicaC", "Barranco", 10);
        Trabajador objT2 = new Operario(111, "Angelica", "Barranco", 10);


        System.out.println(objT1.getNombre() + objT1.pagarSalario());
        System.out.println(objT2.getNombre() + objT2.pagarSalario());

        Trabajador[] trabajador = new Trabajador[3];
        trabajador[0] = new Consultor(000,"d", "ds", 4);
        trabajador[2] = new Operario(222,"ssd", "ds", 3);
        trabajador[1] = new Consultor(111,"dsww", "ds", 5);

        for (int i = 0; i < trabajador.length; i++) {
            System.out.println(trabajador[i].getNombre()+" Salario " + trabajador[i].pagarSalario());
        }


    }
}
