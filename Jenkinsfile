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
     
	
    }
 
    post{
        always{
            allure results:[[path:'report/json_report']]
        }

        success {
            mail(
                to: 'yanq0405@163.com',
                subject: '构建成功',
                body: "恭喜，构建成功！"
            )
        }
        failure {
            mail(
                to: 'yanq0405@163.com',
                subject: '构建失败',
                body: "请注意，构建失败，请及时查看日志。"
            )
        }
    }
   
}
