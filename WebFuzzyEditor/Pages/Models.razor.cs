﻿using WebFuzzyEditor.Fuzzy;
using WebFuzzyEditor.Modals;
using Microsoft.AspNetCore.Components.Web;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace WebFuzzyEditor.Pages
{
    public partial class Models
    {
        FuzzyModel selected_model = null;

        public Models()
        {
            this.selected_model = BoardProvider.Board.SelectedModel;
        }

        private async Task OnDuplicateModel(MouseEventArgs e, FuzzyModel fmodel)
        {
            FuzzyModel fm = fmodel.Clone();
            //fm.Name += " (kopia)";
            //fm.Description += " (kopia)";
            BoardProvider.Board.AddModel(fm);
        }

        private async Task OnEditModelDescription(MouseEventArgs e, FuzzyModel fmodel)
        {
            var in_data = new FuzzyModelDescriptionData(fmodel.Name, fmodel.Description);

            (bool result, FuzzyModelDescriptionData out_data) = await Modals.FuzzyEditors.FuzzyModelDescriptionEditor(this.Modal, in_data);

            if (result)
            {
                fmodel.Description = out_data.Description;
                fmodel.Name = out_data.Name;
            }
        }

        private async Task OnRemoveModel(MouseEventArgs e, FuzzyModel fmodel)
        {
            if (!await MessageBox.OkCancel(this.Modal, "Pytanie", $"Czy chcesz usunąć wybrany <b>model</b>?<p class=\"font-weight-light bg-light rounded\">{fmodel}</p>"))
                return;

            BoardProvider.Board.RemoveModel(fmodel);
            this.selected_model = BoardProvider.Board.SelectedModel;
        }

        private void OnSelectModel(MouseEventArgs e, FuzzyModel fmodel)
        {
            this.selected_model = fmodel;
            BoardProvider.Board.SelectedModel = fmodel;
        }

        private void OnAddModel(MouseEventArgs e)
        {
            Random rnd = new Random();
            BoardProvider.Board.AddModel(new FuzzyModel(
                $"Model-{rnd.Next():X08}",
                $"Description-{rnd.Next():X08}"
                ));
        }
    }
}
