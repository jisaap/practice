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
		int arr[] = new int[k];
		int su = 0;
		int r = 0;
		for(int i = 0; i < k; i ++) {
			arr[i] = i + 1;
		}
		
		for(int i = 0; i < k; i ++) {
			r = (int)(Math.random() * k) + 1;
			if(i != r) {
				su = arr[i];
				arr[i] = arr[r];
				arr[r] = su;
			}
		}
		
		System.out.println(Arrays.toString(arr));
	}
}