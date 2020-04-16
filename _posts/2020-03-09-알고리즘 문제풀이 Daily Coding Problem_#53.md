알고리즘 문제풀이

package solution;

import java.util.Stack;

public class Solution18 {

//	Implement a queue using two stacks. 
//	Recall that a queue is a FIFO (first-in, first-out) data 
//	structure with the following
//	methods: enqueue, which inserts an element into the queue,
//	and dequeue, which removes it.
	
	public static class Queue {
			
		Stack stackA = new Stack();
		Stack stackB = new Stack();
	
		public  void put(Object obj) {
		stackA.add(obj);
		}
	
		public  Object pop() {
		if(stackB.isEmpty()) {
			while(!stackA.isEmpty()) {
			stackB.push(stackA.pop());
			}
		}
		return stackB.pop();
		}
			}
	
	public static void main(String[] args) {
		Queue q = new Queue();
		
	}

}