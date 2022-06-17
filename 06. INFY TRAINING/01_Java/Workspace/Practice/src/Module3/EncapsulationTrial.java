package Module3;
				
class Add2it {				
public int a;				
private int b;				
	public Add2it (int a, int b) {			
		this.a = a;		
		this.b = b;		
	}			
				
	public int addingTwoNum() {			
		int sum = a+b;		
		return sum;		
	}			
				
	public void setA (int a) {			
		this.a=a;		
	}			
	public int getA () {			
		return a;		
	}			
	public void setB (int b) {			
		this.b=b;		
	}			
	public int getB () {			
		return b;		
	}			
}				
				
public class EncapsulationTrial{				
	public static void main (String[] args) {			
		Add2it add1 = new Add2it(100,200);		
		int c = add1.addingTwoNum();		
		System.out.println("a: " + add1.getA());		
		System.out.println("b: " + add1.getB());		
		System.out.println("sum: " + c);		
		add1.setA(55);		
		add1.setB(16);		
		int d = add1.addingTwoNum();		
		System.out.println("a: " + add1.getA());		
		System.out.println("b: " + add1.getB());		
		System.out.println("sum: " + d);		
				
	}			
}				
		
			
	
