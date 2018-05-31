(function () {
    $("#positionBox").hide();

    $("#boxclose").click(function () {
        $("#positionBox").hide()
    });


    $.ajaxSetup({
        error: function () {
            alert('ajax failed');
            return false;
        }
    });


    $.ajax({
        type: 'get',
        url: '../positions.json',
        async: true,
        success: function (data) {
            var dat = data.slice(0,10)
            var t = $('#positionLists').html();
            var f = Handlebars.compile(t);
            var h = f(dat);
            $('#popup').html(h);




            //click popnewwindow
            $(".list-group-item").click(function () {
                for (i=0; i<10; i++){
                    if ($(this).index() == i){
                    var head = $('#heads').html();
                    var hea = Handlebars.compile(head);
                    var he = hea(dat[i]);
                    $('#head').html(he);
                    var detail = $('#positionDetails').html();
                    var jdb = Handlebars.compile(detail);
                    var jd = jdb(dat[i]);
                    $('#positionDetail').html(jd);
                    }
                }
                $("#positionBox").show()
            });



            //search
            var titles = new Array();
            var tt = titles.push(dat[i]);
            $("input[type=text]").change(function () {
                var searchText = $(this).val();
                var $searchLi = "";
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
                if ($searchLi.length <= 0 || arr.length <= 0) {
                    $(".bgc >div >div").html("<h3 style='color:white'>Sorry, no matching jobs were found in Our Position List.</h3><h3 style='color:white'>Would you like to try another keyword please?</h3>")
                } else{
                    $("div:contains('simple')").css("border", "4px solid blue");
                }

            });
            $("input[type=submit]").click(function () {
                $("searchText").change();
            })
        }
    })
})()
