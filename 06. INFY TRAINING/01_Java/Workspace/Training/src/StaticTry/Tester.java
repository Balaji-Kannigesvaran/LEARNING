package StaticTry;

//We are using things from Customer class here

public class Tester {
	public static void main(String[] args) {
		Customer c1 = new Customer(); 		//Creating reference variable
		System.out.println(c1.id);
		System.out.println(Customer.count);
		
		//Mutating variable in other class
		//Normal variable is mutated by using reference variable
		//Static Variable is mutated by using class name
		c1.id = 10;							
		Customer.count=20;
		System.out.println(c1.id);
		System.out.println(Customer.count);
		
		//Calling static method using class name
		Customer.payBillStaticMethod();
		System.out.println(c1.id);
		System.out.println(Customer.count);		
		
		//Calling normal variable with ref variable
		//We cant call non static variable/ method with class(static things)
		//Customer.payBillNormalMethod();
		c1.payBillNormalMethod();
		System.out.println(c1.id);
		System.out.println(Customer.count);
		
		//Similarly we cant call static things with ref variable
		//c1.payBillStaticMethod();
		System.out.println(c1.id);
		//System.out.println(c1.count);	
		//This happens only if we call from other class
		//Go to customer class and see
		
	}

}
