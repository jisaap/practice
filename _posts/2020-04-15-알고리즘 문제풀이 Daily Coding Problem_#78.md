알고리즘 문제풀이



```java
package DailyCoding;

// Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
public class DailyCoding78 {

	public class ListNode {

		int key;
		int val;
		ListNode prev;
		ListNode next;

		public ListNode(int key, int val) {
			this.key = key;
			this.val = val;
			this.prev = null;
			this.next = null;

		}
	}

//	병합 및 정렬
	public ListNode mergeNode(ListNode node1, ListNode node2) {

		if(node1 == null) return node2;
		if(node2 == null) return node1;
		ListNode node;
		
		if(node1.val <= node2.val) {
			node = node1;
			node1.next = mergeNode(node1.next, node2);
		}else {
			node = node2;
			node2.next = mergeNode(node1, node2.next);
		}
		return node;
	}
}

```

