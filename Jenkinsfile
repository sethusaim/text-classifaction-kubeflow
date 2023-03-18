pipeline {
  agent any

  stages {
    stage('Cloning Git') {
      steps {
        git branch: 'main', url: 'https://github.com/sethusaim/text-classification-tekton.git'
      }
    }

    stage('Build and Push Data Ingestion Component') {
      when {
        changeset 'ecom/data_ingestion/*'
      }

      steps {
        script {
          sh 'bash scripts/build_and_push_component.sh ecom/data_ingestion ecom_data_ingestion ${BUILD_NUMBER}'
        }

        build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER), string(name: 'REPO_NAME', value: 'ecom_data_ingestion'), string(name: 'COMP_FILE', value: 'data_ingestion.yaml')]
      }
    }

    stage('Build and Push Data Validation Component') {
      when {
        changeset 'ecom/data_validation/*'
      }

      steps {
        script {
          sh 'bash scripts/build_and_push_component.sh ecom/data_validation ecom_data_validation ${BUILD_NUMBER}'
        }

        build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER), string(name: 'REPO_NAME', value: 'ecom_data_validation'), string(name: 'COMP_FILE', value: 'data_validation.yaml')]
      }
    }

    stage('Build and Push Data Transformation Component') {
      when {
        changeset 'ecom/data_transformation/*'
      }

      steps {
        script {
          sh 'bash scripts/build_and_push_component.sh ecom/data_transformation ecom_data_transformation ${BUILD_NUMBER}'
        }

        build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER), string(name: 'REPO_NAME', value: 'ecom_data_transformation'), string(name: 'COMP_FILE', value: 'data_transformation.yaml')]
      }
    }

    stage('Build and Push Model Training Component') {
      when {
        changeset 'ecom/model_training/*'
      }

      steps {
        script {
          sh 'bash scripts/build_and_push_component.sh ecom/model_training ecom_model_training ${BUILD_NUMBER}'
        }

        build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER), string(name: 'REPO_NAME', value: 'ecom_model_training'), string(name: 'COMP_FILE', value: 'model_training.yaml')]
      }
    }

    stage('Build and Push Model Evaluation Component') {
      when {
        changeset 'ecom/model_evaluation/*'
      }

      steps {
        script {
          sh 'bash scripts/build_and_push_component.sh ecom/model_evaluation ecom_model_evaluation ${BUILD_NUMBER}'
        }

        build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER), string(name: 'REPO_NAME', value: 'ecom_model_evaluation'), string(name: 'COMP_FILE', value: 'model_evaluation.yaml')]
      }
    }

    stage('Build and Push Model Pusher Component') {
      when {
        changeset 'ecom/model_pusher/*'
      }

      steps {
        script {
          sh 'bash scripts/build_and_push_component.sh ecom/model_pusher ecom_model_pusher ${BUILD_NUMBER}'
        }

        build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER), string(name: 'REPO_NAME', value: 'ecom_model_pusher'), string(name: 'COMP_FILE', value: 'model_pusher.yaml')]
      }
    }
  }
}