import java.util.HashMap;

interface Operation {
  int apply(int x, int y);
}

public class IntCalculator {
  public static void main(String[] args) {
    HashMap<String, Operation> operations = new HashMap<>();

    operations.put("ADD", new Operation(){
      public int apply(int x, int y) {
        return x + y;
      }
    });
    operations.put("SUB", new Operation(){
      public int apply(int x, int y) {
        return x - y;
      }
    });
    operations.put("MUL", new Operation(){
      public int apply(int x, int y) {
        return x * y;
      }
    });

  System.out.println(operations.get("ADD").apply(2, 2));


  }
}
