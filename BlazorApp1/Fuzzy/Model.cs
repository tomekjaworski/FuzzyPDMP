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
            @var.ValidateCrispParameters();
            return @var;
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
}
