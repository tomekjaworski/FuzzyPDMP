using System.ComponentModel;

namespace BlazorApp1.Fuzzy
{
    public enum FuzzyConjunctionType
    {
        None,

        [Description("oraz")]
        And,
        
        [Description("lub")]
        Or,
    }
}


