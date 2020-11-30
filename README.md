# How to Create a pipeline job
- Goto Jenkins homepage
- Click on New item inorder to create the job
- Provide a name of the job and select the type as pipeline job

# How to configure the pipeline job
- Open the job yo have created
- Click on configure
- Goto pipeline section of the job
- Select pipeline script from SCM from the dropdown list
- In SCM dropdown select the Git
- In Repository section provide the Repository URL where you have your jenkins and provide the credentials in order to access the repository and git branch name
- In the script path section provide your jenkins file name
- Then click on apply and save

# How to run the job
- Open the job and click on build
