using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;

namespace Qiandao.Models
{
    public class Item
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public DateTime BeginTime { get; set; }
        public DateTime EndTime { get; set; }
    }

    public class ItemContext : DbContext
    {
        public DbSet<Item> ItemList { get; set; }

        public ItemContext(DbContextOptions<ItemContext> options)
            : base(options)
        {
        }
    }

}
