Cache 알고리즘 중에 가장 유명한 알고리즘 중 하나로 LRU 알고리즘 이라는 것이 있다.

 

LRU 알고리즘이란 Least Recently Used Algorithm 의 약자로, 캐시에서 메모리를 다루기 위해 사용되는 알고리즘이다.

 

캐시가 사용하는 리소스의 양은 제한되어 있고, 캐시는 제한된 리소스 내에서 데이터를 빠르게 저장하고 접근할 수 있어야 한다.

이를 위해 LRU 알고리즘은 메모리 상에서 가장 최근에 사용된 적이 없는 캐시의 메모리부터 대체하며 새로운 데이터로 갱신시켜준다.

 

알고리즘의 주요 동작은 다음과 같다.

 



![img](https://k.kakaocdn.net/dn/bW7p8I/btqv5hjmB5E/X3lwMNQP8Np2Jtl2kQg1EK/img.png)



 

가장 최근에 사용된 항목은 리스트의 맨 앞에 위치하고 가장 최근에 사용되지않은 항목 순서대로 리스트에서 제거된다.

LRU 알고리즘의 구현은 위의 그림에서도 볼 수 있듯이 Linked List 를 이용한 Queue 로 이루어지고, 접근의 성능 개선을 위해 Map 을 같이 사용한다.

 

다음 예제코드를 참조하자.

 

```
public class LRUCacheImpl {

	private class ListNode {
		private int key;
		private int val;
		private ListNode prev;
		private ListNode next;

		public ListNode(int key, int val) {
			this.key = key;
			this.val = val;
			this.prev = null;
			this.next = null;
		}
	}

	private Map<Integer, ListNode> nodeMap;
	private int capacity;
	private ListNode head;
	private ListNode tail;

	public LRUCacheImpl(int capacity) {
		this.nodeMap = new HashMap<>();
		this.capacity = capacity;
		head = new ListNode(0, 0);
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
		nodeMap.put(node.key, node);
	}

	public int get(int key) {
		if (!nodeMap.containsKey(key)) {
			return -1;
		}
		ListNode node = nodeMap.get(key);
		remove(node);
		insertToHead(node);
		return node.val;
	}

	public void put(int key, int value) {
		ListNode newNode = new ListNode(key, value);
		if (nodeMap.containsKey(key)) {
			ListNode oldNode = nodeMap.get(key);
			remove(oldNode);
		} else {
			if (nodeMap.size() >= capacity) {
				ListNode tailNode = tail.prev;
				remove(tailNode);
			}
		}
		insertToHead(newNode);
	}
}
```

 

여기서 테크닉적으로 중요한 부분은, Linked List 처리의 효율성과 코딩상의 이점을 위해 Head 와 Tail 을 단순히 포인터로만 둔 상태에서 중간에 노드들을 배치시키는 더블 링크드리스트 형태를 취한다는 점이다.

즉, Head 가 가리키는 head.next 값이 실제 리스트의 첫 원소가 되고, Tail 이 가리키는 Tail.prev 값이 실제 리스트의 마지막 원소가 된다.

 

이렇게 Linked List 와 Map 을 이용해서 구현 시, Get 연산에 O(1), Put 연산에도 O(1) 의 성능을 가져올 수 있다.

 

쉬우면서도 효과적인 알고리즘이자 자료구조이므로 잘 익혀두자.

 

  

출처: https://jins-dev.tistory.com/entry/LRU-Cache-Algorithm-정리 [Jins' Dev Inside]  