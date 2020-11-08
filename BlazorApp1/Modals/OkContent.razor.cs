using Blazored.Modal;
using Blazored.Modal.Services;
using Microsoft.AspNetCore.Components;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp1.Modals
{
    public partial class OkContent
    {

        [CascadingParameter] BlazoredModalInstance BlazoredModal { get; set; }
        [Parameter] public string Message { get; set; }

        void OkClicked()
        {
            BlazoredModal.Close(ModalResult.Ok(true));
        }

    }
}
