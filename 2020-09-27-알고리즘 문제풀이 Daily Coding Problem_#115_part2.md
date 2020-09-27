알고리즘 문제풀이



```java
package DailyCoding;

//Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
//A subtree of s is a tree consists of a node in s and all of this node's descendants.
//The tree s could also be considered as a subtree of itself.

public class DailyCoding115 {

	private static TN t;
	private static TN s;
	private static boolean ck;

	public static void main(String[] args) {
		
		t = new TN(0);
		s= new TN(3);
		TN t1 = new TN(1);
		TN t2 = new TN(2);
		TN t3 = new TN(3);
		TN t4 = new TN(4);
		TN t5 = new TN(5);
		TN t6 = new TN(6);
		
		TN s1 = new TN(4);
		TN s2 = new TN(5);
		TN s3 = new TN(6);

		
		t.setLeft(t1);
		t.setRight(t2);
		t1.setRight(t3);
		t3.setLeft(t4);
		t3.setRight(t5);
		t4.setLeft(t6);
		s.setLeft(s1);
		s.setRight(s2);
		s1.setLeft(s3);
		
		
		TN root = ckRoot(t, s);
		System.out.println(ckTree(root, s));
	}
	public static TN ckRoot(TN m, TN s) {
		TN result = null;
		if(m.getValue() == s.getValue())return m;
		if(m.getLeft() != null)result = ckRoot(m.getLeft(), s);
		if(result == null && m.getRight() != null)result = ckRoot(m.getRight(), s);
		if(result== null && m.getLeft() == null && m.getRight() == null ) return null;
		return result;
	}
	
	public static boolean ckTree(TN m, TN s) {
		boolean ck = false;
		ck = m.getValue() == s.getValue();
		try {
			if(ck != false && s.getLeft() != null)ck = ckTree(m.getLeft(), s.getLeft());
			if(ck != false && s.getRight() != null)ck = ckTree(m.getRight(), s.getRight());
			if(ck != false && s.getLeft() == null  && s.getRight() == null)ck = true;
		}catch (Exception e) {
			ck = false;
		}
		return ck;
	}
}
```
