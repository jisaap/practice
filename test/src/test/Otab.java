package test;

public class Otab extends Mobile{

	
	public Otab() {
		// TODO Auto-generated constructor stub
	}
	
	public Otab(String mobileName, int batterySize, String osType) {
		super();
		this.mobileName = mobileName;
		this.batterySize = batterySize;
		this.osType = osType;
	}
	
	public int operate(int time) {
		int ti = batterySize - (time * 12);
		
		return ti;
	}
	public int charge(int time) {
		int ch = batterySize + (time * 8);
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
