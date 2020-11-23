using Newtonsoft.Json;
using System;
using System.Collections.Specialized;
using System.IO;
using System.Text;

namespace BlazorApp1.Fuzzy
{

    public class BoardProvider
    {
        #region static
        private static BoardProvider mp;
        public static BoardProvider Provider => mp;
        public static Board Model => mp.board;

        static BoardProvider()
        {
            mp = new BoardProvider();
        }
        #endregion

        private Board board;
        string previous_json_document;



        private BoardProvider()
        {
            this.board = new Board();

            //this.CreateDummyModel();
            //this.StoreModel();
            //this.StoreModel();
            //this.CreateDummyModel();
            //this.StoreModel();
            //this.StoreModel();
            this.LoadBoard();
        }

        private void CreateDummyBoard()
        {
            this.board = new Board();

            FuzzyModel fm = board.AddModel("Nazwa", "Opis modelu");

            var var1 = this.board.AddVariable("Nazwa 1", "Opis zmiennej Nazwa I");

            FuzzyValue var1_val1, var1_val2, var1_val3;
            var1_val1 = var1.AddValue("Mało", "Opis wartości Mało");
            var1_val2 = var1.AddValue("Średnio", "Opis wartości Średnio");
            var1_val3 = var1.AddValue("Dużo", "Opis wartości Dużo");
            var1.MembershipType = MembershipFunctionFamily.Trapezoidal;
            var1.Minimum.Value = 10;
            var1.Maximum.Value = 100;

            var1_val1.GetParameter("SuppL").Value = 0;
            var1_val1.GetParameter("KernL").Value = 0;
            var1_val1.GetParameter("KernR").Value = 25;
            var1_val1.GetParameter("SuppR").Value = 40;

            var1_val2.GetParameter("SuppL").Value = 25;
            var1_val2.GetParameter("KernL").Value = 40;
            var1_val2.GetParameter("KernR").Value = 55;
            var1_val2.GetParameter("SuppR").Value = 70;

            var1_val3.GetParameter("SuppL").Value = 55;
            var1_val3.GetParameter("KernL").Value = 70;
            var1_val3.GetParameter("KernR").Value = 110;
            var1_val3.GetParameter("SuppR").Value = 110;


            //val1 = var2.AddValue("Zimno", "Opis wartości Zimno");
            //val2 = var2.AddValue("Ciepło", "Opis wartości Ciepło");
            //val3 = var2.AddValue("Gorąco", "Opis wartości Gorąco");
            //var2.MembershipType = MembershipFunctionFamily.Trapezoidal;
            var var2 = this.board.AddVariable("Nazwa 3", "Opis zmiennej Nazwa III");

            FuzzyValue var2_val1, var2_val2, var2_val3;
            var2_val1 = var2.AddValue("Negatywny", "Opis wartości Negatywny");
            var2_val2 = var2.AddValue("Zerowy", "Opis wartości Zerowy");
            var2_val3 = var2.AddValue("Pozytywny", "Opis wartości Pozytywny");
            var2.MembershipType = MembershipFunctionFamily.Trapezoidal;
            var2.Minimum.Value = -40;
            var2.Maximum.Value = 40;


            var2_val1.GetParameter("SuppL").Value = -41;
            var2_val1.GetParameter("KernL").Value = -41;
            var2_val1.GetParameter("KernR").Value = -20;
            var2_val1.GetParameter("SuppR").Value = 0;

            var2_val2.GetParameter("SuppL").Value = -20;
            var2_val2.GetParameter("KernL").Value = 0;
            var2_val2.GetParameter("KernR").Value = 0;
            var2_val2.GetParameter("SuppR").Value = 20;

            var2_val3.GetParameter("SuppL").Value = 0;
            var2_val3.GetParameter("KernL").Value = 20;
            var2_val3.GetParameter("KernR").Value = 41;
            var2_val3.GetParameter("SuppR").Value = 41;


            //
            FuzzySubexpression _feci;

            FuzzyRule r1 = fm.AddRule();
            _ = r1.AddConclusion(var2_val1);
            _ = r1.AddPremise(var1_val1);
            _feci = r1.AddPremise(var1_val2);
            _feci = r1.AddPremise(FuzzyConjunctionType.And, var1_val2);
            _feci = r1.AddPremise(FuzzyConjunctionType.Or, var2_val3);

            FuzzyRule r2 = fm.AddRule();
            r2.AddConclusion(var2_val2);
            r2.AddConclusion(var2_val3);

            FuzzyRule r3 = fm.AddRule();
            _feci = r3.AddPremise(var1_val1);
            _feci = r3.AddPremise(FuzzyConjunctionType.And, var1_val2);
            _feci = r3.AddPremise(FuzzyConjunctionType.Or, var2_val3);

            FuzzyRule r4 = fm.AddRule();
            _ = r4.AddPremise(var2_val3);
            _ = r4.AddConclusion(var1_val3);
            _ = r4.AddEmptyConclusion();


        }

        internal void LoadBoard()
        {
            var settings = new JsonSerializerSettings()
            {
                PreserveReferencesHandling = PreserveReferencesHandling.All,
                TypeNameAssemblyFormatHandling = TypeNameAssemblyFormatHandling.Simple,
                TypeNameHandling = TypeNameHandling.All,
            };

            try
            {
                Console.Write("Wczytywnie modelu: ");
                string json = File.ReadAllText(Path.Combine("data", "model.json"), Encoding.UTF8);
                this.board = JsonConvert.DeserializeObject<Board>(json, settings);

                Console.WriteLine("Ok.");

            } catch(Exception ex)
            {
                Console.WriteLine($"Błąd: {ex}");
            }

            /*
            // Aktualizacja
            this.board.Models.Add(new FuzzyModel(this.board));
            
            var fm = this.board.Models[0];
            fm.Rules.AddRange(this.board.Rules);
            this.board.Rules.Clear();
            this.StoreBoard();
            */

        }

        internal void StoreBoard()
        {

            var settings = new JsonSerializerSettings()
            {
                PreserveReferencesHandling = PreserveReferencesHandling.All,
                TypeNameAssemblyFormatHandling = TypeNameAssemblyFormatHandling.Simple,
                TypeNameHandling = TypeNameHandling.All,
            };

            try
            {
                Console.Write("Zapis modelu: ");
                string current_json_document = JsonConvert.SerializeObject(this.board, Formatting.Indented, settings);
                if (current_json_document == previous_json_document)
                {
                    Console.WriteLine("brak zmian; zapis pominięty.");
                    return;
                }

                Directory.CreateDirectory("data");
                string[] file_names = new string[] {
                    "model.json",
                    $"model-{DateTime.Now.ToString("yyyy-MM-dd_HH-mm-ss")}.json"
                };

                foreach (string file_name in file_names)
                    File.WriteAllText(Path.Combine("data", file_name), 
                        current_json_document, 
                        Encoding.UTF8);

                previous_json_document = current_json_document;
                Console.WriteLine("Ok.");

            }catch (Exception ex)
            {
                Console.WriteLine($"Zapis modelu: Błąd podczas zapisu pliku: {ex}");
            }


        }
    }
}

