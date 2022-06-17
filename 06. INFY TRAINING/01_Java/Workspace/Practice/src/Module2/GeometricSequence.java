package Module2;

public class GeometricSequence {
	public static void main (String[] args) {
		int a=1;
		int r=2;
		int n=8;
		int seriesNum;
		for (int i=0;i<n;i++) {
			seriesNum=a*(int)Math.pow(r,i);
			if (i==n-1) {
				System.out.print(seriesNum);				
			}
			else {
				System.out.print(seriesNum + ", ");
			}
		}
	}
}
