using System.ComponentModel;

namespace WebFuzzyEditor.Fuzzy
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


