import java.util.Scanner;
public class ConversorMedidas
   {
    public static double metrosParaQuilometros(double metros) {
        return metros / 1000;
    }
    public static double metrosParaCentimetros(double metros) {
        return metros * 100;
    }
    public static double metrosParaMilimetros(double metros) {
        return metros * 1000;
    }
    public static double quilometrosParaMetros(double quilometros) {
        return quilometros * 1000;
    }
    public static double centimetrosParaMetros(double centimetros) {
        return centimetros / 100;
    }
    public static double milimetrosParaMetros(double milimetros) {
        return milimetros / 1000;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Conversor de Métricas");
        System.out.println("Escolha a unidade de entrada:");
        System.out.println("1. Metros");
        System.out.println("2. Quilômetros");
        System.out.println("3. Centímetros");
        System.out.println("4. Milímetros");
        int escolha = scanner.nextInt();

        System.out.print("Digite o valor a ser convertido: ");
        double valor = scanner.nextDouble();
        switch (escolha) {
            case 1: // M
                System.out.println(valor + " metros é igual a " + metrosParaQuilometros(valor) + " quilômetros");
                System.out.println(valor + " metros é igual a " + metrosParaCentimetros(valor) + " centímetros");
                System.out.println(valor + " metros é igual a " + metrosParaMilimetros(valor) + " milímetros");
                break;
            case 2: // Q
                System.out.println(valor + " quilômetros é igual a " + quilometrosParaMetros(valor) + " metros");
                break;
            case 3: // C
                System.out.println(valor + " centímetros é igual a " + centimetrosParaMetros(valor) + " metros");
                break;
            case 4: // Mm
                System.out.println(valor + " milímetros é igual a " + milimetrosParaMetros(valor) + " metros");
                break;
            default:
                System.out.println("Escolha inválida.");
                break;
        }

        scanner.close();
    }
}