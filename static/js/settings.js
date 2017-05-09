$(document).ready(function(){
   $("#email").validate({
    rules:{
      email: "email",
      },
    messages:{
      email: "invalid email entered"
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

  $('#showsocial, #autosave, #showemail, #showpp, #shownum').change(function() {
    if($(this).prop("checked") == true){
        var value = 'True'
    }
    else if($(this).prop("checked") == false){
        var value = 'False'
    }
    name = $(this).attr('name')
    $.ajax({
      url : $('.btcard').data("url"),
      type: 'post',
      data : { csrfmiddlewaretoken : csrftoken,
              'name' : name ,
              'value': value
            },
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
  });
})
