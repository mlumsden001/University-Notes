import java.lang.Math;
import java.net.HttpURLConnection;
import java.net.URL;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.io.IOException;
import java.lang.StringBuffer;
import java.io.BufferedReader;
import java.util.Map;
import java.util.HashMap;

public class Api_Workspace {

  //Fetches all exchange rate data from API
  public static String getRates(String currency) throws IOException {

    URL urlForGetRequest = new URL("https://api.exchangeratesapi.io/latest?base=" + currency);
    String readLine = null;
    HttpURLConnection conection = (HttpURLConnection) urlForGetRequest.openConnection();
    conection.setRequestMethod("GET");
    conection.setRequestProperty("userId", "a1bcdef"); // set userId its a sample here
    int responseCode = conection.getResponseCode();

    if (responseCode == HttpURLConnection.HTTP_OK) {
        BufferedReader in = new BufferedReader(
            new InputStreamReader(conection.getInputStream()));
        StringBuffer response = new StringBuffer();
        while ((readLine = in .readLine()) != null) {
            response.append(readLine);
        } in .close();
        // print result

        String data = response.toString();
        return data;
    } else {
      return "GET DIDN'T WORK";
    }
  }

  public static double findRate(String base, String currency) throws IOException {
    String data = Api_Workspace.getRates(base);
    if (currency == "AUD") {
      return 1;
    } else {
      int index = data.indexOf(currency);
      int start_index = index + 5;
      int end_index = start_index;
      char comma = ',';
      for (int i = end_index; i < data.length(); i ++) {
        if (data.charAt(i) == comma) {
          String str_rate = data.substring(start_index, end_index);
          double rate = Double.parseDouble(str_rate);
          String test = data.substring(data.indexOf(str_rate) - 5, data.indexOf(str_rate) - 2);
          System.out.println(test);
          return rate;
        }
        end_index ++;
      }

      return -1;
    }
  }

  public static double calculator(String current_currency, double amount, String converted_currency) throws IOException{
    double exchange_rate = Api_Workspace.findRate(current_currency, converted_currency);
    return (double)Math.round((amount * exchange_rate) * 100d) / 100d;
  }


  public static void main(String[] args) throws IOException {
      System.out.println(Api_Workspace.getRates("AUD"));
      System.out.println(Api_Workspace.findRate("AUD", "USD"));
      System.out.println(Api_Workspace.calculator("AUD", 100, "USD"));
  }
}
