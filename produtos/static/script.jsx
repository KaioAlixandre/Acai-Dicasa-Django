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

    // Modal de Informações
    const btnInfo = document.getElementById('mais-informacoes-btn');
    const modalInfo = document.getElementById('modal-informacoes');
    const fecharModal = document.getElementById('fechar-modal-informacoes');
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    function setActiveTab(tab) {
        tabBtns.forEach(btn => {
            if (btn.dataset.tab === tab) {
                btn.classList.add('text-purple-700', 'border-purple-700');
                btn.classList.remove('text-gray-500', 'border-transparent');
            } else {
                btn.classList.remove('text-purple-700', 'border-purple-700');
                btn.classList.add('text-gray-500', 'border-transparent');
            }
        });
        tabContents.forEach(content => {
            content.classList.toggle('hidden', content.id !== 'tab-' + tab);
        });
    }

    if (btnInfo && modalInfo && fecharModal) {
        btnInfo.addEventListener('click', function (e) {
            e.preventDefault();
            modalInfo.style.display = 'flex';
            setActiveTab('sobre');
        });

        fecharModal.addEventListener('click', function () {
            modalInfo.style.display = 'none';
        });

        modalInfo.addEventListener('click', function (e) {
            if (e.target === modalInfo) {
                modalInfo.style.display = 'none';
            }
        });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') {
                modalInfo.style.display = 'none';
            }
        });

        tabBtns.forEach(btn => {
            btn.addEventListener('click', function () {
                setActiveTab(btn.dataset.tab);
            });
        });
    }
});