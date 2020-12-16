using Blazored.Modal;
using Blazored.Modal.Services;
using Microsoft.AspNetCore.Components;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace WebFuzzyEditor.Modals
{
    public partial class TextInputContent
    {
        [CascadingParameter] BlazoredModalInstance BlazoredModal { get; set; }
        [Parameter] public string Message { get; set; } = "?";
        [Parameter] public string Value { get; set; }

        void OkClicked()
        {
            BlazoredModal.Close(ModalResult.Ok<string>(string.IsNullOrEmpty(Value) ? "" : Value));
        }

        void CancelClicked()
        {
            BlazoredModal.Cancel();
        }

        void TestClicked()
        {
            this.Message = Value;
        }

    }
}
