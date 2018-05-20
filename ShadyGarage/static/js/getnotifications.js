$(document).ready(function(){
  var notificiations = [];
  function getNotifications(){
    // TODO: fikse urlen til ordentlig nettside url
    var fetchUrl = "../../api/posts/accounts/myactivities/"
    $.ajax({
      url:fetchUrl,
      method: "GET",
      success:function(data){
        notificiations = data.results
        addNotifications()
      }, error:function(data){
        console.log("ERROR: Getting activitys");
      }
    })

  }

  function addNotifications(){
      append_count = 0;
      if(notificiations == 0){

      }else{
        var notSeen = 0;
        $.each(notificiations, function(key, value){
          if(value.post_fk.activity_count > 0){
            if(append_count == 0){
              appendNotificaiton(value.post_fk.activity_count)
              console.log("HEI")
            }
          }
            append_count++;

        })

      }
  }

  function appendNotificaiton(count){
    var toAppend = "<h6 class='badge badge-warning'>" + count + "</h6>"
    $("#activityButton").append(toAppend)
    console.log("KALT")
  }

  getNotifications()


});
