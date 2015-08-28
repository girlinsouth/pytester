$(document).ready(function(){
 getallbug(1);
 $('#kwd').bind('input propertychange', function() {
    getallbug(1);
 });

 $("#pagesize").change(function(){
    getallbug(1);
 });

 $("#status").change(function(){
    getallbug(1);
 });

 $("#projects").change(function(){
    getallbug(1);
 });

});

function getallbug(page)
{
     var kwd = $("#kwd").val();
     var status = $("#status").val();
     var projects = $("#projects").val();
     var pagesize = $("#pagesize option:selected").text();
     var table=$("#bugdata");
     table.html("");
     var datapage=$("#datapage");
     datapage.html("");
     var thread = $('<thead><tr role="row"><th>ID</th><th>所属项目</th><th>标题</th><th>严重程度</th><th>优先级</th><th>指派给</th><th>解决者</th><th>解决方案</th><th>创建者</th><th>更新时间</th></tr></thead>')
     thread.appendTo(table);
     $.ajax({
            type : "GET",
            cache : false,/*不缓存数据*/
            url : "allbugs/",
            data : {"pagesize":pagesize,"page":page,"kwd":kwd,"status":status,"projects":projects},
            success : function(req,status)
            {
                 if(status == 'success')
                 {
                    var tbody=$("<tbody></tbody>");
                    tbody.appendTo(table);
                    var data=req.body.data;
                    outputtable(data,table);

                    var pages=req.body.pages;
                    outputpage(page,pages,datapage,"getallbug",kwd);
                 }
                 else
                 {
                     $("#bugdata").html("数据加载失败");
                 }
            }
     });
}

function outputtable(data,table)
{
  for(var i=0;i<data.length;i++)
  {
     var tr=$("<tr></tr>");
     tr.appendTo(table);
     for(columns in data[i])
     {
        var td=$("<td>"+data[i][columns]+"</td>");
        td.appendTo(tr);
     }
  }
}

function outputpage(page,pages,datapage,fcname,kwd)
{
    //第一页
    var firstli = $("<li><a href='javascript:"+fcname+"(1)"+"'>首页</a></li>");
    firstli.appendTo(datapage);

    //上一页
    if(page == 1)
    {
        var preli = $("<li class='disabled'><a>上一页</a></li>");
    }
    else
    {
        var preli = $("<li><a href='javascript:"+fcname+"("+(page-1)+")"+"'>上一页</a></li>");
    }
    preli.appendTo(datapage);

    //每一页
    for(var x=1;x<=pages;x++)
    {
       if(x==page)
       {
          var cli=$("<li class='active'></li>");//标识当前页
       }
       else
       {
          var cli=$("<li></li>");
       }

       var ca = $("<a href='javascript:"+fcname+"("+x+")"+"'>"+x+"</a>");
       ca.appendTo(cli);
       cli.appendTo(datapage);
    }

    //下一页
    if(page == pages)
    {
        var nextli = $("<li class='disabled'><a>下一页</a></li>");
    }
    else
    {
        var nextli=$("<li><a href='javascript:"+fcname+"("+(page+1)+")"+"'>下一页</a></li>");
    }
    nextli.appendTo(datapage);

    //最后一页
    var lastli = $("<li><a href='javascript:"+fcname+"("+pages+")"+"'>末页</a></li>");
    lastli.appendTo(datapage);
}


