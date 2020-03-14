import java.util.ArrayList;

public class Adult extends People {

  private ArrayList<People> children;

  public Adult(String name, int age, double height, double weight) {
    super(name, age, height, weight);
    this.children = new ArrayList<People>();
  }

  public void addChild(Child c) {
    this.children.add(c);
  }

  public String getChildren() {
    if (this.children.size() == 0) {
      System.out.println("No children");
    }
    int count = 0;
    System.out.print("Children: ");
    for (int i = 0; i < this.children.size(); i ++) {
      if (i == this.children.size() - 1) {
        System.out.println(this.children.get(i).getName() + " ");
      } else {System.out.print(this.children.get(i).getName() + " ");}
      count ++;
    }
    return null;
  }

}
