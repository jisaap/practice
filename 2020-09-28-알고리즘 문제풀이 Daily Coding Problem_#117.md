알고리즘 문제풀이



```java
package DailyCoding;

import java.io.ObjectInputStream.GetField;
import java.util.ArrayList;
import java.util.List;

//Given a binary tree, return the level of the tree with minimum sum.

public class DailyCoding117 {

	private static List<Integer> list = new ArrayList<Integer>();
	public static void main(String[] args) {
		
		
		TN t1 = new TN(1);
		TN t2 = new TN(2);
		TN t3 = new TN(3);
		TN t4 = new TN(4);
		TN t5 = new TN(-15);
		TN t6 = new TN(6);
		TN t7 = new TN(-7);
		TN t8 = new TN(8);
		
		
		t1.setLeft(t2);
		t1.setRight(t3);
		t2.setLeft(t4);
		t2.setRight(t5);
		t3.setRight(t8);
		t8.setLeft(t6);
		t8.setRight(t7);
		
		
		lvSum(t1, 0);
		
		int min = t1.getValue();
		for(int i : list) {
			min = Math.min(min, i);
		}
		System.out.println(min);
	}
	
	public static void lvSum(TN t, int d) {
		if(list.size() > d) list.set(d, list.get(d) + t.getValue());
		else list.add(t.getValue());
		if(t.getLeft() != null)lvSum(t.getLeft(), d + 1);
		if(t.getRight() != null) lvSum(t.getRight(), d + 1);
		if(t.getLeft() == null && t.getRight() == null)return;
	}
	
	
}

```
