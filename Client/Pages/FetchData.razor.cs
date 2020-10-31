using FuzzyPDMP.Shared;
using Microsoft.AspNetCore.Components;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Net.Http.Json;
using System.Threading.Tasks;

namespace FuzzyPDMP.Client.Pages
{
    public partial class FetchData
    {
        private WeatherForecast[] forecasts;

        [Inject]
        HttpClient Http { get; set; }


        protected override async Task OnInitializedAsync()
        {
            forecasts = await Http.GetFromJsonAsync<WeatherForecast[]>("WeatherForecast");
        }
    }
}
