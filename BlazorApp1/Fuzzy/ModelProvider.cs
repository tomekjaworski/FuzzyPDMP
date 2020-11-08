namespace BlazorApp1.Fuzzy
{
    public class ModelProvider
    {
        #region static
        private static ModelProvider mp;
        public static ModelProvider Provider => mp;
        public static Model Model => mp.model;


        static ModelProvider()
        {
            mp = new ModelProvider();
        }
        #endregion

        private Model model;

        private ModelProvider()
        {
            this.model = new Model();

            var var1 = this.model.AddVariable("Nazwa 1", "Opis zmiennej Nazwa I");

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
            var var2 = this.model.AddVariable("Nazwa 3", "Opis zmiennej Nazwa III");

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

            FuzzyRule r1 = model.AddRule();
            _ = r1.AddConclusion(var2_val1);
            _ = r1.AddPremise(var1_val1);
            _feci = r1.AddPremise(var1_val2);
            _feci = r1.AddPremise(FuzzyConjunctionType.And, var1_val2);
            _feci = r1.AddPremise(FuzzyConjunctionType.Or, var2_val3);

            FuzzyRule r2 = model.AddRule();
            r2.AddConclusion(var2_val2);
            r2.AddConclusion(var2_val3);

            FuzzyRule r3 = model.AddRule();
            _feci = r3.AddPremise(var1_val1);
            _feci = r3.AddPremise(FuzzyConjunctionType.And, var1_val2);
            _feci = r3.AddPremise(FuzzyConjunctionType.Or, var2_val3);

            FuzzyRule r4 = model.AddRule();
            _ = r4.AddPremise(var2_val3);
            _ = r4.AddConclusion(var1_val3);
            _ = r4.AddEmptyConclusion();
        }
    }
}
