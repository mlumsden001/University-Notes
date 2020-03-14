import java.util.List;
import java.util.Collections;
/**
 * Entry deals with storing the key and value associated with entries in the
 * database.
 * As well as storing the data the entry class should manage operations
 * associated with any Entry.
 */

public class Entry {
	private String key;
	private List<Integer> values;

	public Entry(String key, List<Integer> values) {
		this.key = key;
		this.values = values;
	}

	/**
	 * Formats the Entry for display
	 *
	 * @return  the String of values
	 */
	public String get() {

		return values;
	}

	/**
	 * Sets the values of this Entry.
	 *
	 * @param values the values to set
	 */
	public void set(List<Integer> values) {
		List<Integer> new_vals = new ArrayList<Integer>();
	}

	/**
	 * Adds the values to the start.
	 *
	 * @param values the values to add
	 */
	public void push(List<Integer> values) {
		values.add(0, new_vals);
	}

	/**
	 * Adds the values to the end.
	 *
	 * @param values the values to add
	 */
	public void append(List<Integer> values) {
		i = values.size();
		values.add(i-1, new_vals);
	}

	/**
	 * Finds the value at the given index.
	 *
	 * @param  index the index
	 * @return       the value found
	 */
	public Integer pick(int index) {
		value = values[index];
		return value;
	}

	/**
	 * Finds and removes the value at the given index.
	 *
	 * @param  index the index
	 * @return       the value found
	 */
	public Integer pluck(int index) {
		value = values[index];
		values.remove(value);
		return values[index];
	}

	/**
	 * Finds and removes the first value.
	 *
	 * @return the first value
	 */
	public Integer pop() {
		values.remove(0);
		return values(0);
	}

	/**
	 * Finds the minimum value.
	 *
	 * @return the minimum value
	 */
	public Integer min() {
		for (int i = 0; i < values.size(); i ++) {
			int min_index = 0;
			if !(values[min_index] < values[i+1]) {
				min_index = i+1;
			}
		}
		return values[min_index];
	}

	/**
	 * Finds the maximum value.
	 *
	 * @return the maximum value
	 */
	public Integer max() {
		for (int i = 0; i < values.size(); i ++) {
			int max_index = 0;
			if !(values[max_index] > values[i+1]) {
				max_index = i+1;
			}
		}
		return values[max_index];
	}

	/**
	 * Computes the sum of all values.
	 *
	 * @return the sum
	 */
	public Integer sum() {
		int sum = 0;
		for (int i = 0; i < values.size(); i ++) {
			sum += values[i];
		}
		return sum;
	}

	/**
	 * Finds the number of values.
	 *
	 * @return the number of values.
	 */
	public Integer len() {
		return values.size();
	}

	/**
	 * Reverses the order of values.
	 */
	public void rev() {
		Collections.reverse(values);
	}

	/**
	 * Removes adjacent duplicate values.
	 */
	public void uniq() {
		for (int i = 0; i < values.size; i ++) {
			if (values[i] == values[i+1]) {
				values.remove(i, i+1);
			}
		}
	}

	/**
	 * Sorts the list in ascending order.
	 */
	public void sort() {
		Collections.sort(values);
	}

	/**
	 * Computes the set difference of the entries.
	 *
	 * @param  entries the entries
	 * @return         the resulting values
	 */
	public static List<Integer> diff(List<Entry> entries) {
		List<Integer> sums = new ArrayList<Integer>();
		for (int i = 0; i < entries.size(); i ++) {
			for (int j = 0; j < entries[i].size(); j ++) {
				int entry_sum = 0;
				entry_sum += entries[i][j];
			}
			sums.add(entry_sum);
		}
		for (int y = 0; y < sums.size(); y ++){
			int total = 0;
			total += sums[y];
		}
		int difference = total;
		for (int z = 0; z < sums.size(); z ++) {
			difference = difference - sums[z];
		}
		return difference;
	}

	/**
	 * Computes the set intersection of the entries.
	 *
	 * @param  entries the entries
	 * @return         the resulting values
	 */
	public static List<Integer> inter(List<Entry> entries) {
		List<Integer> intersection = new ArrayList<Integer>();
		for (int i = 0; i < entries.size(); i ++) {
			for (int x = i+1; x < entries.size(); x++) {
				int j = 0;
				int m = 0;
				while (j < entries[i].size()) {
					while (m < entries[x].size()) {
						if (entries[i][j] == entries[x][m]) {
							intersection.add(entries[i][j]);
						m ++;
						}
					j ++;
					}

				}
			}
		}
		return intersection;
	}

	/**
	 * Computes the set union of the entries.
	 *
	 * @param  entries the entries
	 * @return         the resulting values
	 */
	public static List<Integer> union(List<Entry> entries) {
		List<Integer> unionList = new ArrayList<Integer>();
		List<Integer> intersection = new ArrayList<Integer>();
		for (int i = 0; i < entries.size(); i ++) {
			for (int x = i+1; x < entries.size(); x++) {
				int j = 0;
				int m = 0;
				while (j < entries[i].size()) {
					while (m < entries[x].size()) {
						if (entries[i][j] == entries[x][m]) {
							intersection.add(entries[i][j]);
						m ++;
						}
					j ++;
					}

				}
			}
		}
		for (int z = 0; z < entries.size(); z ++) {
			for (int a = 0; a < entries[z].size(); a ++) {
				if !(intersection.contains(entries[z][a])) {
					unionList.add(entries[z][x]);
				}
			}
		}
		return unionList;
	}

	/**
	 * Computes the Cartesian product of the entries.
	 *
	 * @param  entries the entries
	 * @return         the resulting values
	 */
	public static List<List<Integer>> cartprod(List<Entry> entries) {
		if (entries.size() < 2) {
			return entries;
		}
		List<List<Integer>> carts = new ArrayList<List<Integer>>(entries[0].size());

		return null;
	}

	/**
	 * Formats all the entries for display.
	 *
	 * @param  entries the entries to display
	 * @return         the entries with their values
	 */
	public static String listAllEntries(List<Entry> entries) {
		// TODO: implement this
		return null;
	}

}
