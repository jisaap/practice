알고리즘 문제풀이



```java
package DailyCoding;

import java.util.List;
import java.util.Scanner;

//Given the root of a binary search tree, and a target K,
//return two nodes in the tree whose sum equals K.

//For example, given the following tree and K of 20

public class DailyCoding125 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		TreeNode root = new TreeNode(1);
		int k = sc.nextInt();

		System.out.println(sumNode(root, k));
	}
	public static boolean sumNode(TreeNode node, int k) {
		
		int sum = 0;
		List<TreeNode> list = node.getList();
		
		for(int i = 0; i < list.size(); i ++) {
			if(list.get(i).getList().size() != 0 && sumNode(list.get(i), k) == true)return true;
			sum += list.get(i).getData();
		}
		if(sum == k)return true;
		return false;
	}
	
	
}

public class TreeNode implements Iterable<TreeNode> {


	protected int data;
	protected TreeNode parent;
	protected List<TreeNode> children;
	
	public TreeNode(int data) {
		this.data = data;
		this.children = new LinkedList<TreeNode>();
	}
	
	public TreeNode addChild(int child) {
		TreeNode childNode = new TreeNode(child);
		childNode.parent = this;
		this.children.add(childNode);
		return childNode;
	}
	

	public List getList() {
		return this.children;
	}
	
	public String getData() {
		return this.data;
	}
	
	
	@Override
	public java.util.Iterator<TreeNode> iterator() {
		
		return null;
	}
}
	



```
