알고리즘 문제풀이



```java
package DailyCoding;

import java.util.LinkedList;
import java.util.List;

public class TreeNode implements Iterable<TreeNode> {


	private String data;
	private TreeNode parent;
	private List<TreeNode> children;
	
	public TreeNode(String data) {
		this.data = data;
		this.children = new LinkedList<TreeNode>();
	}
	
	public TreeNode addChild(String child) {
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

```java
package DailyCoding;

import java.util.List;

//Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
//
//	    a
//	   / \
//	  b   c
//	 /
//	d



public class DailyCoding80 {

	static int count = 0;
	static String result = "";
	
	public static void main(String[] args) {
		TreeNode root = new TreeNode("a");
	
		TreeNode r2 = root.addChild("b");
		TreeNode r3 = root.addChild("c");
		TreeNode r4 = r2.addChild("d");

		

		System.out.println(getLevel(root, 0));
	}
	
	
	public static String getLevel(TreeNode t, int level) {
		List<TreeNode> l = t.getList();
		
		for(TreeNode node : l) {
			level ++;
			if(level > count) {
				result = node.getData();
				count = level;
			}
			result = l.size() != 1?getLevel(node, level): result;
			level = 0;
		}
		
		return result;
	}


}

```

