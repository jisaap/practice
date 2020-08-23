알고리즘 문제풀이



```java
package DailyCoding;


//Given a tree, find the largest tree/subtree that is a BST.
//
//Given a tree, return the size of the largest tree/subtree that is a BST.

//	가장 큰 노드 값고ㅏ 서브트리 출력	
public class DailyCoding93 {

	
	
	public static void main(String[] args) {
		
		
		TreeNode2 node1 = new TreeNode2(1);
		TreeNode2 node2 = new TreeNode2(2);
		TreeNode2 node3 = new TreeNode2(3);
		TreeNode2 node4 = new TreeNode2(4);
		TreeNode2 node5 = new TreeNode2(5);
		TreeNode2 node6 = new TreeNode2(6);
		
		node2.setLeft(node1);
		node2.setRight(node3);
		node3.setRight(node6);
		node6.setLeft(node4);
		node4.setRight(node5);
		
		
		System.out.println(getSubTree(getLargestTree(node3, node3.getValue()), 0));
		
	}
	
	public static TreeNode2 getLargestTree(TreeNode2 n, int val) {
		TreeNode2 result = n;
		if(result.getRight() != null) {
			result = getLargestTree(result.getRight(), result.getRight().getValue()); 
		}
		return result;
		
	}
	
	public static int getSubTree(TreeNode2 n, int s) {
		if(n.getRight() != null) {
			s = getSubTree(n.getRight(), s + 1);
		}
		
		if(n.getLeft() != null) {
			s = getSubTree(n.getLeft(), s + 1);
		}
		return s;			
	}
	
}

```
