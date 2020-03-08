알고리즘 문제풀이

LRU 캐시 구현

		package solution;
	
	import java.util.HashMap;
	import java.util.Map;
	
	public class Solution17 {
	
	//	Implement an LRU (Least Recently Used) cache. 
	//	It should be able to be initialized with a cache size n, and contain the following // //methods:
	//
	//		set(key, value): sets key to value.
	//		If there are already n items in the cache and we are adding a new item,
	//		then it should also remove the least recently used item.
	//		
	//		get(key): gets the value at key. If no such key exists, return null.
	//		Each operation should run in O(1) time.
		
	//	LRU 알고리즘이란 Least Recently Used Algorithm 의 약자로,
			캐시에서 메모리를 다루기 위해 사용되는 알고리즘이다.
	
	//	LRU알고리즘은 Linked List 를 이용한 Queue로 이루어지며 접근 개선을 위해 Map을 함께 사용함
		
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
	
	//	처리의 효율성과 코딩상의 이점을 위해 Head 와 Tail을 이용해
			Double Linked List(2개의 Linked List) 형태를 취한다.
		
		public Solution17(int capa) {
			this.nodeMap = new HashMap<>();
			this.capacity = capa;
			head = new ListNode(0,0);
			tail = new ListNode(0, 0);
	// 		Head가 가리키는 head.next 값이 실제 리스트의 첫 원소가 되고
			head.next = tail; //리스트의 첫번째 노드
	//		Tail이 가리키는 tail.prev 값이 실제 리스트의 마지막 원소가 된다.
			tail.prev = head; // 리스트의 마지막 노드
		}
		private void remove(ListNode node) {
	//		이전노드의 next Link 에 다음노드의 prev link를 저장하고
			node.prev.next = node.next;
	//		다음노드의 prev Link에 이전노드의 next Link를 저장하여
			node.next.prev = node.prev;
	//		삭제하는 Node의 Link를 끊고 nodeMap에서 remove함
			nodeMap.remove(node.key);
		}


​		
		private void insertToHead(ListNode node) {
	
	//		리스트의 첫 Node의 prev에 insert할 Node의 주소값 연결
			this.head.next.prev = node;
	//		insert할 Node의 next에 리스트의 첫 Node의 주소값 연결
			node.next = this.head.next;
	//		insert할 Node의 prev에 head의 주소 연결
			node.prev = this.head;
	//		Head의 next 즉 첫번째 값을 insert할 Node값으로 초기화
			this.head.next = node;
	//		Map에 insert할 Node의 내용 추가
			nodeMap.put(node.key,node);
		}


​	
		public int get(int key) {
	
	//		nodeMap에 값이 없으면 return시킴
			if(!nodeMap.containsKey(key)) {
				return -1;
			}
			ListNode node = nodeMap.get(key);
	//		가장 최근에 사용한 데이터를 기존의 List에서 삭제
			remove(node);
	//		가장 최근에 사용한 데이터를 리스트의 맨 앞으로 위치시킴	
			insertToHead(node);
			return node.val;
		}
		
		public void put(int key, int value) {
			
			ListNode newNode = new ListNode(key,value);
	//		List에 값을 추가할때 이미 값이 있는 경우 리스트에서 삭제
			if(nodeMap.containsKey(key)) {
				ListNode oldNode = nodeMap.get(key);
				remove(oldNode);
			}else {
	//			List에 값이 없고 Map의 size가 capacity와 같거나 큰경우 List의 제일 마지막 값 삭제
				if(nodeMap.size() >= capacity) {
					ListNode tailNode = tail.prev;
					remove(tailNode);
				}
			}
	//		Node insert
			insertToHead(newNode);
		}
	}


//출처: https://jins-dev.tistory.com/entry/LRU-Cache-Algorithm-정리 [Jins' Dev Inside]