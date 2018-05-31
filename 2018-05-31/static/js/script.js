(function () {
    $("#positionBox").hide();
    $("#popup").click(function () {
        $("#positionBox").show()
    });
    $("#boxclose").click(function () {
        $("#positionBox").hide()
    });

    function getDateTimeStamp(dateStr) {
        return Date.parse(dateStr.replace(/-/gi, "/"));
    }

    $.ajaxSetup({
        error: function () {
            alert('ajax failed');
            return false;
        }
    });
    //
    // $.getJSON('../positions.json', function (data) {
    //     console.log(data);
    //     var t = $('#positionLists').html();
    //     var f = Handlebars.compile(t);
    //     var h = f(data);
    //     $('#popup').html(h);
    //
    //     var detail = $('#positionDetails').html();
    //     var jd = Handlebars.compile(detail);
    //     var jdb = jd(data);
    //     $('#positionDetail').html(jdb);
    // });

    $.ajax({
        type: 'get',
        url: '../positions.json',
        async: true,
        success: function (data) {
            var t = $('#positionLists').html();
            var f = Handlebars.compile(t);
            var h = f(data);
            console.log(data);
            $('#popup').html(h);

            var detail = $('#positionDetails').html();
            var jd = Handlebars.compile(detail);
            var jdb = jd(data);
            $('#positionDetail').html(jdb);

            var head = $('#heads').html();
            var hea = Handlebars.compile(head);
            var he = hea(data);
            $('#head').html(he);

            for (i = 0; i < 10; i++) {
                // var timestamp = Date.parse(new Date(date));
                // var timestamp_now = Date.parse(new Date());
                var time_list = new Array();
                // a = timestamp_now-timestamp;
                var time_num = getDateTimeStamp(data[i].created_at);
                if (getDateTimeStamp(data[i].created_at) > getDateTimeStamp(data[i + 1].created_at)) {
                    time_list.push(i)
                }
                else (time_list.push(i + 1));
                // console.log(time_list.sort());
                console.log(time_list, "=>", i)
            }


            //search
            var titles = new Array();
            var tt = titles.push(data[0].title);
            $("input[type=text]").change(function () {
                var searchText = $(this).val();//获取输入的搜索内容
                var $searchLi = "";//预备对象，用于存储匹配出的li
                if (searchText != "") {
                    var arr = new Array();
                    arr = searchText.split(" ");
                    if (arr.length >= 2) {
                        arr.length = 0;
                        for (i = 0; i < arr.length; i++) {
                            $searchLi = $("#search").find('a:contains(' + arr[i] + ')').parent();
                            arr.push[$searchLi];
                        }
                    } else {
                        $searchLi = $("#search").find('a:contains(' + searchText + ')').parent();
                    }
                    $("#search").html("");
                }
                //判断搜索内容是否有效，若无效，输出not find
                if ($searchLi.length <= 0 || arr.length <= 0) {
                    $(".bgc >div >div").html("<h3 style='color:white'>Sorry, no matching jobs were found in Our Position List.</h3><h3 style='color:white'>Would you like to try another keyword please?</h3>")
                }
            });
            $("input[type=submit]").click(function () {
                $("searchText").change();
            })
        }
    })
})()
