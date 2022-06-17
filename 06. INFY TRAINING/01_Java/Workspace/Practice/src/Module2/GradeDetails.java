package Module2;

public class GradeDetails {
	public static void main (String[] args) {
		int mark = 65;
		if (mark<50) {
			System.out.print("Fail");
		}
		else if (mark>=50 && mark<60) {
			System.out.print("D");
		}
		else if (mark>=60 && mark<70) {
			System.out.print("C");
		}
		else if (mark>=70 && mark<80) {
			System.out.print("B");
		}
		else if (mark>=80 && mark<90) {
			System.out.print("A");
		}
		else if (mark>=90 && mark<100) {
			System.out.print("A+");
		}
		else {
			System.out.print("Invalid Input");
		}	
	}
}
