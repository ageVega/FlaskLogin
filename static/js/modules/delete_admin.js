// delete_admin.js

export function deleteAdminButtonEvent() {
    const deleteForm = document.getElementById('delete-form');
    if (!deleteForm) return;

    deleteForm.addEventListener('submit', async function(event) {
        event.preventDefault();

        const password = document.getElementById('password').value;
        const adminId = sessionStorage.getItem('admin_id');

        // Primero, confirma la contraseña
        const confirmResponse = await fetch(`/auth/confirm_password/${adminId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ password: password }),
        });

        const confirmData = await confirmResponse.json();

        if (!confirmResponse.ok) {
            alert('Error: ' + confirmData.message);
            return;
        }

        // Si la contraseña es correcta, pregúntale al usuario si realmente quiere eliminar la casa
        const deleteConfirmed = confirm('¿Estás seguro de que quieres eliminar tu cuenta? Esta acción no se podrá deshacer.');
        
        if (!deleteConfirmed) {
            return;
        }

        // Finalmente, realiza la petición para eliminar la casa
        const deleteResponse = await fetch(`/auth/delete/${adminId}`, {
            method: 'DELETE'
        });
        const deleteData = await deleteResponse.json();

        if (!deleteResponse.ok) {
            alert('Error: ' + deleteData.message);
            return;
        }

        alert(deleteData.message);
        window.location.href = '/home';
    });
}
