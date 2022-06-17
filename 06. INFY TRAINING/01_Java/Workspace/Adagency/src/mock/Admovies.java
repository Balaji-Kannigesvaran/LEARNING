package mock;

public class Admovies extends AdAgencyService {
	private double noOfDaysOfShooting;
	private char typeOfAdmovie;
	
	public Admovies (String customerType, Model model, double noOfDaysOfShooting, char typeOfAdmovie) {
		super(customerType,model);
		this.noOfDaysOfShooting=noOfDaysOfShooting;
		this.typeOfAdmovie=typeOfAdmovie;		
	}
	public double getNoOfDaysOfShooting() {
		return noOfDaysOfShooting;
	}
	
	//To Trainees
	public Boolean validateNoOfDaysOFShooting() {
		//Implement your code here
		if (noOfDaysOfShooting>=2 && noOfDaysOfShooting<=100) {
			return true;
		} else {
			return false;
		}	
	}
	public Boolean validateTypeOfAdMovie() {
		//Implement your code here
		if (typeOfAdmovie=='H' || typeOfAdmovie=='A' || typeOfAdmovie=='L') {
			return true;
		} else {
			return false;
		}	
	}
	public long calculateQuotationAmount() {
		long quotationAmount;
		int budget=0;
		double serviceCharge=0;
		double tax=0;
		long actualNoOFShootingDays;
		double totalBudget=0;
		long baseQuotationAmount;
		if (validateTypeOfAdMovie() && validateNoOfDaysOFShooting() && getModel().validateRemunerationPerDay()) {
			if (typeOfAdmovie=='H') {
				budget = 2500000;
				serviceCharge = 25.25;	
			} else if (typeOfAdmovie=='A') {
				budget = 2000000;
				serviceCharge = 17.5;	
			} else if (typeOfAdmovie=='L') {
				budget = 1500000;
				serviceCharge = 12.75;	
			}
			if (getCustomerType().equalsIgnoreCase("Government")) {
				tax = 0;
			} else if (getCustomerType().equalsIgnoreCase("Public")) {
				tax = 15.75;
			} else if (getCustomerType().equalsIgnoreCase("Private")) {
				tax = 20.25;
			}
			
			actualNoOFShootingDays=(long) Math.floor(getNoOfDaysOfShooting());
			totalBudget = budget+getModel().getRemunerationPerDay()*actualNoOFShootingDays;
			serviceCharge = serviceCharge*totalBudget/100;
			tax = tax*totalBudget/100;
			totalBudget=totalBudget+serviceCharge+tax;
			baseQuotationAmount = super.calculateQuotationAmount();
			totalBudget = totalBudget+baseQuotationAmount;
			quotationAmount=(long)totalBudget;
			return quotationAmount;
		} else {
			return -1;
		}
	}
}
