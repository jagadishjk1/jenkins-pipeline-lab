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
                echo "testing config" > config/test-settings.yaml
                sh '''
                echo "Setting up test environment..."
                echo "Installing dependencies..."
                echo "Dependency 1 installed"
                echo "Dependency 2 installed"
                echo "Loading test config..."
                cat config/test-settings.yaml
                echo "Running tests..."
                echo "All tests passed"
            '''
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