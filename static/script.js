// Обработка формы логина
document.getElementById('login-form')?.addEventListener('submit', function(event) {
    event.preventDefault();

    // Получаем значения полей из формы логина
    const formData = new FormData(event.target);

    fetch('/login', {
        method: 'POST',
        body: formData  // Отправляем данные как FormData
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === 'Login successful') {
            window.location.href = '/success';
        } else {
            document.getElementById('error-message').innerText = data.message;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
    });
});

// Обработка формы регистрации
document.getElementById('register-form')?.addEventListener('submit', function(event) {
    event.preventDefault();

    // Получаем значения полей из формы регистрации
    const formData = new FormData(event.target);

    fetch('/register', {
        method: 'POST',
        body: formData  // Отправляем данные как FormData
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === 'Registration successful') {
            // Перенаправляем на страницу логина после успешной регистрации
            window.location.href = '/';
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
    });
});
