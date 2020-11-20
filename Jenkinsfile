node {
    stage('Parameterize') {
        git branch: 'main', url: 'https://github.com/Abhishek176/test.git'
        script{
            sh 'python read_data.py'
        }
           
    }
}
