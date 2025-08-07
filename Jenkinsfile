pipeline {
    agent any
    tools{
		allure'Allure-2.24.1'
    }
    stages {
        stage('拉取代码') {
            steps {
                git url: 'https://github.com/yq996/jkzdh_pingtai.git', branch: 'main',credentialsId:'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'
            }
        }
        
        stage('安装依赖') {
            steps {
                sh '''
                    # 直接使用虚拟环境中的pip安装依赖
                    /var/jenkins_home/workspace/jkzdh_pingtai/venv/bin/pip install -r requirements.txt
                '''
            }
        }
        
        stage('运行测试') {
            steps {
                sh '''
                    # 替换为你的实际测试命令，例如：
                    /var/jenkins_home/workspace/jkzdh_pingtai/venv/bin/python run.py
                '''
            }
        }
        stage('Test Network') {
            steps {
                sh 'ping -c 4 smtp.163.com'
                sh 'nslookup smtp.163.com'
                sh 'curl -v smtps://smtp.163.com:465' // 可能失败，但能验证 SSL/TCP 建链
            }
        }
	
    }
 
    post{
        always{
            allure results:[[path:'report/json_report']]
        }

        success {
            emailext(
             mail to: "yanq0405@163.com" ,
             subject: "Jenkins Job Failed: ${env.JOB_NAME}",
             body: "Job ${env.JOB_NAME} (#${env.BUILD_NUMBER}) failed.\nCheck it at ${env.BUILD_URL}"
            )
        }

        failure {
           mail to: "yanq0405@163.com" ,
             subject: "Jenkins Job Failed: ${env.JOB_NAME}",
             body: "Job ${env.JOB_NAME} (#${env.BUILD_NUMBER}) failed.\nCheck it at ${env.BUILD_URL}"
        }
    }
   
}
