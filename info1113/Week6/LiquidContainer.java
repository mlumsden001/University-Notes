interface LiquidContainer {
  public void pour(double litres);

  public default pourInto(LiquidContainer container, double litres) {
    if(container != null) {
      pour(litres);
      container.fill(litres);
    }
    else {
      pour(litres);
    }
  }

  public void fill(double litres);
}

public class LiquidContainer {
  private double litres;
  public LiquidContainer(double litres) {
    this.litres = litres;
  }


  public static void main(String[] args) {
    CoffeeCup c = new CoffeeCup(0);
    CoffeeShot s = new CoffeeShot(5);
    CoffeeShot m = new CoffeeShot(10);
    LiquidContainer container = new LiquidContainer(0);

    s.pourInto(container, )


  }
}
