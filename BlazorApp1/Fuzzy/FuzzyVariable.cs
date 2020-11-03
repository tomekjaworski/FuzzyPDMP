using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp1.Fuzzy
{
    public class FuzzyVariable
    {
        private List<FuzzyValue> values;

        public string Name { get; set; }
        public string Description { get; set; }

        public FuzzyValue[] Values => this.values.ToArray();

        public override string ToString() => $"{Name}: {Description}";


        public FuzzyVariable()
        {
            this.values = new List<FuzzyValue>();
        }

        public FuzzyValue AddValue(string name, string description)
        {
            FuzzyValue val = new FuzzyValue() { Name = name, Description = description, Variable = this };
            this.values.Add(val);
            return val;
        }

        internal bool RemoveValue(FuzzyValue value)
        {
            if (!this.values.Contains(value))
                return false;

            this.values.Remove(value);
            // todo: aktualziac reguł

            return true;
        }
    }


    public class FuzzyValue
    {
        public string Name { get; set; }
        public string Description { get; set; }
        public FuzzyVariable Variable { get; set; }

        public override string ToString() => $"{Name}: {Description}";
    }
}
