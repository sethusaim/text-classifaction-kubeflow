pipeline {
  agent any

  stages {
    stage('Cloning Git') {
      steps {
        git branch: 'main', url: 'https://github.com/sethusaim/text-classification-tekton.git'
      }
    }

    stage('Build and Push Data Ingestion Component') {
      environment {
        COMP_FILE = "ecom_data_ingestion.yaml"

        REPO_NAME = "ecom_data_ingestion"
      }

      when {
        changeset 'ecom/data_ingestion/*'
      }

      steps {
        script {
          sh 'bash scripts/build_and_push_component.sh ecom/data_ingestion ${REPO_NAME} ${BUILD_NUMBER}'
        }

        build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER), string(name: 'REPO_NAME', value: env.REPO_NAME), string(name: 'COMP_FILE', value: env.COMP_FILE)]
      }
    }

    stage('Build and Push Data Validation Component') {
      environment {
        COMP_FILE = "ecom_data_validation.yaml"

        REPO_NAME = "ecom_data_validation"
      }

      when {
        changeset 'ecom/data_validation/*'
      }

      steps {
        script {
          sh 'bash scripts/build_and_push_component.sh ecom/data_validation ${REPO_NAME} ${BUILD_NUMBER}'
        }

        build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER), string(name: 'REPO_NAME', value: env.REPO_NAME), string(name: 'COMP_FILE', value: env.COMP_FILE)]
      }
    }

    stage('Build and Push Data Transformation Component') {
      environment {

        REPO_NAME = "ecom_data_transformation"

        COMP_FILE = "ecom_data_transformation.yaml"
      }

      when {
        changeset 'ecom/data_transformation/*'
      }

      steps {
        script {
          sh 'bash scripts/build_and_push_component.sh ecom/data_transformation ${REPO_NAME} ${BUILD_NUMBER}'
        }

        build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER), string(name: 'REPO_NAME', value: env.REPO_NAME), string(name: 'COMP_FILE', value: env.COMP_FILE)]
      }
    }

    stage('Build and Push Model Training Component') {
      environment {
        REPO_NAME = "ecom_model_training"

        COMP_FILE = "ecom_model_training.yaml"
      }

      when {
        changeset 'ecom/model_training/*'
      }

      steps {
        script {
          sh 'bash scripts/build_and_push_component.sh ecom/model_training ${REPO_NAME} ${BUILD_NUMBER}'
        }

        build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER), string(name: 'REPO_NAME', value: env.REPO_NAME), string(name: 'COMP_FILE', value: env.COMP_FILE)]
      }
    }

    stage('Build and Push Model Pusher Component') {
      environment {

        REPO_NAME = "ecom_model_pusher"

        COMP_FILE = "ecom_model_pusher.yaml"
      }

      when {
        changeset 'ecom/model_pusher/*'
      }

      steps {
        script {
          sh 'bash scripts/build_and_push_component.sh ecom/model_pusher ${REPO_NAME} ${BUILD_NUMBER}'
        }
      }
    }
  }
}