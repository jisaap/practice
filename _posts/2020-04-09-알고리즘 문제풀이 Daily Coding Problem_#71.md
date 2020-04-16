알고리즘 문제풀이



```java
package DailyCoding;

//Using a function rand7() that returns an integer from 1 to 7 (inclusive)
//with uniform probability, 
//implement a function rand5() that 
//returns an integer from 1 to 5 (inclusive).



public class DailyCoding71 {

	public static void main(String[] args) {
		System.out.println(ran7());
		System.out.println(ran5());
	}
	
	public static int ran7() {
		return (int)(Math.random() * 7) + 1;
	}
	public static int ran5() {
		return (int)(Math.random() * 5) + 1;
	}
}

```
