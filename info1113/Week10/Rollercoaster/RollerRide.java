import java.util.List;
import java.util.ArrayList;
import java.io.*;
import java.lang.Exception;

public class RollerRide {

  public static boolean ageLimit(int age) {
    int limit = 6;
    if (age < limit) {
      return false;
    } else {
      return true;
    }
  }

  public static boolean heightLimit(double height) {
    double limit = 140.0;
    if (height < limit) {
      return false;
    } else {
      return true;
    }
  }

  public static void main(String[] args) {
    List<Person> people = new ArrayList<Person>();
  	RollPerson pete = new RollPerson("Pete", 10, 150.5);
		RollPerson tim = new RollPerson("Tim", 5, 80.2);
		RollPerson lisa = new RollPerson("Lisa", 24, 180.3);
		RollPerson john = new RollPerson("John", 30, 70.2);


    people.add(pete);
    people.add(tim);
    people.add(lisa);
    people.add(john);
		//john.canRide();
		//tim.canRide();
		//lisa.canRide();
		//pete.canRide();
    try {
      for (int i = 0; i < people.size(); i++) {
        if (people.get(i).ageLimit(people.get(i).getAge()) && people.get(i).heightLimit(people.get(i).getHeight())) {
    			System.out.println(people.get(i).getName() + " can ride the rollercoaster");
    		} else {
    			System.out.println(people.get(i).getName() + " cannot ride the rollercoaster");
    		}
      }
    }

    catch (ValueErrorException e) {
      e.printStackTrace();
    }

    if (john.ageLimit(john.getAge()) && john.heightLimit(john.getHeight())) {
			System.out.println(john.getName() + " can ride the rollercoaster");
		} else {
			System.out.println(john.getName() + " cannot ride the rollercoaster");
		}

		if (tim.ageLimit(tim.getAge()) && tim.heightLimit(tim.getHeight())) {
			System.out.println(tim.getName() + " can ride the rollercoaster");
		} else {
			System.out.println(tim.getName() + " cannot ride the rollercoaster");
		}

		if (pete.ageLimit(pete.getAge()) && pete.heightLimit(pete.getHeight())) {
			System.out.println(pete.getName() + " can ride the rollercoaster");
		} else {
			System.out.println(pete.getName() + " cannot ride the rollercoaster");
		}

    if (lisa.ageLimit(lisa.getAge()) && lisa.heightLimit(lisa.getHeight())) {
			System.out.println(lisa.getName() + " can ride the rollercoaster");
		} else {
			System.out.println(lisa.getName() + " cannot ride the rollercoaster");
		}
	}

}
