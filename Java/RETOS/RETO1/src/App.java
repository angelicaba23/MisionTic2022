import java.util.Scanner;

public class App {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        System.out.println("Ingrese el id: ");
        int _Id = sc.nextInt();

        System.out.println("Ingrese el la cedula del cliente: ");
        String _Cedula = sc.next();

        System.out.println("Ingrese el año de nacimiento del cliente: ");
        int _AnoNacimiento = sc.nextInt();

        System.out.println("Ingrese el id de la moto: ");
        String _Identificador = sc.next();

        System.out.println("Ingrese las horas de alquiler: ");
        int _Horas = sc.nextInt();

        System.out.println("Ingrese a cantidad de horas: ");
        int cantidadHoras = sc.nextInt();

        // clase + variable + new(para instanciar) + construcctor
        AlquilerMotoActuatica objAlquiler1 = new AlquilerMotoActuatica(_Id, _Cedula,_AnoNacimiento, _Identificador,_Horas);
        
        System.out.println(objAlquiler1.TerminarAlquiler(cantidadHoras));
    }
}
