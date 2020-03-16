알고리즘 문제풀이



이렇게 하는거 아닌거 같은데;;

Color (1 , 2 )로 구분 아예 칠할수 없는 Node는 -1

```java
package daily_Codiong;

import java.util.Scanner;

public class DailyCoding56 {

//	Given an undirected graph represented as an adjacency matrix and an integer k,
//	write a function to determine whether each vertex in the graph 
//	can be colored such that no two adjacent vertices
//	share the same color using at most k colors.

	public static void main(String[] args) {
        
//		  0 ----1
//		  |  /  |
//        3-----2       
//		Node 수
		int k = 4;
		int colorType = 2;
		int[][] matrix = {{0,1,0,1},      // 0
						  {1,0,1,1},      // 1
						  {0,1,0,1},      // 2
						  {1,1,1,0}};     // 3
		boolean[] color = new boolean[colorType];
		int[] paint = new int[k];
		
		for(int i = 0; i < paint.length; i ++) {
			if(!checkPaint(i, matrix, paint, color)) {
				paint[i] = -1;
			}
			if(i == paint.length - 1)print(paint); 
		}

	}

	
	public static boolean checkPaint(int i, int[][] matrix, int[] paint, boolean[] color) {
		boolean check = false;
		color[0] = true;
		color[1] = true;
		for(int j = 0; j < i; j ++) {
			if(matrix[i][j] == 1) {
				if(paint[j] != -1)color[paint[j]] = false;
			}
		}
			for(int z = 0; z < color.length; z ++) {
				if(color[z] == true) {
					paint[i] = z;
					check = true;
				}
			}
		return check;
	}

	
	
	
	public static void print(int[] paint) {
		
		for(int i = 0; i < paint.length; i ++) {
			System.out.println("Node " + i + " : " + paint[i]);
		}
	}
	
}
```
