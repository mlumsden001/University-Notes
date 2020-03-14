public class Transaction extends Account{
  private String date;
  private String description;
  private double amount;

  public Transaction(String date, String desc, double amount) {
    this.date = date;
    this.description = desc;
    this.amount = amount;
  }

  public String getDate() {
    return date;
  }

  public String getDescription() {
    return description;
  }

  public double getAmount() {
    return amount;
  }
}
