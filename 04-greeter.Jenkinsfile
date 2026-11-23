pipeline {
   agent any

   environment {
        APP_NAME = greeter
   }

   parameters {
        choice(name:'TARGET_ENV', choices:['dev', 'qa', 'prod'], description: 'Select the Environment')
        string(name: 'RELEASE_VERSION', defaultValue: '0.1.0', description: 'Enter the release version')
        booleanParam(name:'RUN_TESTS', defaultValue: true, description: 'check/uncheck the box to run tests')
   }

   stages{

        stage('info') {
            steps {
                sh "echo App Name: $APP_NAME"
                sh "echo Release version : ${params.RELEASE_VERSION}"
                sh "echo Target Environment : ${params.TARGET_ENV}"
                sh "echo Build number : $BUILD_NUMBER"
                sh "echo Git commit: $GIT_COMMIT"
            }
        }
        stage('test'){
            when {
                beforeAgent true
                expression {params.RUN_TESTS}
            }
            
            agent {
                docker { image 'python:3.11-slim' }
            }

            steps  {
                
                sh ''' 
                    python -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r app/requirements-dev.txt
                    python -m pytest tests -v --junitxml=test-results.xml
                    '''
            }
            post {
                always {
                    junit 'backend/test-results.xml'
                }
            }
        stage('publish') {
            when {
                anyof {
                    expression { params.ENVIRONMENT == 'qa'}
                    expression { params.ENVIRONMENT == 'prod'}
                    }
                }
           environment {
                REGISTRY_CREDS = credentials('lab-registry')
                }

            steps{
                sh "echo Publishing greeter 0.1.0 as $REGISTRY_CREDS.USER"
                }
            }

            stage('deploy') {
                steps {
                    sh"echo Deploying greeter 0.1.0 to ${params.TARGET_ENV}"
                }
            }

        }          
   }

   post {
            success { echo 'Pipeline finished successfully!' }
            failure { echo 'Pipeline failed. Check the console output.' }
   }


}