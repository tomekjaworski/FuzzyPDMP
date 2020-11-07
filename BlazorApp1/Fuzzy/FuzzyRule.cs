using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp1.Fuzzy
{
    public class FuzzyRule
    {
        private List<FuzzySubexpression> premise;
        private List<FuzzySubexpression> conclusion;

        public FuzzySubexpression[] Premise => this.premise.ToArray();

        public FuzzySubexpression[] Conclusion => this.conclusion.ToArray();

        public FuzzyRule()
        {
            this.premise = new List<FuzzySubexpression>();
            this.conclusion = new List<FuzzySubexpression>();
        }

        public FuzzySubexpression AddConclusion(FuzzyValue fuzzyValue)
        {
            FuzzySubexpression fs;
            if (this.conclusion.Count == 0)
                fs = new FuzzySubexpression(null, fuzzyValue);
            else
                fs = new FuzzySubexpression(FuzzyConjunctionType.And, fuzzyValue);

            this.conclusion.Add(fs);
            return fs;
        }

        public FuzzySubexpression AddEmptyConclusion()
        {
            FuzzySubexpression fs;
            if (this.conclusion.Count == 0)
                fs = new FuzzySubexpression(null, null);
            else
                fs = new FuzzySubexpression(FuzzyConjunctionType.And, null);

            this.conclusion.Add(fs);
            return fs;
        }


        public bool RemoveConclusion(FuzzySubexpression subexpression)
        {
            if (!this.Conclusion.Contains(subexpression))
                return false;

            this.conclusion.Remove(subexpression);
            if (this.conclusion.Count > 0 && this.conclusion[0].ConjunctionType != null)
                this.conclusion[0].ConjunctionType = null;

            return true;
        }

        private FuzzySubexpression AddPremiseImpl(FuzzyConjunctionType? conjunction, FuzzyValue fuzzyValue)
        {
            if (conjunction == null)
            {
                // już istnieje pierwsza/bezspójnikowa przesłanka
                if (this.Premise.Where(x => x.ConjunctionType == null).Any())
                    return null;

                FuzzySubexpression subexpr = new FuzzySubexpression(conjunction, fuzzyValue);
                this.premise.Insert(0, subexpr);
                return subexpr;
            }
            else
            {
                FuzzySubexpression subexpr = new FuzzySubexpression(conjunction, fuzzyValue);
                this.premise.Add(subexpr);
                return subexpr;
            }
        }

        public FuzzySubexpression AddPremise(FuzzyConjunctionType conjunction, FuzzyValue fuzzyValue = null) 
            => this.AddPremiseImpl(conjunction, fuzzyValue);

        public FuzzySubexpression AddPremise(FuzzyValue fuzzyValue) 
            => this.AddPremiseImpl(null, fuzzyValue);

        public FuzzySubexpression AddEmptyPremise()
            => this.AddPremiseImpl(null, null);

        public bool RemovePremise(FuzzySubexpression subexpression)
        {
            if (!this.Premise.Contains(subexpression))
                return false;

            this.premise.Remove(subexpression);
            return true;
        }


        public override string ToString()
        {
            string p = string.Join(" ", this.Premise.Select(x => $"{x}"));
            string c = string.Join(" ", this.Conclusion.Select(x => $"{x}"));
            p = (p == "") ? "..." : p;
            c = (c == "") ? "..." : c;
            return $"IF {p} THEN {c}";
        }
    }

    public enum FuzzyConjunctionType
    {
        //[Description("---")]
        //None,

        //[Description("lub/oraz")]
        //Unselected,

        [Description("oraz")]
        And,
        
        [Description("lub")]
        Or,
    }

    public class FuzzySubexpression
    {
        private FuzzyValue fuzzy_value;
        private FuzzyVariable fuzzy_variable;

        public FuzzyConjunctionType? ConjunctionType { get; set; }

        public FuzzyValue Value {
            get => this.fuzzy_value;
            set {
                this.fuzzy_value = value;
                this.fuzzy_variable = value.Variable;
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

        public FuzzySubexpression(FuzzyConjunctionType? fuzzyConjunctionType, FuzzyValue fuzzyValue)
        {
            this.ConjunctionType = fuzzyConjunctionType;
            //this.Value = fuzzyValue;

            this.fuzzy_value = fuzzyValue;
            this.fuzzy_variable = fuzzyValue?.Variable;
        }

        public override string ToString() => 
            this.ConjunctionType == null ?
            $"[{this.Value.Variable.Name} IS {this.Value.Name}]" :
            $"{this.ConjunctionType} [{this.Value.Variable.Name} IS {this.Value.Name}]";
    }
}


