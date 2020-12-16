namespace WebFuzzyEditor.Fuzzy
{
    public class NamedParameter
    {
        private double value;

        public string ShortName { get; set; }

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

        public FuzzyVariable ParentVariable { get; set; }
        public FuzzyValue ParentValue { get; set; }

        public NamedParameter()
        {
            //
        }

        public NamedParameter(string shortName, double defaultValue,
            FuzzyVariable parentVariable, FuzzyValue parentValue)
        {
            this.ShortName = shortName;
            this.Value = defaultValue;

            this.ParentValue = parentValue;
            this.ParentVariable = parentVariable;
        }

        public override string ToString() => string.Format("{0} [{1:N4}; {2}]",
            this.FullName, this.Value,
            this.IsValid ? "valid" : "not valid"
            );
    }
}


