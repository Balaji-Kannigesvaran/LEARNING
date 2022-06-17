package mock;

public class Tester {
	public static void main(String[] args) {
		Model modelobj = new Model(23534,35000.0);
		Admovies admoviesobj = new Admovies("pubLIC",modelobj,10.0,'H');
		System.out.println("Amount: "+admoviesobj.calculateQuotationAmount());
	}

}
