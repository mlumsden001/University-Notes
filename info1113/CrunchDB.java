import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.*;
import java.io.*;

/**
 * This is responsible for the overall management of the database.
 * CrunchDB should deal with taking input from the user and displaying the correct
 * output while passing off the more complicated work to the corresponding
 * classes.
 */

public class CrunchDB {

	// TO DO the following data structures are responsible for storing the
	// entries and snapshots related to this instance of the database. You can
	// modify them if you wish, as long as you do not change any method
	// signatures.
	private List<Entry> entries;
	private List<Snapshot> snapshots;

	public CrunchDB(List<Entry> entries, List<Snapshot> snapshots) {
		this.entries = entries;
		this.snapshots = snapshots;
	}

	/**
	 * Displays all keys in current state.
	 */
	private void listKeys(List<Entry> entries) {
		List<String> keys = new ArrayList<String>();
		for (int i = 0; i < this.entries.size(); i ++) {
			keys.add(entries[i][0]);
		}
		return keys;
	}

	/**
	 * Displays all entries in the current state.
	 */
	private void listEntries() {
		return entries;
	}

	/**
	 * Displays all snapshots in the current state.
	 */
	private void listSnapshot() {
		return snapshots;
	}

	/**
	 * Displays entry values.
	 *
	 * @param key the key of the entry
	 */
	private void get(String key) {
		for (int i = 0; i < entries.size(); i ++) {
			if (entries[i][0] == key) {
				List<Integer> value = new ArrayList<Integer>();
				int k = 3;
				while (k < (entries[i].size()-1)) {
					value.add(entries[i][k]);
					k ++;
				}
				return value;
			}
		}
	}

	/**
	 * Deletes entry from current state.
	 *
	 * @param key the key of the entry
	 */
	private void del(String key) {
		for (int i = 0; i < entries.size(); i ++) {
			if (entries[i][0] == key) {
				entries.remove(i);
			}
		}
	}

	/**
	 * Deletes entry from current state and snapshots.
	 *
	 * @param key the key of the entry
	 */
	private void purge(String key) {
		// TODO: implement this
	}

	/**
	 * Sets entry values.
	 *
	 * @param key    the key of the entry
	 * @param values the values to set
	 */
	private void set(String key, List<Integer> values) {
		Set entry = new Set();
		entry.add(key);
		entry.add(values);
		entries.add(entry);
	}

	/**
	 * Pushes values to the front.
	 *
	 * @param key    the key of the entry
	 * @param values the values to push
	 */
	private void push(String key, List<Integer> values) {
		int index = 0;
		for (int i = 0; i < values.size(); i ++) {
			if (entries[i][0] == key) {
				index = i;
			}
		}
		values.push(index);
	}

	/**
	 * Appends values to the back.
	 *
	 * @param key    the key of the entry
	 * @param values the values to append
	 */
	private void append(String key, List<Integer> values) {
		int index = 0;
		for (int i = 0; i < values.size(); i ++) {
			if (entries[i][0] == key) {
				index = i;
			}
		}
		values.pop(index);
	}

	/**
	 * Displays value at index.
	 *
	 * @param key   the key of the entry
	 * @param index the index to display
	 */
	private void pick(String key, int index) {
		// TODO: implement this
	}

	/**
	 * Displays and removes the value at index.
	 *
	 * @param key   the key of the entry
	 * @param index the index to pluck
	 */
	private void pluck(String key, int index) {
		// TODO: implement this
	}

	/**
	 * Displays and removes the front value.
	 *
	 * @param key the key of the entry
	 */
	private void pop(String key) {
		// call pop
	}

	/**
	 * Deletes snapshot.
	 *
	 * @param id the id of the snapshot
	 */
	private void drop(int id) {
		// TODO: implement this
	}

	/**
	 * Restores to snapshot and deletes newer snapshots.
	 *
	 * @param id the id of the snapshot
	 */
	private void rollback(int id) {
		Snapshot.rollback(id);
	}

	/**
	 * Replaces current state with a copy of snapshot.
	 *
	 * @param id the id of the snapshot
	 */
	private void checkout(int id) {
		// TODO: implement this
	}

	/**
	 * Saves the current state as a snapshot.
	 */
	private void snapshot() {
		Snapshot(id, filename);
	}

	/**
	 * Saves snapshot to file.
	 *
	 * @param id       the id of the snapshot
	 * @param filename the name of the file
	 */
	private void archive(int id, String filename) {
		snapshot(id, filename);
	}

