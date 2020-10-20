알고리즘 문제풀이



```java
package DailyCoding;

//You are given a 2-d matrix where each cell represents number of coins in that cell.
//Assuming we start at matrix[0][0], and can only move right or down, 
//find the maximum number of coins you can collect by the bottom right corner.
//
//For example, in this matrix
//
//0 3 1 1
//2 0 0 4
//1 5 3 1
//The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.

public class DailyCoding122 {

	public static void main(String[] args) {

		int[][] input = [[0,3,1,1} , {2,0,0,4}, { 1,5,3,1]];
		
		System.out.println(maxval(input));
	}

	public static int maxval(int[][] input) {
		int[][] dp = new int[input.length][input[0].length];
		dp[0][0] = input[0][0];
		
		for(int i = 1; i < input.length; i ++)  dp[i][0] = dp[i-1][0] + input[i][0];
		for(int i = 1; i < input[0].length; i ++)dp[0][i] = dp[0][i - 1] + input[0][ i];

		for(int i = 1; i < input.length; i ++) {
			for(int j = 1; j < input[0].length; j ++) {
				dp[i][j] = Math.max(dp[i-1][j], dp[i][j - 1]) + input[i][j];
			}
		}
		return dp[input.length - 1][input[0].length - 1];
	}
	
}

```
