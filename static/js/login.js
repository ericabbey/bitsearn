$(document).ready(function(){
  usr = $('#username');
  usr.change(function(e){
    e.preventDefault();
    username = usr.val();
    if (usr.val() != ""){
      $.ajax({
        url : usr.attr("data-validate-username-url"),
        type: 'get',
        data : {'username' : username },
        success : function(json) {
          if (json['error_message']=='exists'){
             $('.errorTxt1').append('<div class="err2">This user does not exist</div>')
             $('.errorTxt1').siblings('.validate.valid').removeClass('valid').addClass('error')
             console.log($('.errorTxt1').siblings('.validate'))
          }else{
            $('.err2').remove()
          }
        },
      });
    }else{
      $('.err2').remove()
    }

  });


  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
         var cookie = jQuery.trim(cookies[i]);
    if (cookie.substring(0, name.length + 1) == (name + '=')) {
      cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
       }
      }
    }
   return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');

  pwd = $('#password');
  pwd.change(function(e){
    e.preventDefault();
    password = pwd.val();
    username = usr.val()
    if (pwd.val() != ""){
      $.ajax({
        url : pwd.attr("data-validate-password-url"),
        type: 'post',
        data : { csrfmiddlewaretoken : csrftoken, 
                'username' : username,
                'password' : password
            },
        success : function(json) {
          if (json['error_message']!='valid'){
             $('.errorTxt2').append('<div class="err2">'+json['error_message']+'</div>')
             $('.errorTxt2').siblings('.validate.valid').removeClass('valid').addClass('error')
          }else{
            $('.err2').remove()
          }
        },
      });
    }else{
      $('.err2').remove()
    }
  });

  $("#signin").validate({
      rules:{
        username: "required",
        password: "required",
        },
      messages:{
        username: "You did not enter any username",
        password: "You did not enter any password"
        },
        errorElement : 'div',
        errorPlacement: function(error, element) {
        var placement = $(element).data('error');
          if (placement) {
          $(placement).append(error)
          } else {
          error.insertAfter(element);
          }
        }
  });
  $('#signin').submit(function(e){
      found = $(this).find('.err2').length
      console.log(found)
      if (found != 0){
        e.preventDefault();
      }
  });
})