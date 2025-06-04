pipeline {
   agent any

   environment {
     IMAGE_NAME = "monitoring-api"
     CONTAINER_NAME = "monitoring-api"
   }

   stages {
     stage('Checkout'){
       steps {
         git branch: 'main', url: 'https://github.com/princemitnick/server-monitoring-api.git'
       }
     }

     stage('Inject Secrets + Create .env') {
       steps {
         sh """
           echo "MONGO_URI=mongodb://localhost:27017" > .env
           echo "MONGO_DB=monitoring" >> .env
           echo "MONGO_COLLECTION=metrics" >> .env
         """
       }
     }

     stage('Build Docker Image') {
       steps {
         script {
           echo "[+] Building Docker image..."
           sh "docker build -t ${IMAGE_NAME}:latest ."
         }
       }
     }

     stage('Deploy MongoDB') {
       steps {
         sh """
           docker stop mongodb || true
           docker rm mongodb || true
           docker run -d --name mongodb -p 27017:27017 mongo
         """
       }
     }

     stage('Stop Previous Container') {
       steps {
         script {
           echo "[+] Stopping old container if exists..."
           sh "docker stop ${CONTAINER_NAME} || true"
           sh "docker rm ${CONTAINER_NAME} || true"
         }
       }
     }

     stage('Run New Container'){
       steps {
         script {
           echo "[+] Running new container..."
           sh """
              docker run -d \\
                --name ${CONTAINER_NAME} \\
                -p 8000:8000 \\
                --env-file .env \\
                --link mongodb \\
                ${IMAGE_NAME}:latest
           """
         }
       }
     }
   }
   post {
     success {
       echo "[✓] Deployment succeeded."
     }
     failure {
       echo "[✗] Deployment failed."
     }
   }
}