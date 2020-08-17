알고리즘 문제풀이



```java
package DailyCoding;

import java.io.ObjectInputStream.GetField;

//Determine whether a tree is a valid binary search tree.
//A binary search tree is a tree with two children,
//left and right, and satisfies the constraint that the
//key in the left child must be less than or equal to the root
//and the key in the right child must be greater than or equal to the root.


public class DailyCoding89 {

	
	static boolean check;
	
	public static void main(String[] args) {
		
		TreeNode2 node1 = new TreeNode2(1);
		TreeNode2 node2 = new TreeNode2(2);
		TreeNode2 node3 = new TreeNode2(3);
		TreeNode2 node4 = new TreeNode2(4);
		TreeNode2 node5 = new TreeNode2(5);
		TreeNode2 node6 = new TreeNode2(6);
		TreeNode2 nodeCk;

		
		node5.setLeft(node3);
		node5.setRight(node6);
		node3.setLeft(node2);
		node3.setRight(node4);
		node2.setLeft(node1);
		
		
		nodeCk = node5.getLeft().getLeft().getLeft().getLeft();
		
		checkRight(node5.getRight(), node5.getValue());
		checkLeft(node5.getLeft(), node5.getValue());
		
		System.out.println(check);
	}
	
	public static boolean checkRight(TreeNode2 n, int val) {
		if(n != null) {
			check = checkRight(n.getRight(), n.getValue());
			if(check == false)return false;
		}else {
			return true;
		}
		return n.getValue() >= val ? true : false; 
	}
	
	public static boolean checkLeft(TreeNode2 n, int val) {
		if(n != null) {
			if(n.getRight() !=  null ) checkRight(n.getRight(), n.getValue());
			check = checkLeft(n.getLeft(), n.getValue());
			if(check == false)return false;
		}else {
			return true;
		}
		return n.getValue() <= val ? true : false; 

	}


}



TreeNode 구조
-------------
package DailyCoding;

public class TreeNode2 {

	private TreeNode2 left;
	private TreeNode2 right;
	private int data;
		
	public TreeNode2(int data) {
				left = null;
				right = null;
				this.data = data;
	}
		
		public void setLeft(TreeNode2 n) {
			if(this.left != null) this.left = null;
			this.left = n;
		}
		
		public void setRight(TreeNode2 n) {
			if(this.right != null) this.right = null;
			this.right = n;
		}
		
		public int getValue() {
			return this.data;
		}
		
		public  TreeNode2 getLeft() {
			return this.left != null ? this.left : null;
		}
		
		public TreeNode2 getRight() {
			return this.right != null ? this.right : null;
		}
		
}



```
