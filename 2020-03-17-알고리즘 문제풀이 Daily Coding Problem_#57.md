알고리즘 문제풀이

```java
package daily_Codiong;

import java.util.Arrays;

//Given a string s and an integer k, 
//break up the string into multiple lines such that each line has a length of k or less. 
//You must break it up so that words don't break across lines.
//Each line has to have the maximum possible amount of words.
//If there's no way to break the text up, then return null.
//
//You can assume that there are no spaces at the ends of the string
//and that there is exactly one space between each word.
//
//For example, given the string
//"the quick brown fox jumps over the lazy dog" and k = 10, 
//you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"].
//		No string in the list has a length of more than 10.

public class DailyCoding57 {

	public static void main(String[] args) {

		String s = "the quick brown fox jumps over the lazy dog";
		int k = 10;
		String result = "";
		String temp = "";
		String[] arr;

		arr = s.split(" ");

		for (int i = 0; i < arr.length; i++) {
			if (arr[i].length() > k) {
				result = null;
				temp = null;
				break;
			} else if (temp.length() + (arr[i].length() + 1) > k) {
				result += "\"" + temp + "\",";

				temp = arr[i];
			} else {
				temp += (temp == "" ? arr[i] : " " + arr[i]);
			}
		}
		if (temp != null)
			result += "\"" + temp + "\"";
		System.out.println(Arrays.toString(
            result != null ? result.split(",") : null));
	}
}

```
