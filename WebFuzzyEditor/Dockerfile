#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:5.0-buster-slim AS base
WORKDIR /app
EXPOSE 11000/tcp

FROM mcr.microsoft.com/dotnet/sdk:5.0-buster-slim AS build
WORKDIR /src
COPY ["WebFuzzyEditor/WebFuzzyEditor.csproj", "WebFuzzyEditor/"]
RUN dotnet restore "WebFuzzyEditor/WebFuzzyEditor.csproj"
COPY . .
WORKDIR "/src/WebFuzzyEditor"
RUN dotnet build "WebFuzzyEditor.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "WebFuzzyEditor.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .

ENTRYPOINT ["dotnet", "WebFuzzyEditor.dll"]
