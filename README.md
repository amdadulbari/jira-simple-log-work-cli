# Jira Worklog CLI 
This project is a Python script that simplifies logging work hours for Jira issues. It reads Jira issue keys from a CSV file, asks the user to input the time spent, date started, and work description, and logs the work hours for each issue.

## Features
* Reads Jira issues from a CSV file
* Asks the user for necessary inputs
* Logs work hours for each issue in Jira
* Displays colored console output

## Prerequisites
* Python 3.6 or higher
* Jira Cloud instance with API access

## Installation
* Clone the repository or download the source code.
* Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
* Create a .env file in the project directory with the following contents:
```ini
JIRA_URL=https://your-domain.atlassian.net
JIRA_USERNAME=your-username
JIRA_API_TOKEN=your-api-token
```
Replace the placeholders with your Jira instance URL, username, and API token.

## Usage
1. Prepare a CSV file named issues.csv with the following format:
```csv
task,issue_key
Task 1,KEY-1234
Task 2,KEY-5678
```
Replace the example task names and issue keys with your own Jira tasks and issue keys.

2. Run the script:
```bash
python log.py
```
3. The script will display the tasks and their corresponding issue keys. Enter the required details when prompted:
* Issue key
* Time spent (e.g., 1h 30m)
* Date started (YYYY-MM-DD) or leave it blank for today
* Work description
4. The script will log the work hours for the selected issue in Jira.

## Contributing
Feel free to submit pull requests or open issues if you find any bugs or have suggestions for improvements.
