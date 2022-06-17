package Module3;

class Demo {					
	public int value = 20;				
					
	void fn1() {				
		value = 40;			
	}				
}					
					
public class Quiz {					
	public static void main(String args[]) {				
		Demo demo = new Demo();			
		System.out.println(demo.value);			
	}				
}					

