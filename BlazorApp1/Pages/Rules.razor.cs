using BlazorApp1.Fuzzy;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using BlazorApp1.Modals;
using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Http;
using System.Diagnostics;
using Microsoft.AspNetCore.Components.Web;

namespace BlazorApp1.Pages
{
    public partial class Rules
    {
        FuzzyModel selected_model = new FuzzyModel(null);

        protected override void OnInitialized()
        {
            this.selected_model = BoardProvider.Board.SelectedModel;

        }


        private async Task OnRemovePremiseClicked(MouseEventArgs e, FuzzyRule rule, FuzzySubexpression premiseExpression)
        {
            string representation = premiseExpression.Value == null ? "" : $"<p class=\"font-weight-light bg-light rounded\">{premiseExpression}</p>";
            if (!await MessageBox.OkCancel(this.Modal, "Pytanie", $"Czy chcesz usunąć wybraną <b>przesłankę</b>?{representation}"))
                return;

            //Model m = ModelProvider.Model;
            rule.RemovePremise(premiseExpression);
        }

        private async Task OnRemoveConclusionClicked(MouseEventArgs e, FuzzyRule rule, FuzzySubexpression conclusionExpression)
        {
            string representation = conclusionExpression.Value == null ? "" : $"<p class=\"font-weight-light bg-light rounded\">{conclusionExpression}</p>";
            if (!await MessageBox.OkCancel(this.Modal, "Pytanie", $"Czy chcesz usunąć wybraną <b>konkluzję</b>?{representation}"))
                return;

            rule.RemoveConclusion(conclusionExpression);
        }

        private void OnAddPremiseClicked(MouseEventArgs e, FuzzyRule rule)
        {
            rule.AddEmptyPremise();
        }

        private void OnAddConclusionClicked(MouseEventArgs e, FuzzyRule rule)
        {
            rule.AddEmptyConclusion();
        }

        private void OnAddRuleClicked(MouseEventArgs e)
        {
            Board m = BoardProvider.Board;
            FuzzyRule fr = new FuzzyRule();
            this.selected_model.AddRule(fr);
        }

        private async Task OnRemoveRuleClicked(MouseEventArgs e, FuzzyRule rule)
        {
            if (!await MessageBox.OkCancel(this.Modal, "Pytanie", $"Czy chcesz usunąć wybraną <b>regułę</b>?<p class=\"font-weight-light bg-light rounded\">{rule}</p>"))
                return;

            Board m = BoardProvider.Board;
            this.selected_model.RemoveRule(rule);
        }

        private async Task OnDuplicateRule(MouseEventArgs e, FuzzyRule rule)
        {
            // todo:  implementacja
            FuzzyRule copy = rule.CreateCopy();
            this.selected_model.AddRule(copy);
        }
    }
}
