알고리즘 문제풀이



```java
package DailyCoding;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.
//
//For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

public class DailyCoding81 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
//		휴대폰 board 입력
		char[][] board = new char[10][3];
		for(int i = 0; i < board.length; i ++) {
			for(int j = 0; j < board[i].length; j ++) {
				board[i][j] = sc.next().charAt(0);
			}
		}
//		원하는 번호
//		String str = sc.nextLine();
		String str = "01";
		List<String> result = new ArrayList();
		int num = 0;
		for(int i = 0; i < str.length(); i ++) {
			num = str.charAt(i) - 48;
			if(i < str.length() - 1) {
			for(int j = 0; j < board[i].length; j ++) {
				for(int k = 0; k < board[num + 1].length; k ++) {
					result.add(board[num][j] +""+ board[num + 1][k]);
				}
			}
			}
		}
		
		
		for(int i = 0; i < result.size(); i ++) {
			System.out.println(result.get(i));
		}
	}

}

```

