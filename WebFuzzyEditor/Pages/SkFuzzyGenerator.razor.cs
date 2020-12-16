using WebFuzzyEditor.Fuzzy;
using System;
using System.Collections.Generic;
using System.Linq;
using WebFuzzyEditor.Modals;
using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Http;
using System.Diagnostics;
using Microsoft.AspNetCore.Components.Web;
using BlazorMonaco.Bridge;
using BlazorMonaco;
using System.Text;
using System.Threading.Tasks;

namespace WebFuzzyEditor.Pages
{
    public partial class SkFuzzyGenerator
    {

		private MonacoEditor _editor { get; set; }

		private async Task OnGenerateCode(MouseEventArgs e)
        {
			try
			{
				PythonModelGenerator generator = new PythonModelGenerator();
				generator.ApplyBoard(BoardProvider.Board);
				generator.Run();
				await this._editor.SetValue(generator.PythonCode);
			}
			catch (Exception ex)
			{
				StringBuilder sb = new StringBuilder();
				sb.AppendLine("\"\"\"");
				sb.AppendLine("### wystąpił wyjątek podczas generowania kodu źródłowego: ###");
				sb.AppendLine(ex.Message);
				sb.AppendLine(ex.StackTrace);
				sb.AppendLine();
				sb.AppendLine("\"\"\"");
				await this._editor.SetValue(sb.ToString());
			}
		}

		private StandaloneEditorConstructionOptions EditorConstructionOptions(MonacoEditor editor)
		{
			return new StandaloneEditorConstructionOptions
			{
				Dimension = new Dimension() { Height = 600 },
				AutomaticLayout = true,
				Language = "python",
				Value = "# Wciśnij przycisk...\r\n"
			};
		}
	}
}
