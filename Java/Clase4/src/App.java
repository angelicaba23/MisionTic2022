import java.util.Scanner;

public class App {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        System.out.println("Ingrese el nombre: ");
        String nombre1 = sc.next();

        System.out.println("Ingrese la edad: ");
        int edad1 = sc.nextInt();

        System.out.println("Ingrese el email: ");
        String email1 = sc.next();

        // clase + variable + new(para instanciar) + construcctor
        Persona objPersona1 = new Persona(nombre1, edad1, email1);

        System.out.println("Ingrese el nombre: ");
        String nombre2 = sc.next();

        System.out.println("Ingrese la edad: ");
        int edad2 = sc.nextInt();

        System.out.println("Ingrese el email: ");
        String email2 = sc.next();

        Persona objPersona2 = new Persona(nombre2, edad2, email2);
        
        System.out.println(objPersona1);
        System.out.println(objPersona2);
    }
}
