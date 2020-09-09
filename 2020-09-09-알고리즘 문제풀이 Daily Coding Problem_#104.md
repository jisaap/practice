알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Stack;

//Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

//For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.

public class DailyCoding104 {

	public static void main(String[] args) {
		LinkedList<Integer> list = new LinkedList<Integer>(Arrays.asList(1,4,3,4,1));
		int count = 0;
		Stack s = new Stack();
		
		for(Integer i : list) {
			
			if(list.size()%2 != 0 && list.size() == count)continue;
			if(count < list.size() / 2) {
				s.push(i);
			}else {
				if(s.peek() == i) {
					s.pop();
				}
			}
			count ++;
		}
		System.out.println(s.size() == 0?true:false);
	}
	
}

```
