using ChartJs.Blazor.ChartJS.Common;
using ChartJs.Blazor.ChartJS.Common.Axes;
using ChartJs.Blazor.ChartJS.Common.Enums;
using ChartJs.Blazor.ChartJS.Common.Properties;
using ChartJs.Blazor.ChartJS.LineChart;
using ChartJs.Blazor.Charts;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp1.Fuzzy
{
    public class ChartHolder
    {
        private FuzzyVariable parent_variable;

        public LineConfig Config;
        public ChartJsLineChart Chart;

        public ChartHolder(FuzzyVariable fuzzyVariable)
        {
            this.parent_variable = fuzzyVariable;

            this.Config = new LineConfig
            {
                Options = new LineOptions
                {
                    Animation = new Animation()
                    {
                        Duration = 0,
                    },
                    Responsive = true,
                    Title = new OptionsTitle
                    {
                        Display = true,
                        Text = $"Zmienna lingwistyczna XXXX: YYYYY"
                    },
                    Tooltips = new Tooltips
                    {
                        Mode = InteractionMode.Nearest,
                        Intersect = true
                    },
                    Hover = new LineOptionsHover
                    {
                        Mode = InteractionMode.Nearest,
                        Intersect = true
                    },

                    Scales = new Scales
                    {

                        xAxes = new List<CartesianAxis>
                        {
                            new LinearCartesianAxis
                            {
                                ScaleLabel = new ScaleLabel("Dziedzina"),
                                Ticks = new ChartJs.Blazor.ChartJS.Common.Axes.Ticks.LinearCartesianTicks()
                                {
                                    Min = null, // != null 
                                    Max = null
                                },
                            }
                        },
                        yAxes = new List<CartesianAxis>
                        {
                            new LinearCartesianAxis
                            {
                                Ticks = new ChartJs.Blazor.ChartJS.Common.Axes.Ticks.LinearCartesianTicks()
                                {
                                    Min = 0.0,
                                    Max = 1.0
                                },
                                ScaleLabel = new ScaleLabel("Przynależność")
                            }
                        }
                    }
                }
            };
        }

        public void UpdateChart()
        {
            this.Config.Options.Title.Text = $"Zmienna lingwistyczna {this.parent_variable.Name}: {this.parent_variable.Description}";
            LinearCartesianAxis lca = this.Config.Options.Scales.xAxes[0] as LinearCartesianAxis;
            lca.Ticks.Min = this.parent_variable.Minimum.Value;
            lca.Ticks.Max = this.parent_variable.Maximum.Value;

            this.Config.Data.Datasets.Clear();

            string[] colors = new[] { "blue", "red", "green", "black", "magenta", "cyan", "brown", "yellow" };
            int icolor = 0;
            foreach (FuzzyValue fval in this.parent_variable.Values)
            {
                LineDataset<Point> data_set = new LineDataset<Point>
                {
                    Label = fval.Name,
                    LineTension = 0,
                    PointRadius = 2,
                    BorderColor = colors[icolor++ % colors.Length],
                    PointHitRadius = 10,
                    BorderWidth = 3,
                };

                if (fval.MembershipType == MembershipFunctionFamily.Trapezoidal)
                {
                    NamedParameter sl = fval.GetParameter("SuppL");
                    NamedParameter kl = fval.GetParameter("KernL");
                    NamedParameter kr = fval.GetParameter("KernR");
                    NamedParameter sr = fval.GetParameter("SuppR");

                    data_set.Add(new Point(this.parent_variable.Minimum.Value, 0));
                    data_set.Add(new Point(sl.Value, 0));
                    data_set.Add(new Point(kl.Value, 1));
                    data_set.Add(new Point(kr.Value, 1));
                    data_set.Add(new Point(sr.Value, 0));
                    data_set.Add(new Point(this.parent_variable.Maximum.Value, 0));

                    this.Config.Data.Datasets.Add(data_set);
                }
            }
        }

    }
}
