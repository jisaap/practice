알고리즘 문제풀이



```java
package DailyCoding;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

//Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.

//According to the definition of LCA on 
//Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T 
//that has both v and w as descendants (where we allow a node to be a descendant of itself).”

//[출처 : [5. LCA, Lowest Common Ancestor (최소 공통 조상)](https://exponential-e.tistory.com/34) [Study/Alogrithm](https://exponential-e.tistory.com/category/Study/Alogrithm)]
//LCA 알고리즘 이해하고 직접 풀어보기
public class DailyCoding112 {

	 	private static ArrayList<Integer>[] tree;
	    private static int[][] parent;
	    private static int[] deep;
	    private static boolean[] visit;

	    private static int N;

	    private static final String NEW_LINE = "\n";

	    public static void main(String[] args) throws Exception{
	        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	        N = Integer.parseInt(br.readLine());

	        tree = new ArrayList[N];
	        for(int i = 0; i < N; i++){
	            tree[i] = new ArrayList<>();
	        }

	        parent = new int[N][21];
	        deep = new int[N];
	        visit = new boolean[N];

	        int loop = N - 1;
//	         트리구조 데이터 값 만들기
	        while(loop-- > 0){
	            StringTokenizer st = new StringTokenizer(br.readLine());
	            int node1 = Integer.parseInt(st.nextToken());
	            int node2 = Integer.parseInt(st.nextToken());

	            tree[node1].add(node2);
	            tree[node2].add(node1);
	        }

	        dfs(0, 0);
	        connecting();

	        StringBuilder sb = new StringBuilder();
	        int Q = Integer.parseInt(br.readLine());

	        while(Q-- > 0){
	            StringTokenizer st = new StringTokenizer(br.readLine());
	            int node1 = Integer.parseInt(st.nextToken());
	            int node2 = Integer.parseInt(st.nextToken());

	            sb.append(LCA(node1, node2)).append(NEW_LINE);
	        }

	        System.out.println(sb.toString());
	    }

	    private static void dfs(int current, int depth){
	        visit[current] = true;
	        deep[current] = depth;

	        for(int next: tree[current]){
	            if(visit[next]) continue;

	            parent[next][0] = current;
	            dfs(next, depth + 1);
	        }
	    }

	    private static void connecting(){
	        for(int p = 1; p < 21; p++){
	            for(int cur = 0; cur < N; cur++){
	                parent[cur][p] = parent[parent[cur][p - 1]][p - 1];
	            }
	        }
	    }

//	    두 노드의 깊이를 결정한다.
	    private static int LCA(int node1, int node2){
	        if(deep[node1] > deep[node2]){
	            int tmp = node1;
	            node1 = node2;
	            node2 = tmp;
	        }

	        for(int i = 20; i >= 0; i--){
	            int jump = 1 << i;
	            if(deep[node2] - deep[node1] >= jump) node2 = parent[node2][i];
	        }

	        if(node1 == node2) return node1;

	        for(int i = 20; i >= 0; i--){
	            if(parent[node1][i] == parent[node2][i]) continue;

	            node1 = parent[node1][i];
	            node2 = parent[node2][i];
	        }

	        return parent[node1][0];
	    }
	}	
	

```
