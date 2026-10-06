"""amostra_cega: leitura das respostas da ficha, kappa e coerência da matriz oficial de CH."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE / "scripts"))
from amostra_cega import COTAS, MATRIZ, kappa, ler_respostas  # noqa: E402


class LeituraDaFicha(unittest.TestCase):
    def test_aceita_numero_com_ou_sem_prefixo_e_branco(self):
        ficha = (
            "# Ficha\n\nCompetência: (não é questão)\n\n"
            "### 01 · ENEM 2013, questão 9\n\nCompetência: 3\nHabilidade: H12\nNota: dúvida com C2\n\n"
            "### 02 · ENEM 2014, questão 8\n\nCompetência: C5\nHabilidade: \nNota: \n"
        )
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "ficha.md"
            p.write_text(ficha, encoding="utf-8")
            r = ler_respostas(p)
        self.assertEqual(r[1], [3, 12, "dúvida com C2"])
        self.assertEqual(r[2], [5, None, ""])
        self.assertEqual(len(r), 2)


class Kappa(unittest.TestCase):
    def test_concordancia_total_e_um(self):
        self.assertAlmostEqual(kappa([(1, 1), (2, 2), (3, 3)]), 1.0)

    def test_sem_respostas_e_none(self):
        self.assertIsNone(kappa([]))


class MatrizOficial(unittest.TestCase):
    def test_seis_competencias_e_trinta_habilidades_com_fonte(self):
        m = json.loads(MATRIZ.read_text(encoding="utf-8"))
        self.assertEqual(sorted(map(int, m["competencias"])), list(range(1, 7)))
        self.assertEqual(sorted(map(int, m["habilidades"])), list(range(1, 31)))
        self.assertEqual(len(m["sha256"]), 64)

    def test_cotas_somam_vinte(self):
        self.assertEqual(sum(COTAS.values()), 20)


if __name__ == "__main__":
    unittest.main()
