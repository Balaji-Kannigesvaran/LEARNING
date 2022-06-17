package Module3;

class Average{
	public double AvgOf3Nums(int num1, int num2, int num3) {
		return ((num1+num2+num3)/3.0);
	}
}
public class Calculator {
	public static void main (String[] args) {
		Average avg = new Average();
		double avgResult = avg.AvgOf3Nums(12, 8, 15);
		System.out.println(Math.round(avgResult*100)/100f);
		System.out.println(Math.round(11.4));
	}
}
