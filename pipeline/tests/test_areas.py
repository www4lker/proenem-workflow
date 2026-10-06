"""Testes de unidade da escolha de dia e faixa por ano e área (config/areas.yaml).

Rodar da raiz do repositório: python -m unittest discover -s pipeline/tests -t pipeline
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import areas  # noqa: E402
from extrair_prova import detectar_dia  # noqa: E402


class FaixaPorAnoEArea(unittest.TestCase):
    def test_ch_ate_2016_e_1_a_45_no_dia_1(self):
        for ano in (2009, 2013, 2016):
            f = areas.faixa("CH", ano)
            self.assertEqual(f.tupla(), (1, 1, 45), ano)

    def test_ch_desde_2017_e_46_a_90_no_dia_1(self):
        for ano in (2017, 2019, 2025, 2030):
            f = areas.faixa("CH", ano)
            self.assertEqual(f.tupla(), (1, 46, 90), ano)

    def test_cn_muda_de_dia_em_2017(self):
        self.assertEqual(areas.faixa("CN", 2016).tupla(), (1, 46, 90))
        self.assertEqual(areas.faixa("CN", 2019).tupla(), (2, 91, 135))

    def test_lc_troca_de_lugar_com_ch(self):
        self.assertEqual(areas.faixa("LC", 2015).tupla(), (2, 91, 135))
        self.assertEqual(areas.faixa("LC", 2018).tupla(), (1, 1, 45))

    def test_mt_sempre_136_a_180_no_dia_2(self):
        for ano in (2010, 2016, 2017, 2025):
            self.assertEqual(areas.faixa("MT", ano).tupla(), (2, 136, 180), ano)

    def test_faixas_de_um_mesmo_dia_nao_se_sobrepoem(self):
        for ano in (2013, 2016, 2017, 2025):
            for dia in (1, 2):
                vistos = {}
                for sigla in areas.siglas():
                    f = areas.faixa(sigla, ano)
                    if f.dia != dia:
                        continue
                    for n in range(f.q_min, f.q_max + 1):
                        self.assertNotIn(n, vistos, f"{ano} dia {dia} Q{n}: {sigla} e {vistos.get(n)}")
                        vistos[n] = sigla
                self.assertEqual(sorted(vistos), list(range(1, 91)) if dia == 1 else list(range(91, 181)),
                                 f"{ano} dia {dia} não cobre o caderno inteiro")

    def test_inverso_area_de_numero(self):
        self.assertEqual(areas.area_de_numero(10, 2015, 1), "CH")
        self.assertEqual(areas.area_de_numero(10, 2019, 1), "LC")
        self.assertEqual(areas.area_de_numero(100, 2019, 2), "CN")
        self.assertIsNone(areas.area_de_numero(100, 2019, 1))

    def test_erros_claros(self):
        with self.assertRaises(KeyError):
            areas.faixa("XX", 2019)
        with self.assertRaises(KeyError):
            areas.faixa("CH", 2008)

    def test_disciplinas_e_competencias_de_ch(self):
        self.assertEqual(areas.disciplinas("CH"), ["geografia", "historia", "sociologia", "filosofia"])
        self.assertEqual(areas.competencias("CH")[6], "Geopolítica/mundialização")
        self.assertTrue(areas.prompt("CH").exists())
        self.assertIsNone(areas.prompt("CN"))


class DiaNoNomeDoPdf(unittest.TestCase):
    def test_nomes_reais_do_inep(self):
        casos = {
            "2019_PV_impresso_D2_CD1.pdf": 2,       # "CD1" é caderno 1, não dia 1
            "2014_PV_impresso_D1_CD1.pdf": 1,
            "CADERNO_1_AZUL_SABADO.pdf": 1,
            "dia1_caderno1_azul.pdf": 1,
            "2025_GB_impresso_D1_CD1.pdf": 1,
            "GAB_ENEM_2018_DIA_1_AZUL.pdf": 1,
            "gabarito_2_dia_caderno_5_amarelo.pdf": None,  # "2_dia" não é reconhecido: cai no None
            "2013_x.pdf": None,
        }
        for nome, dia in casos.items():
            self.assertEqual(detectar_dia(Path(nome)), dia, nome)


if __name__ == "__main__":
    unittest.main()
