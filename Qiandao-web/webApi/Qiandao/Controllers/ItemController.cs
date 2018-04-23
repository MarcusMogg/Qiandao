using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Qiandao.Models;

// For more information on enabling MVC for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace Qiandao.Controllers
{
    [Route("[controller]/[action]")]
    public class ItemController : Controller
    {
        private readonly ItemContext _context;

        public ItemController(ItemContext context)
        {
            _context = context;
        }

        [HttpGet]
        public IEnumerable<Item> GetAll()
        {
            return _context.ItemList.ToList();
        }

        [HttpGet("{name}")]
        public IActionResult GetByName(string name)
        {
            var res = from i in _context.ItemList
                      where i.Name.Contains(name)
                      select i;
            if (!res.Any())
            {
                return NotFound();
            }
            return new ObjectResult(res);
        }

        [HttpGet("btime={btime}&etime={etime}")]
        public IActionResult GetByTime(DateTime btime, DateTime etime)
        {
            var res = from i in _context.ItemList
                      where i.BeginTime > btime && i.EndTime < etime
                      select i;
            if (!res.Any())
            {
                return NotFound();
            }
            return new ObjectResult(res);
        }
    }
}
