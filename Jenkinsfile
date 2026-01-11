pipeline {
    agent any
    options {
        timestamps()
    }
    parameters {
        string(name: "BASE_URL", defaultValue: "http://host.docker.internal:5173", description: "LocalAutomationApp base URL.")
        string(name: "BROWSER", defaultValue: "chrome", description: "Browser name (chrome recommended).")
        string(name: "HEADLESS", defaultValue: "true", description: "Run browser in headless mode (true/false).")
        string(name: "REMOTE_URL", defaultValue: "http://selenium:4444/wd/hub", description: "Remote Selenium URL.")
        booleanParam(name: "USE_APP_PROFILE", defaultValue: false, description: "Use LocalAutomationApp from docker compose --profile app.")
    }
    environment {
        BASE_URL = "${params.BASE_URL}"
        BROWSER = "${params.BROWSER}"
        HEADLESS = "${params.HEADLESS}"
        REMOTE_URL = "${params.REMOTE_URL}"
    }
    stages {
        stage("Resolve Base URL") {
            steps {
                script {
                    if (params.USE_APP_PROFILE) {
                        env.BASE_URL = "http://local-frontend:5173"
                    }
                }
            }
        }
        stage("Install") {
            steps {
                sh "python3 -m venv .venv"
                sh ". .venv/bin/activate && pip install -r requirements.txt"
            }
        }
        stage("Tests") {
            steps {
                sh ". .venv/bin/activate && mkdir -p reports && pytest -q --base-url=${BASE_URL} --browser=${BROWSER} --headless=${HEADLESS} --remote-url=${REMOTE_URL} --junitxml=reports/junit.xml"
            }
        }
    }
    post {
        always {
            junit "reports/junit.xml"
        }
    }
}
