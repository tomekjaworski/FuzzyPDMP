using System.ComponentModel;

namespace BlazorApp1.Fuzzy
{
    public enum MembershipFunctionFamily
    {
        [Description("Nieokreślone/brak funkcji przynależności")]
        Unspecified,

        [Description("Trójkątne/trapezowe")]
        Trapezoidal
    }
}
