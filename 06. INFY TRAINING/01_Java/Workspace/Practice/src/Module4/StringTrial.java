package Module4;

public class StringTrial {
	public static void main(String [] args) {
		String s1 = "Balaji";
		System.out.println(s1.contains("devel"));
		
		System.out.println("<--------------compareTo--------------------->");
		String s2 = "Balaji";
		String s3 = "Abishek";
		String s4 = "Abi";
		System.out.println(s1.compareTo(s2));
		System.out.println(s1.compareTo(s3));
		System.out.println(s1.compareTo(s4));
		System.out.println(s2.compareTo(s1));
		System.out.println(s3.compareTo(s1));
		System.out.println(s4.compareTo(s1));
		
	
		System.out.println("<-------isEmpty----------isBlank---------------->");
		String s5 = "";
		String s6 = " ";
		System.out.println(s1.isEmpty());
		System.out.println(s5.isEmpty());		
		System.out.println(s6.isEmpty());
		System.out.println(s1.isBlank());
		System.out.println(s5.isBlank());		
		System.out.println(s6.isBlank());
		
		System.out.println("<----------------startsWith------------------>");
		System.out.println(s1.startsWith("Ab"));
		System.out.println(s1.startsWith("ab"));
		System.out.println(s1.startsWith("Ba"));
		System.out.println(s1.startsWith("ba"));
		System.out.println(s3.startsWith("Ab"));
		System.out.println(s3.startsWith("ab"));
		System.out.println(s3.startsWith("Ba"));
		System.out.println(s3.startsWith("ba"));

		System.out.println("<--------------endsWith-------------------->");
		System.out.println(s1.endsWith("Ek"));
		System.out.println(s1.endsWith("ek"));
		System.out.println(s1.endsWith("Ji"));
		System.out.println(s1.endsWith("ji"));
		System.out.println(s3.endsWith("Ek"));
		System.out.println(s3.endsWith("ek"));
		System.out.println(s3.endsWith("Ji"));
		System.out.println(s3.endsWith("ji"));
		
		System.out.println("<-----------split----------------------->");
		String s7 = "Balaji is a Java Developer";
		String [] strarr1 = s7.split(" ");
		for (String items:strarr1) {
			System.out.println(items);			
		}
		String [] strarr2 = s7.split("a");
		for (String items:strarr2) {
			System.out.println(items);			
		}
		
		System.out.println("<-----------indexOf----------------------->");
		System.out.println(s7.indexOf('a'));
		System.out.println(s7.indexOf('i'));
		System.out.println(s7.indexOf("is"));
		
		//study diff between trim and strip
		System.out.println("<-----trim------strip----stripLeading----stripTrailing----------->");
		String s8 = "    Balaji is a JAVA Developer    ";
		System.out.println(s8.trim());
		System.out.println(s8.strip());
		System.out.println(s8.stripLeading());
		System.out.println(s8.stripTrailing());
		
		System.out.println("<-----------repeat----------------------->");
		String s9 = "\\\\Balaji//";
		String s10 = "\\\\Balaji is a Java Developer//";
		System.out.println(s9.repeat(3));
		System.out.println(s10.repeat(3));
	}
}