using System;
using System.IO;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace analyse_typedefs
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            var url = @"C:\repos\4.c0\metadata-samples\metadata-utility-services\analyser-algorithms\analyse-typedefs\analyse-typedefs\typedefs.json";
            JObject typedefs = JObject.Parse(File.ReadAllText(url));
            Simulator sim = new Simulator();
            var typeDefs_string = JsonConvert.SerializeObject(typedefs);
            var flattenTypeDefs = sim.flattenJson(typeDefs_string);
            Console.Write(flattenTypeDefs);
            Console.ReadKey();
        }
    }
}
