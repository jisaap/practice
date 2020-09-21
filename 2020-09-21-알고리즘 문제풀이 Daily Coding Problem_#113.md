알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

//Given a string of words delimited by spaces, reverse the words in string.
//For example, given "hello world here", return "here world hello"

//Follow-up: given a mutable string representation, can you perform this operation in-place?

public class DailyCoding113 {

	
	public static void main(String[] args) {

		String input = "Hello World here";
		List list = Arrays.asList(input.split(" "));
		Collections.reverse(list);
		System.out.println(String.join(" ", list));
		
	}
	
}

```
