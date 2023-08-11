// main.js
import * as SimpleFunctions  from './modules/simpleFunctions.js';
import * as DeleteAdmin      from './modules/delete_admin.js';

// Inicializa los formularios de la aplicacion
async function initializeEventListeners() {

    DeleteAdmin.deleteAdminButtonEvent();
}

window.addEventListener('DOMContentLoaded', async () => {
    initializeEventListeners();
    
    SimpleFunctions.clearAdminOnLogout();
    
});
