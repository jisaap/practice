| Hop   홉                                                     | (2020-03-07) |
| ------------------------------------------------------------ | ------------ |
| Next Hop, 다음 홉, Hop Count, 홉 수, Hop Limit, 홉 한계, Hop by Hop, 홉 바이 홉 |              |

[Top](http://www.ktword.co.kr/abbr_view.php?nav=2&id=0) > [통신/네트워킹](http://www.ktword.co.kr/abbr_view.php?nav=2&id=849) > [인터넷/데이터통신](http://www.ktword.co.kr/abbr_view.php?nav=2&id=417) > [라우팅](http://www.ktword.co.kr/abbr_view.php?nav=2&id=435) > [라우팅 프로토콜](http://www.ktword.co.kr/abbr_view.php?nav=2&id=437) > [RIP](http://www.ktword.co.kr/abbr_view.php?nav=2&id=439)

```
1. 홉 (Hop)

  ㅇ 홉이란 영어 뜻 자체로는 건너뛰는 모습을 의미

  ㅇ 데이타통신망에서 각 패킷이 매 노드(또는 라우터)를 건너가는 양상을 비유적으로 표현
     - 이러한 체계를 hop-by-hop 체제라고 함                                ☞ TTL 참조


2. 다음 홉 (Next Hop)

  ㅇ 목적지 네트워크까지 가기위한 바로 다음의 라우터를 말함

  ㅇ 각 노드(라우터)는,
     - 수신된 패킷의 헤더부분에 있는 주소를 조사하여,
     - 라우팅 테이블에 있는 최적 경로 상에 있는 다음 홉 라우터 인터페이스를 찾아내어,
     - 수신 패킷을 다음으로 Hop 할 라우터를 향하는 그 인터페이스에게 넘겨 전달함           


3. 홉 수 (Hop Count)

  ㅇ 거치게되는 라우터 수

  ㅇ RIP 홉카운트 비용 계산
  	- ⓐ 직접 접속되어 있는 네트워크에 대한 비용은 0으로 계산
  	  ⓑ 인접한 라우터 간의 비용은 1로 계산
      ⓒ 인접한 라우팅 정보를 광고할때 기존 비용 값에 1을 더함
  	  ⓓ RIP는 목적지 까지 갈수 있는 여러 경로중에서 홉수가 가장 작은 경로를 선택
  	  ⓔ RIP의 최대 홉수는 15이고, 홉수가 > 15 인것은 해당 목적지 까지 가는 경로가 없는 것으로 판단 
  		
  ㅇ RIP의 장점과 단점
  	- 장점
  	  1) 인터넷 표준 프로토콜로 모든 벤더에서지원
  	  2) 간단하고 이해하기 쉬움
  	  3) 간단하게 구현 및 운영가능
  	  4) 전원이나 메모리 등 시스템 자원의 소모가 적음
  	- 단점
  	  1) 지원하는 최대 홉수가 15개로, 16개부터는 전송이 불가능 하므로 대규모 네트워크에는 부적합
  	  2) 경로 선택방법이 홉수뿐이므로 최적의 경로를 선택할 수 없음
  	  3) 거리 벡터 알고리즘으로 인해 링크 상태에 대한 변화가 느림
  	  4) 서브넷 정보를 처리하지 못함
  		

4. 홉 한계/제한 (Hop Limit 또는 TTL)

  ㅇ IP 헤더 내에서 8 비트로 그 값을 나타냄
     - 헤더 내 필드 명칭 : `TTL(IPv4)` 또는 `Hop Limit(IPv6)`
     - 최대 홉 값  = 28 - 1 = 255
     - 권장 기본값 = 64

  ㅇ 멀티캐스트 패킷의 경우
     - RIPv2, OSPF 에서 이웃라우터를 넘어서 멀티캐스트 패킷을 전달되지 못하도록 함
        . 즉, `TTL(IPv4)` 또는 `Hop Limit(IPv6)` = 1

  ㅇ 한편, IPv6에서 Hop Limit = 255 (가장 큰 수)는 특별한 의미를 갖음
     - 보안성 강화를 위해, 라우터가 이 값의 패킷을 아예 라우팅 처리하지 않음 즉, 무시함
        . 즉, Local Link 영역 내에서 만 통용됨
     - ICMPv6 NDP 메세지(5 종류)에 이 값(255)이 쓰여짐
        . 이 값으로 쓰여지지 않는 NDP 메세지들은 무시되어짐
     - RFC 5082 (The Generalized TTL Security Mechanism, GTSM)
```



출처 : [[Copyrightⓒ written by 차재복 (Cha Jae Bok)](http://www.ktword.co.kr/word/index.php)]



DailyCoding 106번 문제

Given an integer list where each number represents 
the number of hops you can make, 
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.

네트워크에 대한 이해도를 높인뒤에 다시 해보기