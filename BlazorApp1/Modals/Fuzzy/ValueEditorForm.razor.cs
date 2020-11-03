using Blazored.Modal;
using Blazored.Modal.Services;
using Microsoft.AspNetCore.Components;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp1.Modals
{
    public partial class ValueEditorForm
    {
        [CascadingParameter] BlazoredModalInstance BlazoredModal { get; set; }
        
        [Parameter] public VariableEditorData Data { get; set; }

        void OkClicked()
        {
            BlazoredModal.Close(ModalResult.Ok<VariableEditorData>(Data));
        }

        void CancelClicked()
        {
            BlazoredModal.Cancel();
        }
    }
}
