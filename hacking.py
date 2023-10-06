import csv
import json

# List of hacked users.
compromised_users = []

# Open file and push each compromised user to the list.
with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
        compromised_users.append(password_row["Username"])

# Write the compromised users into a text file
with open('compromised_users.txt', 'w') as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user)

# Write boss_message json file.
with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {
        "recipient": "The Boss",
        "message": "Mission Success"
    }
    json.dump(boss_message_dict, boss_message)


# Remove password.csv completely.
with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = """
        U got hacked
        - Slash NULL
    """

    new_passwords_obj.write(slash_null_sig)