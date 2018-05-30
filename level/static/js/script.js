(function(){

    /* your code goes here */

    $(document).ready(function(){
        $("#content").text("")
        })
        $("#box").hide()
        $(".list-group>a").click(function(){
            $("#box").show()
        })
        $("#boxclose").click(function(){
            $("#box").hide()

        })

//        var source   = $("#entry-template").html();
//        var template = Handlebars.compile(source);
//
//
//                //用jquery获取模板
//        var tpl   =  $("#tpl").html();
//        //原生方法
//        var source = document.getElementById('#tpl').innerHTML;
//        //预编译模板
//        var template = Handlebars.compile(source);
//        //模拟json数据
//        var context = { name: "zhaoshuai", content: "learn Handlebars"};
//        //匹配json内容
//        var html = template(context);
//        //输入模板
//        $(body).html(html);
//
//        var context = {title: "My New Post", body: "This is my first post!"};
//        var html    = template(context);

        $.ajax({
                type: 'get',
                url: '/positions',
                async: true,
                success: function (data) {
                    $('.info0').html("<dl><dt>title</dt><dd>" +
                    data[0].title + "</dd></dl><dl><dt>location</dt><dd>"  +
                    data[0].location + "</dd></dl><dl><dt>type</dt><dd>"  +
                    data[0].type + "</dd></dl><dl><dt>Company Name</dt><dd>"  +
                    data[0].company + "</dd></dl><dl><dt>description</dt><dd>"  +
                    data[0].created_at + "</dd></dl>")

                    $('.info1').html("<dl><dt>title</dt><dd>" +
                    data[1].title + "</dd></dl><dl><dt>location</dt><dd>"  +
                    data[1].location + "</dd></dl><dl><dt>type</dt><dd>"  +
                    data[1].type + "</dd></dl><dl><dt>Company Name</dt><dd>"  +
                    data[1].company + "</dd></dl><dl><dt>description</dt><dd>"  +
                    data[1].created_at + "</dd></dl>")

                    $('.info2').html("<dl><dt>title</dt><dd>" +
                    data[2].title + "</dd></dl><dl><dt>location</dt><dd>"  +
                    data[2].location + "</dd></dl><dl><dt>type</dt><dd>"  +
                    data[2].type + "</dd></dl><dl><dt>Company Name</dt><dd>"  +
                    data[2].company + "</dd></dl><dl><dt>description</dt><dd>"  +
                    data[2].created_at + "</dd></dl>")

                    $('.info3').html("<dl><dt>title</dt><dd>" +
                    data[3].title + "</dd></dl><dl><dt>location</dt><dd>"  +
                    data[3].location + "</dd></dl><dl><dt>type</dt><dd>"  +
                    data[3].type + "</dd></dl><dl><dt>Company Name</dt><dd>"  +
                    data[3].company + "</dd></dl><dl><dt>description</dt><dd>"  +
                    data[3].created_at + "</dd></dl>")

                    $('.info4').html("<dl><dt>title</dt><dd>" +
                    data[4].title + "</dd></dl><dl><dt>location</dt><dd>"  +
                    data[4].location + "</dd></dl><dl><dt>type</dt><dd>"  +
                    data[4].type + "</dd></dl><dl><dt>Company Name</dt><dd>"  +
                    data[4].company + "</dd></dl><dl><dt>description</dt><dd>"  +
                    data[4].created_at + "</dd></dl>")

                    $('.info5').html("<dl><dt>title</dt><dd>" +
                    data[5].title + "</dd></dl><dl><dt>location</dt><dd>"  +
                    data[5].location + "</dd></dl><dl><dt>type</dt><dd>"  +
                    data[5].type + "</dd></dl><dl><dt>Company Name</dt><dd>"  +
                    data[5].company + "</dd></dl><dl><dt>description</dt><dd>"  +
                    data[5].created_at + "</dd></dl>")

                    $('.info6').html("<dl><dt>title</dt><dd>" +
                    data[6].title + "</dd></dl><dl><dt>location</dt><dd>"  +
                    data[6].location + "</dd></dl><dl><dt>type</dt><dd>"  +
                    data[6].type + "</dd></dl><dl><dt>Company Name</dt><dd>"  +
                    data[6].company + "</dd></dl><dl><dt>description</dt><dd>"  +
                    data[6].created_at + "</dd></dl>")

                    $('.info7').html("<dl><dt>title</dt><dd>" +
                    data[7].title + "</dd></dl><dl><dt>location</dt><dd>"  +
                    data[7].location + "</dd></dl><dl><dt>type</dt><dd>"  +
                    data[7].type + "</dd></dl><dl><dt>Company Name</dt><dd>"  +
                    data[7].company + "</dd></dl><dl><dt>description</dt><dd>"  +
                    data[7].created_at + "</dd></dl>")

                    $('.info8').html("<dl><dt>title</dt><dd>" +
                    data[8].title + "</dd></dl><dl><dt>location</dt><dd>"  +
                    data[8].location + "</dd></dl><dl><dt>type</dt><dd>"  +
                    data[8].type + "</dd></dl><dl><dt>Company Name</dt><dd>"  +
                    data[8].company + "</dd></dl><dl><dt>description</dt><dd>"  +
                    data[8].created_at + "</dd></dl>")

                    $('.info9').html("<dl><dt>title</dt><dd>" +
                    data[9].title + "</dd></dl><dl><dt>location</dt><dd>"  +
                    data[9].location + "</dd></dl><dl><dt>type</dt><dd>"  +
                    data[9].type + "</dd></dl><dl><dt>Company Name</dt><dd>"  +
                    data[9].company + "</dd></dl><dl><dt>description</dt><dd>"  +
                    data[9].created_at + "</dd></dl>")
                    }
                })




        })()
