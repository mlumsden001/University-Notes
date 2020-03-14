import java.util.List;
import java.util.Collections;
/**
 * Snapshot deals with storing the id and current state of the database.
 * As well as storing this data, the Snapshot class should manage operations
 * related to snapshots.
 */

public class Snapshot {
	private int id;
	private List<Entry> entries;

	public Snapshot(int id, List<Entry> entries) {
		this.id = id;
		this.entries = entries;
	}

	/**
	 * Finds and removes the key.
	 *
	 * @param key the key to remove
	 */
	public void removeKey(String key) {
		for (int i = 0; i < entries.size(); i ++) {
			if (entries[i][0] == key) {
				entries[i].remove(key);
			}
		}
	}

	/**
	 * Finds the list of entries to restore.
	 *
	 * @return the list of entries in the restored state
	 */
	public List<Entry> rollback() {

	}


	/**
	 * Saves the snapshot to file.
	 *
	 * @param filename the name of the file
	 */
	public void archive(String filename) {
		File f = new File(filename);
		try {
			BufferedWriter writer = new BufferedWriter(new FileWriter(filename));
			String values;
			for (Entry x: this.entries) {
				values = x.get();
				values = x.replace("[", "").replace("]", "").replace(" ", "");
				writer.write(x.getKey() + "|" | values | "\n");
			}
			writer.close();
    }
		  catch (FileNotFoundException i) {
			i.printStackTrace();
		}
		  catch (IOException i) {
			i.printStackTrace();
		}
	}

	/**
	 * Loads and restores a snapshot from file.
	 *
	 * @param  filename the name of the file
	 * @return          the list of entries in the restored state
	 */
	public static List<Entry> restore(String filename) {
		// TODO: implement this
		return null;
	}

	/**
	 * Formats all snapshots for display.
	 *
	 * @param  snapshots the snapshots to display
	 * @return           the snapshots ready to display
	 */
	public static String listAllSnapshots(List<Snapshot> snapshots) {

		return snapshots;
	}
}
