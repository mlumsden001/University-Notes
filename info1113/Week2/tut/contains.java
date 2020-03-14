import java.util.*;

public class contains {

  static int contain(int[] a, int element) {
    int count = 0;
    for(int i = 0; i < a.length; i++) {
      if(a[i] == element) {
        count += 1;
      }
    }
    return count;
  }

  static int countDuplicates(int[] a) {
    int j = 0;
    List<Integer> foundDups = new ArrayList<>();
    for(int i = 0; i < a.length; i++) {
      while(j < a.length && !foundDups.contains(a[i]));
        if (a[i] == a[j]) {
          foundDups.add(a[i]);
        j++;
        }
    }
    return foundDups.size();
  }

  static int intersection(int[] x, int[] y) {
    int[] result = new int[x.length < y.length ? x.length : y.length];
    int n_results = 0;

    for (int i = 0; i < x.length; i++) {
      if (count(y, x[i]) > 0 && count(result, x[i]) == 0) {
        result[n_results++] = x[i];
      }

    }
    return result;

  }
  public static void main(String[] args) {
    int[] array1 = {1, 1, 5, 6, 3, 8, 1, 9, 2, 8, 4, 4};
    int[] array2 = {1, 5, 6, 12, 64, 9, 4, 3};

    int result = contain(array1, 1);
    System.out.println(result);

    int duplicates = countDuplicates(array1);
    System.out.println(duplicates);

    Arrays intersections = intersection(array1, array2);
    System.out.println(intersections);
  }

}
