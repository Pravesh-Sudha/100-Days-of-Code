// variables
let name = 'Pravesh';
let age = 45;
let systemName = undefined;
let isApproved = true;

console.log(name);
console.log(systemName);

// Prints the type of variable
typeof(age);

// dynamic Typing
let brother = 'Pravesh';
brother = 'Vinay'

console.log(brother)

// Objects
let student = {
    name: "Pravesh",
    rollNo: 29,
    stream: "Arts"
};

student.name = "Aastha";
// or
student['name'] = "Mary";
console.log(student);

// Arrays
let selectedColors = ['Orange', 'Red', 'Yellow', 'Blue'];
selectedColors.sort();
console.log(selectedColors);
console.log(selectedColors.length);

// functions
function greet(name) {
    return "Hello "+ name;
}

console.log(greet("Pravesh"));