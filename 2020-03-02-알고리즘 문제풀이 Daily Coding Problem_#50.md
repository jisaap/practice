알고리즘 문제풀이



tree를 이용해 계산하는 방식이 아니라 각각의 인덱스를 유지하고 '/', '\\' 가 존재하는 열을 무시하고 하나의 문자열로 합치면 될것 같다는 생각이 들어서 시도 해 봤다. 수식의 레벨에 따라 괄호를 추가하는 식을 추가 해야함



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

public class Solution15 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String[] input = new String[5];
		for(int i = 0; i <  5; i++) {
			input[i] = sc.nextLine();
		}
		
		String[] result = new String[input[4].length()];
		String answer = "";
		
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
		System.out.println(answer);
		//수식 레벨 주고 괄호 작업
		for(int i = 0; i < answer.length(); i ++) {
			if(i%2 == 1) {
				System.out.println(answer.charAt(i));
			}
		}
	}
}