import java.util.Scanner;

interface SayHello {
  public void hello();
  public void goodbye();
}

public class Hello {

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String name = scan.nextLine();
    SayHello h = new SayHello() {

      //String person = name;
      public void hello() {
        System.out.println("Hello " + person);
      }

      public void goodbye() {
        System.out.println("Goodbye " + person);
      }
    };

    h.hello();
    h.goodbye();
  }
}
