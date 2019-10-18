using System;
using System.Collections.Generic;
using System.Text;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.IO;
using System.Globalization;
using System.Linq;

namespace analyse_typedefs
{
    public class Simulator
    {

        // Function that processes flat json into a JSON object - to be used in the ui for building data type .json
        public JObject AnalyseValues(JObject obj, JObject baseObject)
        {
            JObject jObject;
            List<string> processedArrays = new List<string>();
            if (baseObject != null)
            {
                jObject = baseObject;
            }
            else
            {
                jObject = new JObject();
            }

            foreach (KeyValuePair<string, JToken> property in obj)
            {
                //Check if the value is simple create a JValue
                if (!property.Key.ToString().Contains('[') && !property.Key.ToString().Contains('.'))
                {

                    JValue val = new JValue(property.Value.ToString());
                    jObject[property.Key] = val;


                }
                else
                {
                    // Check if its a simple array
                    if (!property.Key.ToString().Contains('.') && property.Key.ToString().Contains('['))
                    {
                        // If its a simple array the first word will always be the name
                        string[] arrayName = property.Key.ToString().Split('[');
                        // The array element has been processed
                        if (jObject.ContainsKey(arrayName[0]))
                        {
                            JArray arr = (JArray)jObject[arrayName[0]];
                            arr.Add(property.Value.ToString());
                        }
                        else
                        {
                            jObject.Add(arrayName[0], new JArray());
                            JArray arr = (JArray)jObject[arrayName[0]];
                            arr.Add(property.Value.ToString());
                        }
                    }
                    // Check if its an object
                    if (property.Key.ToString().Contains('.') && !property.Key.ToString().Contains('['))
                    {
                        string[] keyNames = property.Key.ToString().Split('.');
                        if (keyNames.Length == 2)
                        {
                            // Simple object
                            if (jObject.ContainsKey(keyNames[0]))
                            {
                                JObject kn = (JObject)jObject[keyNames[0]];
                                kn[keyNames[1]] = property.Value.ToString();
                            }
                            else
                            {
                                jObject.Add(keyNames[0], new JObject());
                                JObject kn = (JObject)jObject[keyNames[0]];
                                kn[keyNames[1]] = property.Value.ToString();

                            }

                        }
                        else
                        {
                            // Complex object, Call Analyse values recursively

                            JObject nObj = new JObject();
                            nObj[property.Key.ToString().Replace(keyNames[0] + ".", "")] = property.Value.ToString();
                            if (jObject.ContainsKey(keyNames[0]))
                            {
                                jObject.Add(new JObject(keyNames[0]));
                                jObject[keyNames[0]] = AnalyseValues(nObj, null);
                            }
                            else
                            {
                                jObject[keyNames[0]] = AnalyseValues(nObj, null);
                            }




                        }
                    }

                    if (property.Key.ToString().Contains('.') && property.Key.ToString().Contains('['))
                    {
                        if (property.Key.ToString().IndexOf('.') < property.Key.ToString().IndexOf('['))
                        {
                            // Complex Object with an array ; x.y.z[0]
                            string[] keyNames = property.Key.ToString().Split('.');
                            JObject nObj = new JObject();
                            nObj[property.Key.ToString().Replace(keyNames[0] + ".", "")] = property.Value.ToString();
                            if (jObject.ContainsKey(keyNames[0]))
                            {
                                jObject.Add(new JObject(keyNames[0]));
                                jObject[keyNames[0]] = AnalyseValues(nObj, null);
                            }
                            else
                            {
                                jObject[keyNames[0]] = AnalyseValues(nObj, null);
                            }


                        }
                        else
                        {
                            // Array of complex objects; x[0].y.z[0]...


                            string[] keyNames = property.Key.ToString().Split('[');

                            string propertyToCheck = "";
                            if (!processedArrays.Contains(property.Key.ToString().Split('.')[0]))
                            {
                                string[] eKn = property.Key.ToString().Split(']');

                                if (property.Key.ToString().Substring(property.Key.ToString().IndexOf(']') + 1, 1) == ".")
                                {
                                    // Split keys by . to get the names
                                    string[] ks = property.Key.ToString().Split('.');
                                    JObject nObj = new JObject();
                                    //nObj[property.Key.ToString().Replace(ks[0] + ".", "")] = property.Value.ToString();

                                    if (jObject.ContainsKey(keyNames[0]))
                                    {

                                        // JArray t = (JArray)jObject[keyNames[0]];
                                        //t.Add(AnalyseValues(nObj, null));
                                        JObject tObj = new JObject();
                                        tObj[property.Key.ToString().Replace(ks[0] + ".", "")] = property.Value.ToString();
                                        JObject ttobj = AnalyseValues(tObj, null);
                                        foreach (KeyValuePair<string, JToken> kvp in ttobj)
                                        {
                                            nObj[kvp.Key] = kvp.Value;
                                        }

                                    }
                                    else
                                    {
                                        jObject.Add(keyNames[0], new JArray());
                                        JObject tObj = new JObject();
                                        tObj[property.Key.ToString().Replace(ks[0] + ".", "")] = property.Value.ToString();
                                        propertyToCheck = property.Key.ToString().Replace(ks[0] + ".", "");
                                        JObject ttobj = AnalyseValues(tObj, null);
                                        foreach (KeyValuePair<string, JToken> kvp in ttobj)
                                        {
                                            nObj[kvp.Key] = kvp.Value;
                                        }
                                        // nObj.Add(new JObject(ttobj));

                                    }
                                    // loop through for all the objects in the same array element, add the array element in processedArrays list so this process is skipped
                                    foreach (KeyValuePair<string, JToken> p in obj)
                                    {
                                        string[] kns = p.Key.ToString().Split(']');
                                        if (kns[0] == eKn[0])
                                        {
                                            string[] k = p.Key.ToString().Split('.');
                                            //TODO_SHG: This code is a repeat of code above, try and optimize it later
                                            JObject tObj = new JObject();
                                            // Have already processed the first object in the array above
                                            if (p.Key.ToString().Replace(k[0] + ".", "") != propertyToCheck)
                                            {
                                                tObj[p.Key.ToString().Replace(k[0] + ".", "")] = p.Value.ToString();
                                                // JArray t = (JArray)jObject[keyNames[0]];
                                                JObject ttobj = AnalyseValues(tObj, null);
                                                foreach (KeyValuePair<string, JToken> kvp in ttobj)
                                                {
                                                    nObj[kvp.Key] = kvp.Value;
                                                }
                                            }

                                            // nObj.Add(new JObject(ttobj));



                                        }
                                    }

                                    JArray t = (JArray)jObject[keyNames[0]];
                                    t.Add(nObj);
                                    processedArrays.Add(property.Key.ToString().Split('.')[0]);
                                }
                                else
                                {
                                    JValue val = new JValue(property.Value.ToString());
                                    jObject[property.Key] = val;

                                    // Treat as simple value not an array of complex objects
                                }
                            }



                        }
                    }
                }
            }
            return jObject;
        }
        // Function generates a random value based on the description in the data types file
        // TODO_SHG: Currently the function will be returning a string representation for all data types including numbers and bool
        // Will always return a single value

