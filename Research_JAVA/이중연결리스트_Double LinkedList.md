출처 : https://joooootopia.tistory.com/18



출처 : [[Java 자료구조\] 이중연결리스트(Double LinkedList) 구현](https://joooootopia.tistory.com/18)

2019. 1. 24. 22:46



# 이중연결리스트 :: Double LinkedList

이중연결리스트란, 단순연결리스트 구조에서, 바로 이전 노드를 가리키는 prev 포인터가 추가된 구조라고 생각하면 이해가 쉽다. 역시나 head 포인터가 맨 처음에 저장된 노드를, tail 포인터가 맨 마지막에 저장된 노드를 가리키는 형식이며, head와 tail은 '포인터'의 형태로 일반노드처럼 필드(prev | data | next)가 존재한다고 생각하면 안된다. 





![img](https://t1.daumcdn.net/cfile/tistory/99290A3B5C4987E816)



## 이중연결리스트의 장점

이중연결리스트의 큰 장점은 양방향 연결 구조이기 때문에 노드를 탐색하는 방향도 양방향이라는 데에 있다. 



단순연결리스트의 경우는, 맨 마지막에 위치한 데이터를 탐색하기 위해서 head에서부터 시작하여 순차적으로 방문하며 탐색하지만

이중연결리스트의 경우는 그럴 필요가 없다.



## 이중연결리스트의 단점

이전 노드를 가리키기 위한 변수를 하나 더 사용해야 하므로 그만큼의 메모리를 더 소비하게 된다. 

또한 구현도 단순연결리스트보다는 복잡하다.





구현에 들어가기 앞서서, Node를 저장하는 클래스를 자바빈 형태로 구현해주었다. 

이중연결리스트 구현을 위해 사용한 클래스는 총 세개로, Node 오브젝트를 위한 클래스, 연산을 위한 클래스, 테스트를 진행할 main 클래스이다. head와 tail은 연산을 위해 존재하는 객체이므로 연산을 위한 클래스에 private으로 선언해주었다. 



코드는 아래 전체 코드에서 함께 첨부하겠다.



## 이중연결리스트 구현하기 :: Java

### 삽입 연산



![img](https://t1.daumcdn.net/cfile/tistory/995239455C498DA635)





1. 삽입할 노드 객체를 생성하고 새 노드의 데이터 필드 값을 setting한다.
2. 새 노드의 오른쪽 링크(node.next)에, 새 노드 왼쪽 노드의 오른쪽 링크(next) 값을 복사해서 넣어준다.
3. 그 왼쪽 노드의 오른쪽 링크(next)에 새 노드의 주소를 저장해준다.
4. 새 노드의 왼쪽 링크(node.prev)에, 새 노드 오른쪽 노드의 왼쪽 링크(prev) 값을 복사해서 넣어준다.
5. 그 오른쪽 노드의 왼쪽 링크(prev)에 새 노드의 주소를 저장해준다.



기본적인 새 노드 삽입 연산은 이 순서를 따르므로, 조금 머리를 굴려서 리스트 맨 앞에 데이터를 삭제할 때와 맨 뒤에 데이터를 삭제할 때도 구현할 수 있다. 항상 잊지 말아야할 점은, head는 첫 노드의 주소를 가리키는 포인터 입장이며 tail도 마지막 노드의 주소를 가리키는 포인터 입장이라는 점이다. 



#### 리스트 맨 앞에 노드(데이터)를 삽입하기



public void insertFirstNode(Object data) {

​        Node node = new Node(data);

​        //리스트에 아무 노드가 없다면

​        if(head == null) {

​            head = node;

​            tail = node;

​        }

​        //리스트 내에 노드가 이미 존재한다면

​        else if(head != null) {

​            node.setNext(head); //헤드 포인터 복사

​            head.setPrev(node); //서로서로 가리키게

​            head = node;

​        }

​        size++;

​    }



가장 먼저 리스트가 비어있을 경우를 생각해주었다. 

리스트에 노드가 하나라도 존재하고 있다면 헤드포인터가 가리키는 노드를 변경(처리)해주고, 원래 헤드가 가리키고 있었던, 뒤로 밀려날 노드의 prev를 삽입 노드로 올바르게 가리키도록 셋팅시켜주는 작업만 해 주면 된다.



리스트의 맨 앞에 있는 노드는 prev 인스턴스 값이 null이지만, 이 작업을 Node 클래스(노드의 데이터와 next, prev를 저장하고 있음)에서 초기화를 통해 해주고 있으므로 이 메소드에서는 해 줄 필요가 없다.



#### 리스트 가운데에 노드(데이터)를 삽입하기



public void insertMiddleNode(int index, Object data) {

​        Node node = new Node(data);

​        Node current = getNode(index);

​        Node previous = current.getPrev();

 

​        if(head.getNext() == null || index == 1)

​            insertFirstNode(node.getData());

 

​        else if(index == size+1)

​            insertLastNode(node.getData());

 

​        else {

​            node.setNext(previous.getNext());

​            previous.setNext(node);

​            node.setPrev(current.getPrev());

​            current.setPrev(node);

​        }

​        size++;

​    }



위에서 설명한 것과 같은 방식이다.



#### 리스트 맨 끝에 노드(데이터)를 삽입하기



public void insertLastNode(Object data) {

​        Node node = new Node(data);

​        if(tail == null)

​            insertFirstNode(node.getData());

 

​        else {

​            Node current = getNode(size);

​            current.setNext(node);

​            node.setPrev(current);

​            tail = node;

​        }

​        size++;

​    }


7번째 line에서 current 오브젝트에 올바른 객체를 넣어주기 위해 tail을 넣어줄수도 있다. 

이번에도 마찬가지로, 새로 만들어진 노드의 next 인스턴스 값은 null이지만, Node 생성자에서(Node node = new Node(data);) 이를 처리해주고 있으므로 굳이 코드로 구현하지 않는다. 



tail은 포인터의 역할이므로, 새로운 삽입 노드를 가리키도록 지정시켜주는 것을 잊지 않아야한다.



public Node getNode(int index) {

​        if(index < size/2) {

​            Node current = head;

​            for(int i=0; i<index; i++) {

​                current = current.getNext();

​            }

​            return current;

​        }

​        else {

​            Node current = tail;

​            for(int i=size-1; i>=index; i--) {

​                current = current.getPrev();

​            }

​            return current;

​        }

​    }



getNode() 메소드는 인덱스값을 파라미터로 받아(리스트의 인덱스는 가독성을 위해 1부터 시작하도록 설정하였다. ) 해당 인덱스의 노드 객체를 리턴해준다. 단순연결리스트에 대비되는 이중연결리스트의 장점이 바로 시간이니, 그 장점을 극대화시켜주기 위해 탐색할 노드 인덱스값에 따른 조건문을 설정해주었다.







### 삭제 연산



![img](https://t1.daumcdn.net/cfile/tistory/9994CA355C49BC9C2D)







1. 삭제할 노드의 왼쪽 노드의 오른쪽 링크(next)에, 삭제할 노드의 오른쪽 노드의 주소를 저장해준다.
2. 삭제할 노드의 오른쪽 노드의 왼쪽 링크(prev)에, 삭제할 노드의 왼쪽 노드의 주소를 저장해준다.

삭제 연산에서 가장 중요한 점은, NullPointerException을 방지하는 코드를 구현해야한다는 점이다. 

위의 그림에서 나타낸 구조에서도 보이듯, 맨 앞 노드의 prev가 null을, 맨 마지막 노드의 next가 null을 가리키고 있다. 그 때문에 반복문으로 node.next를 받아 콘솔에 프린트를 해줄때에도, 리스트에 노드가 1개만 남아있을 때에도 null처리를 어떻게 해주어야할지 고민해보아야한다. 



#### 리스트 맨 앞 노드(데이터)를 삭제하기

public void deleteFirstNode() {

​        if(head == null) {

​            System.out.println("삭제할 노드가 없습니다.");

​            return;

​        }

 

​        else if (size == 1) {

​            head = null;

​            tail = null;

​        }

​        else {

​            Node oldNode = head;

​            head = oldNode.getNext();

​            oldNode.getNext().setPrev(null);

​            size--;

​        }

​    }


리스트에 노드가 1개뿐인 상황에서 else문으로 이 연산을 수행시킨다면 head = oldNode.getNext(); 에서 NullPointerException이 발생한다. 리스트에 노드가 1개뿐이라면 head가 가리키는 노드 = tail이 가리키는 노드 = 마지막 노드이기 때문에 head.getNext()는 당연히 아무것도 없기 때문에 에러가 날 수 밖에 없다. 따라서 노드가 1개뿐인 상황을 따로 정의해주고 구현해줘야한다. 


  



public void deleteMiddleNode(int index) {

​        Node oldNode = getNode(index);

​        if(index == 1)

​            deleteFirstNode();

 

​        else if(index == size)

​            deleteLastNode();

 

​        else {

​            Node nextNode = getNode(index+1);

​            Node prevNode = getNode(index-1);

 

​            prevNode.setNext(oldNode.getNext());

​            nextNode.setPrev(oldNode.getPrev());

​            size--;

​        }

​    }

위에서 그림으로 설명한 것과 같은 방식이다.



#### 리스트 맨 끝에 있는 노드(데이터)를 삭제하기





public void deleteLastNode() {

​        if(tail == null) {

​            System.out.println("삭제할 노드가 없습니다.");

​            return;

​        }

 

​        else if (size == 1) {

​            head = null;

​            tail = null;

​        }

 

​        else {

​            Node oldNode = tail;

​            Node prevNode = oldNode.getPrev();

 

​            tail = prevNode;

​            prevNode.setNext(null);

​            size--;

​        }

​    }



아까와 같은 이유로 리스트에 노드가 1개 뿐일 때 Node prevNode = oldNode.getPrev(); 에서 나는 NullPointerException을 방지하기 위해 else if문을 추가하였다.



### 이중연결리스트 구현 :: 전체 코드



class Node {

​    private Node prev;

​    private Object data;

​    private Node next;

 

​    public Node(Object data) {

​        this.data = data;

​        this.prev = null;

​        this.next = null;

​    }

 

​    public void setPrev(Node prev) {

​        this.prev = prev;

​    }

 

​    public Node getPrev() {

​        return this.prev;

​    }

 

​    public Object getData() {

​        return this.data;

​    }

 

​    public void setNext(Node next) {

​        this.next = next;

​    }

 

​    public Node getNext() {

​        return this.next;

​    }

}

 

 

class OperateList {

​    private Node head;

​    private Node tail;

​    int size = 0;

 

​    public void insertFirstNode(Object data) {

​        Node node = new Node(data);

​        //리스트에 아무 노드가 없다면

​        if(head == null) {

​            head = node;

​            tail = node;

​        }

​        //리스트 내에 노드가 이미 존재한다면

​        else if(head != null) {

​            node.setNext(head); //헤드 포인터 복사

​            head.setPrev(node); //서로서로 가리키게

​            head = node;

​        }

​        size++;

​    }

 

​    public void insertMiddleNode(int index, Object data) {

​        Node node = new Node(data);

​        Node current = getNode(index);

​        Node previous = current.getPrev();

 

​        if(head.getNext() == null || index == 1)

​            insertFirstNode(node.getData());

 

​        else if(index == size+1)

​            insertLastNode(node.getData());

 

​        else {

​            node.setNext(previous.getNext());

​            previous.setNext(node);

​            node.setPrev(current.getPrev());

​            current.setPrev(node);

​        }

​        size++;

​    }

 

​    public void insertLastNode(Object data) {

​        Node node = new Node(data);

​        if(tail == null)

​            insertFirstNode(node.getData());

 

​        else {

​            Node current = getNode(size);

​            current.setNext(node);

​            node.setPrev(current);

​            tail = node;

​        }

​        size++;

​    }

 

​    public void deleteFirstNode() {

​        if(head == null) {

​            System.out.println("삭제할 노드가 없습니다.");

​            return;

​        }

 

​        else if (size == 1) {

​            head = null;

​            tail = null;

​        }

​        else {

​            Node oldNode = head;

​            head = oldNode.getNext();

​            oldNode.getNext().setPrev(null);

​            size--;

​        }

​    }

 

​    public void deleteMiddleNode(int index) {

​        Node oldNode = getNode(index);

​        if(index == 1)

​            deleteFirstNode();

 

​        else if(index == size)

​            deleteLastNode();

 

​        else {

​            Node nextNode = getNode(index+1);

​            Node prevNode = getNode(index-1);

 

​            prevNode.setNext(oldNode.getNext());

​            nextNode.setPrev(oldNode.getPrev());

​            size--;

​        }

​    }

 

​    public void deleteLastNode() {

​        if(tail == null) {

​            System.out.println("삭제할 노드가 없습니다.");

​            return;

​        }

 

​        else if (size == 1) {

​            head = null;

​            tail = null;

​        }

 

​        else {

​            Node oldNode = tail;

​            Node prevNode = oldNode.getPrev();

 

​            tail = prevNode;

​            prevNode.setNext(null);

​            size--;

​        }

​    }

 

​    public Node getNode(int index) {

​        if(index < size/2) {

​            Node current = head;

​            for(int i=0; i<index; i++) {

​                current = current.getNext();

​            }

​            return current;

​        }

​        else {

​            Node current = tail;

​            for(int i=size-1; i>=index; i--) {

​                current = current.getPrev();

​            }

​            return current;

​        }

​    }

 

​    public void printList() {

​        Node current = head;

​        if(current == null) {

​            System.out.println("Empty List.");

​            return;

​        }

​        System.out.print("[ ");

​        while(current.getNext() != null) {

​            System.out.print( current.getData() + " ");

​            current = current.getNext();

​        }

​        System.out.print(current.getData());

​        System.out.print(" ]");

​    }

}

 

 

public class DoubleLinkedList {

​    public static void main(String[] args) {

​        OperateList list = new OperateList();

 

​        list.insertFirstNode(150);

​        list.insertFirstNode(140);

​        list.insertLastNode(500);

​        list.insertFirstNode(130);

​        list.insertFirstNode(110);

 

​        list.printList();

​        //                [ 110 130 140 150 500 ]

​        System.out.println();

 

​        list.insertMiddleNode(2, 120);

 

​        list.printList();

​        //                [ 110 120 130 140 150 500 ]

​        System.out.println();

 

​        list.deleteLastNode();

 

​        list.printList();

​        //                [ 110 120 130 140 150 ]

​        System.out.println();

 

​        list.deleteFirstNode();

 

​        list.printList();

​        //                [ 120 130 140 150 ]

​        System.out.println();

 

​        list.deleteMiddleNode(3);

 

​        list.printList();

​        //                [ 120 130 150 ]

​        System.out.println();

 

​        list.deleteLastNode();

​        list.deleteFirstNode();

 

​        list.printList();

​        //                [ 130 ]

​        System.out.println();

 

​        list.deleteLastNode();

 

​        list.printList();

​        //                Empty List.

​        System.out.println();

 

​        list.deleteFirstNode();

​        //                삭제할 노드가 없습니다.

​    }

}





출처 : https://joooootopia.tistory.com/18