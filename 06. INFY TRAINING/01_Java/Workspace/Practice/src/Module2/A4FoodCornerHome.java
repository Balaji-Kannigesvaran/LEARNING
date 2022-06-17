package Module2;

public class A4FoodCornerHome {
	public static void main (String[] args) {
		String typeOfFood = "V";
		int qty = 1;
		float distance = 7f;
		float finalBillAmount;
		int pricePerUnit;
		if (typeOfFood == "V" || typeOfFood == "N") {			
			if(typeOfFood =="V") {
				pricePerUnit = 12;
			}		
			else {
				pricePerUnit = 15;
			}		
			if (qty>=1 && distance>0) {				
				if (distance<=3) {
					finalBillAmount=(pricePerUnit*qty)+0;
				}				
				else if (distance<=6) {
					finalBillAmount=(pricePerUnit*qty)+((3*0)+(distance-3)*1);
				}
				else {
					finalBillAmount=(pricePerUnit*qty)+((3*0)+(3*1)+((distance-6)*2));
				}
			}
			else {
				finalBillAmount = -1;
			}
		}
		else {
			finalBillAmount = -1;
		}
		System.out.println(finalBillAmount);
	}
}
