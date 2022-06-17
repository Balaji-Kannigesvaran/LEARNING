package Module2;

public class Factorial {
	public static void main (String[] args) {
		int num = 7;
		int i=1;
		int temp;
		int fact=1;
		while (i<=num) {
			temp = i;
			fact = fact*temp;
			i += 1;
		}
		System.out.println(fact);
	}
}


