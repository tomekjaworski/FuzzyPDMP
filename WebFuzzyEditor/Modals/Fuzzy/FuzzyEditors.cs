using Blazored.Modal;
using Blazored.Modal.Services;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace WebFuzzyEditor.Modals
{
    public static class FuzzyEditors
    {
       public static async Task<(bool, FuzzyVariableDescriptionData)> EditFuzzyVariable(IModalService modalService, FuzzyVariableDescriptionData defaultValue)
        {
            if (modalService == null)
                throw new NullReferenceException("modalService");

            ModalParameters mp = new ModalParameters();
            mp.Add(nameof(FuzzyVariableEditorForm.Data), defaultValue);

            ModalOptions mo = new ModalOptions();
            mo.DisableBackgroundCancel = true;
            mo.HideCloseButton = true;

            IModalReference result = modalService.Show<FuzzyVariableEditorForm>("Edycja zmiennej lingwistycznej", mp, mo);
            ModalResult mr = await result.Result;
            if (mr.Cancelled)
                return (false, null);
            return (true, mr.Data as FuzzyVariableDescriptionData);
        }


        public static async Task<(bool, FuzzyValueDescriptionData)> FuzzyValueDescriptionEditor(IModalService modalService, FuzzyValueDescriptionData defaultValue)
        {
            if (modalService == null)
                throw new NullReferenceException("modalService");

            ModalParameters mp = new ModalParameters();
            mp.Add(nameof(FuzzyValueEditorForm.Data), defaultValue);

            ModalOptions mo = new ModalOptions();
            mo.DisableBackgroundCancel = true;
            mo.HideCloseButton = true;

            IModalReference result = modalService.Show<FuzzyValueEditorForm>("Edycja wartości lingwistycznej", mp, mo);
            ModalResult mr = await result.Result;
            if (mr.Cancelled)
                return (false, null);
            return (true, mr.Data as FuzzyValueDescriptionData);
        }



        public static async Task<(bool, FuzzyModelDescriptionData)> FuzzyModelDescriptionEditor(IModalService modalService, FuzzyModelDescriptionData defaultValue)
        {
            if (modalService == null)
                throw new NullReferenceException("modalService");

            ModalParameters mp = new ModalParameters();
            mp.Add(nameof(FuzzyModelEditorForm.Data), defaultValue);

            ModalOptions mo = new ModalOptions();
            mo.DisableBackgroundCancel = true;
            mo.HideCloseButton = true;

            IModalReference result = modalService.Show<FuzzyModelEditorForm>("Edycja opisu modelu", mp, mo);
            ModalResult mr = await result.Result;
            if (mr.Cancelled)
                return (false, null);
            return (true, mr.Data as FuzzyModelDescriptionData);
        }


    }
}
