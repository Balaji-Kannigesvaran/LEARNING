package Module5;
import java.util.Scanner;
class Tester{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter a: ");
		int a = sc.nextInt();
		System.out.println("Enter b: ");
		int b = sc.nextInt();
		int c;
		try {
			if (a==0) {
				throw new Exception ("Numerator cannot be Zero");
			}
			c = a/b;
			System.out.println(c);
		}
		catch (ArithmeticException e1) {
			System.out.println("You cannot give Zero in Denominator");
		}
		catch (Exception e) {
			System.out.println("Something Wrong");
			System.out.println(e.getMessage());
		}
		finally {
			System.out.println("Have a  Happy day");
		}
		
	}
}