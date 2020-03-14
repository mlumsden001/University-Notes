import java.util.ArrayList;

public class Account {
  private String acctNumber;
  private String bsbNumber;
  private double interestRate;
  private double balance;
  private List<Transaction> transactions;

  public Account(String acctNum, String bsb, double intRate, double initBalance) {
    this.acctNumber = acctNum;
    this.bsbNumber = bsb;
    this.interestRate = intRate;

    if (initBalance >= 0) {
      balance = initBalance;
    }
    this.transactions = new ArrayList<>();
  }

  public List<Transaction> getTransaction() {
    return transactions;
  }

  public double deposit(double value) {
    
  }
}
