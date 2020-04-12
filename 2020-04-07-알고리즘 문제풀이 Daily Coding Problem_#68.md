알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Scanner;

//On our special chessboard,
//two bishops attack each other if they share the same diagonal. 
//This includes bishops that have another bishop located between them,
//i.e. bishops can attack through pieces.
//
//You are given N bishops, 
//represented as (row, column) tuples on a M by M chessboard.
//Write a function to count the number of pairs of bishops that attack each other.
//The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).
//
//For example, given M = 5 and the list of bishops:
//
//(0, 0)
//(1, 2)
//(2, 2)
//(4, 0)
//The board would look like this:
//
//[b 0 0 0 0]
//[0 0 b 0 0]
//[0 0 b 0 0]
//[0 0 0 0 0]
//[b 0 0 0 0]
//You should return 2, since bishops 1 and 3 attack each other, 
//		as well as bishops 3 and 4.

// 서로 공격이 가능하면 4번도 공격당하는데? 뭐지;;
public class DailyCoding68 {

	static int count = 0;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
//		int n = sc.nextInt();
//		int m = sc.nextInt();
		int n = 4;
		int m = 5;
		int[] ck = new int[n];
//		int[][] arr = new int[n];
//		for(int i = 0; i < n; i ++) {
//			for(int j = 0; j < 2; j ++) {
//				arr[i][j] = sc.nextInt();
//			}
//		}
//		test Value
		int[][] arr = {{0,0},{1,2},{2,2},{4,0}};
		
		int[][] chessBoard = new int[m][m];

		chessBoard = settingArr(arr,chessBoard);
		
		
		for(int i = 0; i < arr.length; i ++) {
			chessBoard[arr[i][0]][arr[i][1]] = 0;
			checkDL(arr[i][0], arr[i][1], chessBoard);
			checkDR(arr[i][0], arr[i][1], chessBoard);
		}
		
		System.out.println(count);
	}

	public static int[][] settingArr(int[][] arr, int[][] c) {
		for(int i = 0; i < arr.length; i ++) {
			for(int j= 0; j < arr[i].length; j ++) {
				c[arr[i][0]][arr[i][1]] = 1;
			}
		}
		return c;
	}

	public static void checkDL(int x , int y, int[][] c) {
		
		if(c[x][y] == 1) {
			count ++;
			return;
		}
//	좌측 아래 검증
				if(y > 0 && x < c.length - 1) {
					checkDL(x + 1, y - 1, c);
				}
				
				return;
	}
	
	public static void checkDR(int x, int y, int[][] c) {
		if(c[x][y] == 1) {
			count ++;
			return;
		}
		//	우측 아래 검증
		if(x < c.length - 1 && y < c[x].length - 1) {
			checkDR(x + 1, y + 1, c);
		}
		
		return;
	}
}

```
