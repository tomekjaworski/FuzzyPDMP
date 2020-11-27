using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System;
using System.Linq;

namespace BlazorApp1.Fuzzy
{
    public class FuzzySubexpression
    {
        private FuzzyValue fuzzy_value;
        private FuzzyVariable fuzzy_variable;

        [JsonConverter(typeof(StringEnumConverter))]
        public FuzzyConnectiveType ConnectiveType { get; set; }

        public FuzzyValue Value {
            get => this.fuzzy_value;
            set {
                this.fuzzy_value = value;
                this.fuzzy_variable = value?.Variable;
                //this.VariableHolder = value.Variable;
            }
        }

        public FuzzyVariable Variable {
            get => this.fuzzy_variable;
            set {
                if (value != this.fuzzy_variable)
                {
                    this.fuzzy_variable = value;
                    this.fuzzy_value = value.Values.FirstOrDefault();
                }
            }
        }

        public bool IsValid => this.InternalValidate();


        public FuzzySubexpression(FuzzyConnectiveType fuzzyConnectiveType, FuzzyValue fuzzyValue)
        {
            this.ConnectiveType = fuzzyConnectiveType;
            //this.Value = fuzzyValue;

            this.fuzzy_value = fuzzyValue;
            this.fuzzy_variable = fuzzyValue?.Variable;
        }


        private bool InternalValidate()
        {
            if (this.fuzzy_value == null)
                return false;
            if (this.fuzzy_variable == null)
                return false;
            if (!this.fuzzy_variable.IsValid)
                return false;
            if (!this.fuzzy_value.IsValid)
                return false;
            return true;
        }

        public override string ToString() => 
            this.ConnectiveType == FuzzyConnectiveType.None ?
            $"[{this.Value?.Variable?.Name ?? "..." } IS {this.Value?.Name ?? "..."}]" :
            $"{this.ConnectiveType} [{this.Value?.Variable?.Name ?? "..."} IS {this.Value?.Name ?? "..." }]";

        public string ToHtmlString()
        {
            string sconn = "???";
            if (this.ConnectiveType == FuzzyConnectiveType.And)
                sconn = "oraz";
            if (this.ConnectiveType == FuzzyConnectiveType.Or)
                sconn = "lub";

            if (this.ConnectiveType == FuzzyConnectiveType.None)
                return $"{this.Value?.Variable?.Name ?? "..." } <span style=\"color:#008000\">jest</span> {this.Value?.Name ?? "..."}";
            else
                return $"<span class=\"\" style=\"color:#0000FF\">{sconn}</span> {this.Value?.Variable?.Name ?? "..."} <span style=\"color:#008000\">jest</span> {this.Value?.Name ?? "..." }";
        }
    }
}


