pipeline {
    agent any

    environment {
        APP_ENV = 'Devlopment_environment'
    }
    stages {
        stage ('Build'){
            steps{
                echo "Building the application in ${APP_ENV}..."
            }
        }
        
        stage ('Test'){
            steps{
                echo "Testing the application in ${APP_ENV}"
                sh 'exit 1'
            }
        }
        
        stage ('Deploy') {
            steps{
                echo "Deploying the application in ${APP_ENV}"
            }
        }
    }

    post{
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }

}