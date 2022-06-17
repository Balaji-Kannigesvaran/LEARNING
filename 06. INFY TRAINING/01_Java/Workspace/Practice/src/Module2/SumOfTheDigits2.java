package Module2;

public class SumOfTheDigits2 {
	public static void main(String[] args) {
		int inputNumber = 281095;
		int sumOfDigits = 0;
		int temp = 0;

		do {
			temp = inputNumber % 10;
			sumOfDigits += temp;
			inputNumber = inputNumber / 10;
		} while (inputNumber > 0);
		System.out.println("Sum of the digits: " + sumOfDigits);
	}
}
