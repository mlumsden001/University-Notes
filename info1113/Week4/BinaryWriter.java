import java.io.FileOutputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class BinaryWriter {

  public static byte[] convert(int v) {
    byte[] b = new byte[4];
    b[0] = (byte) (v >> 24);
    b[1] = (byte) (v >> 16);
    b[2] = (byte) (v >> 8);
    b[3] = (byte) v;
    return b;

  }

  public static void main(String[] args) {

    try {
      FileOutputStream f = new FileOutputStream(args[0]);
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
