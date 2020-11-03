namespace BlazorApp1.Modals
{
    public class ValueEditorData
    {
        public string Name { get; set; }
        public string Description { get; set; }

        public ValueEditorData(string name, string description)
        {
            this.Name = name;
            this.Description = description;
        }
    }
}
