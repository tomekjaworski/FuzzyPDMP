using BlazorApp1.Fuzzy;
using BlazorApp1.Modals;
using Blazored.Modal;
using Blazored.Modal.Services;
using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Web;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp1.Pages
{
    public partial class Variables
    {

        protected override void OnInitialized()
        {
            base.OnInitialized();
            foreach (FuzzyVariable fvar in BoardProvider.Model.Variables)
            {
                fvar.ResetChartHolder();
                fvar.ChartHolder.UpdateChart();
            }
        }

        private async Task OnEditVariableDescription(MouseEventArgs e, FuzzyVariable variable)
        {
            var in_data = new VariableEditorData(variable.Name, variable.Description);

            (bool result, VariableEditorData out_data) = await Modals.FuzzyEditors.EditFuzzyVariable(this.Modal, in_data);

            if (result)
            {
                variable.Description = out_data.Description;
                variable.Name = out_data.Name;
                variable.ChartHolder.UpdateChart();
            }
        }


        private async Task OnEditValueDescription(MouseEventArgs e, FuzzyValue value)
        {
            var in_data = new ValueEditorData(value.Name, value.Description);

            (bool result, ValueEditorData out_data) = await Modals.FuzzyEditors.EditFuzzyValue(this.Modal, in_data);

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

            BoardProvider.Model.RemoveVariable(variable);
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
            variable.AddValue(
                $"Value-{rnd.Next():X08}",
                $"Description-{rnd.Next():X08}");
        }

        private void OnAddVariable(MouseEventArgs e)
        {
            Random rnd = new Random();
            BoardProvider.Model.AddVariable(
                $"Value-{rnd.Next():X08}",
                $"Description-{rnd.Next():X08}");
        }
    }
}
