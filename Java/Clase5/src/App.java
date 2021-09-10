public class App {
    
    public static void main(String[] args) {
        
        //creación del objeto
        Persona objPersona1;
        objPersona1 = new Persona("Byron", 20, "b@gmail.com");
        
        Persona objPersona2 = new Persona("Patricia", 65, "pato@gmail.com");

        System.out.println(objPersona1);
        System.out.println(objPersona2);

        System.out.println(objPersona1.registrarHoras(10));
        objPersona1.validar();
        objPersona2.validar();

        System.out.println(objPersona2.tablaMultiplicarFor(5));
        System.out.println(objPersona2.tablaMultiplicarWhile(6));
        
        objPersona1.setNombre("HOLAA");
        System.out.println(objPersona1.getNombre());

    }

}
