다이나믹 알고리즘 문제풀이 



문제 설명

​	Given a array of numbers representing 
​	the stock prices of a company in chronological order,
​	write a function that calculates the maximum profit 
​	you could have made from buying and selling that stock once. 
​	You must buy before you can sell it.

​	For example, given [9, 11, 8, 5, 7, 10],
​	you should return 5, since 
​	you could buy the stock at 5 dollars and sell it at 10 dollars.



package solution;

public class Solution10 {



	public static void main(String[] args) {
	
		int[] input = {9, 11, 8, 5, 7, 10};
		int[] result = new int[input.length];
		int cost = input[0];
		result[0] = 0;
		for(int i = 1; i < input.length; i++) {
			if(input[i] <= cost) {
				cost = input[i];
				result[i] = 0;
			}else if(input[i] > cost) {
				result[i] = Math.max(input[i] - cost, result[i - 1]);
			}
		}
		System.out.println(result[input.length - 1]);
	}

}