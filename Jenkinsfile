node {
    stage('Parameterize') {
        git url: 'ssh://https://github.com/Abhishek176/pipeline_pratice.git',branch: "main"
        script{
            sh 'python read_data.py'
        }
           
    }
}
