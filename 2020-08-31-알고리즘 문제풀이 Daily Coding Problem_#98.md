알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Scanner;

//Given a 2D board of characters and a word, find if the word exists in the grid.
//
//The word can be constructed from letters of sequentially 
//adjacent cell, where "adjacent" cells are those horizontally or vertically
//neighboring. The same letter cell may not be used more than once.
//
//For example, given the following board:
//
//[
//  ['A','B','C','E'],
//  ['S','F','C','S'],
//  ['A','D','E','E']
//]
//exists(board, "ABCCED") returns true,
//exists(board, "SEE") returns true, exists(board, "ABCB") returns false.

public class DailyCoding98 {

	public static void main(String[] args) {
		
	Scanner sc = new Scanner(System.in);
	
		char[][] board = {
			{ 'A', 'B', 'C', 'E'},
			{ 'S', 'F', 'C', 'S'},
			{ 'A', 'D', 'E', 'E'}
			};
	
		System.out.println(exist(board, sc.next().toUpperCase()));
	
	
	
	
	}
	
	public static boolean exist(char[][] b, String str) {
		boolean ck = false;
		for(int i = 0; i < b.length; i ++) {
			for(int j = 0; j < b[i].length; j ++) {
				if(str.charAt(0) == b[i][j]) {
					if(str.length() == 1) {
						ck = true;
						break;
					}
						ck = check(b, str, i, j , 1, 0);
				}
				if(ck == true) break;
			}
			if(ck == true) break;
		}
		return ck;
	}
	
	public static boolean check(char[][] arr, String str,  int z, int y, int i, int bf) {
		boolean ck = false;
		if(z != 0 && arr[z - 1][y] == str.charAt(i) && bf != 3) {
			ck = i < str.length() - 1?check(arr, str, z - 1, y, i + 1, 1): true;
		}
		else if(y != 0 && arr[z][y - 1] == str.charAt(i) && bf != 4) {
			ck = i < str.length() - 1?check(arr, str, z, y - 1, i + 1, 2):true;
		}
		else if(z < arr.length - 1 && arr[z + 1][y] == str.charAt(i) && bf != 1) {
			ck = i < str.length() - 1?check(arr, str, z + 1, y, i + 1, 3):true;
		}
		else if(y < arr[z].length - 1 && arr[z][y + 1] == str.charAt(i) && bf != 2) {
			ck = i < str.length() - 1?check(arr, str, z, y + 1, i + 1, 4):true;
		}
		return ck;
	}
	
}

```
