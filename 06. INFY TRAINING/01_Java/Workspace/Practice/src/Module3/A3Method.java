package Module3;

class Calci {
	public int num;
	public int sumOfDigits() {
		int temp = 0;
		int sumOfDigits = 0;
		while (num>0) {
			temp = num%10;
			sumOfDigits += temp;
			num /=10;		
		}
		return sumOfDigits;
	}
}

public class A3Method {
	public static void main (String[] args) {
		Calci calculator = new Calci();
		calculator.num = 6547;
		int sumOfDigits = calculator.sumOfDigits();
		System.out.println(sumOfDigits);
	}
}
