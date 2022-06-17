package Module4;

public class E1String {
    public static String removeWhiteSpaces(String str){
		String str1 = str.replace(" ", "");
        return str1;
	}
	
	public static void main(String args[]){
		String str = "Hello   How are you   ";
		str = removeWhiteSpaces(str);
		System.out.println(str);
		
	}
}
