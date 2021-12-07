from flask import Flask, send_file
app = Flask(__name__)


@app.route('/')
def index():
    return "<html><h3>実習資料</h3><a href='/export/raspberrypi'>ダウンロード RaspberryPi用</a><br><br><br><br><a href='/export/pc'>ダウンロード PC用</a></html>"


@app.route("/export/raspberrypi")
def export_action_raspi():
    filename = "./DX_raspi.zip"#"送りたいファイルのパス/ラズパイ用"
    return send_file(
        filename,
        as_attachment=True
    )

@app.route("/export/pc")
def export_action_pc():
    filename = "./DX_PC.zip"#"送りたいファイルのパス/パソコン用"
    return send_file(
        filename,
        as_attachment=True
    )


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True,host='0.0.0.0', port=80)
