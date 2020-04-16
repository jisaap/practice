알고리즘 문제풀이

 로직상 오류와  무한 반복문에서 해매다 결국 찾아 봤다.;;

수정이 좀 생겨서 다음에 다시 정리해야함

package solution;

public class Solution19 {

//	Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits.
//	The objective is to fill the grid with the constraint that every row, column, 
//	and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.
//
//	Implement an efficient sudoku solver.
	static int su = 10;
	static int[][] sudoku = new int[su][su];

	public static void main(String[] args) {
		for (int i = 1; i < su; i++) {
			for (int j = 1; j < su; j++) {
				sudoku[i][j] = 0;
			}
		}
		result(0);
	}
	
	public static void result(int c) {
		if (c == 81) {
			for (int i = 1; i < su; i++) {
				for (int j = 1; j < su; j++) {
					System.out.print(sudoku[i][j]);
				}
				System.out.println();
			}
			System.exit(0);
		}
		int col = 0;
		int row = 0;
		boolean flag = true;
		for (int i = 1; i < su; i++) {
			for (int j = 1; j < su; j++) {
				if (sudoku[i][j] == 0) {
					row = i;
					col = j;
					flag = false;
					break;
				}
			}
			if(!flag)break;
		}
		if(flag)return;


		for (int i = 1; i < su; i++) {
			int num = (int)(Math.random() * 9) + 1;
			if (checked(col, row, num)) {
				sudoku[row][col] = num;
				result(c + 1);
				sudoku[row][col] = 0;
			}
	
	}
	}
	
	public static boolean checked(int col, int row, int num) {
		if (checkCol(col, num) && checkrow(row, num) && check(col, row, num)) {
			return true;
		}
		return false;
	}
	
	public static boolean checkCol(int col, int num) {
		for (int i = 1; i < su; i++) {
			if (sudoku[i][col] == num) return false;
		}
		return true;
	}
	
	public static boolean checkrow(int row, int num) {
		for (int i = 1; i < su; i++) {
			if (sudoku[row][i] == num) return false;
		}
		return true;
	}
		public static boolean check(int col, int row, int num) {
			int c =((int)Math.ceil(col / 3.0) - 1) * 3 + 1;
			int r = ((int)Math.ceil(row / 3.0) - 1) * 3 + 1;
			for (int i = 0; i < 3; i++) {
				for(int j = 0; j < 3; j ++) {
					if (sudoku[r + i][c + j] == num) return false;
				}
			}
		return true;
		}
	}
	


​	
