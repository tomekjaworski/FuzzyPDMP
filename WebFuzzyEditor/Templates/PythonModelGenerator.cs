using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using WebFuzzyEditor.Fuzzy;
using HandlebarsDotNet;

namespace WebFuzzyEditor
{

    public enum TokenType
    {
        FuzzyValue,
        NamedVariable,
        Connective
    }

    public class Token
    {
        public TokenType Type { get; set; }
        public FuzzyValue FuzzyValue { get; set; }
        public FuzzyConnectiveType Connective { get; set; }
        public string Name { get; internal set; }

        public bool IsFuzzyValue => this.Type == TokenType.FuzzyValue;
        public bool IsConnective => this.Type == TokenType.Connective;
        public bool IsNamedVariable => this.Type == TokenType.NamedVariable;

        public bool IsAnd => this.Type == TokenType.Connective && this.Connective == FuzzyConnectiveType.And;
        public bool IsOr => this.Type == TokenType.Connective && this.Connective == FuzzyConnectiveType.Or;

        public override string ToString() => Type switch
        {
            TokenType.NamedVariable => this.Name,
            TokenType.FuzzyValue => this.FuzzyValue.ToString(),
            TokenType.Connective => this.Connective.ToString(),
        };
    }


    class Operation
    {
        public Token Target { get; set; }
        public Token Left { get; set; }
        public Token Op { get; set; }
        public Token Right { get; set; }

        public Operation(Token target, Token left, Token op, Token right)
        {
            this.Target = target;
            this.Left = left;
            this.Op = op;
            this.Right = right;
        }

        public override string ToString() => $"{Target} = {Left} {Op} {Right}";
    }


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
            if (Environment.GetEnvironmentVariable("IDE") == "VS")
                return Path.Combine(Path.GetDirectoryName(Environment.GetCommandLineArgs()[0]), "..\\..\\..\\Templates", fileName);
            else
                return Path.Combine(Path.GetDirectoryName(Environment.GetCommandLineArgs()[0]), "Templates", fileName);
        }

        static string NormalizePythonIdentifier(string text)
        {
            if (string.IsNullOrEmpty(text))
                return "(null?)";

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

            Dictionary<string, object> dict = new Dictionary<string, object>();
            dict["CurrentDate"] = DateTime.Now;

            List<object> models = new List<object>();
            dict["Models"] = models;
            int temp_variable_id = 1;
            int rule_id = 1;

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

                FuzzyValue[] all_values = fmodel.Rules
                    .SelectMany(rule => rule.Premise)
                    .Union(
                        fmodel.Rules
                        .SelectMany(rule => rule.Conclusion)
                    ).Select(expr => expr.Variable)
                        .Distinct()
                        .SelectMany(@var => var.Values).ToArray();

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

                List<object> rule_value_connection = new List<object>();
                List<object> compiled_rules = new List<object>();
                Dictionary<FuzzyValue, List<object> > value2rule = new Dictionary<FuzzyValue, List<object>>();

                foreach (FuzzyRule fr in fmodel.Rules)
                {
                    // Generuj regułe w postaci strumienia tokenów
                    List<Token> tokens = new List<Token>();
                    foreach (FuzzySubexpression expr in fr.Premise)
                    {
                        if (expr.ConnectiveType == FuzzyConnectiveType.And)
                            tokens.Add(new Token() { Type = TokenType.Connective, Connective = FuzzyConnectiveType.And });
                        if (expr.ConnectiveType == FuzzyConnectiveType.Or)
                            tokens.Add(new Token() { Type = TokenType.Connective, Connective = FuzzyConnectiveType.Or });

                        tokens.Add(new Token() { Type = TokenType.FuzzyValue, FuzzyValue = expr.Value });
                    }

                    List<Token> t = new List<Token>();
                    t.AddRange(tokens);
                    t.Add(new Token() { Type = TokenType.Connective, Connective = FuzzyConnectiveType.Or });
                    t.AddRange(tokens);
                    t.Add(new Token() { Type = TokenType.Connective, Connective = FuzzyConnectiveType.And });
                    t.AddRange(tokens);
                    tokens = t;


                    List<Operation> ops = new List<Operation>();
                    // Generuj składowe wyrażenia (baardzo uproszczone)

                    bool substitution_occured;
                    do // AND
                    {
                        substitution_occured = false;
                        for (int i = 1; i < tokens.Count - 1; i++)
                            if (tokens[i].Type == TokenType.Connective && tokens[i].Connective == FuzzyConnectiveType.And)
                            {
                                Token temp = new Token() { Type = TokenType.NamedVariable, Name = $"temp{temp_variable_id++}" };
                                Operation op = new Operation(temp, tokens[i - 1], tokens[i], tokens[i + 1]);
                                ops.Add(op);
                                tokens[i] = temp;
                                tokens.RemoveAt(i + 1);
                                tokens.RemoveAt(i - 1);
                                substitution_occured = true;
                                i--;
                            }
                    } while (substitution_occured);

                    do // OR
                    {
                        substitution_occured = false;
                        for (int i = 1; i < tokens.Count - 1; i++)
                            if (tokens[i].Type == TokenType.Connective && tokens[i].Connective == FuzzyConnectiveType.Or)
                            {
                                Token temp = new Token() { Type = TokenType.NamedVariable, Name = $"temp{temp_variable_id++}" };
                                Operation op = new Operation(temp, tokens[i - 1], tokens[i], tokens[i + 1]);
                                ops.Add(op);
                                tokens[i] = temp;
                                tokens.RemoveAt(i + 1);
                                tokens.RemoveAt(i - 1);
                                substitution_occured = true;
                                i--;
                            }
                    } while (substitution_occured);
                    Debug.Assert(tokens.Count == 1);

                    var compiled_rule = new
                    {
                        Rule = fr,
                        RuleID = rule_id++,
                        Operations = ops.ToArray(),
                        Comment = fr.ToString(),
                        FinalToken = tokens[0],
                        Conclusions = fr.Conclusion.Select(x => x.Value)
                    };
                    compiled_rules.Add(compiled_rule);


                    foreach(FuzzyValue conclusion_value in fr.Conclusion.Select(c=>c.Value))
                    {
                        if (!value2rule.ContainsKey(conclusion_value))
                            value2rule[conclusion_value] = new List<object>();

                        var conn = new
                        {
                            Rule = compiled_rule.Rule,
                            RuleID = compiled_rule.RuleID,
                            ConcludedValue = conclusion_value
                        };
                        value2rule[conclusion_value].Add(conn);
                    }

                }

                models.Add(new
                {
                    IsValid = fmodel.IsValid,
                    ModelName = fmodel.Name,
                    ModelDescription = fmodel.Description,
                    AllValues = all_values,
                    InputVariables = input_variables,
                    OutputVariables = output_variables,
                    CompiledRules = compiled_rules,

                    OutputValueToRuleAssociation = value2rule
                });

            }


            this.code = template(dict);
            Debug.Write(code);

            //
        }
    }
}
