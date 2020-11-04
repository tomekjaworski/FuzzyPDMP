namespace BlazorApp1.Fuzzy
{
    public class ModelProvider
    {
        #region static
        private static ModelProvider mp;
        public static ModelProvider Data => mp;

        static ModelProvider()
        {
            mp = new ModelProvider();
        }
        #endregion

        private Model model;
        public Model Model => this.model;

        private ModelProvider()
        {
            this.model = new Model();

            var var1 = this.model.AddVariable("Nazwa 1", "Opis zmiennej Nazwa I");

            FuzzyValue val1, val2, val3;
            val1 = var1.AddValue("Mało", "Opis wartości Mało");
            val2 = var1.AddValue("Średnio", "Opis wartości Średnio");
            val3 = var1.AddValue("Dużo", "Opis wartości Dużo");
            var1.MembershipType = MembershipFunctionFamily.Trapezoidal;
            var1.Minimum.Value = 10;
            var1.Maximum.Value = 100;

            val1.GetParameter("SuppL").Value = 0;
            val1.GetParameter("KernL").Value = 0;
            val1.GetParameter("KernR").Value = 25;
            val1.GetParameter("SuppR").Value = 40;

            val2.GetParameter("SuppL").Value = 25;
            val2.GetParameter("KernL").Value = 40;
            val2.GetParameter("KernR").Value = 55;
            val2.GetParameter("SuppR").Value = 70;

            val3.GetParameter("SuppL").Value = 55;
            val3.GetParameter("KernL").Value = 70;
            val3.GetParameter("KernR").Value = 110;
            val3.GetParameter("SuppR").Value = 110;


            //val1 = var2.AddValue("Zimno", "Opis wartości Zimno");
            //val2 = var2.AddValue("Ciepło", "Opis wartości Ciepło");
            //val3 = var2.AddValue("Gorąco", "Opis wartości Gorąco");
            //var2.MembershipType = MembershipFunctionFamily.Trapezoidal;
            var var3 = this.model.AddVariable("Nazwa 3", "Opis zmiennej Nazwa III");

            val1 = var3.AddValue("Negatywny", "Opis wartości Negatywny");
            val2 = var3.AddValue("Zerowy", "Opis wartości Zerowy");
            val3 = var3.AddValue("Pozytywny", "Opis wartości Pozytywny");
            var3.MembershipType = MembershipFunctionFamily.Trapezoidal;
            var3.Minimum.Value = -40;
            var3.Maximum.Value = 40;


            val1.GetParameter("SuppL").Value = -30;
            val1.GetParameter("KernL").Value = -30;
            val1.GetParameter("KernR").Value = -20;
            val1.GetParameter("SuppR").Value = 0;

            val2.GetParameter("SuppL").Value = -20;
            val2.GetParameter("KernL").Value = 0;
            val2.GetParameter("KernR").Value = 0;
            val2.GetParameter("SuppR").Value = 20;

            val3.GetParameter("SuppL").Value = 0;
            val3.GetParameter("KernL").Value = 20;
            val3.GetParameter("KernR").Value = 41;
            val3.GetParameter("SuppR").Value = 41;


        }
    }
}
