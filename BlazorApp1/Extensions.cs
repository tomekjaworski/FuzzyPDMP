using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Reflection;
using System.Threading.Tasks;

namespace BlazorApp1
{
    public static class Extensions
    {
        public static string GetEnumDescription<T>(this T value) where T : Enum
        {
            FieldInfo fi = value.GetType().GetField(value.ToString());
            if (fi == null)
                return value.ToString();

            DescriptionAttribute[] da = fi.GetCustomAttributes(typeof(DescriptionAttribute), false) as DescriptionAttribute[];
            if (da == null || da.Any())
                return da.First().Description;
            return value.ToString();
        }
    }
}
