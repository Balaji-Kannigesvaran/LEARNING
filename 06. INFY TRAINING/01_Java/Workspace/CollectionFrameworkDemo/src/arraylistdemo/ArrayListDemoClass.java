package arraylistdemo;

import java.util.ArrayList;

public class ArrayListDemoClass {
	public static void main(String[] args) {
		ArrayList a = new ArrayList();
		a.add('b');
		a.add("Balaji");
		a.add(30);
		a.add(40.5);
		a.add(50.6f);
		a.add(7895648522636L);
		a.add(true);

		for (int i = 0; i < a.size(); i++) {
			System.out.println(a.get(i));
		}
		for (Object element : a) { //cannot use String or Integer	
			System.out.println(element);
		}	

	}
}
