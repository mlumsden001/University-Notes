import java.util.List;
import java.util.ArrayList;

interface Sequences {
	public void genSequence(int n);
	public void getIndex();
}

public class SequenceGenerator {

	public static void main(String[] args) {
		//List<Integer> sequence = new List<Integer>();
    //int[] sequence = [];
		Sequences s = new Sequences() {
    //  int[] sequence = new int[]();

			public void genSequence(int n) {
          int[] sequence = new int[n];
      	//List<Integer> sequence = new List<Integer>();
				for (int x = 0; x < n; x ++) {
					if (n < 0) {
						return null;
					}
					sequence.add(x);
				}
				return sequence;
			}

			public void getIndex() {
				return sequence.get(-1);
			}
		};
	}
}
