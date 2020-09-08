알고리즘 문제풀이



```java
package DailyCoding;

import java.util.HashMap;
import java.util.Map;

//Given a string and a set of characters, 
//return the shortest substring containing all the characters in the set.
//
//For example, given the string "figehaeci" 
// and the set of characters {a, e, i}, you should return "aeci".
//
//If there is no substring containing all the characters in the set, return null.

public class DailyCoding103 {

	public static void main(String[] args) {
		
		String str = "figehaeci";
		char[] c = {'a', 'e', 'i'};
		Map<Integer, String> map =  new HashMap<Integer, String>();

		int index = 0;
		
		for(char s : str.toCharArray()) {
		
			for(int i = 0; i < index; i ++) {
				map.put(i, map.get(i) + s);
			}
			
			for(int i = 0; i < c.length; i ++) {
				if(s == c[i]) {
					map.put(index, s+"");
					index ++;
					break;
				}
			}
		}
		
		int result = ckMap(map, c);
		System.out.println(result != -1?map.get(result):null);
	
	}
	
	public static int ckMap(Map<Integer, String> map, char[] c) {
		boolean ck;
		int result = -1;
		int lIdx = 0;
	
		for(int i = 0; i < map.size(); i ++) {
			ck = true;
			lIdx = 0;
			for(int j = 0; j < c.length; j ++) {
				if(map.get(i).indexOf(c[j]) == -1) {
					ck = false;
					break;
				}else {
					lIdx = Math.max(lIdx, map.get(i).indexOf(c[j]));
				}
				if(j == c.length - 1)map.put(i, map.get(i).substring(0, lIdx + 1));
			}
				if(ck == true) {
					if(result == -1)result = i;
					else result = map.get(result).length() <= map.get(i).length()?result : i;
				}
		}
		return result;
	}
}

```
