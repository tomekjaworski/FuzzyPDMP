using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BlazorApp1.Fuzzy
{
    public class Board
    {
        private List<FuzzyVariable> variables;
        private List<FuzzyModel> models;

        public List<FuzzyVariable> Variables => this.variables;
        public List<FuzzyModel> Models => this.models;

        public Board()
        {
            this.variables = new List<FuzzyVariable>();
            this.models = new List<FuzzyModel>();
        }

        public FuzzyVariable AddVariable(string name, string description)
        {
            FuzzyVariable @var = new FuzzyVariable() { Name = name, Description = description };
            this.variables.Add(@var);
            if (@var.ValidateCrispParameters())
                @var.ChartHolder.UpdateChart();
            
            return @var;
        }

        internal FuzzyModel GetModelBuGuid(Guid modelGuid)
        {
            return this.models.Where(x => x.ID == modelGuid).FirstOrDefault();
        }

        public bool RemoveVariable(FuzzyVariable variable)
        {
            if (!this.variables.Contains(variable))
                return false;


            this.variables.Remove(variable);
            //todo: aktualizacja reguł

            return true;
        }

        internal FuzzyModel AddModel(string modelName, string modelDescription)
        {
            FuzzyModel fm = new FuzzyModel(this) { Name = modelName, Description = modelDescription };
            this.models.Add(fm);
            return fm;
        }
    }
}
