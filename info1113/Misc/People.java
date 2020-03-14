public class People {
  private String name;
  private int age;
  private double height;
  private double weight;

  public People(String name, int age, double height, double weight) {
    this.name = name;
    this.age = age;
    this.height = height;
    this.weight = weight;
  }

  public String getName() {
    return this.name;
  }

  public int getAge() {
    return this.age;
  }

  public double getHeight() {
    return this.height;
  }

  public double getWeight() {
    return this.weight;
  }

  public static void main(String[] args) {
    Adult mary = new Adult("Mary", 40, 182.05, 67.89);
    Child tom = new Child("Tom", 10, 145.20, 54.43);
    Child martin = new Child("Martin", 16, 178.20, 79.22);
    Adult chris = new Adult("Chris", 59, 182.44, 110.11);
    mary.addChild(tom);
    mary.addChild(martin);
    System.out.println("Name: " + mary.getName());
    System.out.println("Age: " + mary.getAge());
    System.out.println("Height: " + mary.getHeight() + "cm");
    System.out.println("Weight: " + mary.getWeight() + "kg");
    mary.getChildren();
    System.out.println("");

    System.out.println("Name: " + chris.getName());
    System.out.println("Age: " + chris.getAge());
    System.out.println("Height: " + chris.getHeight() + "cm");
    System.out.println("Weight: " + chris.getWeight() + "kg");
    chris.getChildren();



  }
}
