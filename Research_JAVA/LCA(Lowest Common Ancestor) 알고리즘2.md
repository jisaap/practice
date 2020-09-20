출처 : [5. LCA, Lowest Common Ancestor (최소 공통 조상)](https://exponential-e.tistory.com/34)

[Study/Alogrithm](https://exponential-e.tistory.com/category/Study/Alogrithm)



**LCA**는 기본적으로 트리에서 사용되는 알고리즘입니다.

간략하게, 트리에 대한 내용은 **트리와 그래프** 포스팅을 참고해 주세요.

[exponential-e.tistory.com/33](https://exponential-e.tistory.com/33)

[ 트리와 그래프컴퓨터공학 전공 중이시라면 당연히 두 자료구조의 이름은 들어보셨을 겁니다. 하지만 뭐.. 저는 학교 다니면서 그 차이점에 대해 전혀 알지 못했었는데요. 그렇게 여러 문제를 접하며 박살exponential-e.tistory.com](https://exponential-e.tistory.com/33)

 

 

일상생활에서 트리구조는 족보 또는 가계도를 예로 들을 수 있습니다.

이렇게까지 설명해야하나 싶지만 이왕 쓰는 김에 저희 집 가계도를 가져와보겠습니다. ㅎㅎ;

 



![img](https://blog.kakaocdn.net/dn/Woms0/btqCuYyiDEy/0mJeQjXvYXUW3pSm3Leue0/img.png)그림 1. 우리 집 가계도



 

네... 뭐 혼인 관계까진 없어도 될 것 같아서 빼두었습니다.

 

Q1. 여기서 보면, 저와 제 동생의 공통 조상은 누군가요?

A1. 아버지와, 친 할아버지입니다.

 

Q2. 그럼 저와 큰 고모 자식인 누나와의 공통 조상은요?

A2. 친 할아버지뿐이죠.

 

Q3. 그럼 각각의 Q1, Q2에서 LCA는 누군가요?

A. Q1에서는 아버지, Q2에서는 친 할아버지입니다.

 

간단하게보면 이게 바로 LCA입니다. :)

좀 더 복잡한 트리구조에서 확인해 보겠습니다.



![img](https://blog.kakaocdn.net/dn/cOPdBN/btqCrjp64VP/PBdlBDxiJgOXkwuTMwVUL1/img.png)그림  2. 트리 1



 

Q1. 4와 3의 LCA?

A1. 0

 

Q2. 10과 7의 LCA?

A2. 3

 

Q3. 12과 14의 LCA?

A3. 7

 

눈으로보면 찾기 쉽죠. ㅎㅎ

하지만 늘상 드리는 말씀이 컴퓨터에게 알려주는 일은 그리 쉬운일이 아닙니다.

 

N개의 노드로 트리를 구성하고, 탐색을 하게 된다면 각 쿼리(Q) 마다 노드 사이의 거리만큼 시간이 걸릴 것이구요.

만약 최악의 조건인 편향 트리가 들어온다 가정했을때, 시간 복잡도는 O(NQ)가 됩니다.

이렇게 직관적으로 짠다면, 구현 자체는 쉽겠죠?

 

하지만, 대개 LCA 문제에서 N이 10만이상으로 주어지고, 쿼리 또한 1만 이상으로 주어지므로 이대로는 사용하기 어렵죠.

 

따라서 우리는 탐색하는 방법을 좀 달리 해볼까 합니다.

1. 우선 **희소 테이블(Sparse table)**이라는 개념을 이용해서 각 노드와 상위 노드에 대한 정보를 담습니다.
2. 노드의 정보란 **각 노드가 어떻게 연결되어 있는지**, 그리고 **노드의 깊이(레벨)는 어느정도 인지**를 의미합니다.
3. 이제부터 쿼리로 들어오는 두 노드를 통해 판별합니다.
4. 첫번째로 node1, node2가 입력으로 들어올 때 **node2를 더 하위 노드라고 가정**합니다.
5. 따라서, 두 노드의 레벨을 비교했을 때 node2가 더 상위 노드라면 두 값의 인덱스를 맞바꿔 줍니다.
6. 그리고 두 노드의 레벨을 맞춰줍니다.
7. 두 노드의 레벨을 맞추고 보니 같은 노드에 존재한다면 node1값을 리턴합니다. (node2도 상관 없습니다.)
8. 같은 노드가 아니라면 아직 서로의 LCA를 찾지 못한 것이므로 **둘 모두의 높이를 맞춰 올려주며** LCA를 찾습니다.
9. 이렇게 둘의 레벨은 같은 레벨로 변경하면서 서로 다른 노드로 탐색을 시작합니다.
10. 이때, **서로 다른 부모 노드를 가지고 있다**면, 그 다음 상위 레벨 노드로 둘 모두를 동시에 올려줍니다.
11. 이렇게 처리한 후 최종적인 값이 두 노드의 LCA가 됩니다.

 

 

일단, 어떻게 구현하는지 보기 전에 Sparse table (희소 테이블) 에 대해서 알아보겠습니다.

해당 테이블은 배열을 이용해 만드는 DP table 입니다. 트리에 매우 적합한데요.

 

어떤 노드에서 한 노드로 이동할 때 그 **경로가 유일한 경우를 테이블에 저장**해둔다 라고 생각하시면 될 것 같습니다.

예를 들어 위의 그림 2에서 14번 노드에서 1번 노드로 가는 경로는 '14 - 8 - 7 - 3 - 0 - 1'로 유일 하잖아요?

이러한 정보들을 저장해두는 겁니다.

 

그런데 그냥 하나하나 N * N 배열로 저장하면 저장하느니만 못하죠. 어차피 오래걸리고 또한 배열 크기도 잡을 수 없을 수 있으니까요.

따라서, 희소 테이블을 이용합니다. 이때 희소는 정보량을 적게한다는 의미에서, **필요한 정보만 추려 넣어서 희소**라 한다고 생각이 됩니다.

(**개인적인 의견**입니다 ㅎㅎ)

 

기본적인 구조는 2차원 배열이며, 저는 parent라는 배열로 선언합니다.

즉 '**int[][] parent = new int[N][21];**'이 되겠습니다.

여기서 **N은 노드의 갯수**를 의미하구요. **21은** **각 노드의 몇 (2^i)번째 부모인가**를 나타냅니다.

이진트리에서 전체 노드가 100만개 있다고 가정했을때 대략 20레벨이면 충분하니까 10만이면 들고도 남죠.

 

그리고 아래 코드를 통해 각 노드마다 **바로 상위 노드에 대한 번호를 저장**합니다.

**dfs method**

```
private static void dfs(int current, int depth){
    visit[current] = true;
    deep[current] = depth;

    for(int next: tree[current]){
    	if(visit[next]) continue;

		parent[next][0] = current;
		dfs(next, depth + 1);
	}
}
```

그림과 같이 봤을 때, parent[1][0] = 0 ~ parent[14][0] = 8 이런식으로 쭉 들어가게 됩니다.

 

 

이렇게 각 노드별 인접한 상위 노드 설정을 한 후에는 **각 노드끼리 연결**을 해줍니다.

그렇다면, 0번 노드는 14번의 4번째 부모인데 이는 parent[14][3] = 0 이어야 하는데 이게 맞을까요? 확인해 보겠습니다.

parent[0][1] = parent[parent[0][0]][0] ~ parent[14][20] = parent[parent[14][19]][19]

**connecting method**

```
private static void connecting(){
	for(int p = 1; p < 21; p++){
		for(int cur = 0; cur < N; cur++){
			parent[cur][p] = parent[parent[cur][p - 1]][p - 1];
		}
    }
}
```

 

 

이와 같이 채워 줬을때 위의 트리 그림과 함께 적용해보면 아래와 같은 결과를 얻을 수 있습니다.

```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
7 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
4 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
5 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
7 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
7 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
8 7 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
```

 

하나씩 차근차근 보겠습니다.

일단 row는 노드의 갯수인 N(15)이고, col은 저희가 임의로 지정한 레벨 크기(21) 입니다.

 

좌측 가장 하단의 값이 8인데, 이는 **parent[14][0] = 8을 의미하고, 위의 그림에 적용했을 때 14번의 부모인 8번과 일치**합니다.

같은 방식으로 **parent[13][0] = 8 ~ parent[0][0] = 0** 까지 채워져있습니다.

 

0번 노드는 부모가 없기때문에 자기 자신을 가리키고 있구요.

이와 같은 값을 갖는 1, 2, 3은 0번이 첫번째 부모기 때문에 모두 0의 값을 갖습니다.

 

다음으로 **parent[14][1] = 7 인데, 이는 14번 노드의 2번째 부모가 7**이라는 것을 의미합니다. 위에도 같은 방식이구요.

 

그런데 이상한 점이 있습니다.

**14번 노드만 봐도 부모는 4번째까지 존재하는데 배열은 1번 배열 즉 2번째 부모까지만 저장**이 되어있습니다.

**하지만 모든 탐색이 가능**합니다. 이게 희소 테이블의 장점이죠. (parent[14][3]은 아니었습니다.^^)

 

14번에서 0번(**4번째 부모**)까지 탐색하는 순서는 아래와 같습니다. (**가장 많이 뛸 수 있는 부모를 알기위해 col이 큰 값부터 탐색**합니다)

1. 14번의 두번째 부모가 7이란 것을 알고있습니다. 그리고 저희가 찾으려는건 네번재 부모죠.
2. 그러면 7이라는 값을 가져와서 다시 그녀석의 부모를 찾습니다.
3. 다음은 parent[7][1] 일겁니다. 해당 값은 0입니다. 7의 (2^1)번째 부모는 0번이라는 뜻이죠.
4. 즉 이렇게 **2번만에 4번째에 있는 최상위 부모**를 찾을 수 있습니다.

 

그러면 각 col값은 실제로 1씩이 아닌 2의 제곱수씩 움직인다는 것을 알아채셨을 겁니다.

이때 이러한 의문이 생기실 수 있습니다. **2****의 제곱수씩 움직인다면 다른 홀수나 2의 제곱수가 아닌 경우**는 어떻게 하지?

 

이 또한 모두 처리가 가능합니다. 만약 **6번째 부모라면 이진수로 110**이고, 따라서 **4번째에서 한번 두번째에서 한번** 뛰니까요.

이해가 안되실 분들을 위해 그림으로 설명해 보겠습니다.



![img](https://blog.kakaocdn.net/dn/bn7HZj/btqCsHRry3S/aB3L6H1L9U8iOXIks3JTTK/img.png)그림 3. 트리 2



 

이러한 경우 Sparse table은 아래와 같이 구성됩니다.

```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
4 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
7 5 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
5 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
9 5 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
5 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
7 5 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
13 6 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
6 7 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
8 9 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
```

 

0번은 14번 노드의 6번째 부모입니다. 아까와 같이 찾아보겠습니다.

1. **6의 2진수는 110** 입니다.
2. 따라서 **1번, 2번째 인덱스만 사용** 할 것이라는 것을 미리 예상할 수 있습니다.
3. 우선 사용 할 값은 뒤에서 부터 봤을때 parent[14][2] 입니다.
4. **2^2만큼 점프를 했을때 6번째라는 값을 넘어가지 않으니 해당 값 4을 갖고 점프**합니다.
5. **4번 노드는 14의 4번째 부모**도 맞네요.
6. 이제 0번 노드까지는 2번이 남았고 이는 col 값으로 바꿨을때 1입니다. (2 = 2^1)
7. 따라서 **parent[4][1]의 값을 참조할 것이구요. 이는 0**입니다.
8. 이렇게 **2의 제곱수가 아니더라도 2진수 표현식에 맞춰 순차 탐색을 진행**한다는 것을 확인 할 수 있습니다.

이해가 여전히 안되신다면 다른 값으로도 테스트 해보시길 권장합니다.

 

 

위에서 했던 방법들이 LCA를 찾는 과정이긴합니다만, 초반에 설명드렸던 순서대로 쭉 코드와 함께 설명드리겠습니다.

우선 우리는 탐색하는 방법에서 **1 ~ 2의 과정들을 connecting, dfs 라는 메소드와 희소 테이블을 구성 및 분석 완료**했습니다.

 

이제 3번 부터의 내용입니다.

두 노드의 깊이를 결정합니다.

그 이유는 쿼리로 들어오는 각 노드의 깊이를 알 수 없기 때문입니다.

**깊이를 알아야 서로의 높이를 맞춰주고 또한 상위 레벨 방향으로 LCA를 찾으며 두 노드를 계속해서 유도**할 수 있겠죠.

**LCA method**

```
private static int LCA(int node1, int node2){
	if(deep[node1] > deep[node2]){
		int tmp = node1;
		node1 = node2;
		node2 = tmp;
	}
}
```

 

 

이렇게 깊이가 더 깊은 노드를 node2라고 지정해주었고 이제 node2를 node1까지의 높이로 맞춰줍니다.

트리 2번 그림에서 쿼리가 10과 14로 들어왔다면 **14번의 레벨을 10번 깊이와 맞는 부모 노드를 찾아 주는 작업**입니다.

부모 노드를 찾는 방법은 바로 위에 보여드렸던 방법과 같습니다.

즉, **10번에서 14번 노드의 레벨을 빼주고, 그만큼 뛰어올라 14의 부모를 찾고의 반복 동작**입니다.

**LCA method 추가**

```
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
}
```

 

다음으로 레벨을 맞춰 주었으니 최종적으로 LCA를 찾아줍니다.

7번의 경우는 레벨을 맞춰준 경우에 그 노드가 LCA라면 값을 반환합니다.

**LCA method 최종**

```
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
```

 

최종 코드

**LCA.java**

```
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class LCA {
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

 

 

이제 맨 처음 트리 그래프에서 사용했던 예시로 결과가 잘 나오는지 보겠습니다.

```
Q1. 4와 3의 LCA?

A1. 0



Q2. 10과 7의 LCA?

A2. 3



Q3. 12과 14의 LCA?

A3. 7
```

 

결과



![img](https://blog.kakaocdn.net/dn/CQAsV/btqCtYFr04Z/vK4u4fb6CGFoOO1xUltOg1/img.png)



 

 

잘 나오네요. ㅎㅎ

시간 복잡도는 Sparse table을 이용한 N개 노드 탐색: logN, 쿼리갯수: Q로 총 **O(QlogN)** 입니다.

 

 

 [출처 : [5. LCA, Lowest Common Ancestor (최소 공통 조상)](https://exponential-e.tistory.com/34) [Study/Alogrithm](https://exponential-e.tistory.com/category/Study/Alogrithm)]

