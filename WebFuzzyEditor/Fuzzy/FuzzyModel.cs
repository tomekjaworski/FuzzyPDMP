using System;
using System.Collections.Generic;

namespace WebFuzzyEditor.Fuzzy
{
    public class FuzzyModel
    {
        public Guid ID { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public Board Board { get; set; }


        public List<FuzzyRule> Rules { get; set; }
        public bool IsValid => this.InternalValidateModel();

        private FuzzyModel()
        {
            this.ID = Guid.NewGuid();
            this.Rules = new List<FuzzyRule>();
            this.Board = null;
        }


        public FuzzyModel(string name, string description)
            :this()
        {
            this.Name  = name;
            this.Description = description;
        }

        public FuzzyModel Clone()
        {
            FuzzyModel copy = new FuzzyModel()
            {
                Name = this.Name,
                Description = this.Description
            };

            foreach(FuzzyRule rule in this.Rules)
            {
                FuzzyRule rule_copy = rule.Clone();
                copy.AddRule(rule_copy);
            }
            return copy;
        }

        public bool RemoveRule(FuzzyRule rule)
        {
            if (!this.Rules.Contains(rule))
                return false;


            this.Rules.Remove(rule);
            //todo: aktualizacja reguł

            return true;
        }


        public FuzzyRule AddRule(FuzzyRule rule)
        {
            this.Rules.Add(rule);
            return rule;
        }



        private bool InternalValidateModel()
        {
            if (this.Rules.Count == 0)
                return false;

            foreach (var rule in this.Rules)
                if (!rule.IsValid)
                    return false;
            return true;
        }


        public override string ToString() => $"{Name}:{Description}";

    }
}