        // Functions that flatten an input JSON and generate data types and a flat JSON structure
        // These to be used in building ui for dt_**.json
        private const string flattenedJsonPropName = "flattenedJson";
        private const string dataTypesJsonPropName = "dataTypesJson";

        public JObject flattenJson(string jsonString)
        {


            JObject jObject = JObject.Parse(jsonString);
            bool isVal = jObject.HasValues;
            JObject analysedJson = AnalyseJson(jObject, "");

           // Console.ReadKey();
            return analysedJson;

            //throw new NotImplementedException();
        }
        public JObject AnalyseJson(JObject obj, string prefix_key)
        {
            JObject jFlattenedJson = new JObject();
            JObject jJsonDataTypes = new JObject();

            foreach (KeyValuePair<string, JToken> property in obj)
            {

                // Simple Values
                if (property.Value.GetType() == typeof(Newtonsoft.Json.Linq.JValue))
                {
                    if (prefix_key.Length > 0)
                    {
                        jFlattenedJson[prefix_key + "." + property.Key] = property.Value.ToString();
                        jJsonDataTypes[prefix_key + "." + property.Key] = AnalyseSimpleValue(property.Value.ToString(), prefix_key + "." + property.Key);
                    }
                    else
                    {
                        jFlattenedJson[property.Key.ToString()] = property.Value.ToString();
                        jJsonDataTypes[property.Key.ToString()] = AnalyseSimpleValue(property.Value.ToString(), prefix_key + "." + property.Key);

                    }

                }
                // It is an array
                if (property.Value.GetType() == typeof(Newtonsoft.Json.Linq.JArray))
                {
                    int i = 0;
                    foreach (var item in property.Value)
                    {

                        if (!item.HasValues)
                        {
                            if (prefix_key.Length > 0)
                            {
                                jFlattenedJson[prefix_key + "." + property.Key + "[" + i + "]"] = item.ToString();
                                jJsonDataTypes[prefix_key + "." + property.Key + "[" + i + "]"] = AnalyseSimpleValue(item.ToString(), prefix_key + "." + property.Key + "[" + i + "]");
                            }
                            else
                            {
                                jFlattenedJson[property.Key + "[" + i + "]"] = item.ToString();
                                jJsonDataTypes[property.Key + "[" + i + "]"] = AnalyseSimpleValue(item.ToString(), property.Key + "[" + i + "]");
                            }
                        }
                        else
                        {
                            JObject o = JObject.Parse(item.ToString());
                            JObject retO = new JObject();
                            if (prefix_key.Length > 0)
                            {

                                retO = AnalyseJson(o, prefix_key + "." + property.Key + "[" + i + "]");
                                foreach (JProperty kv in retO[flattenedJsonPropName])
                                {
                                    jFlattenedJson.Add(kv);
                                }
                                foreach (JProperty kv in retO[dataTypesJsonPropName])
                                {
                                    jJsonDataTypes.Add(kv);
                                }


                            }
                            else
                            {
                                retO = AnalyseJson(o, property.Key + "[" + i + "]");
                                foreach (JProperty kv in retO[flattenedJsonPropName])
                                {
                                    jFlattenedJson.Add(kv);
                                }
                                foreach (JProperty kv in retO[dataTypesJsonPropName])
                                {
                                    jJsonDataTypes.Add(kv);
                                }

                            }

                        }
                        i++;
                    }

                }
                // Its a complex object
                if (property.Value.GetType() == typeof(Newtonsoft.Json.Linq.JObject))
                {
                    JObject retO = new JObject();

                    if (prefix_key.Length > 0)
                    {
                        retO = AnalyseJson(JObject.Parse(property.Value.ToString()), prefix_key + "." + property.Key);
                        foreach (JProperty kv in retO[flattenedJsonPropName])
                        {
                            jFlattenedJson.Add(kv);
                        }
                        foreach (JProperty kv in retO[dataTypesJsonPropName])
                        {
                            jJsonDataTypes.Add(kv);
                        }
                    }
                    else
                    {
                        retO = AnalyseJson(JObject.Parse(property.Value.ToString()), property.Key);
                        foreach (JProperty kv in retO[flattenedJsonPropName])
                        {
                            jFlattenedJson.Add(kv);
                        }
                        foreach (JProperty kv in retO[dataTypesJsonPropName])
                        {
                            jJsonDataTypes.Add(kv);
                        }

                    }
                }
            }
            // TODO_SHG: Is there a better way??
            JObject retresponse = new JObject();
            retresponse[flattenedJsonPropName] = jFlattenedJson;
            retresponse[dataTypesJsonPropName] = jJsonDataTypes;
            return retresponse;
        }
        public string AnalyseSimpleValue(string value, string prefix_key)
        {
            string valueDataType = "string";
            char firstChar = value.ToCharArray()[0];

            // string lastProcessedArray
            // If its starting with a 0, it may be a alphanumeric, number as string and needs to be treated as string
            if (firstChar != '0')
            {
                // Check if long  -- no seperate check for int
                bool isAllDigit = value.All(char.IsDigit);
                if (isAllDigit)
                {
                    valueDataType = "long";
                }
                else
                {
                    // Ensuring that doubles are also taken care of
                    if (double.TryParse(value, out double res))
                    {
                        valueDataType = "double";
                    }
                    else
                    {
                        // Check if bool
                        if (bool.TryParse(value, out bool boolRes))
                        {
                            valueDataType = "bool";
                        }
                    }
                }
            }
            else
            {
                // Check if the value is a date by parsing it into one of the formats, if the parse fails treat it as a string
                // Else treat it as a date time
                string[] formats = { "MM/dd/yyyy", "M/d/yyyy h:mm:ss tt", "M/d/yyyy h:mm tt",
                   "MM/dd/yyyy hh:mm:ss", "M/d/yyyy h:mm:ss",
                   "M/d/yyyy hh:mm tt", "M/d/yyyy hh tt",
                   "M/d/yyyy h:mm", "M/d/yyyy h:mm",
                   "MM/dd/yyyy hh:mm", "M/dd/yyyy hh:mm", "mm-dd-yyyy" };
                DateTime parsedDateTime;
                if (DateTime.TryParseExact(value, formats, new CultureInfo("en-US"), DateTimeStyles.None, out parsedDateTime))
                {
                    valueDataType = "datetime";
                }
                // Else its a number starting with 0, or a alphanumeric both need to be treated as strings
            }
            return valueDataType;
        }

