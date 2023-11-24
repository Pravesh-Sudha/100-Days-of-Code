# Day 60 of 100DaysofCode

Feeling excited to start Day 60 of 100 DaysOfCode, today, I created a Jenkins Declartive CI/CD Pipeline Project, in which I get to know about Jenkins fundamenatals, docker, how to use jenkins along with docker and many more with the help of [ShumhamLondhe](https://www.youtube.com/live/AaVO1Mvr3q4?si=neGeDEZ0h-ugJxdz).

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-60
```

# Simple Notes App
This is a simple notes app built with React and Django.

## Requirements
1. Python 3.9
2. Node.js
3. React

## Installation
1. Clone the repository
```
git clone https://github.com/LondheShubham153/django-notes-app.git
```

2. Build the app
```
docker build -t notes-app .
```

3. Run the app
```
docker run -d -p 8000:8000 notes-app:latest
```

## 1. Install Jenkins<a name="install-jenkins"></a>

### Update Package Repository
```bash
sudo apt update
```

### Install Java Development Kit (JDK)
```bash
sudo apt install default-jdk -y
```

### Install Jenkins
```bash
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install jenkins -y
```

### Start Jenkins Service
```bash
sudo systemctl start jenkins
```

### Enable Jenkins Service on Boot
```bash
sudo systemctl enable jenkins
```

### Open Firewall Port (if using UFW)
```bash
sudo ufw allow 8080
```

Access Jenkins at `http://localhost:8080` in your web browser. Retrieve the initial admin password from `/var/lib/jenkins/secrets/initialAdminPassword`.

## 2. Setup Jenkins<a name="setup-jenkins"></a>

1. Open a web browser and navigate to `http://localhost:8080`.
2. Enter the initial admin password.
3. Follow the instructions to complete the setup wizard.
4. Install suggested plugins.

## 3. Install Required Plugins<a name="install-required-plugins"></a>

1. In Jenkins, go to "Manage Jenkins" > "Manage Plugins."
2. Navigate to the "Available" tab.
3. Search for and install the following plugins:
   - GitHub
   - Pipeline

## 4. Configure GitHub Integration<a name="configure-github-integration"></a>

1. In Jenkins, go to "Manage Jenkins" > "Configure System."
2. Scroll down to the "GitHub" section.
3. Add GitHub credentials (username and personal access token).
4. Test the connection to GitHub.

## 5. Create a Pipeline<a name="create-a-pipeline"></a>

1. Create a new item (project) in Jenkins.
2. Select "Pipeline" as the project type.
3. In the pipeline configuration, set the pipeline script from the SCM.
4. Choose Git as the SCM, and provide the GitHub repository URL (`https://github.com/LondheShubham153/django-notes-app`).
5. Set the script path to `Jenkinsfile` (create this file in your project repository).

Example `Jenkinsfile`:
```groovy
pipeline {
    agent any
    
    stages {
        
        stage('Clone Code'){
            steps {
                echo 'Cloning the Code'
                git url:'https://github.com/LondheShubham153/django-notes-app.git', branch: 'main'
            }
        }
        
        stage('Build'){
            steps {
                    echo 'Building the Image'
                    sh 'docker build -t my-note-app .'
            }    
        }
        
        stage('Push to Docker Hub'){
            steps {
                echo 'Pushing the image to Docker Hub'
                withCredentials([usernamePassword(credentialsId: "<your-cred-ID>",
                passwordVariable:'dockerPass', usernameVariable:'dockerUser')]){
                    sh 'docker login -u ${env.dockerUser} -p ${env.dockerPass}'
                }
                sh 'docker tag my-notes-app ${env.dockerUser}/my-note-app'
                sh 'docker push ${env.dockerUser}/my-note-app'
            }
        }
        
        stage('Deploy'){
            steps {
                echo 'Deploying the Container'
                sh 'docker-compose down && docker-compose up -d'
            }
        }
        
    }
    
}
```

## 6. Run the Pipeline<a name="run-the-pipeline"></a>

1. Save the pipeline configuration.
2. Trigger the pipeline manually or set up automatic triggers.
3. View the pipeline progress and logs in Jenkins.

## 7. Configre Credentials of DockerHub

1. Go to Dashboard -> Manage Jenkins -> Credentials under Security tab.
2. Select Username and Password, add your credentials, give a ID name.
3. Save Your credentials.


