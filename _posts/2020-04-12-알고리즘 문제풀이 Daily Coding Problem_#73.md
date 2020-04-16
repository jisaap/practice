알고리즘 문제풀이



```java
package DailyCoding;

import java.util.LinkedList;


//Given the head of a singly linked list, reverse it in-place.

public class DailyCoding73 {

	static LinkedList<String> list = new LinkedList<String>();
	
	public static void main(String[] args) {
	
	list.add("1");
	list.add("2");
	list.add("3");
	list.add("4");
	
	reverse(list);
	
	System.out.println(list);
	}
	
	public static void reverse(LinkedList<String> list) {
		
		for(int i = 0; i <list.size(); i ++) {
			String temp = list.get(i);
			list.remove(i);
			list.addFirst(temp);
		}
	}



}

```
