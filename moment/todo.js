const toDoForm = document.querySelector(".js-toDoForm"),
    toDoInput = toDoForm.querySelector("input"),
    toDoList = document.querySelector(".js-toDoList");

    const TODOS_LS = "toDos";
    
    let toDos = [];

    // 리스트에 버튼을 눌렀을때 그 버튼의 부모 li를 추적하여 
    function deleteToDo(event) {
        //어떤 버튼이 클릭 이벤트를 발생시켰는지 확인
        const btn = event.target;
        // 버튼의 부모 태그를 찾아냄
        const li = btn.parentNode;
        // 버튼의 부모를 리스트에서 삭제함
        toDoList.removeChild(li);
        // filter함수를 이용해 선택된 li이외의 리스트를 다시 작성한후 localStorage에 다시 저장
        const cleanToDos = toDos.filter(function(todo) {
            return todo.id !== parseInt(li.id);
        });
        toDos = cleanToDos;
        saveToDos();
    }
    //localStorage에 저장할때 object형으로 저장 되지만 이것을 String 형식으로 저장하기위해 JSON.stringify 함수를 이용해 저장
    function saveToDos() {
        localStorage.setItem(TODOS_LS, JSON.stringify(toDos));
    }
    // li와 버튼을 생성해 리스트에 넣어주며 li에 고유의 id값을 부여하며 버튼에 이벤트와 localStorage에 저장하기 위해 object형태로 해당 함수에 매개변수를 통해 전달
    function paintToDo(text) {
        const li = document.createElement("li");
        const deleteBtn = document.createElement("button");
        const span = document.createElement("span");
        const newId = toDos.length + 1;
        deleteBtn.innerText = "x";
        deleteBtn.addEventListener("click", deleteToDo);
        span.innerText = text;
        li.appendChild(deleteBtn);
        li.appendChild(span);
        li.id = newId;
        toDoList.appendChild(li);
        const toDoObj = {
            text : text,
            id : newId
        };
        toDos.push(toDoObj);
        saveToDos(toDoObj);
    }

    //새로 작성한 todo값을 출력할수 있는 함수에 전송
    function handleSubmit(event) {
        event.preventDefault();
        const currentValue = toDoInput.value;
        paintToDo(currentValue);
        toDoInputValue = "";
    }
    
    // 기존에 작성햇던 todo 값을 localStorage에서 불러오며 JSON.parse를 이용해 String 형태를 JSON Object 형태로 다시 형변환 해준다.
    function loadToDos() {
        const loadToDos = localStorage.getItem(TODOS_LS);
        if(loadToDos !== null) {
            const parsedToDos = JSON.parse(loadToDos);
            // JSON Object 형태로 가져온 리스트 값을 foEach문을 통하여 하나하나 출력이 가능한 함수로 전달한다
            parsedToDos.forEach(function(toDo) {
                paintToDo(toDo.text);
            })
        }

    }

    //시작하는 함수 저장된 값을 불러오고 해야할일을 입력할수 있는 event를 할당한다
    function init() {
        loadToDos();
        toDoForm.addEventListener("submit", handleSubmit);
    }

    init();