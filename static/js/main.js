document.querySelectorAll('.option-item').forEach(item => {
    item.addEventListener('click', () => {
        document.querySelectorAll('.option-item').forEach(i => i.classList.remove('active'));
        item.classList.add('active');
    });
});

window.onload = function() {
    document.querySelectorAll('.animate__animated').forEach(element => {
        element.style.visibility = "visible";
    });
};