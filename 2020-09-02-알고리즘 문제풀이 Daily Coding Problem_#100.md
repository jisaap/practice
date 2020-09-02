알고리즘 문제풀이



```java
package DailyCoding;


//You are in an infinite 2D grid where you can move in any of the 8 directions:
//	 (x,y) to
//	    (x+1, y),
//	    (x - 1, y),
//	    (x, y+1),
//	    (x, y-1),
//	    (x-1, y-1),
//	    (x+1,y+1),
//	    (x-1,y+1),
//	    (x+1,y-1)
//	    
//	You are given a sequence of points and the order in which you need to cover the points. 
//	Give the minimum number of steps in which you can achieve it.
//	You start from the first point.
//
//	Example:
//
//	Input: [(0, 0), (1, 1), (1, 2)]
//	Output: 2
//	It takes 1 step to move from (0, 0) to (1, 1).
//	It takes one more step to move from (1, 1) to (1, 2).


public class DailyCoding100 {

	public static void main(String[] args) {
		
		int[][] input = ((0,0),(2,1),(1,3));
		int result = 0;
		for(int i = 1; i < input.length; i ++) {
			result += check(input[i - 1][0], input[i - 1][1], input[i][0], input[i][1]);
		}
		System.out.println(result);
	}
	
	
	public static int check(int stX, int stY, int deX, int deY) {
		int count = 0;
		
		int x = stX - deX > 0 ? stX - deX : deX - stX;
		int y = stY - deY > 0 ? stY - deY : deY - stY;
		
		while(x != 0 || y != 0) {
			if(x > 0 && y > 0) {
				x --;
				y --;
				count ++;
			}else if(x > 0) {
				x --;
				count ++;
			}else if(y > 0) {
				y --;
				count ++;
			}
		}
		
		
		return count;

	}
}

```
