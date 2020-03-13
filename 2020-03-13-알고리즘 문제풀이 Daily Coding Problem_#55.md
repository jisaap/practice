알고리즘 문제풀이



자바에 URLEncoder라는 함수가 있어서 써봤는데 문제를 자세히 읽어 보니 단축 URL만들기네;;

감도 안잡힌다..ㅜ

일요일까지



package daily_Codiong;

import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.net.URLEncoder;
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


​		
		String result = shorten(url);
		
		System.out.println("EnCoding  : " + result);
		
		System.out.println("DeCoding  : " + restore(result));
	}
	
	public static String shorten(String url) {
		String enCode = "";
		try {
			enCode = URLEncoder.encode(url, "UTF-8");
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			enCode = null;
			e.printStackTrace();
		}
		return enCode;
	}
	
	public static String restore(String enCode) {
		String deCode;
		
		try {
			deCode = URLDecoder.decode(enCode, "UTF-8");
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			deCode = null;
			e.printStackTrace();
		}
		return deCode;
	}

}