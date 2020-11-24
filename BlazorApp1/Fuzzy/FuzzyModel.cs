using System;
using System.Collections.Generic;

namespace BlazorApp1.Fuzzy
{
    public class FuzzyModel
    {
        public Guid ID { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public Board Board { get; set; }


        public List<FuzzyRule> Rules { get; set; }


        public FuzzyModel(Board board)
        {
            this.ID = Guid.NewGuid();
            this.Rules = new List<FuzzyRule>();
            this.Board = board;
        }


        public bool RemoveRule(FuzzyRule rule)
        {
            if (!this.Rules.Contains(rule))
                return false;


            this.Rules.Remove(rule);
            //todo: aktualizacja reguł

            return true;
        }


        public FuzzyRule AddRule()
        {
            FuzzyRule fr = new FuzzyRule();
            this.Rules.Add(fr);
            return fr;
        }

        public override string ToString() => $"{Name}:{Description}";

    }
}

