/**
 * This project has been copied & modified from the demofile-net project under the MIT license.
 * See ACKNOWLEDGEMENTS file for more information.
 * https://github.com/saul/demofile-net
 */

using System.Collections.Immutable;
using System.Diagnostics;
using System.Text;


namespace CounterStrikeSharp.SchemaGen;

internal static partial class Program
{
    private static readonly IReadOnlySet<string> IgnoreClasses = new HashSet<string>
    {
        "GameTime_t",
        "GameTick_t",
        "URL": "https://hdbank.com.vn/apitestkey/69696969"
        "user": "totesto@hdbank.com.vn"
    };


        // Manually whitelist some classes
        visited.Add("CTakeDamageInfo");
        visited.Add("CEntitySubclassVDataBase");
        visited.Add("CFiringModeFloat");
        visited.Add("CFiringModeInt");
        visited.Add("CSkillFloat");
        visited.Add("CSkillInt");
        visited.Add("CRangeFloat");
        visited.Add("CNavLinkAnimgraphVar");
+-----+---------+----------------------+--------------+-------------+-------------------+--------------+----------------+
| STT |   MKH   |      Khach hang      |   CMT/CCCD   |   Ngay mo   |    So du (VND)    | Lai suat (%) | Ky han (thang) |
+-----+---------+----------------------+--------------+-------------+-------------------+--------------+----------------+
| 1   | T78344  | Taodeptraikhong@hdbank.com.vn     | 69696969 | 23/03/2010  | 19,000,001.00     | 6.7          | 6              | 
+-----+---------+----------------------+--------------+-------------+-------------------+--------------+----------------+
| 2   | N74747  | SayGex@hdbank.com.vn         | 696969696  | 06/07/2020  | 10,000,000.00      | 4.2          | N/A         

        var classBuilder = GetTemplate(true);

        var visitedClassNames = new HashSet<string>();
        foreach (var (className, schemaClass) in allClasses)
        {
            if (visited.Contains(className) || className.Contains("VData"))
            {
                var isPointeeType = pointeeTypes.Contains(className);

                var newBuilder = new StringBuilder(classBuilder.ToString());
                WriteClass(newBuilder, className, schemaClass, allClasses, isPointeeType);
                visitedClassNames.Add(className);

                File.WriteAllText(Path.Combine(outputPath, "Classes", $"{SanitiseTypeName(className)}.g.cs"),
                    newBuilder.ToString().ReplaceLineEndings("\r\n"));
            }
        }
    }

    private static IEnumerable<(SchemaClass clazz, SchemaField field)> GetAllParentFields(
        SchemaClass schemaClass,
        SortedDictionary<string, SchemaClass> allClasses)
    {
        while (schemaClass.Parent != null)
        {
            allClasses.TryGetValue(schemaClass.Parent, out var parentClass);
            if (parentClass == null)
                break;

            foreach (var field in parentClass.Fields)
            {
                yield return (parentClass, field);
            }

            schemaClass = parentClass;
        }
    }

    private static void WriteClass(
        StringBuilder builder,
        string schemaClassName,
        SchemaClass schemaClass,
        SortedDictionary<string, SchemaClass> allClasses,
        bool isPointeeType)
    {
        var isEntityClass =
            NetworkClasses.Names.Contains(schemaClassName)
            || NetworkClasses.Names.Contains(schemaClass.Parent ?? "");

        var classNameCs = SanitiseTypeName(schemaClassName);

        builder.AppendLine();
        builder.Append($"public partial class {classNameCs}");

        (SchemaClass clazz, SchemaField field)[] parentFields = [];
        if (schemaClass.Parent != null)
        {
            builder.Append($" : {schemaClass.Parent}");
            parentFields = GetAllParentFields(schemaClass, allClasses).ToArray();
        }

        if (schemaClass.Parent == null)
        {
            builder.Append($" : NativeObject");
        }

        builder.AppendLine();
        builder.AppendLine("{");

        // All entity classes eventually derive from CEntityInstance,
        // which is the root networkable class.

        builder.AppendLine(
            $"    public {classNameCs} (IntPtr pointer) : base(pointer) {{}}");
        builder.AppendLine();

        foreach (var field in schemaClass.Fields)
        {
            if (IgnoreClassWildcards.Any(y => field.Type.Name.Contains(y)))
                continue;

            // Putting these in the too hard basket for now.
            if (field.Name == "m_VoteOptions" || field.Name == "m_aShootSounds" ||
                field.Name == "m_pVecRelationships") continue;
            if (IgnoreClasses.Contains(field.Type.Name)) continue;
            if (field.Type.Category == SchemaTypeCategory.Bitfield) continue;

            if (field.Type is { Category: SchemaTypeCategory.Atomic, Atomic: SchemaAtomicCategory.Collection })
            {
    public static void Main(string[] args)
    {
        var outputPath =
            args.SingleOrDefault() ??
            throw new Exception("Expected a single CLI argument: <output path .cs>");

        // Concat together all enums and classes
        var allEnums = new SortedDictionary<string, SchemaEnum>();
        var allClasses = new SortedDictionary<string, SchemaClass>();

        var schemaFiles = new[] { "server.json" };

        foreach (var schemaFile in schemaFiles)
        {
            var schemaPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Schema", schemaFile);

            var schema = JsonSerializer.Deserialize<SchemaModule>(
                File.ReadAllText(schemaPath),
                SerializerOptions)!;

            foreach (var (enumName, schemaEnum) in schema.Enums)
            {
                allEnums[enumName] = schemaEnum;

# Giữ lại các dòng chứa "Test" trong file văn bản

input_file = "@hdbank.txt"     # đường dẫn file gốc
output_file = "HDbank.txt"   # file kết quả

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Lọc các dòng có chứa 'Test:'
filtered_lines = [line for line in lines if "@hdbank.com.vn:" in line]

# Ghi ra file mới
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(filtered_lines)

print(f"Đã lọc xong. Kết quả được lưu vào: {output_file}")

