package Module2;

public class CustomerIDGenerator {
	public static void main(String[] args) {
		// The below code generates customerId
		String customerName = "Vaidheeswari";
		
		System.out.println("FOR LOOP");
		for (int i = 0 ; i < customerName.length() ; i++) {
			System.out.println(customerName.charAt(i));
		}
		
		System.out.println("WHILE LOOP");
		int j = 0;
		while (j<customerName.length()) {
			System.out.println(customerName.charAt(j));
			j++;
		}
		
		
	}
}
