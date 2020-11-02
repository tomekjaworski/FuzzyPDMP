﻿using Microsoft.AspNetCore.Components;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp1.Shared
{
    public partial class SurveyPrompt
    {

        // Demonstrates how a parent component can supply parameters
        [Parameter]
        public string Title { get; set; }
    }
}
