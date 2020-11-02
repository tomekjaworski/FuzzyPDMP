using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp1.Fuzzy
{
    public class Variable
    {
        public string Name { get; set; }
        public string Description { get; set; }


        public override string ToString() => $"{Name}: {Description}";

    }
}
