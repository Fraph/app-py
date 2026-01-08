pipeline {
    agent any

    stages {
        // Etapa 1: Descargar el código (Jenkins lo hace automático, pero aquí confirmamos)
        stage('Preparar Entorno') {
            steps {
                echo 'Iniciando pipeline para el Equipo Rodrigo Caro...'
            }
        }

        // Etapa 2: Construir la imagen Docker
        stage('Construir Imagen') {
            steps {
                script {
                    // Usamos la variable BUILD_ID para que cada imagen tenga una etiqueta única
                    sh 'docker build -t app-rodrigo-caro:${BUILD_ID} .'
                }
            }
        }

        // Etapa 3: "Test" (Verificación básica)
        stage('Verificar') {
            steps {
                // Como tu app es interactiva (pide input), no podemos "correrla" tal cual en la pipeline
                // porque se quedaría esperando a que alguien escriba.
                // Aquí solo verificamos que Python esté instalado dentro de la imagen.
                sh 'docker run --rm app-rodrigo-caro:${BUILD_ID} python --version'
            }
        }
        
        // Etapa 4: Limpieza (Opcional pero recomendada)
        stage('Limpieza') {
            steps {
                sh 'docker rmi app-rodrigo-caro:${BUILD_ID}'
            }
        }
    }
}
