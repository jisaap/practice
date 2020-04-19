알고리즘 문제풀이



```java
package DailyCoding;

//Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
//
//For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

public class DailyCoding82 {

	static int count = 0;

	public static void main(String[] args) {

		System.out.println(read7("Hello world"));
		System.out.println(read7("Hello world"));
		System.out.println(read7("Hello world"));
		
	}
	
	
	
	public static String read7(String str) {
		String result = "";
		for(int i = 0; i < 7; i ++) {
			result += str.length() > i + (count * 7)?str.charAt(i + (count * 7)):"";
		}
		count ++;
		return result;
	}
}

```

