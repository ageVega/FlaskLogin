// dashboard.js
document.addEventListener("DOMContentLoaded", function () {
    const logoutButton = document.getElementById("logout-button");

    logoutButton.addEventListener("click", function () {
        // Aquí puedes agregar la lógica para cerrar sesión cuando tengas la autenticación de usuarios implementada

        // Redirige a la página de inicio después de cerrar sesión
        window.location.href = "/home";
    });
});