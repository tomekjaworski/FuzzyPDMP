﻿using WebFuzzyEditor.Fuzzy;
using WebFuzzyEditor.Modals;
using Blazored.Modal;
using Blazored.Modal.Services;
using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Web;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace WebFuzzyEditor.Pages
{
    public partial class Variables
    {

        protected override void OnInitialized()
        {
            base.OnInitialized();
            foreach (FuzzyVariable fvar in BoardProvider.Board.Variables)
            {
                fvar.ResetChartHolder();
                fvar.ChartHolder.UpdateChart();
            }
        }

        private async Task OnEditVariableDescription(MouseEventArgs e, FuzzyVariable variable)
        {
            var in_data = new FuzzyVariableDescriptionData(variable.Name, variable.Description);

            (bool result, FuzzyVariableDescriptionData out_data) = await Modals.FuzzyEditors.EditFuzzyVariable(this.Modal, in_data);

            if (result)
            {
                variable.Description = out_data.Description;
                variable.Name = out_data.Name;
                variable.ChartHolder.UpdateChart();
            }
        }


        private async Task OnEditValueDescription(MouseEventArgs e, FuzzyValue value)
        {
            var in_data = new FuzzyValueDescriptionData(value.Name, value.Description);

            (bool result, FuzzyValueDescriptionData out_data) = await Modals.FuzzyEditors.FuzzyValueDescriptionEditor(this.Modal, in_data);

            if (result)
            {
                value.Description = out_data.Description;
                value.Name = out_data.Name;
                value.Variable.ChartHolder.UpdateChart();
            }
        }

        private async Task OnRemoveVariable(MouseEventArgs e, FuzzyVariable variable)
        {
            if (!await MessageBox.OkCancel(this.Modal, "Pytanie", $"Czy chcesz <b>usunąć</b> zmienną lingwistyczną {variable.Name}?<br/>Usunięcie zmiennej nie spowoduje usunięcia reguł związanych z tą zmienną"))
                return;

            BoardProvider.Board.RemoveVariable(variable);
        }


        private async Task OnRemoveValue(MouseEventArgs e, FuzzyValue value)
        {
            if (!await MessageBox.OkCancel(this.Modal, "Pytanie", $"Czy chcesz <b>usunąć</b> wartość lingwistyczną {value.Name} ze zmiennej {value.Variable.Name}?"))
                return;

            //ModelProvider.Data.Model.RemoveValue(value);
            value.Variable.RemoveValue(value);
        }


        private void OnAddValue(MouseEventArgs e, FuzzyVariable variable)
        {
            Random rnd = new Random();
            FuzzyValue fv = new FuzzyValue(variable, $"Value-{rnd.Next():X08}",
                $"Description-{rnd.Next():X08}");
            variable.AddValue(fv);
        }

        private void OnAddVariable(MouseEventArgs e)
        {
            Random rnd = new Random();
            FuzzyVariable fv = new FuzzyVariable()
            {
                Name = $"Variable-{rnd.Next():X08}",
                Description = $"Description-{rnd.Next():X08}"
            };
            BoardProvider.Board.AddVariable(fv);
        }


        private void OnDuplicateVariable(MouseEventArgs e, FuzzyVariable variable)
        {
            FuzzyVariable copy = variable.Clone();
            //copy.Name += " (kopia)";
            //copy.Description += " (kopia)";

            foreach (FuzzyValue value in copy.Values)
            {
                //value.Name += " (kopia)";
                //value.Description += " (kopia)";
            }
            BoardProvider.Board.AddVariable(copy);
        }

        private void OnDuplicateValue(MouseEventArgs e, FuzzyVariable variable, FuzzyValue value)
        {
            FuzzyValue copy = value.Clone();
            //copy.Name += " (kopia)";
            //copy.Description += " (kopia)";

            variable.AddValue(copy);
        }
    }
}
