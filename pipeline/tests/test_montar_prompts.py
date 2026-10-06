"""montar_prompts.montar_prompt deve reproduzir a coluna prompt_completo do lote de 05/2026 (cache versionado)."""
import csv
import sys
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))
sys.path.insert(0, str(PIPELINE / "scripts"))
from montar_prompts import montar_prompt  # noqa: E402

csv.field_size_limit(10_000_000)


class ReproduzLoteDeMaio(unittest.TestCase):
    def test_todas_as_linhas_do_batch_completo_raw(self):
        prompt = (PIPELINE / "prompts/classificar_questao.txt").read_text(encoding="utf-8")
        with open(PIPELINE / "corpus_enem/batch_completo_raw.csv", encoding="utf-8", newline="") as f:
            esperado = {r["id"]: r["prompt_completo"] for r in csv.DictReader(f)}
        with open(PIPELINE / "corpus_enem/questoes_raw.csv", encoding="utf-8", newline="") as f:
            questoes = {r["id"]: r for r in csv.DictReader(f)}
        self.assertEqual(len(esperado), 350)
        iguais = 0
        for qid, texto in esperado.items():
            self.assertEqual(montar_prompt(prompt, questoes[qid]), texto, qid)
            iguais += 1
        self.assertEqual(iguais, 350)

    def test_fora_do_lote_sao_as_cinco_sem_enunciado(self):
        with open(PIPELINE / "corpus_enem/batch_completo_raw.csv", encoding="utf-8", newline="") as f:
            no_lote = {r["id"] for r in csv.DictReader(f)}
        with open(PIPELINE / "corpus_enem/questoes_raw.csv", encoding="utf-8", newline="") as f:
            fora = sorted(r["id"] for r in csv.DictReader(f) if r["id"] not in no_lote)
        self.assertEqual(fora, ["2013_CH_042", "2014_CH_016", "2016_CH_035", "2025_CH_005", "2025_CH_040"])


if __name__ == "__main__":
    unittest.main()
