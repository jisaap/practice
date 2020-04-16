알고리즘 문제풀이



```java
package DailyCoding;


//Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
//
//For example, given the following matrix:
//
//[[1,  2,  3,  4,  5],
// [6,  7,  8,  9,  10],
// [11, 12, 13, 14, 15],
// [16, 17, 18, 19, 20]]
//You should print out the following:
//
//1
//2
//3
//4
//5
//10
//15
//20
//19
//18
//17
//16
//11
//6
//7
//8
//9
//14
//13
//12



public class DailyCoding65 {
	
	static int num = 0;
	static int ck = 1;
	
	public static void main(String[] args) {
		
		
//		int[][] arr = 1,  2,  3,  4,  5,
//		              6,  7,  8,  9,  10,
//		              11, 12, 13, 14, 15,
//		              16, 17, 18, 19, 20;
		
		int cnt = arr.length * arr[0].length;
		
		printRight(arr, cnt, 1, 1);
		
		
	}
	
	public static void printRight(int[][] arr, int cnt , int i, int j) {
		int su = 0;
		for(int k = j - 1; k < arr[i].length - ck; k ++) {
			num ++;
			if(cnt == num + 1) {
				System.out.println(arr[i -1][k]);
				return;
			}
			System.out.println(arr[i - 1][k]);
			su = k;
		}
		printDown(arr, cnt, i, su);
		
	}
	public static void printDown(int[][] arr, int cnt , int i, int j) {
		int su = 0;
		for(int k = i - 1; k < arr.length - ck; k ++) {
			num ++;
			System.out.println(arr[k][j + 1]);
			if(cnt == num + 1) {
				System.out.println(arr[k][j + 1]);
				return;
			}
			su = k;
		}
		printLeft(arr, cnt, su, j);

	}
	public static void printLeft(int[][] arr, int cnt , int i, int j) {
		int su = 0;
		for(int k = j + 1; k >= ck; k --) {
			num ++;
			System.out.println(arr[i + 1][k]);
			if(cnt == num + 1) {
				System.out.println(arr[i + 1][k - 1]);
				return;
			}
			su = k;
		}
		printUp(arr, cnt, i, su);
		
	}
	public static void printUp(int[][] arr, int cnt , int i, int j) {
		ck ++;
		int su = 0;
		for(int k = i + 1; k >= ck; k --) {
			num ++;
			System.out.println(arr[k][j - 1]);
			if(cnt == num + 1) {
				System.out.println(arr[k][j - 1]);
				return;
			}
			su = k;
		}
		printRight(arr, cnt, su, j);

	}

}

```
