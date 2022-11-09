(function () {

    const btnDeletar = document.querySelectorAll(".btnDeletar");

    btnDeletar.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirma = confirm('Deseja realmente deletar registro?');
            if (!confirma) {
                e.preventDefault();
            }
        });
    });
    
})();