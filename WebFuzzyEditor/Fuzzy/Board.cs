using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WebFuzzyEditor.Fuzzy
{
    public class Board
    {
        private List<FuzzyVariable> variables;
        private List<FuzzyModel> models;

        public List<FuzzyVariable> Variables => this.variables;
        public List<FuzzyModel> Models => this.models;

        private FuzzyModel selected_model;
        [JsonIgnore]
        public FuzzyModel SelectedModel {
            set => this.selected_model = value;
            get {
                if (this.selected_model == null)
                    this.selected_model = this.models.FirstOrDefault();
                return this.selected_model;
            }
        }


        public Board()
        {
            this.selected_model = null;
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

        public FuzzyVariable AddVariable(FuzzyVariable variable)
        {
            this.variables.Add(variable);
            if (variable.ValidateCrispParameters())
                variable.ChartHolder.UpdateChart();

            return variable;
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

        public bool RemoveModel(FuzzyModel model)
        {

            if (!this.models.Contains(model))
                return false;


            this.models.Remove(model);
            if (this.selected_model == model)
                this.selected_model = null;
            //todo: aktualizacja reguł

            return true;
        }

        public FuzzyModel AddModel(FuzzyModel model)
        {
            model.Board = this;
            this.models.Add(model);
            return model;
        }

    }
}
