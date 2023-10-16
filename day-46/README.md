# Day 46 of 100DaysofCode

Feeling excited to start Day 46 of 100 DaysOfCode, today, I watched an amazing video on [JavaScript Tutorial for Beginners: Learn JavaScript in 1 Hour](https://youtu.be/W6NZfCO5SIk?si=c4c6r6uVAHtpWQa4) by <b>Programming With Mosh</b>. This Video contains beginner guide to javascript, its major componenets like loops, conditional statements, declaring variables and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-46
```

# What is JavaScript?

JavaScript is a high-level, versatile, and widely used programming language that is primarily known for its role in web development. It is an essential component of modern web development, providing the ability to create interactive and dynamic websites. JavaScript is often referred to as the "language of the web" because it allows you to build responsive and user-friendly web applications.

JavaScript is not limited to web development, though. It can be used in various environments, such as server-side development (Node.js), mobile app development, and even in Internet of Things (IoT) devices.

## What Can You Do with JavaScript?

JavaScript offers a wide range of possibilities. Here are some of the key things you can do with JavaScript:

1. **Web Development**: JavaScript is crucial for creating interactive and dynamic web pages. It allows you to add features like sliders, pop-up dialogs, form validation, and real-time updates to web applications.

2. **Front-End Development**: JavaScript is the primary language for front-end development. It works alongside HTML and CSS to build user interfaces and improve the user experience.

3. **Back-End Development**: With Node.js, JavaScript can be used for server-side development. This extends its capabilities to handle server logic, databases, and APIs.

4. **Mobile App Development**: Technologies like React Native and NativeScript enable you to create mobile applications for iOS and Android using JavaScript.

5. **Game Development**: JavaScript can be used for browser-based game development, thanks to libraries and frameworks like Phaser and Three.js.

6. **Browser Extensions**: You can build browser extensions/add-ons using JavaScript to enhance the functionality of web browsers like Chrome and Firefox.

7. **Server-Side Scripting**: JavaScript can be used for server-side scripting, including automating tasks, managing servers, and more.

8. **IoT Development**: JavaScript can run on IoT devices using platforms like Espruino and Johnny-Five, making it versatile for controlling hardware.

## Major Functionality

JavaScript provides the following major functionality:

1. **Variables and Data Types**: JavaScript supports various data types such as numbers, strings, arrays, and objects. You can declare variables and manipulate data.

2. **Functions**: You can define functions to encapsulate reusable blocks of code.

3. **Control Structures**: JavaScript supports if-else statements, loops, and switch statements for controlling program flow.

4. **DOM Manipulation**: JavaScript can interact with the Document Object Model (DOM) of web pages, allowing you to dynamically update and modify content.

5. **Event Handling**: You can respond to user actions and interactions by defining event listeners to trigger specific actions.

6. **Asynchronous Programming**: JavaScript supports asynchronous operations using promises and callbacks, enabling non-blocking code execution.

7. **API Requests**: You can make HTTP requests to external APIs, allowing you to fetch data and integrate it into your applications.

8. **Object-Oriented Programming**: JavaScript supports object-oriented programming (OOP) principles and allows you to create and manipulate objects.

9. **Error Handling**: JavaScript provides error-handling mechanisms to manage and debug issues in your code.

## Getting Started

If you're new to JavaScript, you can start by setting up your development environment and exploring introductory tutorials and courses. Here's a simple example of a "Hello, World!" program in JavaScript:

```javascript
console.log("Hello, World!");
```
see the files/index.html, it contains the `console.log` command.

## Variables

In JavaScript, variables are used to store data. They are declared using the `var`, `let`, or `const` keywords. Variables can hold various data types, including numbers, strings, and objects. Example: 

```javascript
var name = "John";
let age = 30;
const PI = 3.14;
```

There are certain rules regarding name convention: 
- Cannot start with a number (1name).
- Cannot use a reserved keyword like if, else, etc.
- Should be meaningful
- Cannot contains a space or hyphen
- Use CamelNotation

## Constants

Constants, declared with `const`, are similar to variables, but their values cannot be reassigned after declaration. They are typically used for values that should not change during the program's execution.

```javascript
const PI = 3.14;
```

## Primitive Types

JavaScript has several primitive data types:

- **Number**: Represents numeric values, e.g., `42`, `3.14`.

- **String**: Represents text, e.g., `"Hello, world!"`.

- **Boolean**: Represents `true` or `false`.

- **Undefined**: Indicates that a variable has been declared but has not been assigned a value.

- **Null**: Represents an intentional absence of any object value.

- **Symbol**: Introduced in ES6, symbols are unique and primarily used as object property keys.

- **BigInt**: Introduced in ES11 (ES2020), BigInts represent large integers, e.g., `1234567890123456789012345678901234567890n`.

## Dynamic Typing

JavaScript is a dynamically typed language, meaning you don't have to explicitly specify the data type of a variable. The type of a variable can change during runtime.

```javascript
let variable = 42;  // variable is a number
variable = "Hello"; // variable is now a string
```

## Objects

Objects are complex data types that allow you to store collections of key-value pairs. They are defined using curly braces `{}`.

```javascript
let person = {
    name: "Alice",
    age: 25,
    isStudent: true
};
```

## Arrays

Arrays are used to store collections of data. They are defined using square brackets `[]`.

```javascript
let fruits = ["apple", "banana", "orange"];
```

## Functions

Functions are reusable blocks of code that perform specific tasks. You can declare functions using the `function` keyword.

```javascript
function greet(name) {
    return "Hello, " + name + "!";
}
```

## Types of Functions

JavaScript functions can be categorized into different types:

- **Named Functions**: Declared with a name and can be reused throughout the code.

```javascript
function add(a, b) {
    return a + b;
}
```

- **Anonymous Functions**: Functions without a name, often used as callbacks or immediately invoked function expressions (IIFE).

```javascript
const add = function(a, b) {
    return a + b;
};
```

- **Arrow Functions (ES6)**: A concise way to define functions, often used for short functions or callbacks.

```javascript
const add = (a, b) => a + b;
```

- **Constructor Functions**: Used to create instances of objects.

```javascript
function Person(name, age) {
    this.name = name;
    this.age = age;
}
const alice = new Person("Alice", 25);
```

## Parameters V/S Arguments

In the context of functions in programming, "parameters" and "arguments" are related concepts, but they refer to different things.

1. **Parameters**:
   - Parameters are variables declared in a function's definition.
   - They act as placeholders for values that will be passed into the function when it is called.
   - Parameters are used to define the input requirements or expectations of a function.
   - They are used within the function's block to perform operations or calculations.

Example:
```javascript
function greet(name) {
    console.log("Hello, " + name + "!");
}
```
In this example, `name` is a parameter.

2. **Arguments**:
   - Arguments are the actual values or expressions that are passed into a function when it is called.
   - They are used to provide concrete data to the function, replacing the placeholders (parameters) defined in the function's declaration.
   - The number and order of arguments should match the number and order of parameters in the function.

Example:
```javascript
greet("Alice");
```
In this example, `"Alice"` is an argument that is passed to the `greet` function, and it is used to replace the `name` parameter within the function.

In summary, parameters are placeholders defined in a function's declaration, while arguments are the actual values or expressions that are passed into the function when it is called. Parameters and arguments work together to allow functions to receive and work with data provided from the outside.


