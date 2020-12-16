#dotnet run --configuration Release --launch-profile Production 
set ASPNETCORE_ENVIRONMENT=Development
WebFuzzyEditor.exe --urls=http://*:11000/
set ASPNETCORE_ENVIRONMENT=
