package Module2;

public class Quiz {

	public static void main(String[] args) {
		int[] arr1 = {1,2,3,55,66,88,44,55};

		for (int i=0; i < arr1.length; i++) {
			if (arr1[i]==55) {
				System.out.println(arr1[i]);
				break;
			}	
		}
	}
}
