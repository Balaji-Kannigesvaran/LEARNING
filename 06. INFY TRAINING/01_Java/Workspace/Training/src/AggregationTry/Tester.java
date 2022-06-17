package AggregationTry;

public class Tester {
	public static void main(String[] args) {
		Teacher t1 = new Teacher("Anitha");
		Teacher t2 = new Teacher("Swetha");

		Section s1 = new Section("A", t1);
		Section s2 = new Section("B", t2);

		System.out.println("Section Name is " + s1.getSectionName());
		System.out.println("S1 Teacher Name is " + t1.getTeacherName());
		//But in the above line we may give t2 for s1
		//Manual error may happen
		//We can access t1 in s1 itself
		//So above code can be rewritten as
		System.out.println("Section Name is " + s1.getSectionName() + 
				" and Teacher Name is " + s1.teacherName.getTeacherName());
		//Similarly we can do for other class also
		System.out.println("Section Name is " + s2.getSectionName() + 
				" and Teacher Name is " + s2.teacherName.getTeacherName());
	}
}
