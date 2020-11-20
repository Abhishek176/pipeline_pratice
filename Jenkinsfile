node {
    stage('Parameterize') {
        git url: 'ssh://git@code.dtcc.com:7999/cpe/ccoe-remediation-app.git',branch: "release/ec2-backup-cleanup-1"
        script{
            sh 'python read_data.py'
        }
           
    }
}
