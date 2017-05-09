$(document).ready(function(){
    $('html').niceScroll({
        cursorWidth: 30,
        cursorborder: 0,
        cursorborderradius: 0,
        cursorcolor: 'slategray',
        zindex: 1000
    });
    $('.textarea').trigger('autoresize');
    $('select').material_select();
    $('.ham').click(function(){
        console.log("clicked")
        $('.body, .sidebar.mob').toggleClass('active');
    })
    $('.seticon').click(function(){
        console.log('click')
        $(this).parent('td').parent('.set').next('.edit').toggleClass('hidden')
        console.log($(this).parent().parent().next())
        $(".done>div").click(function(){
            var value = $('.input').val();
            if (value != ""){
                $(".pass-value").text(value)
            }
            $('.edit').addClass('hidden')
        });
    });
    $(".mobile").sideNav();

});
$(".link_btn_on").click(function() {
  var ref = $(this).siblings('.ref')
  clipboard.copy(ref.text())
  $('.ref-info').removeClass('disable')
  setTimeout(function() {
    $('.ref-info').addClass('disable')
    }, 1000);
  console.log(ref);
});

$('.bell').click(function(){
  $(this).children('ul').toggleClass('active');
})
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

$('#dsd, #dsi, #show_soc, #autos, #allowemail, #showpp, #shownum').change(function() {
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

$("a[href='#top']").click(function() {
  $("html, body").animate({ scrollTop: 0 }, "fast");
  return false;
});
// var lev_wid = $('.level.u').width()
//   sub_lev = ((0.004/37.023)*lev_wid)
//   $('.inner-level.u').width(sub_lev)
// File Upload
//
function previewImage(){
  function Init() {

    console.log("Upload Initialised");

    var fileSelect    = document.getElementById('profile_img');

    if(fileSelect){
        fileSelect.addEventListener('change', fileSelectHandler, false);
    }
  }

  function fileSelectHandler(e) {
    // Fetch FileList object
    var files = e.target.files || e.dataTransfer.files;

    // Process all File objects
    for (var i = 0, f; f = files[i]; i++) {
      parseFile(f);
    }
  }

  // Output
  function parseFile(file) {

    console.log(file.name);

    // var fileType = file.type;
    // console.log(fileType);
    var imageName = file.name;

    var isGood = (/\.(?=jpg|png|jpeg)/gi).test(imageName);
    if (isGood) {
      document.getElementById('image').src = URL.createObjectURL(file);
    }
  }

  // Check for the various File API support.
  if (window.File && window.FileList && window.FileReader) {
    Init();
  }
}
previewImage();
