import java.util.List;
import java.util.ArrayList;

public abstract class Furniture {
  private String name;
  private List<Part> parts;

  public Furniture(String name) {
    this.name = name;
    this.parts = new ArrayList<Part>();
  }

  public void addPart(Part p) {
    parts.add(p);
  }

  public abstract void stack(Furniture f);


}
