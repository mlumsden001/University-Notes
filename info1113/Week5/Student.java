import java.util.ArrayList;

public class Student extends Person {
  private long studentId;
  private List<Integer> results = new ArrayList(String);

  public List<Integer> getResults() {
    return results;
  }
}
