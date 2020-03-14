public class Grade {
	public static void main(String[] args) {
		int grade = Integer.parseInt(args[0]);
		
		if(grade >= 85) {
			System.out.println("High Distinction");
		}
		
		else if(grade < 85 && grade >= 75) {
			System.out.println("Distinction");
		}
		
		else if(grade < 75 && grade >= 65) {
			System.out.println("Credit");
		}

		else if(grade < 65 && grade >= 50) {
			System.out.println("Pass");
		}

		else {
			System.out.println("Fail");
		}
	}
}
