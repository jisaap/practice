알고리즘 문제풀이



```java
package DailyCoding;

import java.util.ArrayList;
import java.util.List;

//Print the nodes in a binary tree level-wise. 
//For example, the following should print 1, 2, 3, 4, 5.

// 	  1
//	 / \
//	2   3
// 	    / \
//	   4   5

public class DailyCoding107 {

	static List list = new ArrayList<Integer>();
	
	public static void main(String[] args) {
		TN root = new TN(1);
		TN node1 = new TN(2);
		TN node2 = new TN(3);
		TN node3 = new TN(4);
		TN node4 = new TN(5);
		TN node5 = new TN(6);
		TN node6 = new TN(7);

		root.setLeft(node1);
		root.setRight(node2);
		node1.setLeft(node3);
		node1.setRight(node4);
		node2.setLeft(node5);
		node2.setRight(node6);
		list.add(root.getValue());
		print(root, 1);
		System.out.println(list);
	}
	
	public static void print(TN n, int lv) {
		TN l  = n.getLeft() != null ? n.getLeft() : null;
		TN r = n.getRight() != null ? n.getRight() : null;
		int count = 1;
		while(true) {
			if(l == null && r == null)break;
			if(l != null && r != null && lv == count) {
				list.add(l.getValue());
				list.add(r.getValue());
				print(l, lv + 1);
				print(r, lv + 1);
				break;
			}
			if(l != null && lv == count) {
				print(l, lv + 1);
				break;
			}else if(r != null && lv == count) {
				print(r, lv + 1);
				break;
			}
			count ++;
		}
		
		
	}
	
}


```
