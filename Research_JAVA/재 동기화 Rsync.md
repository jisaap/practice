Daily Coding 59번 문제

Implement a file syncing algorithm for two computers over a low-bandwidth network. What if we know the files in the two computers are mostly the same?



파일 동기화에 대한 문제 이며 효율성을 위해 재동기화 Rsync를 구현하는 문제

자료를 찾기 쉽지 않고 Jarsync 는 개발이 중단된 상태이며

github 의 rsync4j를 import 받아서 구현을 시도했지만 메서드의 기능을 알수가 없어서 

이후에 다시 도전해야하는 문제;;

[Rsync 란 ?](https://skibis.tistory.com/16)

\2016. 8. 12. 20:26,  [Dev/OS](https://skibis.tistory.com/category/Dev/OS)

Rsync(Remoe Sync)는 원격에 있는 파일과 디렉토리를 복사하고 동기화 하기 위해서 사용하는 툴이며 동시에 네트워크 프로토콜이다. 리눅스와 유닉스에서는 백업용도로 (아마도)가장 널리 사용하는 툴일 것이다(윈도우와 애플에도 포팅됐다). Rsync는 CLI툴로, 커맨드 라인의 옵션들을 이용해서 배치 프로그램을 개발하기 쉬다는 장점이 있다. 이 스크립트를 cron 등에 올리는 걸로 간단하게 백업 혹은 미러(mirror) 시스템을 구축할 수 있다.

**Rsync의 기능상 장점들**
1) 원격 시스템으로 부터 파일을 효율적으로 복사하거나 동기화 할 수 있다.
2) Link, device, 파일의 소유자와 그룹 권한(permissions)등 파일의 부가정보도 복사할 수 있다.
3) scp보다 빠르다. rsync는 remote-update 프로토콜을 이용해서 차이가 있는 파일만 복사한다. 처음에는 모든 파일과 디렉토리를 복사하겠지만, 다음부터는 차이가 있는 파일만 복사하기 때문에 더 빠르고 효율적으로 작동한다.
4) 데이터를 압축해서 송/수신하기 때문에 더 적은 대역폭을 사용한다.

**Rsync의 동기화 알고리즘**

파일 전송 결정
기본적으로 rsync는 파일의 크기와 수정 시간(modification)을 비교하는 것으로 파일을 전송할지 말지를 결정한다. 이 방법은 아주 작은 CPU 자원을 소모하지만 실수가 발생할 수 있다. 일반적으로 파일의 내용을 변경하면 크기와 수정시간이 변하지만 항상 그렇다고 단정할 수는 없기 때문이다.

--checksum 옵션을 이용하면 비교 방법을 개선할 수 있다. 이 옵션을 켜면, 파일의 checksum을 비교한다. 크기/시간을 이용한 비교 방법보다 안전하지만 더 느리고 더 많은 자원을 사용한다.

전송할 파일 부분의 결정
파일 전송을 결정했다고 가정해보자. 파일을 전송하기 위한 간단한 방법은 "전체 파일을 그대로 복사"해버리는 거다. 쉬운 방법이긴 한데, (특히 파일의 크기가 클 경우) 효율적이지는 않다. 1G 크기의 파일이 있다고 가정해보자. 여기에서 바뀐 부분이 1k 라고 할 때, 1k 때문에 1G를 복사하게 될거다.
Rsync는 파일의 변경된 부분만 효과적으로 복사하기 위한 알고리즘을 가지고 있다.
Rsync는 파일을 고정 크기를 가지는 청크(chunk)로 나눈다음에 checksum을 계산한다. 이 checksum을 서로 계산해서, 다를 경우 해당 부분의 청크만을 복사한다.
만약 파일의 앞 부분의 정보가 수정돼서 정보들이 밀린다면 모든 청크의 checksum이 어긋날 것이다. 이 문제를 피하기 위해서 "Rolling hash"를 사용한다.

기본 사용법
rsync options source destination

모든 배포판에서 패키지 형태로 제공한다.
CentOS는 yum, Ubuntu는 apt-get으로 설치

yum install rsync

 **or**

apt-get install rsync

옵션값 ;
-v : 진행 상황을 상세하게 보여줌
-r : 지정한 디렉토리의 하위 디렉토리까지 재귀적으로 실행
-l : 소프트 링크 보존
-H : 하드 링크 보존
-p : 버전 속성 보존
-o : 소유 속성 보존(루트)
-g : 그룹 속성 보존
-t : 타임스탬프 보존
-D : 디바이스 파일 보존(루트)
-z : 데이터 압축 전송
-b : 낡은 파일은 ~가 붙음
-u : 추가된 파일만 전송 새 파일은 갱신하지 않음
--existing : 추가된 파일은 전송하지 않고 갱신된 파일만 전송
--delete : 서버에 없는 파일은 클라이언트에서도 삭제
-a : 아카이브 모드. rlptgoD를 자동 지정
-c : 서버와 클라이언트의 파일 크기를 세밀히 체크
--stats : 결과를 보고
-e ssh(rsh) : 전송 암호화

주로 사용 옵션

**rsync -avgoh 원본 대상**

ex ) rsync -avgoh 원본 100.100.100.100:/usr/local/src
ex ) rsync -auvhg mysql root@1.234.51.196:/home/

[Remoe Sync](https://skibis.tistory.com/tag/Remoe Sync), [rsync](https://skibis.tistory.com/tag/rsync)

https://skibis.tistory.com/16
출처:  [Skibi's Notepad]

----------------------------------------------------------------------------------------------------------------------------------------

rsync 에 대한 설명

https://fracpete.github.io/rsync4j/java/



RSync4j 를 다운 받은 git url

https://github.com/fracpete/rsync4j.git



Jarsync url

http://jarsync.sourceforge.net/