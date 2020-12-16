using Blazored.Modal;
using Blazored.Modal.Services;
using Microsoft.AspNetCore.Components;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace WebFuzzyEditor.Modals
{
    public partial class FuzzyVariableEditorForm
    {
        [CascadingParameter] BlazoredModalInstance BlazoredModal { get; set; }
        
        [Parameter] public FuzzyVariableDescriptionData Data { get; set; }

        void OkClicked()
        {
            BlazoredModal.Close(ModalResult.Ok<FuzzyVariableDescriptionData>(Data));
        }

        void CancelClicked()
        {
            BlazoredModal.Cancel();
        }
    }
}
