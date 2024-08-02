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
    let amount = prompt('Enter amount', '');
    if (amount === null || amount.trim() === '') {
        alert('Cancel');
        return;
    }
    let SendUrl = `https://saved-surely-crane.ngrok-free.app/api/send/${recipient}`;

    const sendData = {
        PayerId: tg.initDataUnsafe.user.id.toString(),
        Amount: Number(amount)
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
    .then(() => {
        let attempts = 0;
        const maxAttempts = 3;

        function requestCode() {
            let inputcode = prompt('Enter code', '');
            if (inputcode === null || inputcode.trim() === '') {
                alert('Cancel');
                return;
            }

            let SendCodeUrl = `https://saved-surely-crane.ngrok-free.app/api/check_code/${tg.initDataUnsafe.user.id}`;
            const codeData = {
                InputCode: String(inputcode)
            };

            fetch(SendCodeUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(codeData)
            })
            .then(response => response.json())
            .then(responseData => {
                if (responseData["Status:"] === "ok") {
                    alert('Successfully!');
                } else if (responseData["Status:"] === "warning") {
                    alert('The code has expired. Attempts are closed.');
                } else if (responseData["Status:"] === "ErrorCode") {
                    attempts++;
                    if (attempts < maxAttempts) {
                        alert('Incorrect code. Please try again.');
                        requestCode();
                    } else {
                        alert('The code has expired. Attempts are closed.');
                    }
                } else {
                    throw new Error('Unknown error occurred.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred, please try again.');
            });
        }

        requestCode();
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
        alert('An error occurred, please try again.');
    });
}

fetchBalance();
setInterval(fetchBalance, 3000);

let userid = document.getElementById('TextID');
userid.innerText = `id: ${tg.initDataUnsafe.user.id}`;
