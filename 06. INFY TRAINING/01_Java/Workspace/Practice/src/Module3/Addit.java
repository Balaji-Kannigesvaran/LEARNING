package Module3;

public class Addit {
	private int a;
	private int b;

	public Addit(int a, int b) {
		this.a = a;
		this.b = b;
	}

	public int addingTwoNum() {
		int sum = a + b;
		return sum;
	}

	public void setA(int a) {
		this.a = a;
	}

	public int getA() {
		return a;
	}

	public void setB(int b) {
		this.b = b;
	}

	public int getB() {
		return b;
	}
}
