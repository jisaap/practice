알고리즘 문제풀이



```java
package DailyCoding;


//Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.
//
//For example, this matrix has 4 islands.

public class DailyCoding84 {

	
	static int count = 0;

	static int[][] arr = 1, 0, 0, 0, 0,
									0, 0, 1, 1, 0,
									0, 1, 1, 0, 0,
									0, 0, 0, 0, 0,
									1, 1, 0, 0, 1,
									1, 1, 0, 0, 1;
	
	static int[][] bisit = new int[arr.length][arr[0].length];
	public static void main(String[] args) {
		
		for(int i = 0; i < bisit.length; i ++) {
			for(int j = 0; j < bisit[i].length; j ++) {
				bisit[i][j] = 1;
			}
		}
		
		for(int i = 0; i < arr.length; i ++) {
			for(int j = 0; j < arr[i].length; j ++) {
				if(arr[i][j] == 1)  {
					check(i,j,i,j);
				}
			}
		}
		System.out.println(count);
	}
	
	
	public static void check(int i, int j, int x,int y) {
		bisit[i][j] = 0;
		if(arr[i][j]==0) return;
		//위
		if(i > 0 && bisit[i - 1][j] != 0)check(i - 1, j, x, y);
		//왼쪽
		if(j > 0 && bisit[i][j-1] != 0)check(i,j-1,  x, y);
		//아래
		if(i < arr.length - 1  && bisit[i + 1][j] != 0)check(i + 1, j,  x, y);
		// 오른쪽
		if(j < arr[i].length - 1 && bisit[i][j+1] != 0)check(i,j + 1,  x, y);
		
		arr[i][j] = 0;
		if(i == x && j == y)count ++;
	}
	
}

```

