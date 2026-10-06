// Apenas no debug.html: HUD com id/posição do passo atual; tecla "m" = mapa; "0" = primeiro passo.
// Abra em um passo específico com debug.html#/id-do-passo
(function () {
  var hud = document.createElement('div');
  hud.id = 'hud';
  document.body.appendChild(hud);
  var ids = [].map.call(document.querySelectorAll('.step'), function (n) { return n.id; });
  document.addEventListener('impress:stepenter', function (e) {
    var el = e.target;
    document.body.classList.toggle('mapa', el.id === '__mapa');
    hud.textContent = (ids.indexOf(el.id) + 1) + '/' + ids.length + '  #' + el.id +
      '  x=' + el.dataset.x + ' y=' + el.dataset.y + ' scale=' + el.dataset.scale +
      (el.dataset.rotate ? ' rot=' + el.dataset.rotate : '') + '   [m] mapa  [0] início';
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'm') impress().goto('__mapa');
    if (e.key === '0') impress().goto(ids[0]);
  });
})();
