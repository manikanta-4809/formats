# More reusable - configurable behavior
def format_user_names(users, format_func=None):
    if format_func is None:
        format_func = lambda user: f"{user['first_name']} {user['last_name']}"
 
    return [format_func(user) for user in users]
 
# Usage examples
users = [
    {"first_name": "John", "last_name": "Doe", "username": "jdoe"},
    {"first_name": "Jane", "last_name": "Smith", "username": "jsmith"}
]
 
# Default formatting
full_names = format_user_names(users)
print(full_names)  # ['John Doe', 'Jane Smith']
 
# Custom formatting
usernames = format_user_names(users, lambda user: f"@{user['username']}")
print(usernames)  # ['@jdoe', '@jsmith']
 
# Assignmnet 2 Easy : ['jhondoe@minfytech.com']

emails = format_user_names(users, lambda user: f"{user['last_name'].lower()}{user['first_name'].lower()}@minfytech.com")
print(emails)  # ['johndoe@minfytech.com', 'janesmith@minfytech.com']
 
 
formal_names = format_user_names(users, lambda user: f"{user['last_name']}, {user['first_name']}")
print(formal_names)  # ['Doe, John', 'Smith, Jane']

 