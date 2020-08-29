알고리즘 문제풀이



```java
package DailyCoding;


//Write a map implementation with a get function
//that lets you retrieve the value of a key at a particular time.

//It should contain the following methods:

//set(key, value, time): sets key to value for t = time.
//get(key, time): gets the key at t = time.
//The map should work like this. If we set a key at a particular time,
//it will maintain that value forever or until it gets set at a later time.
//In other words, when we get a key at a time, 
//it should return the value that was set 
//		for that key set at the most recent time.

//Consider the following examples:

//d.set(1, 1, 0) # set key 1 to value 1 at time 0
//d.set(1, 2, 2) # set key 1 to value 2 at time 2
//d.get(1, 1) # get key 1 at time 1 should be 1
//d.get(1, 3) # get key 1 at time 3 should be 2
//d.set(1, 1, 5) # set key 1 to value 1 at time 5
//d.get(1, 0) # get key 1 at time 0 should be null
//d.get(1, 10) # get key 1 at time 10 should be 1
//d.set(1, 1, 0) # set key 1 to value 1 at time 0
//d.set(1, 2, 0) # set key 1 to value 2 at time 0
//d.get(1, 0) # get key 1 at time 0 should be 2

public class DailyCoding97 {

	public static void main(String[] args) {
		
		
		Sample s = new Sample();
		
		s.set(1, 1, 2);
		
		System.out.println(s.get(1, 0));
		
		
	}	
	
	
}



--------------------------------------------------------------
    
    import java.util.HashMap;
import java.util.Map;

public class Sample {

	private Map kv = new HashMap();
	private Map kvt = new HashMap();

	
	
		public Object get(Object key, int time) {
			Object value = kv.get(key);
			return (int)kvt.get(key +""+value) < time?kv.get(key):null;
		}
		
		public void set(Object key, Object value, int time) {
			kv.put(key, value);
			kvt.put(key +""+value, time);
		}
	}

```
