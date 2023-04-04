import csv
from jira import JIRA
from dateutil.parser import parse
from colorama import init, Fore, Style
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Read the Jira instance URL, username, and API token from the .env file
JIRA_URL = os.getenv('JIRA_URL')
JIRA_USERNAME = os.getenv('JIRA_USERNAME')
JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN')

def main():
    # Connect to Jira
    jira = JIRA(JIRA_URL, basic_auth=(JIRA_USERNAME, JIRA_API_TOKEN))

    # Read the CSV file
    csv_file = 'issues.csv'
    issues = read_csv(csv_file)

    # Fetch and display available projects from the CSV file
    print(Fore.CYAN + "Task : Issue ID" + Style.RESET_ALL)
    for issue in issues:
        print(Fore.BLUE + f"{issue['task']}: {issue['issue_key']}" + Style.RESET_ALL)

    # Get user inputs
    issue_key = input('Enter the issue key: ').strip()
    time_spent = input('Enter the time spent (e.g. 1h 30m): ').strip()
    date_started = input('Enter the date started (YYYY-MM-DD) or leave blank for today:').strip()
    work_description = input('Enter the work description: ').strip()

    if not date_started:
        date_started = datetime.now().date().isoformat()

    log_work(jira,issue_key, time_spent, date_started, work_description)

def read_csv(file):
    issues = []
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            issues.append(row)
    return issues

def get_project_keys(issues):
    return list(set(issue['project_key'] for issue in issues))

def log_work(jira, issue_key, time_spent, date_started, work_description):
    issue = jira.issue(issue_key)
    started_datetime = parse(f'{date_started}T00:00:00')  # Add time part with timezone info
    jira.add_worklog(issue, timeSpent=time_spent, started=started_datetime, comment=work_description)
    print(Fore.GREEN + f'Logged work for issue {issue_key}: {time_spent} on {date_started} - {work_description}' + Style.RESET_ALL)

if __name__ == '__main__':
    main()

