알고리즘 문제풀이



문제를 이해 할수도 없었다 

내일 까지 분석 해보기



//	Implement an LRU (Least Recently Used) cache. 
//	It should be able to be initialized with a cache size n, and contain the following methods:
//
//		set(key, value): sets key to value.
//		If there are already n items in the cache and we are adding a new item,
//		then it should also remove the least recently used item.
//		
//		get(key): gets the value at key. If no such key exists, return null.
//		Each operation should run in O(1) time.
	



package solution;

import java.util.HashMap;
import java.util.Map;

public class Solution17 {

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
	
	public Solution17(int capa) {
		this.nodeMap = new HashMap<>();
		this.capacity = capa;
		head = new ListNode(0,0);
		tail = new ListNode(0, 0);
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
		nodeMap.put(node.key,node);
	}
	
	public int get(int key) {
		if(!nodeMap.containsKey(key)) {
			return -1;
		}
		ListNode node = nodeMap.get(key);
		remove(node);
		insertToHead(node);
		return node.val;
	}
	
	public void put(int key, int value) {
		ListNode newNode = new ListNode(key,value);
		if(nodeMap.containsKey(key)) {
			ListNode oldNode = nodeMap.get(key);
			remove(oldNode);
		}else {
			if(nodeMap.size() >= capacity) {
				ListNode tailNode = tail.prev;
				remove(tailNode);
			}
		}
		insertToHead(newNode);
	}
}





출처: https://jins-dev.tistory.com/entry/LRU-Cache-Algorithm-정리 [Jins' Dev Inside]  