import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello!");
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Digite el numero 1");
        int numOne = sc.nextInt();
        System.out.println("Digite el numero 2");
        int numTwo = sc.nextInt();

        System.out.println("Suma: "+sumar(numOne,numTwo));
    }
    public static int sumar(int a, int b) {
        return a+b;
    }
}
