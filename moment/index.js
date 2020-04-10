const title = document.querySelector("#title");

const BASE_COLOR = "rgb(52, 73, 94)";
const OTHER_COLOR = "#7f8c8d";
const CLICKED_CLASS = "clicked";

function handleClick() {
   
    // toggle 은 함수안에 있는 값을 체크해 클래스가 있으면 remove 없으면 add 해줌
    title.classList.toggle(CLICKED_CLASS);
    // 같은 역할을 하는 토글로 대체함
    // const currentClass = title.className;
    // const hasClass = title.classList.contains(CLICKED_CLASS);
    // if(!hasClass) {
    //     title.classList.add(CLICKED_CLASS);
    // }else {
    //     title.classList.remove(CLICKED_CLASS);
    // }
}


// function handleClick() {
//     const currentColor = title.style.color;
//     if(currentColor === BASE_COLOR) {
//         title.style.color = OTHER_COLOR;
//     }else {
//         title.style.color = BASE_COLOR;    
//     }
// }

function init() {
    title.style.color = BASE_COLOR;
    title.addEventListener("click", handleClick);
}

init();

function handleOffline() {
    console.log("Bye bye");
}
function handelOnline() {
    console.log("Welcome Back");
}


// 인터넷이 끊길 경우 이벤트
window.addEventListener("offline", handleOffline);

// 인터넷이 연결될때 의 이벤트
window.addEventListener("online", handelOnline);
