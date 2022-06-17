package AssociationTry;

public class Section {
	String sectionName;
	String teacherName;
	
	Section(String sectionName){
		this.sectionName=sectionName;
	}
	
	public String getSectionName() {
		return sectionName;
	}
	public void setTeacherName(Teacher teacherNameObj) {
		this.teacherName=teacherNameObj.teacherName;
	}
	public String getTeacherName() {
		return this.teacherName;
	}
}
