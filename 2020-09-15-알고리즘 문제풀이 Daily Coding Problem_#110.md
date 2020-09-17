package DailyCoding;
import java.util.ArrayList;
import java.util.List;

//Given a binary tree, return all paths from the root to leaves.
//For example, given the tree:

// 	  1
//	 / \
//	2   3
// 	    / \
//	   4   5

public class DailyCoding110 {

	static List list = new ArrayList<List>();
	
	public static void main(String[] args) {
		TN root = new TN(1);
		TN node1 = new TN(2);
		TN node2 = new TN(3);
		TN node3 = new TN(4);
		TN node4 = new TN(5);

		root.setLeft(node1);
		root.setRight(node2);
		node2.setLeft(node3);
		node2.setRight(node4);
		
		List l = new ArrayList<Integer>();
		checkRoot(root, l);
		System.out.println(list);
	}
	
	public static void checkRoot(TN t, List l) {
		l.add(t.getValue());

		if(t.getLeft() != null)checkRoot(t.getLeft(), l);

		if(t.getRight() != null) checkRoot(t.getRight(), l);
		
		if(t.getLeft() == null && t.getRight() == null) {
			List li = new ArrayList<Integer>();
			li.addAll(l);
			list.add(li);
		}
		l.remove(l.size() - 1);

	}
	
}
