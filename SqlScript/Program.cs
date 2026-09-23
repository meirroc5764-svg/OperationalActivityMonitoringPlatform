using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using SqlScript.connect;
using SqlScript.Reader;

var builder = Host.CreateApplicationBuilder(args);

var connectionString = builder.Configuration.GetConnectionString("Default");

Console.WriteLine(connectionString);

builder.Services.AddDbContext<StationSqlDbContext>(options =>
    options.UseMySql(
        connectionString,
        ServerVersion.AutoDetect(connectionString)));

using var host = builder.Build();

using var scope = host.Services.CreateScope();

var context = scope.ServiceProvider
    .GetRequiredService<StationSqlDbContext>();


var reader = new CsvReader();
var allData = await reader.readDataAsync("./../stations.csv");

await context.AddRangeAsync(allData);
await context.SaveChangesAsync();