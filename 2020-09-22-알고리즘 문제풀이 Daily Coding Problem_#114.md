알고리즘 문제풀이



```java
package DailyCoding;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

//Given a string and a set of delimiters, reverse the words in the string 
//while maintaining the relative order of the delimiters. 
//For example, given "hello/world:here", return "here/world:hello"

//Follow-up: Does your solution work 
//for the following cases: "hello/world:here/", "hello//world:here"

public class DailyCoding114 {

	public static void main(String[] args) {
		
//		String input = "hello/world:here";
//		String input = "hello/world:here/";
		String input = "hello//world:here";

		Stack<String> stack = new Stack<String>();
		Queue<String> q = new LinkedList<String>();
		int i = 0;
		int j = 0;
		String result = "";
		boolean ck = false;
		for(char c : input.toCharArray()) {
			
				if(checkChar(c)) {
					j ++;
					ck = false;
				}else {
					stack.add(input.substring(i,j));
					if(ck == true)q.add(q.remove() + c);
					else q.add(c+"");
					ck = true;
					i = ++j;
				}
				if(j == input.length() && i != j)stack.add(input.substring(i,j));
		}
			while(!q.isEmpty() || !stack.isEmpty()) {
				if(!stack.isEmpty())result += stack.pop();
				if(!q.isEmpty())result += q.remove();
		}
		System.out.println(result);
	}
	
	public static boolean checkChar(char c) {
		return c >= 'A' && c <= 'Z' || c >= 'a' && c <= 'z';
	}
	
}

```
