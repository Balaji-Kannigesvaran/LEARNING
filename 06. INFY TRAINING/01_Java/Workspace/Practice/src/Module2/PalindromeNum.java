package Module2;

public class PalindromeNum {
	public static void main(String[] args) {	
		int originalNum = 281095;
		int revNum = 0;
		int remainder;
		
		for (int num = originalNum; num!=0;) {
			remainder = num%10;
			revNum = revNum*10 + remainder;
			num = num/10;
		}
		if (originalNum == revNum) {
			System.out.println(originalNum);
//			System.out.println(num);
			System.out.println(revNum);
			System.out.println("It is a palindrome");
		} else {
			System.out.println(originalNum);
//			System.out.println(num);
			System.out.println(revNum);
			System.out.println("It is not a palindrome");			
		}
	}
}
