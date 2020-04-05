알고리즘 문제풀이



```java
package DailyCoding;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

//Implement an LFU (Least Frequently Used) cache.
//It should be able to be initialized with a cache size n, and contain the following methods:
//set(key, value): sets key to value. 
//If there are already n items in the cache and we are adding a new item,
//then it should also remove the least frequently used item.
//If there is a tie, then the least recently used key should be removed.
//get(key): gets the value at key. If no such key exists, return null.
//Each operation should run in O(1) time.


// Double Linked List 를 사용해서 두개의 리스트를 이용해 효율성을 높이는 방법
// 최근에 사용한 데이터를 계속 앞쪽에 위치시키면서 데이터 관리 
// 전체 데이터는 nodeMap에서 관리
public class DailyCoding67 {

	private class ListNode {
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

	Map<Integer, ListNode> nodeMap;
	int capacity;
	ListNode head;
	ListNode tail;
	
	public DailyCoding67(int c) {
		this.nodeMap = new HashMap<>();
		this.capacity = c;
		head = new ListNode(0,0);
		tail = new ListNode(0,0);
		head.next = tail;
		tail.prev = head;
		
	}	
	
	
	private void remove(ListNode node) {
		node.prev.next = node.next;
		node.next.prev = node.prev;
		
		nodeMap.remove(node.key);
	}
	
	private void insertToHead(ListNode node) {
		this.head.next.prev = node;
		node.next = this.head.next;
		node.prev = this.head;
		this.head.next = node;
		nodeMap.put(node.key, node);
	}
	
	public int get(int key) {
		if(!nodeMap.containsKey(key)) {
			return - 1;
		}
		
		ListNode node = nodeMap.get(key);
		remove(node);
		insertToHead(node);
		return node.val;
		
	}
	
	public void put(int key, int val) {
		
		ListNode newNode = new ListNode(key, val);
		
		if(nodeMap.containsKey(key)) {
			ListNode oldNode = nodeMap.get(key);
			remove(oldNode);
		}else {
			if(nodeMap.containsKey(key)) {
				ListNode tailNode = tail.prev;
				remove(tailNode);
			}
		}
		
		insertToHead(newNode);
	}
}

```
