using System.ComponentModel;

namespace BlazorApp1.Fuzzy
{
    public enum FuzzyConnectiveType
    {
        None,

        [Description("oraz")]
        And,
        
        [Description("lub")]
        Or,
    }
}


