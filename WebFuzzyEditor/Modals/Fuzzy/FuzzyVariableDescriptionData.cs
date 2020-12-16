namespace WebFuzzyEditor.Modals
{
    public class FuzzyVariableDescriptionData
    {
        public string Name { get; set; }
        public string Description { get; set; }

        public FuzzyVariableDescriptionData(string name, string description)
        {
            this.Name = name;
            this.Description = description;
        }
    }
}

