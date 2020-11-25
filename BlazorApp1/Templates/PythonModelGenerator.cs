using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using BlazorApp1.Fuzzy;
using HandlebarsDotNet;

namespace BlazorApp1
{
    public class PythonModelGenerator
    {
        private Board board;
        private string code;

        public string PythonCode => this.code;

        public PythonModelGenerator()
        {
            //
        }

        public void ApplyBoard(Board board)
        {
            this.board = board;
        }

        private static string GetFullPath(string fileName)
        {
            return Path.Combine(Path.GetDirectoryName(Environment.GetCommandLineArgs()[0]), "..\\..\\..\\Templates", fileName);
        }

        public void Run()
        {
            string template_string = File.ReadAllText(GetFullPath("code.handlebars"), Encoding.UTF8);
            Handlebars.RegisterHelper("normalize",
                (writer, context, parameters) =>
                    writer.WriteSafeString(NormalizePythonIdentifier(parameters[0] as string))
                );
            Handlebars.RegisterHelper("D2",
                (writer, context, parameters) =>
                    writer.Write(((double)parameters[0]).ToString("N2",
                    System.Globalization.CultureInfo.InvariantCulture))
                );
            Handlebars.RegisterHelper("D4",
                (writer, context, parameters) =>
                   writer.Write(((double)parameters[0]).ToString("N4",
                   System.Globalization.CultureInfo.InvariantCulture))
               );

            string[] color_names = new string[] { "blue", "red", "green", "black", "magenta", "cyan", "brown", "yellow" };
            Handlebars.RegisterHelper("color",
               (writer, context, parameters) =>
                  writer.Write(color_names[((int)parameters[0]) % color_names.Length])
              );

            Handlebars.Configuration.UnresolvedBindingFormatter = "???";

            var template = Handlebars.Compile(template_string);

            string NormalizePythonIdentifier(string text)
            {
                string iconv = "ĘEęeÓOóoĄAąaŚSśsŁLłlŻZżzŹZźzĆCćcŃNńn";
                string ok = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890_ ";
                string result = "";
                foreach (char ch in text)
                    if (iconv.IndexOf(ch) % 2 == 0)
                        result += iconv[iconv.IndexOf(ch) + 1];
                    else
                        if (ok.IndexOf(ch) != -1)
                        result += ch;
                result = string.Join("",
                result.Split(' ', StringSplitOptions.RemoveEmptyEntries).
                    Select(x =>
                    {
                        if (!char.IsLetter(x[0]))
                            return x;
                        else
                            return char.ToUpper(x[0]) + x.Substring(1).ToLower();
                    }));
                return result;
            }

            Dictionary<string, object> dict = new Dictionary<string, object>();
            dict["CurrentDate"] = DateTime.Now;

            List<object> models = new List<object>();
            dict["Models"] = models;
            foreach (FuzzyModel fmodel in BoardProvider.Board.Models)
            {
                if (!fmodel.IsValid)
                {
                    models.Add(new
                    {
                        IsValid = false,
                        ModelName = fmodel.Name,
                        ModelDescription = fmodel.Description,
                    });
                    continue;
                }

                FuzzyValue[] values = fmodel.Rules
                    .SelectMany(rule => rule.Premise)
                    .Union(
                        fmodel.Rules
                        .SelectMany(rule => rule.Conclusion)
                    ).Select(expr => expr.Variable)
                        .Distinct()
                        .SelectMany(@var => var.Values).ToArray();

                //FuzzyVariable[] variables = fmodel.Rules
                //    .SelectMany(rule => rule.Premise)
                //    .Union(
                //        fmodel.Rules
                //        .SelectMany(rule => rule.Conclusion)
                //    ).Select(expr => expr.Variable)
                //        .Distinct()
                //        .ToArray();

                FuzzyVariable[] input_variables = fmodel.Rules
                    .SelectMany(rule => rule.Premise)
                    .Select(expr => expr.Variable)
                    .Distinct()
                    .ToArray();

                FuzzyVariable[] output_variables = fmodel.Rules
                    .SelectMany(rule => rule.Conclusion)
                    .Select(x => x.Variable)
                    .Distinct()
                    .ToArray();

                models.Add(new
                {
                    IsValid = fmodel.IsValid,
                    ModelName = fmodel.Name,
                    ModelDescription = fmodel.Description,
                    Values = values,
                    InputVariables = input_variables,
                    OutputVariables = output_variables,
                    XStep = 0.1,
                });

            }


            this.code = template(dict);
            Debug.Write(code);

            //
        }
    }
}
