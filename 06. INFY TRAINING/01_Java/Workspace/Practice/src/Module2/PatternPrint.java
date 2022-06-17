package Module2;

public class PatternPrint {
	public static void main(String[] args) {
		int rows = 5;
		for (int i = 1; i <= rows; ++i) {
			for (int j = 1; j <= i; ++j) {
				// print displays the text without adding a new line
				System.out.print(j + " "); 
			}
			//println displays the text along with a new line
			System.out.println(""); 
		}
	}
}
