package StaticTry;

public class Customer {
	public int id = 1;
	public static int count = 500;
	
	public static void payBillStaticMethod() {
		count++;
		//static method cant access non static variable
		//id++;
	}
	
	public void payBillNormalMethod() {
		//non static method can access both static and non static variable
		count++;
		id++;
	}

}
