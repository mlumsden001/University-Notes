import java.util.HashMap;

interface Operation {
  int apply(int x, int y);
}


public class HelloLambda {

  public static void main(String[] args) {

    HashMap<String, Operation> operations = new HashMap<>();

    operations.put("ADD", (x, y) -> x + y);
    operations.put("SUB", (x, y) -> x - y);
    operations.put("MUL", (x, y) -> x * y);

    System.out.println(operations.get("ADD").apply(2, 2));


  }
}
