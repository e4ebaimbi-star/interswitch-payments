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

                sh 'mkdir -p /tmp/interswitch_web'
                sh 'cp -r web/* /tmp/interswitch_web/'

                sh '''
                   mkdir -p /tmp/interswitch_deploy
                   cp -r /tmp/interswitch_web/* /tmp/interswitch_deploy/
                  '''

                echo 'Files deployed to /tmp/interswitch_deploy successfully.'
            }
        }    
 
        stage('Health Check') {
            steps {
                echo 'Verifying deployment...'
                sh '''
                    if [ ! -f /tmp/interswitch_deploy/index.html ]; then
                    echo "HEALTH CHECK FAILED: index.html not found in deploy directory"
                    exit 1
                fi
                echo "OK: index.html found"

                if ! grep -q 'Interswitch' /tmp/interswitch_deploy/index.html; then
                    echo "CONTENT CHECK FAILED: Page does not contain expected content"
                    exit 1
                fi
                echo "Content check passed: Interswitch portal files are in place"
            '''
            }
        }
    }    
    post {
        success {
            echo '================================================'
            echo "Pipeline ${APP_NAME} completed successfully."
            echo "BUILD #${BUILD_NUMBER} SUCCEEDED"
            echo "Job: ${JOB_NAME}"
            echo "Duration: ${currentBuild.durationString}"
            echo '================================================'
        }
        failure {
            echo '================================================'
            echo "Pipeline ${APP_NAME} FAILED. Check the console output above."
            echo "BUILD #${BUILD_NUMBER} FAILED"
            echo "Job: ${JOB_NAME}"
            echo 'Review the console output above for the failing step.'
            echo '================================================'   
        }
        always {
            echo "Build result: ${currentBuild.result ?: 'IN PROGRESS'}"
            // In a real pipeline, this is where you would:
            // - Send a Slack or email notification
            // - Archive build artefacts
            // - Clean up the workspace
        }
    }
}