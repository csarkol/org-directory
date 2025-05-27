import json

# Load users from users.json
with open('users.json') as f:
    users = json.load(f)

# Load groups from groups.json
with open('groups.json') as f:
    groups = json.load(f)

# Loop through groups and update dynamic memberships
for group_name, group in groups.items():
    if group['type'] == 'dynamic':
        criteria = group.get('criteria', {})
        # Find matching users
        group['members'] = [
            user['username']
            for user in users
            if all(user.get(key) == value for key, value in criteria.items())
        ]

# Save updated groups.json
with open('groups.json', 'w') as f:
    json.dump(groups, f, indent=2)

print("✅ Dynamic groups updated based on user titles.")
