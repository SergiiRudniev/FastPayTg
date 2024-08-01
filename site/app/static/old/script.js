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

            responseDiv.innerHTML = `<h1 class="maintext">${data.value} $</h1>`;
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
}

function SendMoney() {
    let recipient = prompt('Enter recipient Id', '');
    if (recipient === null || recipient.trim() === '') {
        alert('Cancel');
        return;
    }
    let Amount = prompt('Enter amount', '');
    if (Amount === null || Amount.trim() === '') {
        alert('Cancel');
        return;
    }
    let SendUrl = `https://saved-surely-crane.ngrok-free.app/api/send/${recipient}`;

    const sendData = {
        PayerId: tg.initDataUnsafe.user.id,
        Amount: Amount
    };

    fetch(SendUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(sendData)
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(errData => {
                throw new Error('Pay Error: ' + errData.detail);
            });
        }
        return response.json();
    })
    .then(data => {
        alert('Transaction status:', data.status);
        let code = prompt('Enter code', '');
        if (code === null || code.trim() === '') {
            alert('Cancel');
            return;
        }
        const sendData = {
            code: tg.initDataUnsafe.user.id
        };
        fetch(SendUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(sendData)
        })
    })
    .catch(error => {
        alert('There has been a problem with your fetch operation:', error);
    });
}
fetchBalance()
setInterval(fetchBalance, 3000);

let userid = document.getElementById('TextID');
userid.innerText = `id: ${tg.initDataUnsafe.user.id}`;
