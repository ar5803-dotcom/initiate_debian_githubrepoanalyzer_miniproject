import requests


def get_github_repo_info(owner, repo, token):
    headers = {
        'Authorization': f'token {token}',
    }

    url = f'https://api.github.com/repos/{owner}/{repo}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repo_info = response.json()
        return repo_info
    else:
        return None


def get_repo_contents(owner, repo, token):
    headers = {
        'Authorization': f'token {token}',
    }

    url = f'https://api.github.com/repos/{owner}/{repo}/contents'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repo_contents = response.json()
        return repo_contents
    else:
        return None


def display_repo_info(repo_info, repo_contents):
    print(f"Repository: {repo_info['full_name']}")
    print(f"Description: {repo_info['description']}")
    print(f"Language: {repo_info['language']}")
    print(f"License: {repo_info['license']['name'] if repo_info['license'] else 'N/A'}")
    print(f"Stars: {repo_info['stargazers_count']}")
    print(f"Forks: {repo_info['forks_count']}")
    print(f"Watchers: {repo_info['subscribers_count']}")
    print(f"Open Issues: {repo_info['open_issues_count']}")
    print(f"Last Updated: {repo_info['pushed_at']}")
    print("\nContents of the Repository:")

    for file in repo_contents:
        print(f"File: {file['name']}, Type: {file['type']}")


def request_scopes():
    print("Select scopes:")
    print("1. repo - Full control of private repositories")
    print("2. repo:status - Access commit status")


    selected_scopes = input("Enter the scopes you want to request (comma-separated): ")
    return [scope.strip() for scope in selected_scopes.split(',')]


if __name__ == "__main__":
    owner = "ar5803-dotcom"
    repo = "Maze-Solver-Agent"

    scopes = request_scopes()
    token = "Confidential"

    token_scopes = input("Enter the scopes associated with your token (comma-separated): ").split(',')
    if not all(scope in token_scopes for scope in scopes):
        print("Error: The provided token does not have the required scopes.")
        exit()

    repo_info = get_github_repo_info(owner, repo, token)
    repo_contents = get_repo_contents(owner, repo, token)

    if repo_info and repo_contents:
        display_repo_info(repo_info, repo_contents)
    else:
        print("Failed to fetch repository information. Check your input and token.")
