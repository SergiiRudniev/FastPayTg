let tg = window.Telegram.WebApp;

tg.expand();
const url = `https://saved-surely-crane.ngrok-free.app/api/getbalance/${tg.initDataUnsafe.user.id}`;

function fetchBalance() {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const responseDiv = document.getElementById('balance');

            responseDiv.innerHTML = `<h2>${data.value} $</h2>`;
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
}
fetchBalance()
setInterval(fetchBalance, 3000);

let userid = document.getElementById('TextID');
userid.innerText = `id: ${tg.initDataUnsafe.user.id}`;
