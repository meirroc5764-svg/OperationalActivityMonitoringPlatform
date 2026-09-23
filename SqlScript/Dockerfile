FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build

WORKDIR /app

COPY SqlScript.csproj .
RUN dotnet restore

COPY . .
RUN dotnet publish -c Release -o out --no-restore

FROM mcr.microsoft.com/dotnet/runtime:8.0

WORKDIR /app

COPY --from=build /app/out .

ENTRYPOINT ["dotnet", "SqlScript.dll"]