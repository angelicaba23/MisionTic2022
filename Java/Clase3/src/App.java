import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello!");
        
        System.out.println("Digite un numero entero");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        menorMayorMenor (n);

        System.out.println("1. Suma \n" +
                           "2. Resta \n" +
                           "3. Multiplicación \n" +
                           "4. División \n" +
                           "Seleccione una opción:");
        int op = sc.nextInt();
        calculadora (op);



    }

    public static void menorMayorMenor (int n){
        if (n < 0){
            System.out.println("Es menos que 0");
        }else if (n == 0){
            System.out.println("Es igual a 0");
        }else{
            System.out.println("Es mayor que 0");
        }
    }
    public static void calculadora (int op){
        System.out.println("Digite el numero 1");
        int n1 = sc.nextInt();
        System.out.println("Digite el numero 2");
        int n2 = sc.nextInt();
        switch (op){
            case 1: System.out.println("Suma");
                    break;
            case 2: System.out.println("Resta");
                    break;   
            case 3: System.out.println("Multiplicación");
                    break;
            case 4: System.out.println("División");
                    break; 
            default: System.out.println("La opcción seleccionada no es correcta");
                    break;
        }  
    }
}
