namespace BlazorApp1.Fuzzy
{
    public class NamedParameter
    {
        private double value;

        public string ShortName { get; }

        public string FullName => ParentValue == null ? this.ShortName :
            $"{this.ParentValue.Name}::{this.ShortName}";

        public double Value {
            get => this.value;
            set {
                this.value = value;
                if (this.ParentVariable != null)
                    if (this.ParentVariable.ValidateCrispParameters())
                        this.ParentVariable.ChartHolder.UpdateChart();
            }
        }

        public bool IsValid { get; set; }

        public FuzzyVariable ParentVariable { get; }
        public FuzzyValue ParentValue { get; }

        public NamedParameter(string shortName, double defaultValue,
            FuzzyVariable parentVariable, FuzzyValue parentValue)
        {
            this.ShortName = shortName;
            this.Value = defaultValue;

            this.ParentValue = parentValue;
            this.ParentVariable = parentVariable;
        }

        public override string ToString() => $"{this.FullName} [{this.Value:N4}]";
    }
}


