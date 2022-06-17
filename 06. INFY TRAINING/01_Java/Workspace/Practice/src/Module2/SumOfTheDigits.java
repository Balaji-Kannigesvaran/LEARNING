package Module2;

public class SumOfTheDigits {
	public static void main(String[] args) {
		int inputNumber = 281095;
		int sumOfDigits = 0;
		int temp = 0;
		while (inputNumber > 0) {
			temp = inputNumber % 10;
			sumOfDigits += temp;
			inputNumber = inputNumber / 10;
		}
		System.out.println("Sum of the digits: " + sumOfDigits);
	}
}
