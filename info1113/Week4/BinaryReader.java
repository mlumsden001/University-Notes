import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class BinaryWriter {

  public static byte[] convert(int v) {
    byte[] b = new byte[4];
    

  }

  public static void main(String[] args){

    try {
      FileOutputStream f = new FileInputStream(args[0]);
      int v = 50;
      byte[] buffer = new convert(v);
      f.write(buffer);
    } catch (FileNotFoundException e){
        e.printStackTrace();
    } catch (IOException e){
      e.printStackTrace();
    }
  }
}
