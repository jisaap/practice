알고리즘 문제풀이





Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

```
    *
   / \
  +    +
 / \  / \
3  2  4  5
```

You should return 45, as it is (3 + 2) * (4 + 5).



package solution;

import java.util.Scanner;
import java.util.Stack;

public class Solution15 {

//    *
//   / \
//  +    +
// / \  / \
//3  2  4  5
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String[] input = new String[5];
		for(int i = 0; i <  5; i++) {
			input[i] = sc.nextLine();
		}
		
		String[] result = new String[input[4].length()];
		String answer = "";
		String temp = "";
		char c = ' ';
		int size = 0;
		int index = 0;
		int count = 0;
		Stack<Integer> stack = new Stack<Integer>();
		
		for(int i = 0; i < 5; i ++) {
			if(i%2 == 0 ) {
				for(int j = 0; j < input[4].length(); j ++) {
					if(input[i].length() <= j) {
						break;
					}else {
						if(input[i].charAt(j) != ' ') {
							result[j] = input[i].charAt(j)+"";
						}
					}
				}
			}
			
		}
		for(int i = 0; i < result.length; i ++) {
			if(result[i] != null) {
				answer += result[i].trim();
			}
		}
		//수식 레벨 주고 괄호 작업
		for(int i = 0; i < answer.length(); i ++) {
			if(i%2 == 1) {
					if(answer.charAt(i) == '+' || answer.charAt(i) == '-' ) {
						stack.push(i);
						c = answer.charAt(i);
					}else {
						size = stack.size();
						for(int j = 0; j < size; j ++) {
							index = stack.peek();
							stack.pop();
							//괄호 추가
							c = answer.charAt(i);
							temp = "(" + answer.substring(index - 1, i) + ")";
							answer = answer.substring(index + 2, answer.length());
							answer = temp+answer;
							count = count  + 2;
						}
					
				}
			}
		}
		if(!stack.isEmpty()) {
			for(int i = 0; i < stack.size(); i ++) {
				index = stack.peek();
				stack.pop();
			}
			temp = "(" + answer.substring((index - count) + 1, answer.length())+ ")";
			answer = answer.substring(0, index - 1);
			answer = answer + temp;
			System.out.println(answer);
		}
	}
}