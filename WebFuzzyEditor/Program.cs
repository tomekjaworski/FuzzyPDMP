﻿using System;
using System.Diagnostics;
using System.IO;
using System.Threading;
using System.Threading.Tasks;
using WebFuzzyEditor.Fuzzy;
using Highlight;
using Highlight.Engines;


using Microsoft.AspNetCore;
using Microsoft.AspNetCore.Hosting;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace WebFuzzyEditor
{
    public static class Program
    {
        public static void Main(string[] args)
        {
            string environment = Environment.GetEnvironmentVariable("ASPNETCORE_ENVIRONMENT");
            Console.WriteLine($"Środowisko: {environment}");
            Console.WriteLine($"Katalog roboczy: {Directory.GetCurrentDirectory()}");
            Console.WriteLine($"Wejście: {System.Reflection.Assembly.GetExecutingAssembly().Location}; PID:{Process.GetCurrentProcess().Id}");

            //
#if DEBUG
            BoardProvider.Provider.LoadBoard();
            PythonModelGenerator pmg = new PythonModelGenerator();
            pmg.ApplyBoard(BoardProvider.Board, "code_anfis.handlebars");
            while (true)
            {
                pmg.Run();
                string pc = pmg.PythonCode;
                Console.WriteLine(pc);
                return;
            }

#endif
            //
            //

            cts = new CancellationTokenSource();
            Thread th = new Thread(new ThreadStart(StoreThread));
            th.Start();
            CreateHostBuilder(args).Build().Run();
            cts.Cancel();
            th.Join();
            BoardProvider.Provider.StoreBoard();
        }

        private static CancellationTokenSource cts;
        private static void StoreThread()
        {
            CancellationToken ct = cts.Token;
            DateTime last_store = DateTime.Now;
            while (!ct.IsCancellationRequested)
            {
                Thread.Sleep(1000);
                DateTime now = DateTime.Now;
                if ((now - last_store).TotalSeconds < 60)
                    continue;

                last_store = now;
                BoardProvider.Provider.StoreBoard(); // todo: threadsafe
            }
        }

        public static IHostBuilder CreateHostBuilder(string[] args)
        {
            IHostBuilder hb = Host.CreateDefaultBuilder(args);

            hb.ConfigureWebHostDefaults(webBuilder =>
            {

                //webBuilder.UseUrls("http://*:11000");
                webBuilder.UseStartup<Startup>();
            });

            return hb;
        }
    }
}
