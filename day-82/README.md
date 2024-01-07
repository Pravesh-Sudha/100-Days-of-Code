# Day 82 of 100DaysOfCode

Feeling excited to start Day 82 of 100 DaysOfCode, today, I dived deep into Shell and Shell scripting by making a devops project, So I wrote a shell scripting that would inform me about the contributors of a github project's Organisation that have access to the repo with guidance of [Abhishek Veermalika](https://youtu.be/OuyNM5-r8P8?si=MvzcqW04JCA9oP5a).

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-82
```

# GitHub Repository Access Checker

This Bash script utilizes the GitHub API to list users with read access to a specified GitHub repository.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
   cd day-82
   ```

2. **Set up your GitHub credentials:**

   Open the script (`access_checker.sh`) in a text editor and provide your GitHub username and personal access token by updating the following lines:

   ```bash
   # GitHub username and personal access token
   USERNAME=$username
   TOKEN=$token
   ```

3. **Run the script with repository information:**

   ```bash
   ./access_checker.sh <REPO_OWNER> <REPO_NAME>
   ```

   Replace `<REPO_OWNER>` and `<REPO_NAME>` with the actual owner and name of the GitHub repository.

## Script Explanation

- **GitHub API URL:** The script uses the GitHub API endpoint (`https://api.github.com`) to interact with the repository.

- **User and Repository Information:** The owner and name of the repository are provided as command-line arguments when executing the script.

- **Helper Function:**

  - `helper`: Checks if the required number of command-line arguments is provided. If not, it displays a message prompting the user to execute the script with the correct arguments.

- **Functions:**

  - `github_api_get`: Performs a GET request to the GitHub API with authentication using the provided username and personal access token.

  - `list_users_with_read_access`: Fetches the list of collaborators on the specified repository who have read access and displays their usernames.

- **Main Script:**

  - Invokes the `helper` function to check if the required command-line arguments are provided.

  - Displays a message indicating that it is listing users with read access to the specified repository.

  - Calls the `list_users_with_read_access` function to fetch and display the relevant information.

## Error Handling:

- The script checks whether there are collaborators with read access and displays a message accordingly.

- The `helper` function ensures that the script is executed with the correct number of command-line arguments.


