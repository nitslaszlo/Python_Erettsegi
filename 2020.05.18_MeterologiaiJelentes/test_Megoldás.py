import filecmp
from unittest import TestCase
from Jelentés import Jelentés
from Megoldás import Megoldás


class TestMegoldas(TestCase):
    def setUp(self):
        self.m: Megoldás = Megoldás('tavirathu13.txt')

    def test__telepules_kodok(self):
        self.assertSetEqual(self.m.településkódok, {'SM', 'PP', 'SN', 'BP', 'PR', 'PA', 'KE', 'BC', 'DC'})

    def test_utolso_jelentes_ideje(self):
        self.assertEqual(self.m.utolsó_jelentés_ideje('SM'), '23:45')

    def test_max_t_j(self):
        self.assertEqual(self.m.max_t_j().__str__(), 'DC 13:15 35')

    def test_min_t_j(self):
        self.assertEqual(self.m.min_t_j().__str__(), 'SM 23:45 16')

    def test_homerseklet_stat(self):
        self.assertTrue(self.m.hőmérséklet_stat.__contains__('KE NA;Hőmérséklet - ingadozás: 13'))
        self.assertTrue(self.m.hőmérséklet_stat.__contains__('PP NA;Hőmérséklet - ingadozás: 6'))
        self.assertTrue(self.m.hőmérséklet_stat.__contains__('BC NA;Hőmérséklet - ingadozás: 14'))
        self.assertTrue(self.m.hőmérséklet_stat.__contains__('BP Középhőmérséklet: 23;Hőmérséklet - ingadozás: 8'))
        self.assertTrue(self.m.hőmérséklet_stat.__contains__('SN Középhőmérséklet: 26;Hőmérséklet - ingadozás: 13'))
        self.assertTrue(self.m.hőmérséklet_stat.__contains__('PA Középhőmérséklet: 21;Hőmérséklet - ingadozás: 7'))
        self.assertTrue(self.m.hőmérséklet_stat.__contains__('DC Középhőmérséklet: 29;Hőmérséklet - ingadozás: 15'))
        self.assertTrue(self.m.hőmérséklet_stat.__contains__('SM Középhőmérséklet: 22;Hőmérséklet - ingadozás: 8'))
        self.assertTrue(self.m.hőmérséklet_stat.__contains__('PR Középhőmérséklet: 21;Hőmérséklet - ingadozás: 8'))

    def test_szelcsendes(self):
        self.assertTrue(self.m.szélcsendes.__contains__(Jelentés('BP 0100 00000 22')))
        self.assertTrue(self.m.szélcsendes.__contains__(Jelentés('DC 0215 00000 22')))
        self.assertTrue(self.m.szélcsendes.__contains__(Jelentés('SN 0315 00000 21')))
        self.assertTrue(self.m.szélcsendes.__contains__(Jelentés('BC 0445 00000 21')))
        self.assertTrue(self.m.szélcsendes.__contains__(Jelentés('DC 0445 00000 23')))
        self.assertTrue(self.m.szélcsendes.__contains__(Jelentés('SN 0515 00000 25')))
        self.assertTrue(self.m.szélcsendes.__contains__(Jelentés('SN 0545 00000 26')))
        self.assertTrue(self.m.szélcsendes.__contains__(Jelentés('KE 0845 00000 29')))
        self.assertTrue(self.m.szélcsendes.__contains__(Jelentés('BC 1145 00000 33')))

    def test_write_data(self):
        self.assertTrue(filecmp.cmp('txt_files/BC.txt', 'txt_files_oh/BC_oh.txt', shallow=False))
        self.assertTrue(filecmp.cmp('txt_files/BP.txt', 'txt_files_oh/BP_oh.txt', shallow=False))
        self.assertTrue(filecmp.cmp('txt_files/DC.txt', 'txt_files_oh/DC_oh.txt', shallow=False))
        self.assertTrue(filecmp.cmp('txt_files/KE.txt', 'txt_files_oh/KE_oh.txt', shallow=False))
        self.assertTrue(filecmp.cmp('txt_files/PA.txt', 'txt_files_oh/PA_oh.txt', shallow=False))
        self.assertTrue(filecmp.cmp('txt_files/PP.txt', 'txt_files_oh/PP_oh.txt', shallow=False))
        self.assertTrue(filecmp.cmp('txt_files/PR.txt', 'txt_files_oh/PR_oh.txt', shallow=False))
        self.assertTrue(filecmp.cmp('txt_files/SM.txt', 'txt_files_oh/SM_oh.txt', shallow=False))
        self.assertTrue(filecmp.cmp('txt_files/SN.txt', 'txt_files_oh/SN_oh.txt', shallow=False))
