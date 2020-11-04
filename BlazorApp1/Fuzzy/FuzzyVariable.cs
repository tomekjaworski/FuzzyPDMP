using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp1.Fuzzy
{
    public class FuzzyVariable
    {
        private List<FuzzyValue> values;
        private MembershipFunctionFamily membership_family;
        private NamedParameter dmin, dmax;


        public string Name { get; set; }
        public string Description { get; set; }

        public FuzzyValue[] Values => this.values.ToArray();

        public void ValidateCrispParameters()
        {
            // sprawdź dziedzinę
            this.dmin.IsValid = this.dmax.IsValid = this.dmin.Value <= this.dmax.Value;

            foreach (FuzzyValue fv in this.values)
                fv.ValidateCrispParameters();
        }

        public override string ToString() => $"{Name}: {Description}";

        public MembershipFunctionFamily MembershipType {
            get => this.membership_family;
            set {
                this.membership_family = value;
                foreach (var v in this.values)
                    v.SetMembershipType(value);

                this.ValidateCrispParameters();
            }
        }

        public NamedParameter[] Parameters {
            get {
                List<NamedParameter> pars = new List<NamedParameter>();
                pars.AddRange(new[] { this.dmin, this.dmax });
                pars.AddRange(this.values.SelectMany(x => x.Parameters));
                return pars.ToArray();
            }
        }

        public NamedParameter Minimum => this.dmin;
        public NamedParameter Maximum => this.dmax;

        public byte[] ImageBytes { get; set; }


        public FuzzyVariable()
        {

            Bitmap bmp = new Bitmap(512, 128, System.Drawing.Imaging.PixelFormat.Format32bppArgb);
            using(Graphics g = Graphics.FromImage(bmp))
            {
                g.FillRectangle(Brushes.Red, 0, 0, 512, 128);
            }

            using (var stream = new MemoryStream())
            {
                bmp.Save(stream, System.Drawing.Imaging.ImageFormat.Png);
                this.ImageBytes = stream.ToArray();
            }
            

            this.values = new List<FuzzyValue>();
            this.membership_family = MembershipFunctionFamily.Unspecified;

            this.dmin = new NamedParameter("Dmin", 0, this, null);
            this.dmax = new NamedParameter("Dmax", 10, this, null);
            this.ValidateCrispParameters();
        }

        public FuzzyValue AddValue(string name, string description)
        {
            FuzzyValue val = new FuzzyValue(this, name, description, this.membership_family);
            this.values.Add(val);
            this.ValidateCrispParameters();
            return val;
        }

        internal bool RemoveValue(FuzzyValue value)
        {
            if (!this.values.Contains(value))
                return false;

            this.values.Remove(value);
            // todo: aktualziac reguł

            this.ValidateCrispParameters();
            return true;
        }



    }
}
