document.getElementById('registerForm').addEventListener('submit', function(event) {
    var isValid = true;
    var username = document.forms["registerForm"]["username"].value;
    var password = document.forms["registerForm"]["password"].value;

    // Ejemplo de validación de username
    if (username.length > 150 || !/^[a-zA-Z0-9@.+\-/_]+$/.test(username)) {
        document.getElementById('usernameRequirements').style.display = 'block';
        isValid = false;
    } else {
        document.getElementById('usernameRequirements').style.display = 'none';
    }

    // Ejemplo de validación de contraseña
    if (password.length < 8 || password.match(/password123/)) {
        document.getElementById('passwordRequirements').style.display = 'block';
        isValid = false;
    } else {
        document.getElementById('passwordRequirements').style.display = 'none';
    }

    if (!isValid) {
        event.preventDefault();
    }
});