pipeline {
    agent any
    
    stages {
        stage('拉取代码') {
            steps {
                git url: 'https://github.com/yq996/jkzdh_pingtai.git', branch: 'main',CredentialId:'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'
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
}
