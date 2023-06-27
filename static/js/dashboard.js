// dashboard.js
document.addEventListener("DOMContentLoaded", function () {
    const logoutButton = document.getElementById("logout-button");

    logoutButton.addEventListener("click", function () {
        // Redirige a la página de inicio después de cerrar sesión
        window.location.href = "/home";
    });
});