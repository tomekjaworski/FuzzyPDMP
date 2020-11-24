using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.Linq;

namespace BlazorApp1.Fuzzy
{
    public class FuzzySubexpression
    {
        private FuzzyValue fuzzy_value;
        private FuzzyVariable fuzzy_variable;

        [JsonConverter(typeof(StringEnumConverter))]
        public FuzzyConjunctionType ConjunctionType { get; set; }

        public FuzzyValue Value {
            get => this.fuzzy_value;
            set {
                this.fuzzy_value = value;
                this.fuzzy_variable = value?.Variable;
                //this.VariableHolder = value.Variable;
            }
        }

        public FuzzyVariable Variable {
            get => this.fuzzy_variable;
            set {
                if (value != this.fuzzy_variable)
                {
                    this.fuzzy_variable = value;
                    this.fuzzy_value = value.Values.FirstOrDefault();
                }
            }
        }

        public FuzzySubexpression(FuzzyConjunctionType fuzzyConjunctionType, FuzzyValue fuzzyValue)
        {
            this.ConjunctionType = fuzzyConjunctionType;
            //this.Value = fuzzyValue;

            this.fuzzy_value = fuzzyValue;
            this.fuzzy_variable = fuzzyValue?.Variable;
        }

        public override string ToString() => 
            this.ConjunctionType == FuzzyConjunctionType.None ?
            $"[{this.Value?.Variable?.Name ?? "..." } IS {this.Value?.Name ?? "..."}]" :
            $"{this.ConjunctionType} [{this.Value?.Variable?.Name ?? "..."} IS {this.Value?.Name ?? "..." }]";
    }
}


