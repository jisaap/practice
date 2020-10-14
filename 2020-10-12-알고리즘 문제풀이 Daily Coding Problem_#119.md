알고리즘 문제풀이



```java
package DailyCoding;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

//Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.

//For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.

public class DailyCoding119 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String str = "";
		sc.nextLine();
		List<List<Integer>> listSet = new ArrayList<List<Integer>>();
		for(int i = 0; i < N; i ++) {
			listSet.add(new ArrayList<Integer>());
			str = sc.nextLine();
			
			List<Integer> input = listSet.get(i);
			for(int j = 0; j < 2; j ++) {
				input.add(Integer.parseInt(str.split(", ")[j]));
			}
		}
		System.out.println(solution(listSet));
	}
	
	public static List<Integer> solution(List<List<Integer>> input) {
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		List<Integer> result = new ArrayList<Integer>();
		int su;
		for(int i = 0; i < input.size(); i ++) {
			for(int j = 0; j < input.get(i).size(); j ++) {
				su = input.get(i).get(j);
				if(map.containsKey(su))map.put(su, map.get(su) + 1);
				else map.put(su, 1);
			}
		}
		int aVal = 0;
		int bVal = 0;
		String temp = "aVal";
		for(int key : map.keySet()) {
			if(result.size() != 0) {
				if(aVal <= map.get(key) || bVal <= map.get(key))temp = aVal < bVal?"aVal":aVal ==bVal?"CK":"bVal";
			}
			if(temp == "CK") temp = result.get(0) > result.get(1)?"aVal":"bVal";
			if(temp == "aVal" && aVal <= map.get(key) ) {
				if(result.size() != 0)result.remove(0);
				aVal = map.get(key);
				result.add(0, key);
			}
			if(temp == "bVal" && bVal <= map.get(key)) {
				if(result.size() != 1)result.remove(1);
				bVal = map.get(key);
				result.add(1, key);
			}
			
			temp = "";
			
		}
		if(result.get(0) > result.get(1)) {
			temp = result.get(0) + "";
			result.remove(0);
			result.add(Integer.parseInt(temp));
		}
		return result;
	}
	
}

```
