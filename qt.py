from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'I love Yuting Qing forever'


if __name__ == '__main__':
    # app.run()
    # **这里得“0.0.0.0”代表任何ip都可访问，并非写成你的ip地址**端口是5200，你的安全组配置5000端口一定要打开
    app.run(host='0.0.0.0', port=5200)
