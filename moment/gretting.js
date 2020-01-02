
const form = document.querySelector(".js-form")
    input = form.querySelector("input"),
    gretting = document.querySelector(".js-grettings");
//로컬 스토리지에 저장할 키값을 지정 하고 display none를 해제해줄 클래스 명을 저장해놓음
const User_ls = "currentUser",
    showing_cn = "showing";
// 유저 이름이 null이 아닌 경우 form태그를 보이지 않게 설정후 유저이름이 보이도록 함
function paintGreeting(text) {
    form.classList.remove(showing_cn);
    gretting.classList.add(showing_cn);
    gretting.innerText = `Hello ${text}`;
}

// 유저의 이름을 localStorage에 저장
function saveName(text) {
    localStorage.setItem(User_ls, text);
}

// 
function handleSubmit(event) {
    // 이벤트의 실행을 막아 놓음
    event.preventDefault();
    const currentValue = input.value;

    // 유저의 이름을 보이게 하는 함수와 localStrage에 저장하는 함수 호출
    paintGreeting(currentValue);
    saveName(currentValue);
}

// 유저의 이름을 모를때 form 태그에 showing 클래스를 추가해 유저 이름 입력창이 보이게 함
function askForName() {
    form.classList.add(showing_cn);
    form.addEventListener("submit", handleSubmit);
}
// 저장된 이름을 localStorage에서 불러오며 없을 경우 이름을 작성할수 있는 창을 열어주고 있을경우 유저 이름이 보이도록 함
function loadName() {
    const currentUser = localStorage.getItem(User_ls);
    if(currentUser === null) {
        askForName();
    }else {
        paintGreeting(currentUser);
    }
}

// 시작하자마자 실행하는 함수 저장된 유저이름의 유무를 판단해 이후 로직을 수행하도록 함
function init() {
    loadName();
}

init();