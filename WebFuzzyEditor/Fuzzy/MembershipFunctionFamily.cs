using System.ComponentModel;

namespace WebFuzzyEditor.Fuzzy
{
    public enum MembershipFunctionFamily
    {
        [Description("Nieokreślone/brak funkcji przynależności")]
        Unspecified,

        [Description("Trójkątne/trapezowe")]
        Trapezoidal
    }
}