	/**
	 * Loads and restores snapshot from file.
	 *
	 * @param filename the name of the file
	 */
	private void restore(String filename) {
		Entry.restore(filename);
	}

	/**
	 * Displays minimum value.
	 *
	 * @param key the key of the entry
	 */
	private void min(String key) {
		Entry.min(key);
	}

	/**
	 * Displays maximum value.
	 *
	 * @param key the of the entry
	 */
	private void max(String key) {
		Entry.max(key);
	}

	/**
	 * Displays the sum of values.
	 *
	 * @param key the key of the entry
	 */
	private void sum(String key) {
		Entry.sum(key);
	}

	/**
	 * Displays the number of values.
	 *
	 * @param key the key of the entry
	 */
	private void len(String key) {
		Entry.len(key);
	}

	/**
	 * Reverses the order of values.
	 *
	 * @param key the key of the entry
	 */
	private void rev(String key) {
		Entry.rev(key);
	}

	/**
	 * Removes repeated adjacent values.
	 *
	 * @param key the key of the entry
	 */
	private void uniq(String key) {
		Entry.uniq(key);
	}

	/**
	 * Sorts values in ascending order.
	 *
	 * @param key the key of the entry
	 */
	private void sort(String key) {
		Entry.sort(key);
	}

	/**
	 * Displays set difference of values in keys.
	 * Needs at least two keys.
	 *
	 * @param keys the keys of the entries
	 */
	private void diff(List<String> keys) {
		Entry.diff(keys);
	}

	/**
	 * Displays set intersection of values in keys.
	 * Needs at least two keys.
	 *
	 * @param keys the keys of the entries
	 */
	private void inter(List<String> keys) {
		Entry.inter(keys);
	}

	/**
	 * Displays set union of values in keys.
	 * Needs at least two keys.
	 *
	 * @param keys the keys of the entries
	 */
	private void union(List<String> keys) {
		Entry.union(keys);
	}

	/**
	 * Displays cartesian product of the sets.
	 * Needs at least two keys.
	 *
	 * @param keys the keys of the entries
	 */
	private void cartprod(List<String> keys) {
		// TODO: implement this
	}

	private static final String HELP =
		"BYE   clear database and exit\n"+
		"HELP  display this help message\n"+
		"\n"+
		"LIST KEYS       displays all keys in current state\n"+
		"LIST ENTRIES    displays all entries in current state\n"+
		"LIST SNAPSHOTS  displays all snapshots in the database\n"+
		"\n"+
		"GET <key>    displays entry values\n"+
		"DEL <key>    deletes entry from current state\n"+
		"PURGE <key>  deletes entry from current state and snapshots\n"+
		"\n"+
		"SET <key> <value ...>     sets entry values\n"+
		"PUSH <key> <value ...>    pushes values to the front\n"+
		"APPEND <key> <value ...>  appends values to the back\n"+
		"\n"+
		"PICK <key> <index>   displays value at index\n"+
		"PLUCK <key> <index>  displays and removes value at index\n"+
		"POP <key>            displays and removes the front value\n"+
		"\n"+
		"DROP <id>      deletes snapshot\n"+
		"ROLLBACK <id>  restores to snapshot and deletes newer snapshots\n"+
		"CHECKOUT <id>  replaces current state with a copy of snapshot\n"+
		"SNAPSHOT       saves the current state as a snapshot\n"+
		"\n"+
		"ARCHIVE <id> <filename> saves snapshot to file"+
		"RESTORE <filename> loads snapshot from file"+
		"\n"+
		"MIN <key>  displays minimum value\n"+
		"MAX <key>  displays maximum value\n"+
		"SUM <key>  displays sum of values\n"+
		"LEN <key>  displays number of values\n"+
		"\n"+
		"REV <key>   reverses order of values\n"+
		"UNIQ <key>  removes repeated adjacent values\n"+
		"SORT <key>  sorts values in ascending order\n"+
		"\n"+
		"DIFF <key> <key ...>   displays set difference of values in keys\n"+
		"INTER <key> <key ...>  displays set intersection of values in keys\n"+
		"UNION <key> <key ...>  displays set union of values in keys"+
		"CARTPROD <key> <key ...>  displays set union of values in keys";

	public static void bye() {
		System.out.println("bye");
	}

	public static void help() {
		System.out.println(HELP);
	}


	public static void main(String[] args) {
		Scanner scan = new Scanner(String);
		String command = scan.nextLine();
		while (command != "BYE") {
			if (command == "HELP") {
				System.out.println(HELP);
			}
			if (command = "LIST KEYS") {

			}
		}
	}
}
