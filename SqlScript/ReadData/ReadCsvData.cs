using SqlScript.Model;

namespace SqlScript.Reader;

public class CsvReader
{
    public async Task<List<Station>> readDataAsync(string path)
    {
        List<Station> stations = new List<Station>();
        var allData = await File.ReadAllLinesAsync(path);

        foreach (var line in allData)
        {
            var values = line.Split(',');
            var station = new Station
            {
                StationId = values[0],
                Name = values[1],
                Sector = values[2],
                Status = values[3]
            };

            stations.Add(station);
        }
        return stations;

    }
}