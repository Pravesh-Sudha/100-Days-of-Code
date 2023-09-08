# Day 21 of 100DaysofCode

Feeling excited to start Day 21 of 100 DaysOfCode, today, I built Two personel projects in go lang and python. The go-lang project is a loadbalancer program which distrubtes traffic to different servers according to the loads. The Python program is a simple typing test which provides you with a predefined paragraph and you can write it and check your typing speed in words per min (wpm).

## Usage

### Go-Loadbalancer

Clone this repository or simply refer to the README for a quick reference on how this project works. Feel free to customize the commands based on your needs. Ensure you have Go installed on your system.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-21/go-loadbalancer
go run main.go
```

### Python-typing-test

Clone this repository or simply refer to the README for a quick reference on how this project works. Feel free to customize the commands based on your needs. Ensure you have Python installed on your system.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-21/python-typing-test
python3 main.py 
```

## How does it Work

## Go-Loadbalancer

1. The program will start and display the port it's hosting on:

```bash
Server is hosting at port 8000
```

2. You can access the load balancer by opening a web browser or using a tool like curl and making requests to `http://localhost:8000`. The load balancer will distribute incoming requests to the configured backend servers (in this case, Facebook, Google, and Yahoo) in a round-robin fashion.

3. The program will forward requests to the selected backend server and display the address of the server handling the request in the console.

4. You can customize the backend servers and their addresses by modifying the servers slice in the main function. Simply add or remove servers as needed.

```bash
servers := []Server{
    newSimpleServer("https://www.facebook.com"),
    newSimpleServer("https://www.google.com"),
    newSimpleServer("https://www.yahoo.com"),
}
```

5. `main.go`: Contains the main program logic, including server setup and request handling.

6. `simple_server.go`: Defines the simpleServer struct, which represents a backend server, and implements the Server interface methods.

7. `load_balancer.go`: Defines the LoadBalancer struct, which manages the round-robin distribution of requests among backend servers.

8. Error handling: The program includes error handling for parsing server URLs and exiting on error.


## Python-typing-test

This Python program allows you to test your typing speed by typing a randomly selected paragraph and then calculates your typing speed in words per minute (WPM) along with the number of mistakes you made.

1. The program imports the required modules: `time` and `random`.

2. It defines two functions:

   - `mistake(paratest, usertest)`: This function compares the characters in the provided test paragraph (`paratest`) with the user's input paragraph (`usertest`) and counts the number of mistakes made.

   - `speed_time(time_s, time_e, words)`: This function calculates the typing speed based on the time taken (`time_s` and `time_e`) and the number of words typed (`words`). It returns the typing speed in words per minute.

3. The program defines a list of test paragraphs in the `test` variable.

4. It selects a random paragraph from the `test` list using the `random.choice` function and stores it in `test_1`.

5. The program then prompts the user to test their typing speed by displaying the selected paragraph.

6. It records the start time (`time_1`) and end time (`time_2`) when the user finishes typing.

7. The user's input is stored in the `test_input` variable.

8. The program calculates and displays the typing speed in WPM using the `speed_time` function and the number of mistakes using the `mistake` function.