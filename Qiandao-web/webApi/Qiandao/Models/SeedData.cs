using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;

namespace Qiandao.Models
{
    public static class SeedData
    {
        public static void Initialize(IServiceProvider serviceProvider)
        {
            using (var context = new ItemContext(
                serviceProvider.GetRequiredService<DbContextOptions<ItemContext>>()))
            {
                if (context.ItemList.Any())
                {
                    return;   
                }

                context.ItemList.Add(
                    new Item()
                    {
                        Id = 0,
                        Name = "seed",
                        BeginTime = DateTime.Now,
                        EndTime = DateTime.Now
                    }
                );
                context.SaveChanges();
            }
        }
    }
}
