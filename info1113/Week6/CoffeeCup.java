public class CoffeeCup implements LiquidContainer {

  private double litres = 0;

  public CoffeeCup(double litres) {
    this.litres = litres;
  }
  public void pour(double litres) {
    this.litres -= litres;
  }

  public void fill(double litres) {
    this.litres += litres;
  }
}
