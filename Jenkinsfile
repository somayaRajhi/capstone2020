pipeline {
  agent {
    docker {
      image 'python:3.8'
    }
  }
  stages {
    stage('Create Virtual Environment') {
      steps {
        sh '''
          python3 -m venv .venv
          . .venv/bin/activate
          pip install -r requirements.txt
          pip install .
        '''
      }
    }

    stage('Unit Tests') {
      steps {
        sh '''
          . .venv/bin/activate
          make test
        '''
      }
      post {
        always {
          publishHTML target: [
            allowMissing: true,
            alwaysLinkToLastBuild: false,
            keepAll: true,
            reportDir: 'htmlcov',
            reportFiles: 'index.html',
            reportName: 'UT Coverage'
          ]
          junit 'unit-python.xml'
        }
      }

    }
    stage('Static Analysis') {
      steps {
        sh '''
          . .venv/bin/activate
          make static
        '''
      }
    }
  }
}
