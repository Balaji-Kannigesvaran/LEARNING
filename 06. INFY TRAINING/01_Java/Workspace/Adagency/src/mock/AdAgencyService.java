package mock;

public class AdAgencyService {
	protected String quotationId;
	private String customerType;
	private Model model;
	private static int counter = 1001;
	
	public AdAgencyService (String customerType, Model model) {
		this.customerType=customerType;
		this.model=model;
		identifyCustomerType();
		quotationId = getCustomerType().substring(0,3).toUpperCase()+counter;
	}
	public String getCustomerType() {
		return customerType;
	}
	public Model getModel() {
		return model;
	}
	public void identifyCustomerType() {
		//implement your Code here
	}
	public long calculateQuotationAmount() {
		long a = 500L;
		return a;
	}
}
