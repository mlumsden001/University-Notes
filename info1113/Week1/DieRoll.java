import java.util.Random;

public class DieRoll {
	public static void main(String[] args) {
		Random r = new Random();
		int number = r.nextInt(7);
	
	if(number >= 1) {
		System.out.println(number);	
	}
	}
}
