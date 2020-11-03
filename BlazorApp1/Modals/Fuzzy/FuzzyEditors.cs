using Blazored.Modal;
using Blazored.Modal.Services;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp1.Modals
{
    public static class FuzzyEditors
    {
       public static async Task<(bool, VariableEditorData)> EditFuzzyVariable(IModalService modalService, VariableEditorData defaultValue)
        {
            if (modalService == null)
                throw new NullReferenceException("modalService");

            ModalParameters mp = new ModalParameters();
            mp.Add(nameof(VariableEditorForm.Data), defaultValue);

            ModalOptions mo = new ModalOptions();
            mo.DisableBackgroundCancel = true;
            mo.HideCloseButton = true;

            IModalReference result = modalService.Show<VariableEditorForm>("Edycja zmiennej lingwistycznej", mp, mo);
            ModalResult mr = await result.Result;
            if (mr.Cancelled)
                return (false, null);
            return (true, mr.Data as VariableEditorData);
        }


        public static async Task<(bool, ValueEditorData)> EditFuzzyValue(IModalService modalService, ValueEditorData defaultValue)
        {
            if (modalService == null)
                throw new NullReferenceException("modalService");

            ModalParameters mp = new ModalParameters();
            mp.Add(nameof(ValueEditorForm.Data), defaultValue);

            ModalOptions mo = new ModalOptions();
            mo.DisableBackgroundCancel = true;
            mo.HideCloseButton = true;

            IModalReference result = modalService.Show<ValueEditorForm>("Edycja wartości lingwistycznej", mp, mo);
            ModalResult mr = await result.Result;
            if (mr.Cancelled)
                return (false, null);
            return (true, mr.Data as ValueEditorData);
        }


    }
}
