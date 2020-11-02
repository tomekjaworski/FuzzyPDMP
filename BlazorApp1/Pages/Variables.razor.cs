using Blazored.Modal;
using Blazored.Modal.Services;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp1.Pages
{
    public partial class Variables
    {
        private int currentCount = 0;

        private void IncrementCount()
        {
            currentCount++;
        }

        private async Task TestMe()
        {
            ModalParameters mp = new ModalParameters();
            mp.Add(nameof(Confirm.Message), "msg?");
            var result = Modal.Show<Confirm>("aaa", mp);
            ModalResult mr = await result.Result;
        }
    }
}
