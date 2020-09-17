알고리즘 문제풀이



```java
package DailyCoding;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

//Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.

//According to the definition of LCA on 
//Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T 
//that has both v and w as descendants (where we allow a node to be a descendant of itself).”

//LCA 알고리즘 이해하고 내일 직접 풀어보기
// 이해 못함
public class DailyCoding112 {

	  private static ArrayList<Integer>[] con;
	  private static int[] tree;
	  private static final int MAX_N = 100000;
	  private static final int MAX_D = 17;
	  private static int[][] par;
	  private static int tmp;
	  private static int A;
	  private static int B;
	  
	public static void main(String[] args) throws IOException {
		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		    StringTokenizer st = null;
		    par = new int[MAX_D + 1][MAX_N + 1];

		    int N = Integer.parseInt(br.readLine().trim());
		    con = new ArrayList[N + 1];
		    tree = new int[N + 1];
		    for (int i = 1; i <= N; i++) {
		      con[i] = new ArrayList<Integer>();
		    }
		    for (int i = 1; i < N; i++) {
		      st = new StringTokenizer(br.readLine().trim());

		      A = Integer.parseInt(st.nextToken());
		      B = Integer.parseInt(st.nextToken());

		      con[A].add(B);
		      con[B].add(A);
		    }
		    for (int i = 1; i <= N; i++) {
		      tree[i] = -1;
		    }
		    dfs(1, 0);
		    int M = Integer.parseInt(br.readLine().trim());
		    for (int i = 1; i <= M; i++) {
		      st = new StringTokenizer(br.readLine().trim());

		      A = Integer.parseInt(st.nextToken());
		      B = Integer.parseInt(st.nextToken());

		      System.out.println(lca(A, B));
		    }
		  }

		  private static void dfs(int node, int depth) {
		    if (tree[node] != -1)
		      return;

		    tree[node] = depth;
		    for (int next : con[node]) {
		      if (tree[next] != -1)
		        continue;
		      par[0][next] = node;
		      for (int i = 1; i <= MAX_D; i++) {
		                if(par[i - 1][next] == 0) break;
		                par[i][next] = par[i - 1][par[i - 1][next]];
		            }
		        
		      dfs(next, depth + 1);
		    }
		  }

		  private static int lca(int a, int b) {
		    if (tree[a] > tree[b]) {
		      tmp = a;
		      a = b;
		      b = tmp;
		    }
		    for (int i = MAX_D; i >= 0; i--) {
		      if (tree[b] - tree[a] >= (1 << i))
		        b = par[i][b];
		    }
		    if (a == b)
		      return a;
		    for (int i = MAX_D; i >= 0; i--) {
		      if (par[i][a] != par[i][b]) {
		        a = par[i][a];
		        b = par[i][b];
		      }
		    }
		    return par[0][a];
		  
		
	}
	
	
}

```
