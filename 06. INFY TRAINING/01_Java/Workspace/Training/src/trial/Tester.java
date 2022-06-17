package trial;

import java.util.ArrayList;

import java.util.stream.Stream;

class Tester {

	public static void main(String args[]) {
        
        /**
		 * Scenario #1
		 */
		Stream<String> langNames1 = Stream.of("Java","Python","C++","C","C#","Dot Net");
		
		//Stream Operation #1
		langNames1.filter(name -> name.charAt(0)=='C')
		          .sorted()                                   
		          .forEach(name -> System.out.println(name)); //Line1
		//Stream Operation #2
		langNames1.map(name -> name.toLowerCase())
		          .forEach(name-> System.out.println(name));
		         
		//Comment Scenario 1 and Uncomment Scenario 2!
//		/**
//		 * Scenario #2
//		 */
//	    Stream<String> langNames2 = Stream.of("Java","Python","C++","C","C#","Dot Net");
//		
//		//Stream Operation #1
//		langNames2.filter(name -> name.charAt(0)=='C')
//		          .sorted();                                   //Line2
//		
//		//Stream Operation #2
//		langNames2.map(name -> name.toLowerCase())
//		          .forEach(name-> System.out.println(name));         
	}
}
