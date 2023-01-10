// Initialize all toasts
const toastElList = document.querySelectorAll('.toast');
const toastList = [...toastElList].map(toastEl => new bootstrap.Toast(toastEl, null));

const n = toastList.length;
let i = 0;

for(; i < n; i++) {
    toastList[i].show();
}