using BlazorApp1.Fuzzy;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using BlazorApp1.Modals;
using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Http;
using System.Diagnostics;

namespace BlazorApp1.Pages
{
    public partial class Rules
    {
        FuzzyModel selected_model = new FuzzyModel(null);

        protected override void OnInitialized()
        {
        }

        protected override async Task OnAfterRenderAsync(bool firstRender)
        {
            Guid model_guid = await SessionStorage.GetItemAsync<Guid>("selected_fuzzy_model");
            if (model_guid == Guid.Empty)
                this.selected_model = BoardProvider.Model.Models.FirstOrDefault();
            else
                this.selected_model = BoardProvider.Model.GetModelBuGuid(model_guid);
        }

        private async Task OnRemovePremiseClicked(FuzzyRule rule, FuzzySubexpression premiseExpression)
        {
            string representation = premiseExpression.Value == null ? "" : $"<p class=\"font-weight-light bg-light rounded\">{premiseExpression}</p>";
            if (!await MessageBox.OkCancel(this.Modal, "Pytanie", $"Czy chcesz usunąć wybraną <b>przesłankę</b>?{representation}"))
                return;

            //Model m = ModelProvider.Model;
            rule.RemovePremise(premiseExpression);
        }

        private async Task OnRemoveConclusionClicked(FuzzyRule rule, FuzzySubexpression conclusionExpression)
        {
            string representation = conclusionExpression.Value == null ? "" : $"<p class=\"font-weight-light bg-light rounded\">{conclusionExpression}</p>";
            if (!await MessageBox.OkCancel(this.Modal, "Pytanie", $"Czy chcesz usunąć wybraną <b>konkluzję</b>?{representation}"))
                return;

            rule.RemoveConclusion(conclusionExpression);
        }

        private void OnAddPremiseClicked(FuzzyRule rule)
        {
            rule.AddEmptyPremise();
        }

        private void OnAddConclusionClicked(FuzzyRule rule)
        {
            rule.AddEmptyConclusion();
        }

        private void OnAddRuleClicked()
        {
            Board m = BoardProvider.Model;
            this.selected_model.AddRule();
        }

        private async Task OnRemoveRuleClicked(FuzzyRule rule)
        {
            if (!await MessageBox.OkCancel(this.Modal, "Pytanie", $"Czy chcesz usunąć wybraną <b>regułę</b>?<p class=\"font-weight-light bg-light rounded\">{rule}</p>"))
                return;

            Board m = BoardProvider.Model;
            this.selected_model.RemoveRule(rule);
        }
    }
}
