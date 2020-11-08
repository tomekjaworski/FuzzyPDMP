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
        private List<FuzzyRule> rules;

        public List<FuzzyVariable> Variables => this.variables;

        public List<FuzzyRule> Rules => this.rules;


        public Model()
        {
            this.variables = new List<FuzzyVariable>();
            this.rules = new List<FuzzyRule>();

        }

        public FuzzyVariable AddVariable(string name, string description)
        {
            FuzzyVariable @var = new FuzzyVariable() { Name = name, Description = description };
            this.variables.Add(@var);
            if (@var.ValidateCrispParameters())
                @var.ChartHolder.UpdateChart();
            
            return @var;
        }

        public bool RemoveRule(FuzzyRule rule)
        {
            if (!this.rules.Contains(rule))
                return false;


            this.rules.Remove(rule);
            //todo: aktualizacja reguł

            return true;
        }

        public bool RemoveVariable(FuzzyVariable variable)
        {
            if (!this.variables.Contains(variable))
                return false;


            this.variables.Remove(variable);
            //todo: aktualizacja reguł

            return true;
        }

        internal FuzzyRule AddRule()
        {
            FuzzyRule fr = new FuzzyRule();
            this.rules.Add(fr);
            return fr;
        }

    }
}
