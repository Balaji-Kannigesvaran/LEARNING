package Module5;

class Cabin {
	public int cabinNumber;

	Cabin(int number) {
		this.cabinNumber = number;
	}
}

public class Professor {
	public String name;
	public Cabin cabin;

	public Professor(String name, Cabin c) {
		this.name = name;
		this.cabin = c;
	}

	public void updateCabin(Cabin c) {
		this.cabin.cabinNumber = c.cabinNumber;
	}

	public static void main(String args[]) {
		Cabin c1 = new Cabin(121);
		Cabin c2 = new Cabin(122);
		Professor p1 = new Professor("Ronald", c1);
		Professor p2 = new Professor("Bonnie", c2);
		Cabin c3 = new Cabin(123);
		p1.updateCabin(c3);
		System.out.println(p1.cabin.cabinNumber);
		System.out.println(p2.cabin.cabinNumber);
	}

}
