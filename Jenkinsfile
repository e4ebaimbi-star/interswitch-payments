pipeline {
    agent any

    environment {
        APP_NAME = 'interswitch-merchant-portal'
        WEB_DIR  = 'web'
    }

    stages {

        stage('Validate') {
            steps {

                echo '================================================'
                echo "Pipeline: ${APP_NAME}"
                echo "Build: #${BUILD_NUMBER}"
                echo "Branch: ${GIT_BRANCH}"
                echo '================================================'
                echo ''

                echo 'Checking web directory...'
                sh 'ls -la web/'

                echo 'Checking index.html exists and is not empty...'
                sh '''
                    if [ ! -f web/index.html ]; then
                        echo 'ERROR: web/index.html not found'
                        exit 1
                    fi

                    if [ ! -s web/index.html ]; then
                        echo 'ERROR: web/index.html is empty'
                        exit 1
                    fi

                    echo 'OK: web/index.html found and is not empty'
                '''

                echo 'Checking style.css exists and is not empty...'
                sh '''
                    if [ ! -f web/style.css ]; then
                        echo 'ERROR: web/style.css not found'
                        exit 1
                    fi

                    if [ ! -s web/style.css ]; then
                        echo 'ERROR: web/style.css is empty'
                        exit 1
                    fi

                    echo 'OK: web/style.css found and is not empty'
                '''

                echo 'Validate stage complete. All files present.'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Starting local deployment...'

                  // Ensure the staging directory exists
                sh 'mkdir -p /tmp/interswitch_web'

                 // Copy the web files to the staging directory
                sh 'cp -r web/* /tmp/interswitch_web/'

                // Move files into a local "web root" and fix permissions
                sh '''
                    sudo mkdir -p /usr/share/nginx/html
                    sudo cp -r /tmp/interswitch_web/* /usr/share/nginx/html/
                    sudo chown -R $(whoami):$(whoami) /usr/share/nginx/html/
                    sudo chmod -R 755 /usr/share/nginx/html/
                  '''

                echo 'Files deployed to local Nginx web root successfully.'
            }
        }    
    }

    post {
        success {
            echo "Pipeline ${APP_NAME} completed successfully."
        }

        failure {
            echo "Pipeline ${APP_NAME} FAILED. Check the console output above."
        }
    }
}