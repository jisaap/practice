알고리즘 문제풀이



```java
package DailyCoding;



//Given a 2D matrix of characters and a target word, 
//write a function that returns whether the word
//can be found in the matrix by going left-to-right, or up-to-down.
//
//For example, given the following matrix:
//
//[['F', 'A', 'C', 'I'],
// ['O', 'B', 'Q', 'P'],
// ['A', 'N', 'O', 'B'],
// ['M', 'A', 'S', 'S']]
//and the target word 'FOAM', 
//you should return true,
//		since it's the leftmost column. Similarly,
//		given the target word 'MASS',
//		you should return true, since it's the last row.

public class DailyCoding63 {

	public static void main(String[] args) {

		char[][] matrix = {{'F', 'A', 'C', 'I'},
				{'O', 'B', 'Q', 'P'},
				{'A', 'N', 'O', 'B'},
				{'M', 'A', 'S', 'S'}};
		String targetWord = "MASS";
		
		System.out.println(checkWord(matrix, targetWord));
		
	}
	
	public static boolean checkWord(char[][] m, String tw) {
		
		String col = "";
		String row = "";
		for(int i = 0; i < m.length; i ++) {
			for(int j = 0; j < m[i].length; j ++) {
				col += m[i][j];
				row += m[j][i];
				System.out.println("col : " + col + "       row : " + row);
				if(col.equals(tw)) {
					return true;
				}else if(row.equals(tw)) {
					return true;
				}
			}
			col = "";
			row = "";
		}
		return false;
	}
	
}

```
