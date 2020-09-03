알고리즘 문제풀이



```java
package DailyCoding;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//Given an even number (greater than 2), 
//return two prime numbers whose sum will be equal to the given number.
//
//A solution will always exist. See Goldbach’s conjecture.
//
//Example:
//
//Input: 4
//Output: 2 + 2 = 4
//If there are more than one solution possible, 
//return the lexicographically smaller solution.
//
//If [a, b] is one solution with a <= b, 
//and [c, d] is another solution with c <= d, then
//
//[a, b] < [c, d]
//If a < c OR a==c AND b < d.  <<== 어떤 경우를 말하는지 모르겟다.


public class DailyCoding101 {

	
	public static void main(String[] args) {
		List list = new ArrayList();
		Scanner sc = new Scanner(System.in);
		int a = 0;
		int b = 0;
		int input = sc.nextInt();
		
		list.add(2);
		
		for(int i = 2; i < input; i ++) {
			int count = 0;
			for(int j = 0; j < list.size(); j ++) {
				if(i%(int)list.get(j) != 0) {
					count ++;
				}
				if(count == list.size())list.add(i);
			}
		}
		
		System.out.println(list);

		if(list.contains(input/2)) {
			a = input/2;
			b = input/2;
		}else {
			int n = 0;
			int m = 0;
			for(int i = 0; i < list.size(); i ++) {
				if(input/2 - (int)list.get(i) < 0) {
					n = i;
					m = i;
					break;
				}
				
			}
			int sum = 0;
			while(n > 0 && m < list.size()) {
				sum = (int)list.get(n) + (int)list.get(m);
				if(sum > input) {
					n--;
				}else if(sum < input) {
					m++;
				}else {
					a = (int)list.get(n);
					b = (int)list.get(m);
					break;
				}
			}
		}
		
		System.out.println("Output : " + a +" + " + b + " = " + input);
		
		
	}
}

```
