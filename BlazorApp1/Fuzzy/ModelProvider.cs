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

            var v1 = this.model.AddVariable("Nazwa 1", "Opis zmiennej Nazwa I");
            var v2 = this.model.AddVariable("Nazwa 2", "Opis zmiennej Nazwa II");
            var v3 = this.model.AddVariable("Nazwa 1", "Opis zmiennej Nazwa III");
            var v4 = this.model.AddVariable("Nazwa 4", "Opis zmiennej Nazwa IV");

            v1.AddValue("Mało", "Opis wartości Mało");
            v1.AddValue("Średnio", "Opis wartości Średnio");
            v1.AddValue("Dużo", "Opis wartości Dużo");

            v2.AddValue("Zimno", "Opis wartości Zimno");
            v2.AddValue("Ciepło", "Opis wartości Ciepło");
            v2.AddValue("Gorąco", "Opis wartości Gorąco");


            v3.AddValue("Negatywny", "Opis wartości Negatywny");
            v3.AddValue("Zerowy", "Opis wartości Zerowy");
            v3.AddValue("Pozytywny", "Opis wartości Pozytywny");

        }

    }
}
