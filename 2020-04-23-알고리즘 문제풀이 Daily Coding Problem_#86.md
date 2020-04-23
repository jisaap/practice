알고리즘 문제풀이



```java
package DailyCoding;

//Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).
//
//For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.

public class DailyCoding86 {

	
	public static void main(String[] args) {
		
		String str = "()())()";
		char c = ' ';
		char result = ' ';
		int count = 0;
		for(int i = 0; i < str.length(); i ++) {
			c = str.charAt(i);
			if(result ==' ' && c == '(') result = c;
			else if(result == '(' && c == ')')result = ' ';
			else count ++;
		}
		
		System.out.println(count);
	}
}

```

