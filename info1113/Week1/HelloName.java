import java.util.Scanner;

public class HelloName {

	public static void main(String[] args) {
		System.out.print("Hi, what is your name? ");
		Scanner scan = new Scanner(System.in);
		String name = scan.nextLine();
		System.out.printf("Hello %s\n", name);

	}
}
