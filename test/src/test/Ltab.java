package test;

public class Ltab extends Mobile{

	
	public Ltab() {
		// TODO Auto-generated constructor stub
	}
	
	public Ltab(String mobileName, int batterySize, String osType) {
		super();
		this.mobileName = mobileName;
		this.batterySize = batterySize;
		this.osType = osType;
	}
	
	public int operate(int time) {
		int ti = batterySize - (time * 10);
		
		return ti;
	}
	public int charge(int time) {
		int ch = batterySize + (time * 10);
				return ch;
	}
	
	public String getMobileName() {
		return mobileName;
	}
	public void setMobileName(String mobileName) {
		this.mobileName = mobileName;
	}
	public int getBatterySize() {
		return batterySize;
	}
	public void setBatterySize(int batterySize) {
		this.batterySize = batterySize;
	}
	public String getOsType() {
		return osType;
	}
	public void setOsType(String osType) {
		this.osType = osType;
	}
	
	
}
