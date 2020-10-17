Signleton - pattern 에제

```java
//   일반적인 싱글톤 패턴 ( Eager Initalization (이른 초기화 , Thred - safe)
		public class Singleton {
			private static Singleton uniqueInstance = new Singleton();
		
			public Singleton() {
				// TODO Auto-generated constructor stub
			}
			public static Singleton getInstance() {
				return uniqueInstance;
			}
			
		}
//		일반적인 싱글톤 패턴 ( Lazy Initialization with synchronized (동기화 블럭, Thread-safe)
		public class Singleton implements Serializable{
//			volatile 는 메인 메모리에 변수를 저장하겠다는 뜻
//			매번 변수의 값을 읽어올때 마다 CPU Cache 에 저장된 값이 아닌 메인 메모리에서 읽어온다
//			변수에 값을 작성할 때마다 메인 메모리의 값또한 갱신해준다.
			private volatile static Singleton uniqueInstance;
			
		    private Singleton() {}

		    // Lazy Initailization
		    public Singleton getInstance() {
		    	if(uniqueInstance == null) {
		    		synchronized (Singleton.class) {
						if(uniqueInstance == null) uniqueInstance = new Singleton();
					}
		    	}
		    	return uniqueInstance;
		    }
		}
		
```

​	synchronized 키워드를 사용하면 성능이 약 100배까지 떨어질수 있다.

​	인스턴스가 생성되지 않은 경우에만 동기화 블럭이 실행되도록 구현하여 성능 저하를 최소화 한다.