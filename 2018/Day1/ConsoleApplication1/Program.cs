using System;
using System.Collections.Generic;
using System.IO;

namespace ConsoleApplication1
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var lines = File.ReadAllLines(
                "D:\\Code\\AdventOfCode_2018\\AdventOfCode_Day1\\adventOfCode_Day1_input.txt");

            var result = 0;
            HashSet<int> duplicateFreqDetectionDict = new HashSet<int>();
            var duplicateFound = false;
            
            while (!duplicateFound)
                foreach (var line in lines)
                {
                    int number;
                    if (int.TryParse(line, out number))
                        result += number;

                    if (duplicateFreqDetectionDict.Contains(result))
                    {
                        duplicateFound = true;
                        break;
                    }
                        
                    duplicateFreqDetectionDict.Add(result);
                }
            
            Console.WriteLine(result);
        }
    }
}