package Module3;

class Addition {		
int a;		
int b;
	public Addition () {
		this(50,60);
	}

	public Addition (int a, int b) {	
		this.a = a;
		this.b = b;
	}	
	public int addingTwoNum() {	
		int sum = a+b;
		return sum;
	}	
}		
		
public class MethodAndConstructorTrial{		
	public static void main (String[] args) {	
		Addition add = new Addition();
		int c = add.addingTwoNum();
		System.out.println(c);
		Addition add2 = new Addition(500,2000);
		int d = add2.addingTwoNum();
		System.out.println(d);
		
	}	
}		
				
			
		
