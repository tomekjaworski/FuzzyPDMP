namespace WebFuzzyEditor.Modals
{
    public class FuzzyModelDescriptionData
    {
        public string Name { get; set; }
        public string Description { get; set; }

        public FuzzyModelDescriptionData(string name, string description)
        {
            this.Name = name;
            this.Description = description;
        }
    }
}
