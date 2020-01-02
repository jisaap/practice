
const weather = document.querySelector(".js-weather");

const COORDS = 'coords';
const API_KEY = '17e7eb67e2c598d3d738dbb0db0a289f';


function getWeather(lat, lon) {
    fetch(
        `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
        ).then(function(response) {
            return response.json();
        })
        .then(function(json) {
            const temperature = json.main.temp;
            const place = json.name;
            weather.innerText = `${temperature} @ ${place}`;
        });
}


function saveCoords(coordsObj) {
    localStorage.setItem(COORDS, JSON.stringify(coordsObj));
}


function handleGeoSucces(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude
    const coordsObj = {
        latitude,
        longitude
    };
    saveCoords(coordsObj);
    getWeather(latitude, longitude);
}

function handleGeoError() {
    console.log("error");
}

function askForCoords() {
    navigator.geolocation.getCurrentPosition(handleGeoSucces, handleGeoError);
}


function loadCoords() {
    const loadedcoords = localStorage.getItem(COORDS);
    if(loadedcoords === null) {
        askForCoords();
    }else {
        const parseCoords = JSON.parse(loadedcoords)
        getWeather(parseCoords.latitude, parseCoords.longitude);
    }

}

function init() {
    loadCoords();
}

init();