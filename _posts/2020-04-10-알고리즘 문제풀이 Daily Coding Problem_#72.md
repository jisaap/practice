알고리즘 문제풀이



```java
package DailyCoding;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

//In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.
//
//Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.
//
//The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.
//
//For example, the following input graph:
//
//ABACA
//[(0, 1),
// (0, 2),
// (2, 3),
// (3, 4)]
//Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).
//
//The following input graph:
//
//A
//[(0, 0)]
//Should return null, since we have an infinite loop.


public class DailyCoding72 {

	static int  count = 0;

	static Map<Character, Integer> map = new HashMap<Character, Integer>();

	
	public static void main(String[] args) {
		
//	Scanner sc = new Scanner(System.in);
//
//	int n = sc.nextInt();
//	int m = sc.nextInt();
	
//	int[][] path = new int[m][2];
//	char[] nodes = new char[n];
//		for(int i = 0; i < n; i ++) {
//			nodes[i] = sc.next().charAt(0);
//		}
//	
//	for(int i = 0; i < m; i++) {
//		for(int j = 0; j < 2; j ++) {
//			path[i][j] = sc.nextInt();
//		}
//	}
//	Test Value
	int n = 5;
	int m = 4;
	int[][] path =          0, 1,
	            			0, 2,
	            			2, 3,
	            			3, 4;
	char[] nodes = 'A','B','A','C','A';
	

		
		for(int i = 0; i < nodes.length; i ++) {
			map.put(nodes[i], 0);
		}
		
		
		check(path,nodes, 0);
		
		System.out.println(count);
	}

	public static void resetMap() {
		int ck = 0;
		for(char k : map.keySet()) {
			
			if(map.get(k) > ck) {
				ck = map.get(k);
			}
			map.put(k, 0);
		}
		count = Math.max(count, ck);
	}

	public static void check(int[][] p, char[] n, int x) {
		char k = n[x];
		map.put(k, map.get(k) + 1);
		if(x >= p.length) {
			return;
		}
		if(p[x][0] == p[x][1]) {
			System.out.println("null");
			System.exit(0);
		}
		for(int i = 0; i < p.length; i ++) {
			if(p[x][1] == p[i][1]) {
				check(p, n, p[i][1]);
			}
		}
		resetMap();
	}
	
}

```
