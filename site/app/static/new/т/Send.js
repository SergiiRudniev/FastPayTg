if (typeof window.Telegram !== 'undefined' && typeof window.Telegram.WebApp !== 'undefined') {
    let tg = window.Telegram.WebApp;

    tg.expand();

    const balanceUrl = `https://saved-surely-crane.ngrok-free.app/api/getbalance/${tg.initDataUnsafe.user.id}`;

    function fetchBalance() {
        fetch(balanceUrl)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                const responseDiv = document.getElementById('balance');
                responseDiv.innerHTML = `Your balance: ${data.value} $`;
            })
            .catch(error => {
                console.error('There has been a problem with your fetch operation:', error);
            });
    }

    function sendMoney() {
        const recipient = document.getElementById('input-field').value.trim();
        const amount = document.getElementById('summ-field').value.trim();

        // Проверка на валидность входных данных
        if (recipient === '') {
            alert('Please enter a valid recipient ID.');
            return;
        }

        if (amount === '' || isNaN(amount) || Number(amount) <= 0) {
            alert('Please enter a valid amount.');
            return;
        }

        const sendUrl = `https://saved-surely-crane.ngrok-free.app/api/send/${recipient}`;

        const sendData = {
            PayerId: tg.initDataUnsafe.user.id.toString(),
            Amount: Number(amount)
        };

        fetch(sendUrl, {
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
            openCodeModal();
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
            alert('An error occurred, please try again.');
        });
    }

    function openCodeModal() {
        const modal = document.getElementById('codeModal');
        const closeButton = modal.querySelector('.close');
        const submitButton = document.getElementById('submitCode');
        const codeInput = document.getElementById('codeInput');

        modal.style.display = 'block';

        codeInput.value = '';

        closeButton.onclick = function() {
            modal.style.display = 'none';
        }

        submitButton.onclick = function() {
            const code = codeInput.value.trim();
            if (code === '') {
                alert('Please enter a valid code.');
                return;
            }

            verifyCode(code);
        }

        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        }
    }

    function verifyCode(inputCode) {
        const sendCodeUrl = `https://saved-surely-crane.ngrok-free.app/api/check_code/${tg.initDataUnsafe.user.id}`;
        const codeData = {
            InputCode: String(inputCode)
        };

        fetch(sendCodeUrl, {
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
                document.getElementById('codeModal').style.display = 'none';
            } else if (responseData["Status:"] === "warning") {
                alert('The code has expired. Attempts are closed.');
                document.getElementById('codeModal').style.display = 'none';
            } else if (responseData["Status:"] === "ErrorCode") {
                alert('Incorrect code. Please try again.');
                openCodeModal();
            } else {
                throw new Error('Unknown error occurred.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred, please try again.');
        });
    }

    fetchBalance();
    setInterval(fetchBalance, 3000);
} else {
    console.error("Telegram WebApp is not available.");
    alert("This feature is only available within the Telegram WebApp.");
}
