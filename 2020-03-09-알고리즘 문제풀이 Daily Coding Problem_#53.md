알고리즘 문제풀이



package solution;

import java.util.Stack;

public class Solution18 {


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
		q.put("1");
		q.put("2");
		q.put("3");
		
		System.out.println(q.pop());
		System.out.println(q.pop());
		System.out.println(q.pop());
		
	}

}