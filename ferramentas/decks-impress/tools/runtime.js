// Runtime mínimo da apresentação (inline no index.html e no debug.html).
// Ao entrar numa moldura (data-contains), os passos contidos "acendem" (opacidade total).
(function () {
  document.addEventListener('impress:stepenter', function (e) {
    var lit = document.querySelectorAll('.step.lit');
    for (var i = 0; i < lit.length; i++) lit[i].classList.remove('lit');
    // Mergulho: o passo pai do detalhe ("sobre") continua aceso por baixo.
    var sobre = document.getElementById(e.target.getAttribute('data-sobre') || '');
    if (sobre) sobre.classList.add('lit');
    var list = e.target.getAttribute('data-contains');
    if (!list) return;
    list.split(',').forEach(function (id) {
      var n = document.getElementById(id);
      if (n) n.classList.add('lit');
    });
  });
  impress().init();
})();
