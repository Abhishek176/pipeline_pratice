import data
for acc_id, env_data in data.aws_accounts.items():
    print(acc_id, env_data['environment'])
