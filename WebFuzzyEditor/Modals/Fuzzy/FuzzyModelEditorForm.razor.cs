using Blazored.Modal;
using Blazored.Modal.Services;
using Microsoft.AspNetCore.Components;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace WebFuzzyEditor.Modals
{
    public partial class FuzzyModelEditorForm
    {
        [CascadingParameter] BlazoredModalInstance BlazoredModal { get; set; }

        [Parameter] public FuzzyModelDescriptionData Data { get; set; }

        void OkClicked()
        {
            BlazoredModal.Close(ModalResult.Ok<FuzzyModelDescriptionData>(Data));
        }

        void CancelClicked()
        {
            BlazoredModal.Cancel();
        }
    }
}
