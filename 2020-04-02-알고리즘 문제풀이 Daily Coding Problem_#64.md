알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Scanner;

//A knight's tour is a sequence of moves
//by a knight on a chessboard such that all squares are visited once.
//Given N, write a function to return
//the number of knight's tours on an N by N chessboard.


public class DailyCoding64 {

	static int count = 0;
	
	static Scanner sc = new Scanner(System.in);
	
	static int n = sc.nextInt();

	static int[][] ck = new int[n][n];
	
			
	public static void main(String[] args) {
		

		for(int i = 0; i < n; i ++) {
			for(int j = 0; j < n; j ++) {
				reset();
				tourCount(i, j, i, j);
			}
		}
		System.out.println(count);
	}
//	점점 햇갈리기 시작했다..;; ㅈ내일하쟈
	public static void tourCount(int i, int j, int x, int y) {
		ck[i][j] = 1;
 //		리턴
		if(check()) {
			reset();
			ck[x][y] = 1;
			count ++;
			return;
		}
		
//		위로
		if(i > 0 && ck[i - 1][j] != 1)  { 
			tourCount(i - 1, j, x, y);
			if(i != x && j != y) return;
		}
//		왼쪽
		if(j > 0 && ck[i][j - 1] != 1) { 
			tourCount(i, j - 1, x, y);
			if(i != x && j != y) return;
		}
//		아래
		if(i < n - 1 && ck[i + 1][j] != 1) { 
			tourCount(i + 1, j, x, y);
			if(i != x && j != y) return;
		}
//		오른쪽
		if(j < n - 1 && ck[i][j + 1] != 1) { 
			tourCount(i, j + 1, x, y);
			if(i != x && j != y) return;
		}
	}	
	
	public static boolean check() {
		for(int i = 0; i < n; i ++) {
			for(int j = 0; j < n; j ++) {
				if(ck[i][j] == 0) {
					return false;
				}
			}
		}
		
		return true;
	}
	
	public static void reset() {
		for(int i = 0; i < n; i ++) {
			for(int j = 0; j < n; j ++) {
				ck[i][j] = 0;
			}
		}
	}
}

```