        // Functions to generate Random JSON object from given dt_**.json

        public JObject generateRandomJson(JObject dtObject)
        {
            // Default Lengths
            long strLength = 10;
            JObject outJson = new JObject();
            // Loop through  the datatype json to generare              
            foreach (KeyValuePair<string, JToken> kv in dtObject)
            {
                JObject dt = JObject.Parse(kv.Value.ToString());
                string dtType = "";
                if (dt.ContainsKey("type"))
                {
                    dtType = dt["type"].ToString().ToLower();
                }
                if (dtType == "string")
                {
                    long startRange = 0;
                    long endRange = 0;
                    if (dt.ContainsKey("startRange"))
                    {
                        long.TryParse(dt["startRange"].ToString(), out startRange);
                    }
                    if (dt.ContainsKey("endRange"))
                    {
                        long.TryParse(dt["endRange"].ToString(), out endRange);
                    }
                    strLength = Math.Abs(endRange - startRange);



                    outJson[kv.Key.ToString()] = generateRandomString(strLength);

                }
                if (dtType == "bool")
                {
                    Random rnd = new Random();
                    int b = rnd.Next(0, 1);
                    bool.TryParse(b.ToString(), out bool res);
                    outJson[kv.Key.ToString()] = res.ToString();
                }
                if (dtType == "guid")
                {
                    outJson[kv.Key.ToString()] = Guid.NewGuid().ToString();
                }
                if (dtType == "double")
                {
                    int startRange = 0;
                    int endRange = 0;
                    if (dt.ContainsKey("startRange") && dt.ContainsKey("endRange"))
                    {
                        int.TryParse(dt["startRange"].ToString(), out startRange);
                        int.TryParse(dt["endRange"].ToString(), out endRange);

                    }
                    outJson[kv.Key.ToString()] = generateRandomDouble(startRange, endRange);
                }
                //TODO_SHG treat long and int as two different values
                if (dtType == "int" || dtType == "long")
                {
                    int startRange = 0;
                    int endRange = 0;
                    if (dt.ContainsKey("startRange") && dt.ContainsKey("endRange"))
                    {
                        int.TryParse(dt["startRange"].ToString(), out startRange);
                        int.TryParse(dt["endRange"].ToString(), out endRange);

                    }
                    outJson[kv.Key.ToString()] = generateRandomInt(startRange, endRange);

                }
                if (dtType == "datetime")
                {
                    string res = "";
                    if (dt.ContainsKey("endRange"))
                    {

                        int endRangeinDays = 0;
                        if (int.TryParse(dt["endRange"].ToString(), out endRangeinDays))
                        {
                            res = generateRandomDate(endRangeinDays);
                        }
                    }
                    else
                    {
                        res = generateRandomDate();
                    }

                    outJson[kv.Key.ToString()] = res.ToString();

                }
                if (dtType == "value.list")
                {
                    JArray valuesList = (JArray)dt["values"];
                    List<string> vals = valuesList.ToObject<List<string>>();
                    string res = generateRandomListValue(vals);
                    outJson[kv.Key.ToString()] = res.ToString();
                }

                if (dtType == "array")
                {
                    int arrLength = 0;
                    if (dt.ContainsKey("values"))
                    {
                        JArray valuesList = (JArray)dt["values"];
                        List<string> vals = valuesList.ToObject<List<string>>();
                        if (dt.ContainsKey("startRange") && dt.ContainsKey("endRange"))
                        {
                            int startRange = 0;
                            int endRange = 0;
                            if (int.TryParse(dt["startRange"].ToString(), out startRange) && int.TryParse(dt["endRange"].ToString(), out endRange))
                            {
                                arrLength = Math.Abs(endRange - startRange);
                            }

                        }
                        outJson[kv.Key.ToString()] = JArray.FromObject(generateRandomList(vals, arrLength));
                    }
                    else
                    {
                        outJson[kv.Key.ToString()] = dt.ToString();
                    }

                }
                if (dtType == "complex")
                {
                    if (dt.ContainsKey("body"))
                    {
                        JArray complexVal = JArray.Parse(dt["body"].ToString());
                        if (complexVal.HasValues)
                        {

                            try
                            {
                                JObject value = new JObject();
                                outJson.Add(kv.Key.ToString(), new JObject());
                                for (int i = 0; i < complexVal.Count; i++)
                                {
                                    JObject tObj = JObject.Parse(complexVal[i].ToString());
                                    JObject obj = generateRandomJson(tObj);
                                    foreach (KeyValuePair<string, JToken> k in obj)
                                    {
                                        value[k.Key.ToString()] = k.Value;
                                    }

                                }

                                outJson[kv.Key.ToString()] = value;

                            }
                            catch (Exception e)
                            {
                                // Treat it as a string value
                                outJson[kv.Key.ToString()] = dt.ToString();
                            }
                        }
                        else
                        {
                            // Treat it as a string value
                            outJson[kv.Key.ToString()] = dt.ToString();
                        }
                    }
                    else
                    {
                        // Treat it as a string value
                        outJson[kv.Key.ToString()] = dt.ToString();

                    }

                }
                if (dtType == "array.complex")
                {
                    if (dt.ContainsKey("body"))
                    {
                        JArray complexVal = JArray.Parse(dt["body"].ToString());
                        if (complexVal.HasValues)
                        {
                            outJson.Add(kv.Key.ToString(), new JArray());
                            JArray jArr = (JArray)outJson[kv.Key.ToString()];
                            try
                            {
                                if (dt.ContainsKey("startRange") && dt.ContainsKey("endRange"))
                                {
                                    int.TryParse(dt["startRange"].ToString(), out int startRange);
                                    int.TryParse(dt["endRange"].ToString(), out int endRange);
                                    Random rnd = new Random();
                                    int length = rnd.Next(startRange, endRange);
                                    for (int i = 0; i < length - 1; i++)
                                    {

                                        JObject value = new JObject();
                                        //outJson.Add(kv.Key.ToString(), new JObject());
                                        for (int j = 0; j < complexVal.Count; j++)
                                        {
                                            JObject tObj = JObject.Parse(complexVal[j].ToString());
                                            JObject obj = generateRandomJson(tObj);
                                            foreach (KeyValuePair<string, JToken> k in obj)
                                            {
                                                value[k.Key.ToString()] = k.Value;
                                            }

                                        }
                                        jArr.Add(value);
                                    }
                                }
                                else
                                {

                                    JObject value = new JObject();
                                    //outJson.Add(kv.Key.ToString(), new JObject());
                                    for (int l = 0; l < complexVal.Count; l++)
                                    {
                                        JObject tObj = JObject.Parse(complexVal[l].ToString());
                                        JObject obj = generateRandomJson(tObj);
                                        foreach (KeyValuePair<string, JToken> k in obj)
                                        {
                                            value[k.Key.ToString()] = k.Value;
                                        }

                                    }
                                    jArr.Add(value);
                                }



                            }
                            catch (Exception e)
                            {
                                // Treat it as a string value
                                outJson[kv.Key.ToString()] = dt.ToString();
                            }
                        }
                        else
                        {
                            // Treat it as a string value
                            outJson[kv.Key.ToString()] = dt.ToString();
                        }
                    }
                    else
                    {
                        // Treat it as a string value
                        outJson[kv.Key.ToString()] = dt.ToString();

                    }

                }

            }



            return outJson;
        }
        public string generateRandomString(long strLength)
        {
            // ASCII: A-65, Z-90
            string rndString = "";
            Random rnd = new Random();
            for (long i = 0; i < strLength; i++)
            {
                rndString = rndString + Char.ConvertFromUtf32(rnd.Next(65, 90));
            }
            return rndString.ToLower();
        }
        public int generateRandomInt(int startRange, int endRange)
        {
            int val = 0;
            Random rnd = new Random();
            if (startRange > 0 && endRange > 0 && startRange < endRange)
            {
                val = rnd.Next(startRange, endRange);
            }
            else
            {
                val = rnd.Next();
            }
            return val;
        }
        public double generateRandomDouble(double startRange, double endRange)
        {
            double val = 0;
            Random rnd = new Random();
            if (startRange > 0 && endRange > 0 && startRange < endRange)
            {
                val = rnd.NextDouble() * (rnd.Next((int)Math.Round(startRange, 0), (int)Math.Round(endRange, 0)));
            }
            else
            {
                val = rnd.NextDouble() * rnd.Next();
            }
            return val;
        }
        public string generateRandomDate(int endRange = 0)
        {
            DateTime start = DateTime.UtcNow;
            // This random date code is not working, for the timebeing replaced it with current DateTime
            /*
            DateTime start = new DateTime(1995, 1, 1);
           Random gen = new Random();
            int range = 0;
            if (endRange>0)
            {
                start = DateTime.Today.AddDays(double.Parse((gen.NextDouble()* endRange).ToString()));
             }
            else
            {
                range = (DateTime.Today - start).Days;
                start.AddDays(gen.Next(range,range+100)).AddHours(gen.Next(0, 24)).AddMinutes(gen.Next(0, 60)).AddSeconds(gen.Next(0, 60));
            }
           */

            return start.ToString();
        }
        public string generateRandomListValue(List<string> listValues)
        {
            Random rnd = new Random();
            string val = listValues[rnd.Next(listValues.Count - 1)];
            return val;
        }
        public List<string> generateRandomList(List<string> listValues, int length)
        {
            // Using HasSet to ensure the list values are not repeated
            Random rnd = new Random();
            List<string> val = new List<string>();
            if (length > 0)
            {
                length = rnd.Next(listValues.Count);
            }
            // If the length is less than list values
            if (length < listValues.Count)
            {
                HashSet<int> uniqueNumbers = new HashSet<int>();
                int cnt = 0;
                while (cnt <= length)
                {
                    int index = rnd.Next(listValues.Count - 1);
                    if (uniqueNumbers.Add(index))
                    {
                        val.Add(listValues[index]);
                        cnt++;
                    }
                }
            } // Else return the whole list
            else
            {
                val = listValues;
            }

            return val;
        }

    }
}


namespace JsonOperationsSimulators
{
   
}
