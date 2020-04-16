알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Scanner;

//You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.
//
//For example, given the following table:
//
//	cba
//	daf
//	ghi
//This is not ordered because of the a in the center. We can remove the second column to make it ordered:
//
//	ca
//	df
//	gi
//So your function should return 1, since we only needed to remove 1 column.
//
//As another example, given the following table:
//
//	abcdef
//Your function should return 0, since the rows are already ordered (there's only one row).
//
//As another example, given the following table:
//
//	zyx
//	wvu
//	tsr
//Your function should return 3, since we would need to remove all the columns to order it.




public class DailyCoding76 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
//		int n = sc.nextInt();
//		int m = sc.nextInt();
//		
//		char[][] arr = new char[n][m];
//		
//		
//		for(int i = 0; i < n; i ++) {
//			for(int j = 0; j < m; j ++) {
//				arr[i][j] = sc.next().charAt(0);
//			}
//		}
//		
		
//		TestValue
		
		int n = 3;
		int m = 3;
		char[][]arr = new char[n][m];
//		char[][] arr = 'c','b','a','d','a','f','g','h','i';
//		char[][] arr = 'z','y','x','d','a','f','g','h','i';
//		char[][] arr = 'a','b','c','d','e','f';

		int num;
		int count = 0;
		
		for(int i = 0; i < m; i ++) {
			num = 0;
			for(int j = 0; j < n; j ++) {
				if(num < arr[j][i]) {
					num = arr[j][i];
				}else {
					count ++;
					break;
				}
			}
		}
		System.out.println(count);
	}
}

```
