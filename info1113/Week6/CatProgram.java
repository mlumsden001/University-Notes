public class CatProgram {

  public static void main(String[] args) {
    Cat[] cats = {new Cat("Felix"), new DomesticCat("Garfield"), new Lion("Simba:")
    };
    for (Cat c : cats) {
      c.makeNoise();
    }

  }
}
