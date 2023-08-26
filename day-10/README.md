# Day 10 of 100DaysofCode

Feeling excited to start Day 10 of 100 DaysOfCode, today, I learnt about go Lang and made a weather program in it.

# Go Lang Weather Program

This is a simple weather program written in Go that fetches weather information using the OpenWeatherMap API.

## Prerequisites

Before you begin, make sure you have the following:

- [Go programming language](https://golang.org/doc/install) installed on your system.
- An API key from [OpenWeatherMap](https://openweathermap.org/) to access their weather data.

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
    cd day-10/weather-app
    ```

2. **Get your API Key:**

    - Go to [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and sign up for an account.
    - Once logged in, go to your profile and find the API Keys tab to generate a new API key.
    - Copy the generated API key.

3. **Insert your API Key:**

    - Open the `.apiConfig` file in a text editor.
    - Look for the line that says `OpenWeatherMapApiKey = "YOUR_API_KEY_HERE"`.
    - Replace `YOUR_API_KEY_HERE` with your actual OpenWeatherMap API key.

4. **Run the program:**

    ```bash
    go run main.go
    ```
    
4. **See the Result:**

   - Open your web Browser and Go to ```localhost:8080/hello```, it will display a "Hello from go" text.
   - Go to ```localhost:8080/weather/city``` replace the city with an actual city name, it will display the weather of the city


## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests.
