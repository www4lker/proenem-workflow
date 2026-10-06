#!/usr/bin/env python3
"""Põe os passos do deck nas faces de um prisma octogonal em pé (um "tambor") e reescreve a geometria do layout.json.

Uso (de dentro de aula/03-slides/):  python3 prisma.py [--seco]

Cada bloco da aula ocupa uma face lateral; os slides do bloco descem pela face, e a abertura fica sempre na primeira
linha, de modo que as ilustrações formam uma faixa em volta do topo. Na troca de bloco a câmera gira 45° em volta do
eixo vertical, sempre no mesmo sentido (rotateY de 0 a 315). O título fica deitado na tampa (rotateX 90) e o ponto do
QR logo à frente dele. A visão geral (mapa-final) olha o tambor de cima e de frente, inclinada, e mostra o objeto
inteiro.

Ordem, why, class e transicao continuam no layout.json; aqui ficam só a geometria e quem vai em cada face. Para trocar
um passo de face, mexa em FACES e rode de novo. Precisa do patch 3D do decks-impress (rotateX, rotateY, camera).
"""
import json
import math
import sys
from pathlib import Path

LAYOUT = Path(__file__).with_name('layout.json')

# Uma face por bloco, na ordem da aula; a face k tem rotateY = 45·k.
FACES = [
    ['quatro-eixos'],
    ['abertura-ecologia', 'ecossistema', 'serie-historica'],
    ['abertura-impactos', 'impacto', 'intervencao-benefica', 'quem-paga'],
    ['abertura-sustentabilidade', 'sustentavel', 'planejamento', 'limpa-para-quem'],
    ['abertura-residuos', 'residuos', 'residuos-4r', 'residuos-charge', 'residuos-mapa', 'residuos-logistica'],
    ['abertura-caso', 'nuvem', 'lixo-eletronico', 'questao-autoral', 'eldorado'],
    ['questao-aral', 'questao-cerrado', 'questao-veredas', 'questao-quioto'],
    ['fechamento'],
]

# Mergulhos: deslocamento no referencial do passo pai (x para a direita, y para baixo do slide). Ficam no plano do
# pai, um pouco à frente dele, e herdam o giro.
MERGULHOS = {
    'rio-2004': ('serie-historica', -440, 20),
    'rio-2023': ('serie-historica', 480, 20),
    'safs-2023': ('serie-historica', 410, 0),
    'entroncamento': ('eldorado', -480, -70),
}

APOTEMA = 2700   # distância do eixo do tambor a cada face; a face mede 2·2700·tan 22,5° ≈ 2237 (slide 1920 + folga)
LINHA = 1300     # de uma linha à seguinte na mesma face (slide 1080 + folga)
TAMPA = -650     # altura da tampa: logo acima da primeira linha (que vai de -540 a 540)
GRADE = 100

# Tampa: título deitado (escala 2) e, à frente dele, o ponto do QR. rotateY 360 no QR evita que a câmera desgire.
TITULO = {'x': 0, 'y': TAMPA, 'z': 0, 'scale': 2, 'rotateX': 90}
QR = {'x': 0, 'y': TAMPA - 4, 'z': 1600, 'rotateX': 90, 'rotateY': 360}

# Visão geral: de cima e de frente, continuando o giro (315 → 360). Escala e altura da câmera acertadas no navegador
# (1280×720): o tambor ocupa ~85% da altura, centrado. Com a inclinação, a tampa sobe na tela; por isso o centro da
# câmera fica acima do meio da altura do tambor.
VISTA = {'inclinacao': 40, 'escala': 7, 'y': 1800}


def grade(v):
    return round(v / GRADE) * GRADE


def montar():
    pos = {}
    for k, ids in enumerate(FACES):
        rot = 45 * k
        a = math.radians(rot)
        for i, sid in enumerate(ids):
            pos[sid] = {'x': round(APOTEMA * math.sin(a)), 'y': i * LINHA, 'z': round(APOTEMA * math.cos(a)),
                        'rotateY': rot}
    for sid, (pai, dx, dy) in MERGULHOS.items():
        p = pos[pai]
        a = math.radians(p['rotateY'])
        pos[sid] = {'x': round(p['x'] + dx * math.cos(a) + 3 * math.sin(a)), 'y': p['y'] + dy,
                    'z': round(p['z'] - dx * math.sin(a) + 3 * math.cos(a)), 'rotateY': p['rotateY']}
    pos['titulo'] = dict(TITULO)
    pos['material-online'] = dict(QR)
    return pos


def camera():
    """Moldura da visão geral: centrada no eixo do tambor, inclinada para mostrar a tampa e a frente."""
    return {'x': 0, 'y': VISTA['y'], 'z': 0, 'scale': VISTA['escala'], 'rotateX': VISTA['inclinacao'], 'rotateY': 360}


def main():
    dados = json.loads(LAYOUT.read_text(encoding='utf-8'))
    pos = montar()
    passos = {s['id'] for s in dados['steps'] if not s.get('fit')}
    faltam = passos - set(pos)
    if faltam:
        sys.exit(f'passos sem lugar no prisma: {", ".join(sorted(faltam))}')
    for s in dados['steps']:
        for chave in ('x', 'y', 'z', 'rotate', 'rotateX', 'rotateY'):
            if not s.get('fit'):
                s.pop(chave, None)
        if s.get('fit'):
            s['camera'] = camera()
            continue
        for chave, v in pos[s['id']].items():
            if v:
                s[chave] = v
    dados.get('meta', {}).pop('maxRotate', None)
    print(f'apótema {APOTEMA}; {len(FACES)} faces; visão geral: {camera()}')
    if '--seco' not in sys.argv:
        LAYOUT.write_text(json.dumps(dados, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(f'gravado: {LAYOUT.name}')


if __name__ == '__main__':
    main()
