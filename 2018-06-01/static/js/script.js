(function () {
    //popup window hide
    $("#positionBox").hide();

    $("#boxclose").click(function () {
        $("#positionBox").hide()
    });

    //ajax failed warning
    $.ajaxSetup({
        error: function () {
            alert('ajax failed');
            return false;
        }
    });

    $('#sub').one("submit", function () {
        var a = $('#sub').attr('action');
        if (a === '/apply') {
            $.ajax({
                type: 'post',
                url: '/apply',
                async: true,
                success: function (data) {
                    window.location.href = '/applysuccess';
                }
            })
        } else {
            return false;
        }
    });


    $.ajax({
        type: 'post',
        url: '/apply',
        async: true,
        success: function (data) {
            $('#apply').html('<h3>' + data.message + '</h3><a href="/">Back to Homepage</a>');
        }
    });


    //get application info
    $.ajax({
        type: 'get',
        url: '/applications',
        async: true,
        success: function (data) {
            var le = data.applications.length;
            var dat = data.applications;

            for (i = 0; i < le; i++) {
                if (dat[i].position_id && dat[i].first_name && dat[i].last_name && dat[i].years_experience && dat[i].expertise) {
                    $('table').append('<tr><td>'
                        + dat[i].position_id + '</td><td>'
                        + dat[i].first_name + '</td><td>'
                        + dat[i].last_name + '</td><td>'
                        + dat[i].years_experience + '</td><td>'
                        + dat[i].expertise + '</td></tr>');
                }
            }
        }
    });

    //get positions info
    $.ajax({
        type: 'get',
        url: '/positions',
        async: true,
        success: function (data) {
            var len = data.length;

            function loadmore() {
                for (i = 0; i < 10; i++) {
                    $('#popup').append('<a class="list-group-item"><dl class="dl-horizontal"><dt id="search">title</dt><dd>'
                        + data[i].title + '</dd></dl><dl class="dl-horizontal"><dt>location</dt><dd>'
                        + data[i].location + '</dd></dl><dl class="dl-horizontal"><dt>type</dt><dd>'
                        + data[i].type + '</dd></dl><dl class="dl-horizontal"><dt>Company Name</dt><dd>'
                        + data[i].company + '</dd></dl><dl class="dl-horizontal"><dt>Created At</dt><dd>'
                        + data[i].created_at + '</dd></dl></a>');
                }
            }

            if ($('#popup').children().length < 10) {
                loadmore()
            }

            $('#loadMore').click(function () {
                loadmore()
            });

            //click popnewwindow and infos in window
            $("#popup").on("click", $(".list-group-item"), function () {
                $(".list-group-item").click(function () {
                    for (i = 0; i < len; i++) {
                        if ($(this).index() == i) {
                            $('#head').html('<img class="fl" src="'
                                + data[i].company_logo + '" alt="logo"><div class="pTitle fl"><h4>'
                                + data[i].title + '</h4><h5>'
                                + data[i].company + '--'
                                + data[i].location + '</h5><h5>'
                                + data[i].type + '</h5></div>');

                            $('#detail').html('<dt>Job Description</dt><dd>' + data[i].description + '</dd>');
                        }
                    }
                    $("#positionBox").show()
                });
            });


            //search requirement
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
                }

            });
            $("input[type=submit]").click(function () {
                $("searchText").change();
            })
        }
    })
})()
