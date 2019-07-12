package test;

public class MobileTest {

	public static void main(String[] args) {
		
		Ltab lt = new Ltab("Ltab", 500, "AP-01");
		Otab ot = new Otab("Otab", 1000, "AND-20");
		
		System.out.println("Mobile \t\t       Battary \t\t       Ostype");
		System.out.println(lt.getMobileName() + "\t\t\t" + lt.getBatterySize()
		+"\t\t\t" + lt.getOsType());
		System.out.println(ot.getMobileName() + "\t\t\t" + ot.getBatterySize()
		+"\t\t\t" + ot.getOsType());
		
		
		System.out.println("10분 충전");
		lt.setBatterySize(lt.charge(10));
		ot.setBatterySize(ot.charge(10));
		System.out.println("Mobile \t\t       Battary \t\t       Ostype");
		System.out.println(lt.getMobileName() + "\t\t\t" + lt.getBatterySize()
		+"\t\t\t" + lt.getOsType());
		System.out.println(ot.getMobileName() + "\t\t\t" + ot.getBatterySize()
		+"\t\t\t" + ot.getOsType());
		
		
		System.out.println("5분 통화");
		lt.setBatterySize(lt.operate(5));
		ot.setBatterySize(ot.operate(5));
		System.out.println("Mobile \t\t       Battary \t\t       Ostype");
		System.out.println(lt.getMobileName() + "\t\t\t" + lt.getBatterySize()
		+"\t\t\t" + lt.getOsType());
		System.out.println(ot.getMobileName() + "\t\t\t" + ot.getBatterySize()
		+"\t\t\t" + ot.getOsType());
	}
}
