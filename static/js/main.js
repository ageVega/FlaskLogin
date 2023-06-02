document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("login-form");

    loginForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        console.log("Usuario:", username);
        console.log("Contraseña:", password);

        // Aquí puedes agregar la lógica para iniciar sesión cuando tengas la base de datos y el registro de usuarios implementado

        // Redirige a la página de inventario después de iniciar sesión
        window.location.href = "/dashboard";
    });
});