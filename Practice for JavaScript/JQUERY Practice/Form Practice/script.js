function addStudent (){
  var name =$('#name').val();
  var color=$('#color').val();
  var artist=$('#artist').val();


var listItem= name + "'s favorite color is" + color + ".";
listItem = listItem + "Favorite Artist:" + artist;

$('#mylist'). append ("<li>" + listItem + "</li");
}


$(document).ready(function(){
  $('#addStudent').click(addStudent);
});
