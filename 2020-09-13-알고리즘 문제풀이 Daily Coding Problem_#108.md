알고리즘 문제풀이



```java
package DailyCoding;

//Given two strings A and B, return whether or not A can be shifted some number of times to get B.

//For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.

public class DailyCoding108 {

	public static void main(String[] args) {
		
		String a = "abcde";
		String b = "cdeab";
		
		int move = a.indexOf("a") - b.indexOf("a");
		String temp = "";
		if(move > 0) {
			temp = a.substring(move - 1, a.length()) + a.substring(0, move - 1);
		}else {
			temp = a.substring(Math.abs(move + 1), a.length()) + a.substring(0, Math.abs(move + 1));
		}
		System.out.println(temp.matches(b)? true:false);
		
	}
}

```
