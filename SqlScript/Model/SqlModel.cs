using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace SqlScript.Model;

public class Station
{
    [Key]
    [Column("station_id")]
    [StringLength(50)]
    public string Id {  get; set; }

    [Column("name")]
    [StringLength(100)]
    public string Name { get; set; }

    [Column("sector")]
    [StringLength(100)]
    public string Sector {  get; set; }

    [Column("status")]
    [StringLength(20)]
    public string Status { get; set; }

    public DateTime CreateAt { get; set; }= DateTime.Now;
}