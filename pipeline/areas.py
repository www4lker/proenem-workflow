"""Lê config/areas.yaml: dia de prova, faixa de questões, disciplinas e prompt de cada área por ano.

    from areas import faixa, disciplinas
    dia, q_min, q_max = faixa("CH", 2019)   # -> (1, 46, 90)
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

CONFIG_PADRAO = Path(__file__).resolve().parent / "config" / "areas.yaml"


@dataclass(frozen=True)
class Faixa:
    area: str
    ano: int
    dia: int
    q_min: int
    q_max: int
    conferido: str

    def contem(self, numero: int) -> bool:
        return self.q_min <= numero <= self.q_max

    def tupla(self) -> tuple[int, int, int]:
        """(dia, primeira questão, última questão)."""
        return (self.dia, self.q_min, self.q_max)


_cache: dict[Path, dict] = {}


def carregar(caminho: Path | str | None = None) -> dict:
    """Devolve o dicionário `areas` do YAML (com cache por caminho) e valida o essencial."""
    caminho = Path(caminho) if caminho else CONFIG_PADRAO
    if caminho not in _cache:
        with open(caminho, encoding="utf-8") as f:
            dados = yaml.safe_load(f)
        areas = dados.get("areas") if isinstance(dados, dict) else None
        if not areas:
            raise ValueError(f"{caminho}: falta a chave 'areas'")
        for sigla, cfg in areas.items():
            for p in cfg.get("periodos", []):
                ini, fim = p["anos"]
                q0, q1 = p["questoes"]
                if fim is not None and fim < ini:
                    raise ValueError(f"{caminho}: {sigla} período {p['anos']} invertido")
                if not (1 <= q0 <= q1 <= 180):
                    raise ValueError(f"{caminho}: {sigla} faixa {p['questoes']} fora de 1–180")
                if p["dia"] not in (1, 2):
                    raise ValueError(f"{caminho}: {sigla} dia {p['dia']} inválido")
        _cache[caminho] = areas
    return _cache[caminho]


def siglas(caminho=None) -> list[str]:
    return list(carregar(caminho))


def faixa(area: str, ano: int, caminho=None) -> Faixa:
    """Dia e faixa de questões da área naquele ano. Erro claro se a área ou o ano não estiverem no YAML."""
    areas = carregar(caminho)
    if area not in areas:
        raise KeyError(f"área {area!r} não está em areas.yaml (há: {', '.join(areas)})")
    ano = int(ano)
    for p in areas[area]["periodos"]:
        ini, fim = p["anos"]
        if ini <= ano and (fim is None or ano <= fim):
            q0, q1 = p["questoes"]
            return Faixa(area, ano, int(p["dia"]), int(q0), int(q1), str(p.get("conferido", "")))
    raise KeyError(f"área {area}: nenhum período cobre o ano {ano} em areas.yaml")


def disciplinas(area: str, caminho=None) -> list[str]:
    return list(carregar(caminho)[area].get("disciplinas", []))


def competencias(area: str, caminho=None) -> dict[int, str]:
    return {int(k): str(v) for k, v in (carregar(caminho)[area].get("competencias") or {}).items()}


def prompt(area: str, caminho=None) -> Path | None:
    p = carregar(caminho)[area].get("prompt")
    return (CONFIG_PADRAO.parent.parent / p) if p else None


def area_de_numero(numero: int, ano: int, dia: int, caminho=None) -> str | None:
    """Inverso: dado o número da questão, o dia e o ano, qual área? (None se nenhuma faixa bater.)"""
    for sigla in carregar(caminho):
        try:
            f = faixa(sigla, ano, caminho)
        except KeyError:
            continue
        if f.dia == dia and f.contem(numero):
            return sigla
    return None
