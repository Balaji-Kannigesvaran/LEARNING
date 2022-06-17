package Module3;

class Rectangle{
	public float length;
	public float width;
	public double calculateArea() {
		return Math.round(length * width*100)/100.0;
	}
	public double calculatePerimeter() {
		return Math.round(2*(length + width)*100)/100.0;
	}
}

public class A4Method {
	public static void main(String[] args) {
		Rectangle rectangle = new Rectangle();
		rectangle.length = 12f;
		rectangle.width = 5f;
		double area = rectangle.calculateArea();
		double perimeter = rectangle.calculatePerimeter();
		System.out.println("Area of the rectangle is " + area);
		System.out.println("Perimeter of the rectangle is " + perimeter);
	}

}
