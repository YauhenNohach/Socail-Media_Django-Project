document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const password = form.querySelector('#id_password1').value;
        const confirmPassword = form.querySelector('#id_password2').value;

        if (password !== confirmPassword) {
            alert("Пароли не совпадают!");
            event.preventDefault();
        }
    });
});

