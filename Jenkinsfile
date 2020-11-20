node {
    stage('Parameterize') {
        git url: 'ssh://https://github.com/Abhishek176/test.git',branch: "main"
        script{
            sh 'python read_data.py'
        }
           
    }
}
