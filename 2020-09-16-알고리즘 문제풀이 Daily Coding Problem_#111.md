package DailyCoding;

import java.util.ArrayList;
import java.util.List;

//Given a word W and a string S, find all starting indices in S which are anagrams of W.

//For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

public class DailyCoding111 {

	
	public static void main(String[] args) {
		
		String S = "abxaba";
		String W = "ab";
		List list = new ArrayList<Integer>();
		int ck = 0;
		int result;
		
		for(char c : W.toCharArray()) {
			ck += c;
		}

		for(int i = 0; i < S.length() - (W.length() - 1); i ++) {
			result = S.charAt(i);
			for(int j = 1; j < W.length(); j ++) {
				result += S.charAt(i + j);
				if(ck == result) {
					list.add(i);
				}
			}
		}
		System.out.println(list);
	}
}
