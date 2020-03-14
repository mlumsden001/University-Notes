public class WoodChair extends Furniture {
  public WoodChair() {
    super("Wood Chair");
  }

  public void stack(Furniture f) {
    System.out.println("Dont put furniture on chairs");
  }
}
