package Module1;



class Tester {

	public static void main(String[] args) {
		int num1 = 0;
		int num2 = 0;
		for (int var = 0; var < 5; var++) {
			System.out.println("-------------------------");
			System.out.println("var is " + var);
			System.out.println(num1 + " and " + num2);
			if ((++num1 > 2) && (++num2 > 2)) {
				num1++;
			}
			System.out.println(num1 + " and " + num2);
		}
		System.out.println(num1 + " and " + num2);
	}

}