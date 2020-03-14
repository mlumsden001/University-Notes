public class Sort3 {
	public static void main(String[] args) {
		int x = Integer.parseInt(args[0]);
		int y = Integer.parseInt(args[1]);
		int z = Integer.parseInt(args[2]);
		
		if(x >= y && x >= z) {
			System.out.println("x is the largest integer");
			if(y >= z) {
				System.out.println("y is the second largest integer");
				System.out.println("z is the small integer");
			}
			else if(z >= y) {
				System.out.println("z is the second largest integer");
				System.out.println("y is the smaller integer");
			}
		}
		else if(y >= x && x >= z) {
			System.out.println("y is the largest integer");
		 	if(x >= z) {
				System.out.println("x is the second largest integer");
				System.out.println("z is the smallest integer");
			}
			else {
				System.out.println("z is the second largest integer");
				System.out.println("x is the smallest integer");
			}
		}
		
		if(z >= y && z >= x) {
			System.out.println("z is the largest integer");
			if(x >= y) {
				System.out.println("x is the second largest integer");
				System.out.println("y is the smallest integer");
			}
			else if(y >= x) {
				System.out.println("y is the second largest integer");
				System.out.println("x is the smallest integer");

			}
		}
	}
}
