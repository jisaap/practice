### AtomicInteger 란?

**AtomicInteger란 원자성을 보장하는 Interger를 의미한다.** 멀티 쓰레드 환경에서 동기화 문제를 별도의 synchronized 키워드 없이 해결하기 위해서 고안된 방법이다. (일반적으로 동기화 문제는 synchronized, Atomic, volatile 세가지 키워드로 해결한다.) synchronized은 특정 Thread가 해당 블락 전체를 lock 하기 때문에 다른 Thread는 아무작업을 못하고 기다리는 상황이 되어 낭비가 심하다. 그래서 NonBlocking하면서 동기화 문제를 해결하기 위한 방법이 Atomic이다. AtomicInterger 동작의 핵심 원리는 바로 **CAS알고리즘(Compare and Swap)**에 있다.



### CAS (Compare And Swap) 알고리즘



| ![CAS 알고리즘](https://t1.daumcdn.net/cfile/tistory/994F7B375AE9DAF00B)*[그림1] CAS 알고리즘* | ![CPU 캐시 메모리](https://t1.daumcdn.net/cfile/tistory/99406D3F5AE9DBB006)*[그림2] CPU 캐시 메모리* |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |





멀티 쓰레드 환경, 멀티 코어 환경에서 각 CPU는 메인 메모리에서 변수값을 참조하는게 아닌, 각 CPU의 캐시 영역에서 메모리를 값을 참조하게 된다. (*[그림2] CPU 캐시 메모리* 참고) 이때, 메인 메모리에 저장된 값과 CPU 캐시에 저장된 값이 다른 경우가 있다. (이를 가시성 문제라고 한다.) 그래서 사용되는 것이 CAS 알고리즘이다. **현재 쓰레드에 저장된 값과 메인 메모리에 저장된 값을 비교하여 일치하는 경우 새로운 값으로 교체하고, 일치 하지 않는 다면 실패하고 재시도를 한다.** 이렇게 처리되면 CPU캐시에서 잘못된 값을 참조하는 가시성 문제가 해결되게 된다.



참고로 synchronized 블락의 경우 synchronized블락 진입전 후에 메인 메모리와 CPU 캐시 메모리의 값을 동기화 하기 때문에 문제가 없도록 처리한다. 



### AtomicInteger 들여다보기

아래는 직접 AtomicInterger를 Decompile 하여 요약한 내용이다.

```
public class AtomicInteger extends Number implements java.io.Serializable {
	
    private volatile int value;

    public final int incrementAndGet() {
        int current;
        int next;
        do {
            current = get();
            next = current + 1;
	} while (!compareAndSet(current, next)); 
	return next;
    }
	
    public final boolean compareAndSet(int expect, int update) {
        return unsafe.compareAndSwapInt(this, valueOffset, expect, update);
    }	
}
```



중요한 것은 incrementAndGet() 메소드 내부에서 CAS알고리즘의 로직을 구현하고 있다. compareAndSet()의 결과 리턴 받아서 성공할때까지 while을 통해서 무한 루프를 돈다. compareAndSet()내부에서는 compareAndSwapInt()를 호출하여 메모리에 저장되어진 값과 현재 CPU캐시에 저장된 expect 값을 비교하여 동일한 경우만 변경하려는 값 update로 쓰기를 수행한다.



다른 AtomicInteger 메소드 들도 거의 유사한 패턴으로 구현되어 있다. 또한 눈여겨 볼 점은 volatile int value; 선언부 인데 voliatile는 변수의 가시성 문제를 해결하기 위해서 사용된다. volatile 키워드가 붙어 있는 객체는 CPU캐시가 아닌 메인 메모리에서 값을 참조해온다. 그렇다면 굳이 CAS알고리즘을 적용하지 않아도 문제가 없는 것 아닐까? 그렇지 않다. volatile 키워드는 오직 한개의 쓰레드에서 쓰기작업을 할 때, 그리고 다른 쓰레드는 읽기 작업만 할 때 안정성을 보장한다. 그런데 AtomicIntger는 여러 쓰레드에서 읽기/쓰기 작업을 병행한다. 그래서 CAS알고리즘이라는 2중의 안정장치를 설치해 놓은 것이다.



출처: https://javaplant.tistory.com/23 [자바공작소] 

-   AtomicInterger 완전정복 - CAS알고리즘(compareAndSet)

   