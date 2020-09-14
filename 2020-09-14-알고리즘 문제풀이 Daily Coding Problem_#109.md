알고리즘 문제풀이



```java
package DailyCoding;

import java.util.BitSet;

//Given an unsigned 8-bit integer, swap its even and odd bits.
//The 1st and 2nd bit should be swapped,
//the 3rd and 4th bit should be swapped, and so on.

//For example, 10101010 should be 01010101.
//11100010 should be 11010001.

//Bonus: Can you do this in one line?

// 10101010 과 01010101 을 이용하여 계산
// 입력값 과 10(170)의 and 연산을 통해 값을 추려내고 Right Shift 1 을 해준다.
// 입력값 과 01(85)의 and 연산을 통해 값을 추려내고 Left Shift 1을 해준다
// 이후 비트 OR 연산을 통해 둘중 하나라고 1을 포함하고 있으면 1을 아니면 0을 반환해준다.

public class DailyCoding109 {

	public static void main(String[] args) {

		int b = 214;
		System.out.println(String.format("%08d", Integer.parseInt(Integer.toBinaryString(b).toString())));
		System.out.println(String.format("%08d", Integer.parseInt(Integer.toBinaryString((b & 170) >> 1 | (b & 85) << 1).toString())));
	}
	
}


```
