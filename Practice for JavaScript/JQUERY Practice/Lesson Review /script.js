$(document). ready (
  function(){
    $('#insert_button').click(createListELement);
  }
);

function createListELement(){
  var person = $('#assignee').val();
  var task= $('#new_task').val();
  $('#task_list').append( '<li>' + person + " " + task + '</li>' );


}
