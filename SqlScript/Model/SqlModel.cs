using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace SqlScript.Model;

public class Station
{
    [Key]
    [Column("station_id")]
    public string StationId {  get; set; }

    [Column("name")]
    public string Name { get; set; }

    [Column("sector")]
    public string Sector {  get; set; }

    [Column("status")]
    public string Status { get; set; }
}