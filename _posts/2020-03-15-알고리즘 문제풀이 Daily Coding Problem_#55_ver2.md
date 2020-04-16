알고리즘 문제풀이



HashMap을 이용해 URL을 6글자로 줄이고 6글자를 KEY값으로 활용해 DeCode 하는 형태

```java
package daily_Codiong;

import java.util.HashMap;
import java.util.Scanner;

//shorten(url), which shortens the url into
//a six-character alphanumeric string, such as zLg6wl.
//restore(short), which expands the shortened string 
//into the original url. If no such shortened string exists,
//return null.
//
//Hint: What if we enter the same URL twice?

public class DailyCoding55 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String url = sc.nextLine();
		int divide = 0;
		HashMap<Character, String> map = new HashMap<Character, String>();

		divide = (int) (Math.ceil(url.length() / 6.0));

		String result = shorten(url, map, divide);

		System.out.println("EnCoding  : " + result);

		System.out.println("DeCoding  : " + restore(result, map));
	}

	public static char settingURL(HashMap<Character, String> map) {
		char result = ' ';
		int num = (int) (Math.random() * 3) + 1;
		switch (num) {
		case 1:
//		대문자 char 값
			result = (char) ((int) (Math.random() * 25) + 65);
			break;
		case 2:
//		소문자 char 값
			result = (char) ((int) (Math.random() * 25) + 97);
			break;
		case 3:
//		숫자 char값 
			result = (char) ((int) (Math.random() * 10) + 48);
			break;
		}
			if (!map.containsKey(result)) {
				return result;
			} else {
				return settingURL(map);
			}
	}

	public static String shorten(String url, HashMap<Character, String> map, int divide) {
		char c = ' ';
		int firstIndex = 0;
		int lastIndex = 0;
		String enCode = "";

		for (int i = 0; i < 6; i++) {
			firstIndex = i * divide;
			lastIndex = firstIndex + divide;
			if (lastIndex < url.length()) {
				c = settingURL(map);
				map.put(c, url.substring(firstIndex, lastIndex));
				// divide로 나눌때 값이 떨어지지 않아 나누는 수보다는 적게 남은 경우
			} else if (firstIndex < url.length() && url.length() <= lastIndex) {
				String arr = "";
				for (int j = firstIndex; j < url.length(); j++) {
					arr += url.charAt(j);
				}
				c = settingURL(map);
				map.put(c, arr);
			} else {
				c = settingURL(map);
				map.put(c, "");
			}
			enCode += c;
		}

		return enCode;
	}

	public static String restore(String enCode, HashMap<Character, String> map) {
		String deCode = "";
		for (int i = 0; i < enCode.length(); i++) {
			deCode += map.get((char) enCode.charAt(i));
		}

		return deCode;
	}

}
```
