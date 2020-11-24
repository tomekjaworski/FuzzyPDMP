using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Linq;
using System.Runtime.InteropServices.ComTypes;

namespace BlazorApp1.Fuzzy
{

    public class FuzzyValue
    {
        public Guid ID { get; set; }

        private MembershipFunctionFamily membership_family;
        private Dictionary<MembershipFunctionFamily, OrderedDictionary> parameters;


        public string Name { get; set; }
        public string Description { get; set; }
        public FuzzyVariable Variable { get; set; }

        [JsonIgnore]
        public NamedParameter[] MembershipParameters => this.parameters[this.membership_family].Values.OfType<NamedParameter>().ToArray();

        public Dictionary<MembershipFunctionFamily, OrderedDictionary> AllParameters => this.parameters;

        [JsonConverter(typeof(StringEnumConverter))] 
        public MembershipFunctionFamily MembershipType => this.membership_family;

        public override string ToString() => $"{Name}: {Description}";

        


        public FuzzyValue(FuzzyVariable fuzzyVariable, string name, string description, MembershipFunctionFamily membershipFamily)
        {
            this.ID = Guid.NewGuid();

            this.Variable = fuzzyVariable;

            this.Name = name;
            this.Description = description;

            this.parameters = new Dictionary<MembershipFunctionFamily, OrderedDictionary>();
            this.SetMembershipType(membershipFamily);
        }

        public NamedParameter GetParameter(string parameterName)
        {
            OrderedDictionary pars = this.parameters[this.membership_family];
            if (!pars.Contains(parameterName))
                return null;

            return pars[parameterName] as NamedParameter;
        }

        public bool ValidateCrispParameters()
        {
            OrderedDictionary pars = this.parameters[this.membership_family];
            if (pars.Count == 0)
                return true;

            if (this.membership_family == MembershipFunctionFamily.Trapezoidal)
            {
                NamedParameter sl = pars["SuppL"] as NamedParameter; // support left
                NamedParameter sr = pars["SuppR"] as NamedParameter; // support right
                NamedParameter kl = pars["KernL"] as NamedParameter; // kernel left
                NamedParameter kr = pars["KernR"] as NamedParameter; // kernel right

                sl.IsValid =
                    sl.Value <= kl.Value &&
                    sl.Value < kr.Value &&
                    sl.Value < sr.Value;

                kl.IsValid =
                    kl.Value >= sl.Value &&
                    kl.Value <= kr.Value &&
                    kl.Value < sr.Value;

                kr.IsValid =
                    kr.Value > sl.Value &&
                    kr.Value >= kl.Value &&
                    kr.Value <= sr.Value;

                sr.IsValid =
                    sr.Value > sl.Value &&
                    sr.Value > kl.Value &&
                    sr.Value >= kr.Value;

                return sl.IsValid && kl.IsValid && kr.IsValid && sr.IsValid;
            }

            return true;
        }

        internal void SetMembershipType(MembershipFunctionFamily value)
        {
            this.membership_family = value;
            if (!this.parameters.ContainsKey(value))
            {
                this.parameters[value] = new OrderedDictionary();

                // trapezy
                if (value == MembershipFunctionFamily.Trapezoidal)
                {
                    NamedParameter support_left = new NamedParameter("SuppL", 1.0, this.Variable, this);
                    NamedParameter kernel_left = new NamedParameter("KernL", 2.0, this.Variable, this);
                    NamedParameter kernel_right = new NamedParameter("KernR", 3.0, this.Variable, this);
                    NamedParameter support_right = new NamedParameter("SuppR", 4.0, this.Variable, this);

                    this.parameters[value].Add(support_left.ShortName, support_left);
                    this.parameters[value].Add(kernel_left.ShortName, kernel_left);
                    this.parameters[value].Add(kernel_right.ShortName, kernel_right);
                    this.parameters[value].Add(support_right.ShortName, support_right);
                }
            }
        }
    }
}


