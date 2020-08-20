알고리즘 문제풀이



```java
package DailyCoding;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


//	We're given a hashmap associating each courseId key 
//		with a list of courseIds values,
//	which represents that the prerequisites of courseId are courseIds.
//	Return a sorted ordering of courses such that we can finish all courses.
//
//	Return null if there is no such ordering.
//
//	For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].

public class DailyCoding92 {

	static List<String> result = new ArrayList<String>();
	public static void main(String[] args) {
		
		Map<String, List>map = new HashMap<String, List>();
		
		
		List<String> CS300 = new ArrayList<String>();
		List<String> CS200 = new ArrayList<String>();
		List<String> CS100 = new ArrayList<String>();
		List<String> CS400 = new ArrayList<String>();
		CS300.add("CS100");
		CS300.add("CS200");
		CS200.add("CS100");
		CS400.add("CS100");
		CS400.add("CS200");
		CS400.add("CS300");
		
		map.put("CS400", CS400);
		map.put("CS300", CS300);
		map.put("CS200", CS200);
		map.put("CS100", CS100);
		
		System.out.println(makeCourse("CS400", map, map.get("CS400")));
		
	}
	
	public static List makeCourse(String key, Map<String, List> courses, List<String> list) {
		if(result.contains(key))return result;
		if(!courses.containsKey(key) || courses.get(key) == null)result = null;
		else {
			
			for(int i = 0; i < list.size(); i ++) {
				makeCourse(list.get(i), courses, courses.get(list.get(i)));
			}
			result.add(key);
		}	
		return result;
	}
}

```
