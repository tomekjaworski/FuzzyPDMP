using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp1.Fuzzy
{
    public class FuzzyRule
    {
        public Guid ID { get; set; }

        private List<FuzzySubexpression> premise;
        private List<FuzzySubexpression> conclusion;

        public List<FuzzySubexpression> Premise => this.premise;

        public List<FuzzySubexpression> Conclusion => this.conclusion;

        public FuzzyRule()
        {
            this.ID = Guid.NewGuid();
            this.premise = new List<FuzzySubexpression>();
            this.conclusion = new List<FuzzySubexpression>();
        }

        public FuzzySubexpression AddConclusion(FuzzyValue fuzzyValue)
        {
            FuzzySubexpression fs;
            if (this.conclusion.Count == 0)
                fs = new FuzzySubexpression( FuzzyConjunctionType.None, fuzzyValue);
            else
                fs = new FuzzySubexpression(FuzzyConjunctionType.And, fuzzyValue);

            this.conclusion.Add(fs);
            return fs;
        }

        public FuzzySubexpression AddEmptyConclusion()
        {
            FuzzySubexpression fs;
            if (this.conclusion.Count == 0)
                fs = new FuzzySubexpression(FuzzyConjunctionType.None, null);
            else
                fs = new FuzzySubexpression(FuzzyConjunctionType.And, null);

            this.conclusion.Add(fs);
            return fs;
        }


        public bool RemoveConclusion(FuzzySubexpression subexpression)
        {
            if (!this.conclusion.Contains(subexpression))
                return false;

            this.conclusion.Remove(subexpression);
            
            // W pierwszej konkluzji usuń spójnik; nie ma on w takim przypadku sensu.
            if (this.conclusion.Count > 0 && this.conclusion[0].ConjunctionType != FuzzyConjunctionType.None)
                this.conclusion[0].ConjunctionType = FuzzyConjunctionType.None;

            return true;
        }

        private FuzzySubexpression AddPremiseImpl(FuzzyConjunctionType? conjunction, FuzzyValue fuzzyValue)
        {
            FuzzySubexpression subexpr;
            if (this.premise.Count == 0)
                subexpr = new FuzzySubexpression( FuzzyConjunctionType.None, fuzzyValue);
            else
                subexpr = new FuzzySubexpression(conjunction ?? FuzzyConjunctionType.And, fuzzyValue);

            this.premise.Add(subexpr);
            return subexpr;
        }

        public FuzzySubexpression AddPremise(FuzzyConjunctionType conjunction, FuzzyValue fuzzyValue = null) 
            => this.AddPremiseImpl(conjunction, fuzzyValue);

        public FuzzySubexpression AddPremise(FuzzyValue fuzzyValue) 
            => this.AddPremiseImpl(null, fuzzyValue);

        public FuzzySubexpression AddEmptyPremise()
            => this.AddPremiseImpl(null, null);

        public bool RemovePremise(FuzzySubexpression subexpression)
        {
            if (!this.premise.Contains(subexpression))
                return false;

            this.premise.Remove(subexpression);

            // W pierwszej konkluzji usuń spójnik; nie ma on w takim przypadku sensu.
            if (this.premise.Count > 0 && this.premise[0].ConjunctionType != FuzzyConjunctionType.None)
                this.premise[0].ConjunctionType = FuzzyConjunctionType.None;

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
}


