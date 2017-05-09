$(document).ready(function(){
    
    usr = $('#usrname');
    usr.change(function(e){
      e.preventDefault();
      username = usr.val();
      $.ajax({
        url : usr.attr("data-validate-username-url"),
        type: 'get',
        data : {'username' : username },
        success : function(json) {
          if (json['error_message']=='exists'){
            $('.err2').remove()
          }else{
            $('.errorTxt1').append('<div class="err2">'+json['error_message']+'</div>') 
          }
        },
      });
    });

    eml = $('#email');
    eml.change(function(e){
      e.preventDefault();
      email = eml.val();
      $.ajax({
        url : eml.attr("data-validate-email-url"),
        type: 'get',
        data : {'email' : email },
        success : function(json) {
          if (json['error_message']=='exists'){
            $('.err2').remove()
          }else{
            $('.errorTxt2').append('<div class="err2">'+json['error_message']+'</div>') 
          }
        },
      });
    });

    $("#signup").validate({
      rules:{
        first_name: "required",
        last_name: "required",
        sec_q: "required",
        sec_a: "required",
        country: "required",
        username:{
          required: true,
          minlength: 2,
        },
        email:{
          required: true,
          email: true,
        },
        password:{
          required: true,
          minlength: 6
        },
        cpassword:{
          required: true,
          equalTo: "#password"
        },
        phone_num:{
          required: true,
          digits: true
        },
      },  
      messages: {
        fname: "Provide your firstname",
        lname: "Provide your lastname",
        sec_q: "Required security question",
        sec_a: "Answer to question",
        country: "Where are from",
        usrname: {
          required: "Please enter your username",
          minlength: "Your username should be more than 2 characters"
        },
        email: {
          required: "The email address is required",
          email: "This is not a valid email address"
        },
        password: {
          required: "Your password is required",
          minlength: "Password should be more than 6 characters"
        },
        cpassword:{
          required: "Please confirm your password",
          equalTo: "The password did not match"
        },
        phone_num:{
          required: "Please your phone number",
          digits: "Please enter a valid phone number"
        },
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
})