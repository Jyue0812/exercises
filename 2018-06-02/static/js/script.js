(function () {
    $.getJSON('/positions', function (data) {
        //covert time to a different way
        function displayTime(data) {
            var str = data;
            var timePublish = new Date(str);
            var timeNow = new Date();
            var minute = 1000 * 60;
            var hour = minute * 60;
            var day = hour * 24;
            var month = day * 30;
            var diffValue = timeNow - timePublish;
            var diffMonth = diffValue / month;
            var diffWeek = diffValue / (7 * day);
            var diffDay = diffValue / day;
            var diffHour = diffValue / hour;
            var diffMinute = diffValue / minute;

            if (diffValue < 0) {
                alert("wrong time");
            }
            else if (diffMonth > 3) {
                result = timePublish.getFullYear() + "-";
                result += timePublish.getMonth() + "-";
                result += timePublish.getDate();
                alert(result);
            }
            else if (diffMonth > 1) {
                result = parseInt(diffMonth) + " Month(s) Ago";
            }
            else if (diffWeek > 1) {
                result = parseInt(diffWeek) + " Week(s) Ago";
            }
            else if (diffDay > 1) {
                result = parseInt(diffDay) + " Day(s) Ago";
            }
            else if (diffHour > 1) {
                result = parseInt(diffHour) + " Hour(s) Ago";
            }
            else if (diffMinute > 1) {
                result = parseInt(diffMinute) + " Minute(s) Ago";
            }
            else {
                result = "Several Minutes Ago";
            }
            return result;
        }

        //loop json data
        function jobDetails(i, j) {
            for (i = 0; i < j; i++) {
                $('.jp').append('<div class="col-md-4 jobPanel"><div class="text"><h3>'
                    + data[i].title + '</h3><span>Posted '
                    + displayTime(data[i].created_at) + '</span><h4>Company Name</h4><span>'
                    + data[i].company + '</span><h4>Location</h4><span>'
                    + data[i].location + '</span><h4>Detail</h4><span class="ellipsis">'
                    + data[i].description + '</span><div class="companyweb"><a href="'
                    + data[i].company_url + '">Visit Website</a></div></div></div>');
            }
        }

        //call funcation
        jobDetails(0, 12);

        //view all the positions button
        $('.viewall').one('click', function () {
            jobDetails(12, data.length);
            $('.viewall').remove()
        });
        $('#close').hide();
        $('.job-detail').hide();

        //change data in the right window according to the position clicked
        $('.jp').on("mouseenter", $('.jobPanel'), function () {
            $('.jobPanel').click(function () {
                for (i = 0; i < data.length; i++) {
                    if ($(this).index() == i) {
                        $('.job-detail').show().animate({right: '0'}).html('<div class="text"><h3 class="bolda">'
                            + data[i - 1].title + '</h3><p><span class="bolda">Id:&nbsp</span>'
                            + data[i - 1].id + '</p><p>Posted '
                            + displayTime(data[i - 1].created_at) + '</p><button class="job-apply" type="submit">Fill the Job Application Form</button><div class="fillForm">' +
                            '<form class="form-group" action="/apply" method="post">' +
                            '<input class="form-control" name="first_name" placeholder="first name">\n' +
                            '        <input class="form-control" name="last_name" placeholder="last name">\n' +
                            '        <input class="form-control" name="position_id" placeholder="position id">\n' +
                            '        <input class="form-control" name="years_experience" placeholder="years experience">\n' +
                            '        <input class="form-control" name="expertise" placeholder="expertise">\n' +
                            '        <input class="form-control input-submit" type="submit" value="Submit">\n' +
                            '    </form>\n' +
                            '</div><h4 class="bolda">Company</h4><span>'
                            + data[i - 1].company + '</span><h4 class="bolda">Location</h4><span>'
                            + data[i - 1].location + '</span><h4 class="bolda">Type</h4><span>'
                            + data[i - 1].type + '</span><a href="'
                            + data[i - 1].company_url + '"><img src="'
                            + data[i - 1].company_logo + '" alt="logo"></a><h4 class="bolda">Detail</h4><p></p>'
                            + data[i - 1].description + '</div>')
                    }
                }
                $('#close').show();
                $('.job-filter').hide();
                $('.fillForm').hide();
                $('.job-apply').click(function () {
                    $('.fillForm').fadeToggle();
                });
                $('.input-submit').click(function () {
                    window.location.href = '/'
                })
            });

        });

        //close the window
        $('#close').click(function () {
            $('#close').hide();
            $('.job-filter').show();
            $('.job-detail').animate({right: '-600px'});
        });
    });

    //get data from /applications
    $.getJSON('/applications', function (data) {
        // console.log(data)
    });

    //get data from /applications
    $.getJSON('/applications', function (data) {

        var a = data.applications;
        var b = a.length;
        if (b > 9){
            b = 9;
            a = a.slice(-10,-1)
        }
        for (i=0;i<b;i++){
            $('#applications').append('<li>Position Id: '
                +a[i].position_id +' First Name:'
                +a[i].first_name+'Last Name:'
                +a[i].last_name+'Years of Experience:'
                +a[i].years_experience +' Expertise:'
                +a[i].expertise+'</li>')
            }
        $('#closeMask').click(function () {
            $('#closeMask').hide();
            $('.mask').hide();
            window.location.href='/'
        });
    });

})()
