namespace BlazorApp1.Modals
{
    public class FuzzyValueDescriptionData
    {
        public string Name { get; set; }
        public string Description { get; set; }

        public FuzzyValueDescriptionData(string name, string description)
        {
            this.Name = name;
            this.Description = description;
        }
    }
}
