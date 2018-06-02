(function () {
    $.getJSON('/positions', function (data) {
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
                alert("错误时间");
            }
            else if (diffMonth > 3) {
                result = timePublish.getFullYear()+"-";
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
        console.log(displayTime(data[12].created_at));
        for (i = 0; i < 12; i++) {
            $('.jp').append('<div class="col-md-4 jobPanel"><div class="text"><h3>'
                + data[i].title + '</h3><span>Posted '
                + displayTime(data[12].created_at) + '</span><h4>Company Name</h4><span>'
                + data[i].company + '</span><h4>Location</h4><span>'
                + data[i].location + '</span><h4>Detail</h4><span class="ellipsis">'
                + data[i].description + '</span><div class="companyweb"><a href="'
                + data[i].company_url + '">Visit Website</a></div></div></div>')
        }
        $('.viewall').one('click',function () {
            for (i = 12; i < data.length; i++) {

                $('.jp').append('<div class="col-md-4 jobPanel"><div class="text"><h3 class="ellipsis">'
                    + data[i].title + '</h3><span>Posted '
                    + displayTime(data[12].created_at) + '</span><h4>Company Name</h4><span>'
                    + data[i].company + '</span><h4>Location</h4><span>'
                    + data[i].location + '</span><h4>Detail</h4><span class="ellipsis">'
                    + data[i].description + '</span><div class="companyweb"><a href="'
                    + data[i].company_url + '">Visit Website</a></div></div></div>')
            } $('.viewall').remove()
        })




    })
})()
