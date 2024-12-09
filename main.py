import requests

github_user = input("Enter github username: ")

git_api = requests.get(f'https://api.github.com/users/{github_user}/events/public')

if git_api.status_code == 200:
    print("--Last five events--")
    push_count = 0
    for i in git_api.json():
        if i['type'] == 'PushEvent':
            push_count += 1
            print(i['payload']['commits'][0]['message'])
        if push_count == 5:
            break

else:
    print(f'API error code {git_api.status_code}')