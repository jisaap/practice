알고리즘 문제풀이



```java
package DailyCoding;


//here is an N by M matrix of zeroes. Given N and M, 
//write a function to count the number of ways of starting 
//at the top-left corner and getting to the bottom-right corner.
//You can only move right or down.
//
//For example, given a 2 by 2 matrix,
//you should return 2,
//		since there are two ways to get to the bottom-right:
//
//Right, then down
//Down, then right
//Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

// 오른쪽, 아래로만 갈수 있다.
// 재귀함수로 구현
// 재귀 함수 flag 의미 없음

public class DailyCoding62 {

	public static int count = 0;
	public static int n = 5;
	public static int m = 5;

	public static void main(String[] args) {
		
		find(0,0);
		System.out.println(count);
	}
	
	public static void find(int x, int y) {
		if(x == n - 1 && y == m - 1) {
			count ++;
		}
		
		//아래로 가는 경우
		if(x < n - 1) {
				find(x+1,y);
		}
		//오른쪽으로 가는 경우
		if(y < m -1) {
			find(x,y+1);
		}
		
	}

}

```
