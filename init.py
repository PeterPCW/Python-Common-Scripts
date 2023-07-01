# Still have to create the repo manually on GitHub, could use API and access key instead but eh

import os
import time
import msvcrt
import argparse

# Prompt for repository name and commit message
repo_name = input("Enter the repository name: ")

# Wait for user input to write the commit message, use default after 30s
def get_commit_message(timeout=30):
    start_time = time.time()
    message = ""
    while True:
        if msvcrt.kbhit():  # Check if a key has been pressed
            char = msvcrt.getwche()  # Read a character without waiting for a newline
            if char == '\r':  # If the Enter key was pressed, exit the loop
                break
            message += char  # Append the character to the message
        elif time.time() - start_time > timeout:  # If the timeout has elapsed, exit the loop
            break
    if not message:
        message = "commit from deploy"  # Use default message if no input was received
    return message

print('Enter a commit message (optional, 30s timeout for "commit from deploy", careful no backspace!):')
commit_message = get_commit_message()

# Run 'git init' command
os.system('git init')

# Run 'git add .' command to stage all files and git commit -m to commit with message
os.system(f'git add . && git commit -m "{commit_message}"')

# Run 'git remote add origin' command to add the remote repository
remote_url = f"https://github.com/peterpcw/{repo_name}.git"
os.system(f'git remote add origin "{remote_url}"')

# Run 'git push -u origin master' command to push the files
os.system('git push -u origin main')

print("Files have been committed and pushed to GitHub.")
