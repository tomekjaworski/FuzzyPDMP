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

        public bool IsValid => this.InternalValidateRule();


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
                fs = new FuzzySubexpression( FuzzyConnectiveType.None, fuzzyValue);
            else
                fs = new FuzzySubexpression(FuzzyConnectiveType.And, fuzzyValue);

            this.conclusion.Add(fs);
            return fs;
        }

        public FuzzySubexpression AddEmptyConclusion()
        {
            FuzzySubexpression fs;
            if (this.conclusion.Count == 0)
                fs = new FuzzySubexpression(FuzzyConnectiveType.None, null);
            else
                fs = new FuzzySubexpression(FuzzyConnectiveType.And, null);

            this.conclusion.Add(fs);
            return fs;
        }


        public bool RemoveConclusion(FuzzySubexpression subexpression)
        {
            if (!this.conclusion.Contains(subexpression))
                return false;

            this.conclusion.Remove(subexpression);
            
            // W pierwszej konkluzji usuń spójnik; nie ma on w takim przypadku sensu.
            if (this.conclusion.Count > 0 && this.conclusion[0].ConnectiveType != FuzzyConnectiveType.None)
                this.conclusion[0].ConnectiveType = FuzzyConnectiveType.None;

            return true;
        }

        private FuzzySubexpression AddPremiseImpl(FuzzyConnectiveType? conjunction, FuzzyValue fuzzyValue)
        {
            FuzzySubexpression subexpr;
            if (this.premise.Count == 0)
                subexpr = new FuzzySubexpression( FuzzyConnectiveType.None, fuzzyValue);
            else
                subexpr = new FuzzySubexpression(conjunction ?? FuzzyConnectiveType.And, fuzzyValue);

            this.premise.Add(subexpr);
            return subexpr;
        }

        public FuzzySubexpression AddPremise(FuzzyConnectiveType conjunction, FuzzyValue fuzzyValue = null) 
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
            if (this.premise.Count > 0 && this.premise[0].ConnectiveType != FuzzyConnectiveType.None)
                this.premise[0].ConnectiveType = FuzzyConnectiveType.None;

            return true;

        }


        public FuzzyRule CreateCopy()
        {
            FuzzyRule copy = new FuzzyRule();
            foreach (FuzzySubexpression fs in this.premise)
            {
                FuzzySubexpression fs_copy = fs.CreateCopy();
                copy.premise.Add(fs_copy);
            }
            foreach (FuzzySubexpression fs in this.conclusion)
            {
                FuzzySubexpression fs_copy = fs.CreateCopy();
                copy.conclusion.Add(fs_copy);
            }
            return copy;
        }



        private bool InternalValidateRule()
        {
            if (this.premise.Count == 0)
                return false;
            if (this.conclusion.Count == 0)
                return false;

            foreach (FuzzySubexpression expr in this.premise)
                if (!expr.IsValid)
                    return false;
            foreach (FuzzySubexpression expr in conclusion)
                if (!expr.IsValid)
                    return false;

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

        public string ToHtmlString()
        {
            string p = string.Join(" ", this.Premise.Select(expr => $"{expr.ToHtmlString()}"));
            string c = string.Join(" ", this.Conclusion.Select(expr => $"{expr.ToHtmlString()}"));
            p = (p == "") ? "..." : p;
            c = (c == "") ? "..." : c;
            return $"<span class=\"font-weight-bold\" style=\"color:#0000FF\">Jeżeli</span> {p} <span class=\"font-weight-bold\" style=\"color:#0000FF\">to wtedy</span> {c}.";
        }
    }
}


