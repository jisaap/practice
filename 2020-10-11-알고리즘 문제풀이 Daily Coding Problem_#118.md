알고리즘 문제풀이



```java
package DailyCoding;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

//Given a sorted list of integers, square the elements and give the output in sorted order.

//For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

public class DailyCoding118 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		List<Integer> input = new ArrayList<Integer>();
		
		for(int i = 0; i < N; i ++) {
			input.add(sc.nextInt());
		}
		
		System.out.println(solution(input));
	}
	
	public static List<Integer> solution(List<Integer> input) {
		Stack<Integer> s = new Stack<Integer>();
		List<Integer> result = new ArrayList<Integer>();
		
		for(int i = 0; i < input.size(); i ++) {
			if(input.get(i) >= 0) {
				if(s != null && s.peek() < input.get(i) * input.get(i)) {
					result.add(s.pop());
				}
				result.add(input.get(i) * input.get(i));
			}else s.add(input.get(i) * input.get(i));
		}
		if(s != null) {
			for(int i = 0; i < s.size(); i ++) {
				result.add(s.pop());
			}
		}
		return result;
	}
	
}

```
