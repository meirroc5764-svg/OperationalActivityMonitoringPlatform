using Microsoft.EntityFrameworkCore;
using SqlScript.Model;

namespace SqlScript.connect;
public class StationSqlDbContext : DbContext
{
    public StationSqlDbContext(DbContextOptions<StationSqlDbContext> options)
        : base(options)
    {

    }

    public DbSet<Station> Stations { get; set; }
}