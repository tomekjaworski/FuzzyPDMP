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
            if (fuzzyValue == null)
                throw new NullReferenceException("fuzzyValue");


            FuzzySubexpression fs;
            if (this.conclusion.Count == 0)
                fs = new FuzzySubexpression(null, fuzzyValue);
            else
                fs = new FuzzySubexpression(FuzzyConjunctionType.And, fuzzyValue);

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

        public FuzzySubexpression AddPremise(FuzzyConjunctionType conjunction, FuzzyValue fuzzyValue) 
            => this.AddPremiseImpl(conjunction, fuzzyValue);

        public FuzzySubexpression AddPremise(FuzzyValue fuzzyValue) 
            => this.AddPremiseImpl(null, fuzzyValue);


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
            return $"IF {p} THEN {c}";
        }
    }

    //public class FuzzyRuleBase
    //{
    //    public List<FuzzyRule> Rules { get; }

    //    public FuzzyRuleBase()
    //    {
    //        this.Rules = new List<FuzzyRule>();
    //    }
    //}

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
        public FuzzyConjunctionType? ConjunctionType { get; set; }

        public FuzzyValue Value { get; set; }
        public FuzzyVariable Variable => this.Value?.Variable;

        public FuzzySubexpression(FuzzyConjunctionType? fuzzyConjunctionType, FuzzyValue fuzzyValue)
        {
            this.ConjunctionType = fuzzyConjunctionType;
            this.Value = fuzzyValue;
        }

        public override string ToString() => 
            ConjunctionType == null ?
            $"[{Variable.Name} IS {Value.Name}]" :
            $"{ConjunctionType} [{Variable.Name} IS {Value.Name}]";
    }
}


