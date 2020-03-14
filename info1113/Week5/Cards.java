public class Cards {

  protected String name;
  protected int id;

  public String getName() {
    return name;
  }

  public int getId() {
    return id;
  }

  public class BankCard extends Cards {
    protected float expiryDate;
    protected boolean securityChip;
    protected String bankName;

    this.name = name;
    this.id = id;

    public void setExpiry(float expiryDate) {
      
    }
  }
}
