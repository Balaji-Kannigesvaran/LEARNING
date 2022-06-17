package Module2;

public class DiscountCalculator {
	public static void main (String[] args) {
		float amount;
		String foodItem = "poori";
		
		switch (foodItem) {
		case "Dosa":
			amount = 20;
			break;
		case "Idly":
			amount = 10;
			break;
		case "Pizza":
			amount = 100;
			break;
		case "Burger":
			amount = 80;
			break;
		case "Briyani":
			amount = 150;
			break;
		default:
			amount = 50;
			break;
		}
		System.out.print("Amount: " + amount);
	}

}
