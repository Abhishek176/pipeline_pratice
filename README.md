# EC2_Volume_Remediation

#### branch
```branch
Enter the git branch name
```
#### account
```account
Enter account number
```
#### region
```region
Enter Region
```
#### scope
```scope
Enter SYSID to remediate only the specific application resources.
Enter ALL_SYSID to remediate all the resources in the account.
```
#### command
```command
Select the specific remediation command
```
#### preview
```preview
Set to true to display results of the remediation plan without taking any action.
```

# AutoTagger

#### branch
```branch
Enter the git branch name
```
#### account
```account
Enter account number
```
#### region
```region
Enter Region
```
#### command
```command
Select the specific remediation command
```
#### preview
```preview
Set to true to display results of the remediation plan without taking any action.
```
# EC2_Volume_Remediation

#### branch
```branch
Enter the git branch name
```
#### account
```account
Enter account number
```
#### region
```region
Enter Region
```
#### instance_id
```instance_id
instance ID, whose volumes to re-encrypt
```
#### new_kms_key_alias
```new_kms_key_alias
The value of the new CMK alias to use, if one is not found, a new one will be created
```
#### delete_original_volumes
```delete_original_volumes
When checked, this automation will delete the original volumes
```
#### restart_instance
```restart_instance
When checked, this automation will restart the EC2 instance
```
#### preview
```preview
When checked, this automation will display the remediation plan without taking any action
```
