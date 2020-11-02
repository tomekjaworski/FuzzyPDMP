using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BlazorApp1.Fuzzy
{
    public class Model
    {
        public List<Variable> Variables { get; set; }

        public Model()
        {
            this.Variables = new List<Variable>();
        }
    }

    public class ModelProvider
    {
        #region static
        private static ModelProvider mp;
        public static ModelProvider Data => mp;

        static ModelProvider()
        {
            mp = new ModelProvider();
        }
        #endregion

        private Model model;
        public Model Model => this.model;

        private ModelProvider()
        {
            Model m;
            using (FileStream fs = File.OpenRead("Data\\model.json"))
            {
                StreamReader sr = new StreamReader(fs, Encoding.UTF8);
                string str = sr.ReadToEnd();
                m = JsonConvert.DeserializeObject<Model>(str);
            }
            this.model = m;
        }
    }
}
