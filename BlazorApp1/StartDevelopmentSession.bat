#dotnet run --configuration Release --launch-profile Production 
set ASPNETCORE_ENVIRONMENT=Development
BlazorApp1.exe --urls=http://*:11000/
set ASPNETCORE_ENVIRONMENT=
