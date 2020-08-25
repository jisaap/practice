알고리즘 문제풀이



```java
package DailyCoding;

//Given a binary tree of integers,
//find the maximum path sum between two nodes.
//The path must go through at least one node,
//and does not need to go through the root.

//수의 이진 트리가 주어지면 
//두 노드 간의 최대 경로 합계를 찾습니다. 
//경로는 하나 이상의 노드를 통과해야하며 루트를 통과 할 필요가 없습니다

public class DailyCoding94 {

	
	public static void main(String[] args) {
		
		
		
		TreeNode2 node1 = new TreeNode2(1);
		TreeNode2 node2 = new TreeNode2(2);
		TreeNode2 node3 = new TreeNode2(3);
		TreeNode2 node4 = new TreeNode2(4);
		TreeNode2 node5 = new TreeNode2(5);
		TreeNode2 node6 = new TreeNode2(6);
		
		node5.setLeft(node3);
		node5.setRight(node6);
		node3.setRight(node4);
		node3.setLeft(node1);
		node1.setRight(node2);

		System.out.println(getSum(node3, 0));
		
	}
	public static int getSum(TreeNode2 node, int n) {
		int r = 0;
		int l = 0;
		if(node.getRight() != null) {
			r = getSum(node.getRight(), n + node.getValue());
		}
		
		if(node.getLeft() != null) {
			l = getSum(node.getLeft(), n + node.getValue());			
		}
		return Math.max(r, Math.max(n + node.getValue(), l));
	}
	
	
}

```
