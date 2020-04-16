알고리즘 문제풀이



```java
package DailyCoding;


//Implement integer exponentiation. 
//That is, implement the pow(x, y) function,
//where x and y are integers and returns x^y.
//
//Do this faster than the naive method of repeated multiplication.
//
//For example, pow(2, 10) should return 1024.


public class DailyCoding61 {

	

	public static void main(String[] args) {
		
		int x = 2;
		int y = 10;
		
		System.out.println(pow(x,y));
	}
	
	
	public static int pow(int x, int y) {
		int su = 0;
		int result = 0;
		if(y == 0) {
			return 1;
		}
		su = pow(x, y/2);
		result = su*su;
		
		if(y%2 == 0) {
			return result;
		}else {
			return x * result;
		}
		
	}
	
}

```
