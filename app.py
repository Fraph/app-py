pipeline {
    agent any

    tools {
        // Aquí llamamos a la herramienta que configuramos en el paso 3.3
        jdk 'Default' // A veces necesario, si falla quítalo
        scannerHome 'sonar-scanner' 
    }

    stages {
        stage('Preparar Entorno') {
            steps {
                echo 'Iniciando pipeline con SonarQube...'
            }
        }
        
        // NUEVA ETAPA: Análisis de Código estático
        stage('Análisis de SonarQube') {
            steps {
                // "SonarQube" es el nombre que pusimos en el paso 3.2 (System)
                withSonarQubeEnv('SonarQube') {
                    // Ejecutamos el scanner pasando la KEY del proyecto
                    sh "${scannerHome}/bin/sonar-scanner \
                        -Dsonar.projectKey=App-Rodrigo-Caro \
                        -Dsonar.sources=. \
                        -Dsonar.python.version=3"
                }
            }
        }

        stage('Construir Imagen') {
            steps {
                script {
                    sh 'docker build -t app-rodrigo-caro:${BUILD_ID} .'
                }
            }
        }

        stage('Limpieza') {
            steps {
                sh 'docker rmi app-rodrigo-caro:${BUILD_ID}'
            }
        }
    }
}
