document.addEventListener('DOMContentLoaded', function () {
    const btnCategorias = document.querySelector('[data-categorias-btn]');
    const dropdown = document.getElementById('dropdown-categorias');

    if (btnCategorias && dropdown) {
        btnCategorias.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            dropdown.style.display = dropdown.style.display === 'none' || dropdown.style.display === '' ? 'block' : 'none';
        });

        dropdown.addEventListener('click', function(e) {
            e.stopPropagation();
        });

        document.addEventListener('click', function () {
            dropdown.style.display = 'none';
        });
    }
});