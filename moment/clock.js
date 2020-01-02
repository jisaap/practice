
const clockContainer = document.querySelector(".js-clock"),
      clockTitle = clockContainer.querySelector("h1");

      // 시간을 알아내기 위한 함수 new Date로 선언된 시간이 저장되기때문에 Interval 함수를 이용해 1초에 한번씩 다시 실행해줌
function getTime() {
    const date = new Date();
    const minutes = date.getMinutes();
    const hours = date.getHours();
    const seconds = date.getSeconds();
    //시간이 1 ~ 9 면 앞 자리에 0 을 붙여주어 더욱 자연스럽게 보일수 있도록 삼항연산자를 이용해 구현
    clockTitle.innerText = `${hours < 10 ? `0${hours}` : hours}:${minutes < 10 ? `0${minutes}` : minutes}:${seconds < 10 ?  `0${seconds}` : seconds}`;
}

function init() {
    getTime();
    setInterval(getTime, 1000);
}

init();