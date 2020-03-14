public class Plant {

	private boolean isAlive;
	private int soilMoistureLevel;
	private String nickname;
	private int height;

	public Plant(int height) {
		this("", height);
	}

	public Plant(String nickname, int height) {
		this.nickname = nickname;
		this.height = height;
		soilMoistureLevel = 0;
		isAlive = true;
	}
	
	public void setNickname(String nickname) {
		this.nickname = nickname;
	}

	public String getNickname() {
		return nickname;
	}

	public void water() {
		if(soilMoistureLevel > 5) {
			isAlive = false;
		}
		else {
			soilMoistureLevel ++;
		}
	}
	public boolean isDead() {
		return !isAlive;
	}
}
