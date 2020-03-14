public class Container<T> {
	private T element;

	public Container(T element) {
		this.element = element;

	}

	public boolean isNull() {
		if (element == null) {
			return true;
		} else {
			return false;
		}
	}

	public void set(T newElement) {
		this.element = newElement;
	}

	public T get() {
		return element;
	}


	public static void main(String[] args) {
		Container<Integer> number = new Container<>(Integer.valueOf(5));
		Integer i = number.get();
		System.out.println(i);
	}
}
