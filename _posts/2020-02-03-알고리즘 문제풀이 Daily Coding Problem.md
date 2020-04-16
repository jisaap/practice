다이나믹 알고리즘 문제풀이 



문제 설명

	Given a string, find the longest palindromic contiguous substring.
	If there are more than one with the maximum length, return any one.
	
			For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
			The longest palindromic substring of "bananas" is "anana".


package solution;

public class Solution12 {

	public static void main(String[] args) {
		String[] ex = {"aabcdcb", "bananas"};
		
		for(int i = 0; i < ex.length; i ++) {
			System.out.println(solution(ex[i]));
		}
	}
	
	public static String solution(String s) {
		String result = "";
		String temp = "";
		for(int i = 0; i < s.length(); i ++) {
			temp = s.substring(s.indexOf(s.charAt(i)),  s.lastIndexOf(s.charAt(i)) + 1);
			if(result.length() < temp.length()) {
				result = temp;
			}
		}
		return result;
	}

}