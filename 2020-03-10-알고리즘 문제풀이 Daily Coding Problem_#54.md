알고리즘 문제풀이

package solution;

public class Solution19 {

//	Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits.
//	The objective is to fill the grid with the constraint that every row, column, 
//	and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.
//
//	Implement an efficient sudoku solver.
	
	static int[][] sudoku =  new int[9][9];
	int temp = 0;
	
	public static void main(String[] args) {
		
		for(int i = 0; i < 9; i ++) {
			for(int j = 0; j < 9; j ++) {
				sudoku[i][j] = j + 1;
				System.out.print(sudoku[i][j] + " ");
			}
			System.out.println();
		}
		
		System.out.println("-----------------------------------------------------------");
		check();
		
		print();
	}
	public static void check() {
		for(int i = 0; i < 9; i ++) {
			for(int j = 0; j < 9; j ++) {
​						 check2(i, j ,sudoku[i][j]);
​			}
​			}
​		

	}
	
	public static void check2(int i,int j,  int num) {
			for(int k = 0; k < 9; k ++) {
				if(i != k && sudoku[k][j] == num) {
					shuffle(num, k);
				}
			
		}
		
	}
	
	public static void shuffle(int n, int i) {
		for(int j = 1; j < 9; j ++) {
			sudoku[i][j -1] = sudoku[i][j];
		}
		sudoku[i][8] = n;
		}


​	
​	
	//3 * 3 검증 로직 추가하기


​	
	public static void print() {
		for(int i = 0; i < 9; i ++) {
			for(int j = 0; j < 9; j ++) {
				System.out.print(sudoku[i][j] + " ");
			}
			System.out.println();
		}
	}
}