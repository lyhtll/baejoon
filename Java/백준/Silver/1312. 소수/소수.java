import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int num3 = sc.nextInt();
        int n=0;
        for (int i=0;i<num3;i++){
            num1=(num1%num2)*10;
            n= num1/num2;
        }
        System.out.println(n);
    }
}