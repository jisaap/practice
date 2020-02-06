알고리즘 문제풀이 



문제 설명

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
													34  -16  42  56   51  137
					i -1    i   result - 1
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.



public class Solution13 {


	public static void main(String[] args) {
		
		int[] arr = {34, -50, 42, 14, -5, 86};
		int[] arr2  = {-5, -1, -8, -9};
		System.out.println(calculator(arr));
		System.out.println(calculator(arr2));
	}
	
	public static int calculator(int[] arr) {
		int[] result = new int[arr.length];
		int answer = 0;
	
		result[0] = arr[0];
		for(int i = 1; i < arr.length; i++) {
			result[i] = Math.max(arr[i], Math.max(result[i - 1] + arr[i], 0));
			if(answer < result[i])answer = result[i];
		}
		return answer;
	}
}