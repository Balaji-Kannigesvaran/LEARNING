package AssociationTry;

//In aggregation we have instantiated an instance variable of one class
// - in other and initialized it in constructor and then used
//But in association, we are not gonna instantiate it as instance variable
// - and also not gonna initialize it using constructor
//Instead we are gonna use it directly in a method in other class


public class Tester {
	public static void main(String[] args) {
		Section s1 = new Section("A");
		Section s2 = new Section("B");
		
		Teacher t1 = new Teacher("Anitha");
		Teacher t2 = new Teacher("Swetha");
		
		s1.setTeacherName(t1);
		s2.setTeacherName(t2);

		System.out.println("Section Name is " + s1.getSectionName() + 
				" and Teacher Name is " + s1.getTeacherName());
		//Similarly we can do for other class also
		System.out.println("Section Name is " + s2.getSectionName() + 
				" and Teacher Name is " + s2.getTeacherName());
	}
}
