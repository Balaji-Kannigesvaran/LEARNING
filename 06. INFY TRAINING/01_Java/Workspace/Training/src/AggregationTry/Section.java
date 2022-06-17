package AggregationTry;

public class Section {
	String sectionName;
	Teacher teacherName;
	
	Section(String sectionName,Teacher teacherName){
		this.sectionName=sectionName;
		this.teacherName=teacherName;
	}
	
	public String getSectionName() {
		return sectionName;
	} 

}
