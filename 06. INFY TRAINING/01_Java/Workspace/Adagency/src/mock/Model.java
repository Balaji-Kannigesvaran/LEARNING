package mock;

public class Model {
	private int modelId;
	private int modelGrade;
	private double remunerationPerDay;
	private static double[] modelRemuneration = {25000.0,30000.0,45000.0,57500.0,100000.0,150000.0};
	
	//To Trainees
	public Model (int modelId,double remunerationPerDay) {
		//Implement Your Code Here
		this.modelId = modelId;
		this.modelGrade = modelId/10000;
		this.remunerationPerDay=remunerationPerDay;
	}
	public int getModelId() {
		return modelId;
	}
	public int getModelGrade() {
		return modelGrade;
	}
	public double getRemunerationPerDay() {
		return remunerationPerDay;
	}
	public static double[] getModelRenumeration() {
		return modelRemuneration;
	}
	public Boolean validateRemunerationPerDay() {
		//Implement your code here
		double minimumLimit = modelRemuneration[modelGrade-1];
		double maximumLimit = modelRemuneration[modelGrade];
		if (remunerationPerDay>minimumLimit && remunerationPerDay<=maximumLimit) {
			return true;
		} else {
			return false;
		}
	}
}
