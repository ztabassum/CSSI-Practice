//
// function iThink(statement){
//
//   console.log("Functions are lists of instructions  " + statement);
//
// }
//
// iThink("....I think")
//
// function addTodayIlearned(statement){
//
//   console.log(statement + "  Functions can take multiple inputs but only return a single output");
//   console.log(statement + " Functions can take multiple inputs but only return a single output");
// }
//
// addTodayIlearned("Today I learned");
//
// function checkout (tax) {
//  return  tax * 1.095
// }
//
// var temperature = 61;
// if (temperature === 80){
//   console.log("Wear Shorts")
//   /*then do thus */
// } else if (temperature > 60) {
//   console.log ("wear a light jacket")
//
// }
// else {
//   console.log("wear a coat")
// }
//
// function rateSkiBall(score){
//   if (score < 150){
//     window.alert ("Wow, that was terrible. You did pretty bad, and should probably give up :)!");
//   }
//
//    else if ( score >= 150 && score < 250) {
//     window.alert ("Ehh, decent score.")
//
//   }
//
//    else if (  score >=  250 && score < 350) {
//     window.alert ("Great job!")
//
//   }
//
//   else if (score >= 350 && score < 450){
//     window.alert ("Woah, great!")
//   }
//
//    else if (score >= 450){
//     window.alert (" Holy cow! That is amazing!")
//   }
// }
//
// var student= ["Jackie", "Yulissa", "Arm", "X" ]
//
// function printName(name) {
//   console.log (name);
// }
//
// student.push("Shaun");
// student.pop ();
// printName(student);
//
// var myArr= [ ]
// myArr[0]= "hello"
// myArr[2]=54.3
// myArr[3]=true
//
// var fruits = ["Apples", "Oranges", "Pears", "Bananas"];
//
//
// var instructors = [
//   "monsur",
//   "nicki",
//   "riccardo",
//   "justin",
// ];
//
// for (var i = 0;
//   i < instructors.length; i+=1){
//     console.log(instructors[i])
//   }
//
//   var temperature = 80;
//   var idealTemperature = 60;
//
//   while ( temperature > idealTemperature){
//     temperature -= 1;
//     console.log(temperature);
//
//   }
//
//   console.log("AC off, it is freezing in here!");



function doubleNumbers (array1){
  for (var i=0; i < array1.length; i += 1){
  console.log(array1[i] * 2);

  }
}

var person = {
        firstName: "Jane",
        surname: "Doe",
        age: 24,
        gender: "Female",
        talk: function(){console.log('Hello')}}
