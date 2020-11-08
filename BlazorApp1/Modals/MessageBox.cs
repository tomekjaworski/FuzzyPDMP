using Blazored.Modal;
using Blazored.Modal.Services;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp1.Modals
{
    public static class MessageBox
    {
        public static async Task Ok(IModalService modalService, string title, string message)
        {
            if (modalService == null)
                throw new NullReferenceException("modalService");

            ModalParameters mp = new ModalParameters();
            mp.Add(nameof(OkContent.Message), message);
            
            ModalOptions mo = new ModalOptions();
            mo.DisableBackgroundCancel = true;
            mo.HideCloseButton = true;

            IModalReference result = modalService.Show<OkContent>(title, mp, mo);
            ModalResult mr = await result.Result;
        }

        public static async Task<bool> OkCancel(IModalService modalService, string title, string message)
        {
            if (modalService == null)
                throw new NullReferenceException("modalService");

            ModalParameters mp = new ModalParameters();
            mp.Add(nameof(OkCancelContent.Message), message);

            ModalOptions mo = new ModalOptions();
            mo.DisableBackgroundCancel = true;
            mo.HideCloseButton = true;

            IModalReference result = modalService.Show<OkCancelContent>(title, mp, mo);
            ModalResult mr = await result.Result;
            if (mr.Cancelled)
                return false;
            return true;
        }

        public static async Task<(bool, string)> TextInput(IModalService modalService, string title, string message, string defaultValue = null)
        {
            if (modalService == null)
                throw new NullReferenceException("modalService");

            ModalParameters mp = new ModalParameters();
            mp.Add(nameof(TextInputContent.Message), message);
            mp.Add(nameof(TextInputContent.Value), defaultValue);

            ModalOptions mo = new ModalOptions();
            mo.DisableBackgroundCancel = true;
            mo.HideCloseButton = true;

            IModalReference result = modalService.Show<TextInputContent>(title, mp, mo);
            ModalResult mr = await result.Result;
            if (mr.Cancelled)
                return (false, null);
            return (true, mr.Data as string);
        }


    }
}
