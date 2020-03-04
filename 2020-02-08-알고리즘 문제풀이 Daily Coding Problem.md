알고리즘 문제풀이

package solution;

import java.util.Arrays;
import java.util.Scanner;

public class Solution16 {

//	Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, 
//	write a function that shuffles a deck of cards represented as an array using only swaps.
//	It should run in O(N) time.

	public static void main(String[] args) {
	
		Scanner sc = new Scanner(System.in);
		
		int k = sc.nextInt();
		int random = 0;
			
			random = (int)(Math.random() * k) + 1;
	
			System.out.println(Arrays.toString(Swap(random)));
	}
	
	public static int[] Swap(int r) {
		String temp = r+"";
		int su = 0;
		int[] result = new int[temp.length()];
		for(int i = 0; i < temp.length(); i ++) {
			result[i] = temp.charAt(i) - '0';
			System.out.println(result[i]);
		}
		
		for(int i = 1; i < temp.length(); i++) {
			su = result[i];
			result[i] = result[i - 1];
			result[i - 1] = su;
		}
		
		return result;
	}
}