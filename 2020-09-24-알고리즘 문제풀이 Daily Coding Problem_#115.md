알고리즘 문제풀이



```java
package DailyCoding;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

//Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
//A subtree of s is a tree consists of a node in s and all of this node's descendants.
//The tree s could also be considered as a subtree of itself.

//비어 있지 않은 두 개의 이진 트리 s와 t가 주어지면 트리 t가 s의 하위 트리를 가진 구조와
//노드 값이 정확히 동일한 지 확인합니다.
//s의 하위 트리는 s의 노드와이 노드의 모든 하위 항목으로 구성된 트리입니다.
//트리는 자체 하위 트리로 간주 될 수도 있습니다.

public class DailyCoding115 {

	private static ArrayList<Integer>[] s;
	private static ArrayList<Integer>[] t;
	private static int[][] parent;
	private static boolean[] visit;
	
	private static int N;
	private static int M;
	
	private static final String NEW_LINE = "\n";
	
	public static void main(String[] args) throws Exception {
		BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		visit = new boolean[N];

		s = new ArrayList[N];
//		트리 초기화
		for(int i = 0; i < N; i ++) {
			s[i] = new ArrayList<Integer>();
		}

		int loopN = N - 1;
//		s 데이터 입력
		while(loopN -- > 0) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int node1 = Integer.parseInt(st.nextToken());
			int node2 = Integer.parseInt(st.nextToken());
			s[node1].add(node2);
			s[node2].add(node1);
		}
		M = Integer.parseInt(br.readLine());
		t = new ArrayList[M];

		
		for(int i = 0; i < M; i ++) {
			t[i] = new ArrayList<Integer>();
		}
		int loopM = M - 1;
//		t 데이터 입력
		while(loopM -- > 0) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int node1 = Integer.parseInt(st.nextToken());
			int node2 = Integer.parseInt(st.nextToken());
			t[node1].add(node2);
			t[node2].add(node1);
		}
		
		findRoot(0, 0, 0);
	}
//	값이 같은지 체크 (재귀함수)
	public static boolean findRoot(int current, int depth, int ck) {
		visit[current] = true;
		
		for(int sn : s[current]) {
			if(visit[sn])continue;
//			t의 root 와 같은 값 찾기(구현 필요)
//			while 사용할지 부모 루트 찾을지 t노드와 비교할 방법 찾기
//			for(int tn : t[ck]) {
//				
//			}
//			if(t[ck].get(tn) == sn) {
//				boolean c = findRoot(sn, depth + 1, ck + 1);
//				return c == true?true:false;
//			}else {
//				if(ck == 0)findRoot(sn, depth + 1, ck);
//			}
			
		}
		
		return false;
	}
	
//	input 데이터 샘플
//		10
//		9 8
//		9 7
//		7 6
//		6 0
//		0 1
//		0 2
//		0 3
//		1 4
//		4 5
//
//		6
//		0 1
//		0 2
//		0 3
//		1 4
//		4 5
	
	
}

```
