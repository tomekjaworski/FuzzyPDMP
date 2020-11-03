using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Linq;
using System.Runtime.InteropServices.ComTypes;

namespace BlazorApp1.Fuzzy
{

    public class FuzzyValue
    {
        private MembershipFunctionFamily membership_family;
        private Dictionary<MembershipFunctionFamily, OrderedDictionary> parameters;


        public string Name { get; set; }
        public string Description { get; set; }
        public FuzzyVariable Variable { get; set; }

        public CrispParameter[] Parameters => this.parameters[this.membership_family].Values.OfType<CrispParameter>().ToArray();

        public override string ToString() => $"{Name}: {Description}";

        


        public FuzzyValue(FuzzyVariable fuzzyVariable, string name, string description, MembershipFunctionFamily membershipFamily)
        {
            this.Variable = fuzzyVariable;

            this.Name = name;
            this.Description = description;

            this.parameters = new Dictionary<MembershipFunctionFamily, OrderedDictionary>();
            this.SetMembershipType(membershipFamily);
        }

        internal void ValidateCrispParameters()
        {
            OrderedDictionary pars = this.parameters[this.membership_family];
            if (pars.Count == 0)
                return;

            if (this.membership_family == MembershipFunctionFamily.Trapezoidal)
            {
                CrispParameter sl = pars["SuppL"] as CrispParameter; // support left
                CrispParameter sr = pars["SuppR"] as CrispParameter; // support right
                CrispParameter kl = pars["KernL"] as CrispParameter; // kernel left
                CrispParameter kr = pars["KernR"] as CrispParameter; // kernel right

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
            }
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
                    CrispParameter support_left = new CrispParameter("SuppL", 1.0, this.Variable, this);
                    CrispParameter kernel_left = new CrispParameter("KernL", 2.0, this.Variable, this);
                    CrispParameter kernel_right = new CrispParameter("KernR", 3.0, this.Variable, this);
                    CrispParameter support_right = new CrispParameter("SuppR", 4.0, this.Variable, this);

                    this.parameters[value].Add(support_left.ShortName, support_left);
                    this.parameters[value].Add(kernel_left.ShortName, kernel_left);
                    this.parameters[value].Add(kernel_right.ShortName, kernel_right);
                    this.parameters[value].Add(support_right.ShortName, support_right);
                }
            }
        }
    }
}


