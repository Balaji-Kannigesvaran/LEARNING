package StaticTry;

abstract class Automobile {
	private String vehicleNo;

	public abstract void start();

	public abstract void stop();

	public String getvehicleNo() {
		return vehicleNo;
	}

	public void setvehicleNo(String vehicleNo) {
		this.vehicleNo = vehicleNo;
	}

}

class Bike extends Automobile {
	public void start() {
		System.out.println("Bike" + "getvehicleNo()" + "Bike started");
	}

	public void stop() {
		System.out.println("Bike" + "getvehicleNo()" + "Bike stoped");
	}
}

class Car extends Automobile {
	public void start() {
		System.out.println("Car" + "getvehicleNo()" + "Car started");
	}

	public void stop() {
		System.out.println("Car" + "getvehicleNo()" + "Car stoped");
	}
}

public class AbstractDemo1 {
	public static void main(String[] args) {
		Automobile b = new Bike();
		Automobile c = new Car();
		b.setvehicleNo("TN-2345");
		c.setvehicleNo("Tn-7834");
		System.out.println(b.getvehicleNo());
		System.out.println(c.getvehicleNo());
		b.start();
		c.start();

		startAutomobile(b);
		startAutomobile(c);
	}

	static void startAutomobile(Automobile a) {
		a.start();
	}

}
