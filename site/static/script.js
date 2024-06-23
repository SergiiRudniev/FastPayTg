let tg = window.Telegram.WebApp;

tg.expand();
const url = `https://saved-surely-crane.ngrok-free.app/api/getbalance/${tg.initDataUnsafe.user.id}`;

fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        const responseDiv = document.getElementById('balance');

        responseDiv.innerHTML = `<h1 class="maintext">${data.value} $</h1>`;
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });

let userid = document.getElementById('TextID');
userid.innerText = `id: ${tg.initDataUnsafe.user.id}`;
