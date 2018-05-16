$(document).ready(function check_user_name(){
    var len= $('#user_name').val().length;
    if(len<5||len>20){
        $('#user_name').next().html('请输入5-20个字符的用户名');
        $('#user_name').next().show();
        error_name = true;
    }
    else {
        $.get('/user/register_exit/?iname='+$('#user_name').val(), function(data){
            if (data.count==1){
                $('#user_name').next().html('用户名已经存在').show();
                error_name = true;
            }else{
                $('#user_name').next().hide();
                error_name = false;
            }
        });
    }
});

$('#user_name').blur(check_user_name());