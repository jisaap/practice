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

// 방문했던 node를 재방문 해야하는 경우가 많음
// visit을 체크해서 못가게 만들면 경우의 수를 구할수가 없다.
// 오른쪽 아래로만 갈수 있다. 아래로 갈수 없을 경우 오른쪽으로 갈수 있는지 확인
// visit 체크를 어떻게 할것인지...
// 오른쪽으로 이동하는 것만 카운트 하고 카운트한 수가 m과 같으면 flase
// 재귀함수로 구현

public class DailyCoding62 {

	public static int count = 0;
	public static int n = 5;
	public static int m = 5;
	public static int check = 0;
	public static boolean [][] flag = new boolean[n][m];

	public static void main(String[] args) {
		
		// 초기화
		flag = resetFlag(flag);
		find(0,0);
		System.out.println(count);
	}
	
	public static void find(int x, int y) {
		
		if(x == n - 1 && y == m - 1) {
			count ++;
		}
		
		//아래로 가는 경우
		if(x < n - 1) {
			if(flag[x+1][y]!= false) {
				check = 0;
				find(x+1,y);
			}
		}
		//오른쪽으로 가는 경우
		if(y < n -1) {
			check ++;
			find(x,y+1);
			if(check == m) {
				flag[x][y] = false;
			}
		}
		
	}
	
	public static boolean[][] resetFlag(boolean[][] b) {
		
		for(int i = 0; i < b.length; i ++) {
			for(int j = 0; j < b[1].length; j ++) {
				b[i][j] = true;
						}
		}
		return b;
	}

}

```
