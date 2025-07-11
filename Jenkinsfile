pipeline {
    agent none
	stages {
	    stage('Hello World') {
	        agent {
	            docker { image 'node:16-alpine' }
	        }
	        steps {
	            echo 'Hello World'
	            sh 'node --version'
	            sh 'ls'
	        }
	    }
	    stage('Test') {
	        agent {
	            docker { image 'python:3' }
	        }
	        steps {
	            sh 'python --version'
	            sh 'python -m venv .venv'
	            sh 'ls'
                sh '''
. .venv/bin/activate
pip install pytest
pytest
'''
	        }
	    }
	}
}
