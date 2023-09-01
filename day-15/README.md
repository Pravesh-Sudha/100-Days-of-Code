# Day 15 of 100DaysofCode

Feeling excited to start Day 15 of 100 DaysOfCode, today, I learnt about cron, CronJobs, Executing shells scripts using cron jobs in a great Video by [Train With Shubhum](https://youtube.com/playlist?list=PLlfy9GnSVerQr-Se9JRE_tZJk3OUoHCkh&si=RpQBLv9geaalTCek). This video includes What is cron?, what is cron jobs, creating your first cron jobs, How devOps engineer thinks about Cron jobs and Executing your shell scripts using cron jobs.

## Prerequisites

Before using these commands, ensure you have one of the following environments set up:

- **Ubuntu Desktop:** Install Ubuntu on your local machine by following the official installation guide at [ubuntu.com](https://ubuntu.com/download/desktop).

- **Windows Subsystem for Linux (WSL):** If you're using Windows, set up WSL by following the instructions at [Microsoft Docs](https://docs.microsoft.com/en-us/windows/wsl/install).

- **Amazon EC2 Instance:** If you prefer a cloud environment, create an Amazon EC2 instance running a Linux distribution. Follow the steps outlined in the [AWS documentation](https://aws.amazon.com/getting-started/hands-on/run-your-app-using-amazon-ec2/).

## What is Cron?

Cron is a time-based job scheduling daemon in Unix-like operating systems. It allows you to schedule and automate the execution of tasks, commands, or scripts at specific intervals or times. These scheduled tasks are referred to as "cron jobs."

A cron job is a command or script that is set to run automatically at specified time intervals or at particular times of the day, week, month, or year. Cron jobs are especially useful for automating repetitive tasks such as backups, log cleaning, data synchronization, and more.

Cron jobs are defined using a file called the "crontab," which contains a list of commands or scripts along with their schedule specifications. Each line in the crontab represents a separate cron job. The crontab format consists of fields that specify the minute, hour, day of the month, month, day of the week, and the command to be executed.

```bash 
* * * * * command_to_execute
```

The fields represent:

- Minute (0-59)
- Hour (0-23)
- Day of the month (1-31)
- Month (1-12)
- Day of the week (0-6, where 0 is Sunday)
- Command to execute

Asterisks (*) in any of the time-related fields indicate "every" value. For example, if you put an asterisk in the "Minute" field, the command will be executed every minute.

Here's an example of a crontab entry that runs a backup script every day at 2 AM:

```bash
0 2 * * * /path/to/backup_script.sh
```

The below command helps to view to all available crontab.

```bash
crontab -l
```

## Creating Your First CronTab

- Use crontab -e for starting the file in editor mode.

```bash
crontab -e <vim or nano>
```
- At the end of file, using the format of asterisks (*) specify the time like:

```bash
0 2 * * * echo "This is my first cron job" > home/leefo/test_cronjob.txt
```

- This cron job will Print the message ("This is my first cron job") in every two minutes in the `test_cronjob.txt` file.


## Usage

Clone this repository or simply refer to the README for a quick reference on using the basic Linux commands. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-15
```

## Contributing

If you would like to contribute to this repository, please open a pull request. Feel free to suggest new commands or improvements to existing ones.
