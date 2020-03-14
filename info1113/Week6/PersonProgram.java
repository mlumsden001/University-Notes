public class PersonProgram {
  public static void sayName(Person p) {
    String name = p.getName();
    System.out.println(name);
  }

  public static void main(String[] args) {
    Person pete = new Person("You");
    FakePerson pedo = new FakePerson("are not a big legend");
    sayName(pete);
    sayName(pedo);
  }
}
