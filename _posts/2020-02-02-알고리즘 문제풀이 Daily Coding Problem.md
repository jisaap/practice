문제 설명





​	Using a function rand5() that returns an integer from 1 to 5 (inclusive) 
​		with uniform probability,
​	implement a function rand7()
​			that returns an integer from 1 to 7 (inclusive).



public class Solution11 {

	public static void main(String[] args) {
		
		int ranFive = ran5();
		int ranSeven = ran7();
		System.out.println(ranFive);
		System.out.println(ranSeven);
	}
	
	public static int ran5() {
		return (int)((Math.random()* 5) + 1);
	}
	
	public static int ran7() {
		return (int)((Math.random() * 7) + 1);
	}
}