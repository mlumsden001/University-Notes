
public class Card {
  private String cardType;
  private String[] data;

  public

  public Cards(String cardType, String[] cardInformation) {
    this.cardType = cardType;
    this.data = cardInformation;
  }

  public String getCardType() {
    return cardType;
  }

  public void setCardType(String type) {
    this.cardType = type;
  }

  public String[] getInformation() {
    return data;
  }

  public void setInformation(String[] cardInformation) {
    this.data = cardInformation;
  }


}
