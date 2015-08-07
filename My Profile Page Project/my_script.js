console.log("Hello World");
function goToLunch(student) {
  //Instruction to go to lunch
  console.log(student +", Walk around the desk");
  console.log(student + ", turn right");
  console.log(student + ", Walk ten paces");
  console.log(student + ", grab door handle");
  console.log(student + ", turn handle");
  return student.toUpperCase();
}

function add(firstNumber,secondNumber){
  return firstNumber + secondNumber;
}

goToLunch("Shaun"); //var student
goToLunch("jessie");
goToLunch("Jackie");

//jquery




$(document).ready( function() {

  $('#worktag').animate(
    {
      fontSize: 100,
      color: '#ff0000'
    };
  });



  $('img').slideDown();

  $('img').click(function(){
  window.alert("Wow, don't I look good :)?")  ;


  });

});
