public class CoffeeShot implements LiquidContainer {

  private double litres = 0;
  public CoffeeShot(double litres) {
    this.litres = litres;
  }

  public void pour(double litres) {
    this.litres -= litres;
  }

  public void fill(double litres) {
    this.litres += litres;
  }
}
