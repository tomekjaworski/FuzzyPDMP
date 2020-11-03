using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BlazorApp1.Fuzzy
{
    public class Model
    {
        private List<FuzzyVariable> variables;
        public FuzzyVariable[] Variables => this.variables.ToArray();

        public Model()
        {
            this.variables = new List<FuzzyVariable>();
        }

        public FuzzyVariable AddVariable(string name, string description)
        {
            FuzzyVariable @var = new FuzzyVariable() { Name = name, Description = description };
            this.variables.Add(@var);
            return var;
        }

        public bool RemoveValue(FuzzyValue value)
        {
            if (!this.variables.Contains(value.Variable))
                return false;

            return value.Variable.RemoveValue(value);
        }

        public bool RemoveVariable(FuzzyVariable variable)
        {
            if (!this.variables.Contains(variable))
                return false;


            this.variables.Remove(variable);
            //todo: aktualizacja reguł

            return true;
        }
    }

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
