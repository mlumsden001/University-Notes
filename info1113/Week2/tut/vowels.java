public class vowels {
	static int countVowels(String s) {
		int count = 0;
		for(int i = 0; i < s.length; i ++) {
			if(sa.charAt(i) == "a" || s.charAt(i) == "e" || s.charAt(i) == "i" || s.charAt(i) == "o"
				|| s.charAt(i) == "u") {
				count ++;
			}
		}
		return count;
	}
		public static void main(String[] args) {
		String s = "astronaut";
		int result = countVowels(s);
		System.out.println(result);

	}

}
