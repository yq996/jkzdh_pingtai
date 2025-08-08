pipeline {
    agent any
    tools {
        // 关联 Jenkins 中配置的 Allure 工具（名称要和系统配置里一致）
        allure 'Allure-2.24.1' 
    }
    stages {
        stage('拉取代码') {
            steps {
                git(
                    url: 'https://github.com/yq996/jkzdh_pingtai.git', 
                    branch: 'main', 
                    credentialsId: 'af4e933e-f1f4-4bab-b7e9-fbef5e60e531'
                )
            }
        }

        stage('创建虚拟环境') {
            steps {
                sh '''
                    # 确保系统有 Python3 和 venv 模块
                    python3 -m venv venv
                '''
            }
        }

        stage('安装依赖') {
            steps {
                sh '''
                    # 使用 POSIX 兼容的点命令激活虚拟环境，适配所有 Shell
                    . venv/bin/activate && \
                    pip install --upgrade pip && \
                    pip install -r requirements.txt && \
                    deactivate
                '''
            }
        }

        stage('运行测试') {
            steps {
                sh '''
                    # 同样使用点命令激活虚拟环境
                    . venv/bin/activate && \
                    # 替换为实际测试命令（例如 pytest 或项目启动命令）
                    python run.py && \
                    deactivate
                '''
            }
        }
    }

    post {
        always {
            // 指定 Allure 结果路径（根据实际测试生成的结果目录调整）
            allure results: [[path: 'report/json_report']] 
        }
        success {
            mail(
                to: 'yanq0405@163.com,yanq@pwithe.com',
                subject: "✅ 构建成功：${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "点击查看详情：${env.BUILD_URL}"
            )
        }
        failure {
            mail(
                to: 'yanq0405@163.com,yanq@pwithe.com',
                subject: "❌ 构建失败：${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "点击查看详情：${env.BUILD_URL}"
            )
        }
    }
}
