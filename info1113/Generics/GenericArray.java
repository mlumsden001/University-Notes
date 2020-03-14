import java.util.*;
import java.lang.IndexOutOfBoundsException;

public class GenericArray<T> {

	private T[] array;

	public GenericArray(int capacity) {
		this.array = (T[]) new Object[capacity];
	}

	public int size() {
		return this.array.length;
	}

	public void set(int index, T element) {
		this.array[index] = element;
	}

	public T get(int index) {
		if ((index + 1) > this.array.length || index < 0) {
			throw new IndexOutOfBoundsException();
		} else {
			return this.array[index];
		}
	}

	public int resize(int newSize) {
		int oldSize = this.size();
		T[] newArray = (T[]) new Object[(int) newSize];
		for (int i = 0; i < newSize; i ++) {
			newArray[i] = this.array[i];
		}
		return oldSize;
	}

	public static void main(String[] args) {
		GenericArray<Integer> arr = new GenericArray(10);
		arr.size();
		arr.set(0, Integer.valueOf(42));
		arr.set(5, Integer.valueOf(22));
		arr.set(9, Integer.valueOf(10));
		System.out.println(arr);

	}

}
