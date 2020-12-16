using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace WebFuzzyEditor.Fuzzy
{
    public class FuzzyVariable
    {
        public Guid ID { get; set; }

        private List<FuzzyValue> values;

        private MembershipFunctionFamily membership_family;
        private NamedParameter dmin, dmax;


        public string Name { get; set; }
        public string Description { get; set; }

        public List<FuzzyValue> Values => this.values;

        [JsonConverter(typeof(StringEnumConverter))]
        public MembershipFunctionFamily MembershipType {
            get => this.membership_family;
            set {
                this.membership_family = value;
                foreach (var v in this.values)
                    v.SetMembershipType(value);

                this.ValidateCrispParameters();
            }
        }

        [JsonIgnore]
        public NamedParameter[] Parameters {
            get {
                List<NamedParameter> pars = new List<NamedParameter>();
                pars.AddRange(new[] { this.dmin, this.dmax });
                pars.AddRange(this.values.SelectMany(x => x.MembershipParameters.Values.OfType<NamedParameter>()));
                return pars.ToArray();
            }
        }

        public NamedParameter Minimum => this.dmin;
        public NamedParameter Maximum => this.dmax;

        [JsonIgnore]
        public ChartHolder ChartHolder { get; set; }

        public bool IsValid => this.InternalValidate();

     
        public FuzzyVariable()
        {
            this.ID = Guid.NewGuid();
            this.ResetChartHolder();

            this.values = new List<FuzzyValue>();
            this.membership_family = MembershipFunctionFamily.Trapezoidal;

            this.dmin = new NamedParameter("Dmin", 0, this, null);
            this.dmax = new NamedParameter("Dmax", 10, this, null);
            bool is_ok = this.ValidateCrispParameters();
            if (is_ok)
                this.ChartHolder.UpdateChart();
        }

        public bool ValidateCrispParameters()
        {
            // sprawdź dziedzinę
            bool is_ok = true;
            this.dmin.IsValid = this.dmax.IsValid = this.dmin.Value <= this.dmax.Value;
            is_ok &= this.dmin.IsValid;

            foreach (FuzzyValue fv in this.values)
                is_ok &= fv.ValidateCrispParameters();

            return is_ok;
        }

        internal void ResetChartHolder()
        {
            this.ChartHolder = new ChartHolder(this);
        }

        public override string ToString() => $"{Name}: {Description}";

        public FuzzyValue AddValue(string name, string description)
        {
            FuzzyValue val = new FuzzyValue(this, name, description);
            this.values.Add(val);
            val.Variable = this;

            if (this.ValidateCrispParameters())
                this.ChartHolder.UpdateChart();
            return val;
        }

        public FuzzyValue AddValue(FuzzyValue value)
        {
            Debug.Assert(value.Variable == null || value.Variable == this);
            this.values.Add(value);
            value.Variable = this;
            if (this.ValidateCrispParameters())
                this.ChartHolder.UpdateChart();
            return value;
        }

        public FuzzyVariable Clone()
        {
            FuzzyVariable var_copy = new FuzzyVariable() { Name = this.Name, Description = this.Description, MembershipType = this.MembershipType };
            var_copy.Minimum.Value = this.Minimum.Value;
            var_copy.Maximum.Value = this.Maximum.Value;

            foreach (FuzzyValue fv in this.Values)
            {
                FuzzyValue val_copy = fv.Clone();
                var_copy.AddValue(val_copy);
            }
            return var_copy;
        }

        internal bool RemoveValue(FuzzyValue value)
        {
            if (!this.values.Contains(value))
                return false;

            this.values.Remove(value);
            // todo: aktualziac reguł

            if (this.ValidateCrispParameters())
                this.ChartHolder.UpdateChart();
            return true;
        }

        private bool InternalValidate()
        {
            if (string.IsNullOrEmpty(this.Name))
                return false;
            if (string.IsNullOrEmpty(this.Description))
                return false;

            if (this.values.Count == 0)
                return false;

            if (!this.ValidateCrispParameters())
                return false;

            foreach (FuzzyValue fv in this.values)
                if (!fv.IsValid)
                    return false;

            return true;
        }

    }
}
