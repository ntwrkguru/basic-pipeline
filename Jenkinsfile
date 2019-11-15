#!groovy

node {
    stage('Checkout source code') {
        updateGitlabCommitStatus name: 'build', state: 'pending'
        checkout scm
    }
    stage('Execute Playbook') {
        docker.image('juniper/pyez-ansible').inside('-u root -e ANSIBLE_FORCE_COLOR=true') {
            ansiColor('xterm') {
                echo "Running Ansible playbook"
                sh "ansible-playbook -i inventory/home.inv project/test.yml"
            }
        }
    }
    stage('Run a robot test') {
        def robotRunner = docker.build("robot-runner:${env.BUILD_ID}","./dockerfiles/robot")
        robotRunner.inside('-u root -v $WORKSPACE/:/tests -v $WORKSPACE/output/:/output') {
            sh 'robot -V /tests/robot/yaml/switch.yaml -d /output robot/tests/version_check.robot'
        }
        step([
                $class : 'RobotPublisher',
                outputPath : 'output',
                outputFileName : "*.xml",
                disableArchiveOutput : false,
                passThreshold : 100,
                unstableThreshold: 95.0,
                onlyCritical : true,
                otherFiles : "*.png",
            ])
        if (currentBuild.result == 'SUCCESS') {
            updateGitlabCommitStatus name: 'build', state: 'success'
        }
        
    }
}