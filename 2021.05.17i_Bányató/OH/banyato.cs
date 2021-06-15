using System;
using System.IO;

namespace banyato
{
    class Program
    {
        static int[,] melyseg = new int[100, 100];
        static int sorok;
        static int oszlopok;

        static void Main(string[] args)
        {
            Feladat1();
            Feladat2();
            Feladat3();
            Feladat4();
            Feladat5();
            Feladat6();

            Console.ReadKey();
        }

        static void Feladat6()
        {
            //Sávdiagram készítése
            Console.WriteLine("6. feladat");
            Console.Write("A vizsgált szelvény oszlopának azonosítója=");
            int oszlop = Convert.ToInt32(Console.ReadLine());
            StreamWriter sw = new StreamWriter("diagram.txt");
            for (int sor = 1; sor <= sorok; sor++)
            {
                string egysor = sor.ToString("D2");
                for (int i = 0; i < Math.Round((double)melyseg[sor, oszlop] / 10); i++)
                    egysor = egysor + "*";
                sw.WriteLine(egysor);
            }
            sw.Close();
        }

        static void Feladat5()
        {
            //A tó kerülete
            Console.WriteLine("5. feladat");
            int db = 0;
            for (int sor = 2; sor < sorok; sor++)
                for (int oszlop = 2; oszlop < oszlopok; oszlop++)
                    if (melyseg[sor, oszlop] > 0)
                    {
                        if (melyseg[sor - 1, oszlop] == 0) db++;
                        if (melyseg[sor + 1, oszlop] == 0) db++;
                        if (melyseg[sor, oszlop - 1] == 0) db++;
                        if (melyseg[sor, oszlop + 1] == 0) db++;
                    }
            Console.WriteLine("A tó partvonala {0} m hosszú", db);
        }

        static void Feladat4()
        {
            //A tó legmélyebb pontja(i)
            Console.WriteLine("4. feladat");
            int max = melyseg[1, 1];
            for (int sor = 1; sor <= sorok; sor++)
                for (int oszlop = 1; oszlop <= oszlopok; oszlop++)
                    if (max < melyseg[sor, oszlop]) max = melyseg[sor, oszlop];
            Console.WriteLine("A tó legnagyobb mélysége: {0} dm", (double)max);

            Console.WriteLine("A legmélyebb helyek sor-oszlop koordinátái: ");
            for (int sor = 1; sor <= sorok; sor++)
                for (int oszlop = 1; oszlop <= oszlopok; oszlop++)
                    if (max == melyseg[sor, oszlop]) Console.Write("({0}; {1})   ", sor, oszlop);
            Console.WriteLine();
        }

        static void Feladat3()
        {
            //A tó felszíne és átlagos mélysége
            Console.WriteLine("3. feladat");
            int f = 0;
            double s = 0;
            for (int sor = 1; sor <= sorok; sor++)
                for (int oszlop = 1; oszlop <= oszlopok; oszlop++)
                    if (melyseg[sor, oszlop] > 0)
                    {
                        f++;
                        s += melyseg[sor, oszlop];
                    }
            Console.WriteLine("A tó felszíne: {0} m2, átlagos mélysége: {1} m", f, ((double)s / (10 * f)).ToString("F2"));
        }

        static void Feladat2()
        {
            //Tó mélysége adott helyen
            Console.WriteLine("2. feladat");
            Console.Write("A mérés sorának azonosítója=");
            int sor = Convert.ToInt32(Console.ReadLine());
            Console.Write("A mérés oszlopának azonosítója=");
            int oszlop = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("A mért mélység az adott helyen {0} dm", melyseg[sor, oszlop]);
        }

        static void Feladat1()
        {
            //Adatok beolvasása
            StreamReader sr = new StreamReader("melyseg.txt");
            sorok = Convert.ToInt32(sr.ReadLine());
            oszlopok = Convert.ToInt32(sr.ReadLine());
            string[] egysor = new string[oszlopok];

            for (int sor = 1; sor <= sorok; sor++)
            {
                egysor = sr.ReadLine().Split(' ');
                for (int oszlop = 1; oszlop <= oszlopok; oszlop++)
                    melyseg[sor, oszlop] = Convert.ToInt32(egysor[oszlop - 1]);
            }
            sr.Close();
        }
    }
}
