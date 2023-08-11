// simpleFunctions.js

export function clearAdminOnLogout() {
    const urlPath = window.location.pathname;
    if (urlPath === '/' || urlPath === '/home') {
        sessionStorage.removeItem('admin_id');
        sessionStorage.removeItem('admin_nickname');
    }
}