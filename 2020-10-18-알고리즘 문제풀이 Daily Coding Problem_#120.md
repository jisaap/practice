알고리즘 문제풀이



```java
package DailyCoding;

import java.io.Serializable;
import java.util.concurrent.atomic.AtomicInteger;

//Implement the singleton pattern with a twist.
//First, instead of storing one instance, store two instances.
//And in every even call of getInstance(), 
// return the first instance and in every odd call of getInstance(), 
// return the second instance.
	
	public final class Singleton implements Serializable, Cloneable {
		
		private static final long serialVersionUID = 42L;	
		private static Singleton evenInstance;
		private static Singleton oddInstance;
		private static AtomicInteger counter = new AtomicInteger(1);
		
		
		
		
		public Singleton() {
			if(evenInstance != null || oddInstance != null) {
//				throw new RuntimeException("");
			}
	
}
		public static Singleton getInstance() {
//		AtomicInteger 의 getAndUncrement 함수는 AtomicInteger 변수의 값은 1씩 증가시키는 함수 ex)Integer ++;
			boolean ck = counter.getAndIncrement() %2 == 0;
//			ck 값이 true 이고 짝수 Instance 가 null값 이라면 새로운 Instance 생성
			if(ck && evenInstance == null) {
//				클래스 데이터 동기화
				synchronized (Singleton.class) {
					if(evenInstance == null) {
						evenInstance = new Singleton();
					}
				}
			}else if(!ck && oddInstance == null) {
				synchronized (Singleton.class)  {
					if(oddInstance == null) {
						oddInstance = new Singleton();
					}
				}
			}
		
			return ck ? evenInstance : oddInstance;
		}
		
		protected Singleton readResolve() {
			return getInstance();
		}
		
		@Override
		protected Object clone() throws CloneNotSupportedException {
			throw new CloneNotSupportedException("");
		}
	}
	

```
