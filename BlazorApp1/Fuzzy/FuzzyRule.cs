using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp1.Fuzzy
{
    public class FuzzyRule
    {
        List<FuzzyExpressionChainItem> Premise { get; }
        List<FuzzyVariable> Conclusion { get; }

        public FuzzyRule()
        {
            this.Premise = new List<FuzzyExpressionChainItem>();
            this.Conclusion = new List<FuzzyVariable>();
        }
    }

    public class FuzzyRuleBase
    {
        public List<FuzzyRule> Rules { get; }

        public FuzzyRuleBase()
        {
            this.Rules = new List<FuzzyRule>();
        }
    }

    public enum FuzzyConjunctionType
    {
        [Description("---")]
        None,

        [Description("lub/oraz")]
        Unselected,

        [Description("oraz")]
        And,
        
        [Description("lub")]
        Or,
    }

    public class FuzzyExpressionChainItem
    {
        public FuzzyConjunctionType ConjunctionType { get; set; }

        public FuzzyValue Value { get; set; }
        public FuzzyVariable Variable => this.Value?.Variable;

        public FuzzyExpressionChainItem(FuzzyConjunctionType fuzzyConjunctionType, FuzzyValue fuzzyValue)
        {
            this.ConjunctionType = fuzzyConjunctionType;
            this.Value = fuzzyValue;
        }
    }
}
