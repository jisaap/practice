알고리즘 문제풀이



```java
package DailyCoding;

import java.text.DecimalFormat;
import java.text.ParseException;
import java.util.Scanner;

//Given a string, return whether it represents a number.
//Here are the different kinds of numbers:

//"10", a positive integer
//"-10", a negative integer
//"10.1", a positive real number
//"-10.1", a negative real number
//"1e5", a number in scientific notation
//And here are examples of non-numbers:

//"a"
//"x 1"
//"a -2"
//"-"


public class DailyCoding123 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String input = sc.nextLine();
		
		
		System.out.println(ckNum(input));
		
		
		
	}
	
	
	
	public static Number ckNum(String in) {
		String s = "";
		boolean ck = false;
		int[] val = {0,0};
		for(int i = 0; i < in.length(); i ++) {
			char c = in.charAt(i);
			if(c == ' ')continue;
			if(ck) {
				if(val[1] == 0 && c == '-')val[1] =  -1;
				else if(val[1] == -1 && 48 <= c && c <= 57)val[1] = val[1] * Integer.parseInt(c +"");
				else if(val[1] != -1 && 48 <= c && c <= 57)val[1] = val[1] *10 + Integer.parseInt(c +"");
				else {
					ck = false;
					s += Math.pow(val[0], val[1]);
				}
				s += i == in.length() - 1? Math.pow(val[0], val[1]):"";
				continue;
			}
			c = c == 'x' || c == 'X'? '*' : c;
			if(c == '^') ck = true;
			else if(48 <= c && c <= 57) {
				val[0] = val[0]  * 10 + Integer.parseInt(c + "");
			}else {
				s += val[0] !=0?val[0]:"" + (c + "");
				val[0] = 0;
			}
		}
		DecimalFormat df = new DecimalFormat("0.################");
		Number num;
		try {
			num = df.parse(s);
		} catch (ParseException e) {
			return null;
		}
		
		return num;
	}
	
	
	
	
}

```
