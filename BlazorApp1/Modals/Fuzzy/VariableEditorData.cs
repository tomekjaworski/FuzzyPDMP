namespace BlazorApp1.Modals
{
    public class VariableEditorData {
        public string Name { get; set; }
        public string Description { get; set; }

        public VariableEditorData(string name, string description)
        {
            this.Name = name;
            this.Description = description;
        }
    }
}
