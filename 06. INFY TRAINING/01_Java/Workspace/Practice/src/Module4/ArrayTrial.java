package Module4;

class Dummy{
	private int[] inputArray = { 3, 2, 3, 6 };
	public int[] getArray() {
		return inputArray;
	}
}

public class ArrayTrial {
	public static void main(String[] args) {
		Dummy d = new Dummy();

		for (int i = 0; i < d.getArray().length; i++) {
			if(d.getArray()[i]==3) {
				System.out.println("3 is there "+ d.getArray()[i]);
			} else {
				System.out.println("3 is not there "+ d.getArray()[i]);
			}
		}
	}
}
