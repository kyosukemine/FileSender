from flask import Flask, send_file
app = Flask(__name__)



@app.route('/')
def index():
    return "<html><h>ダウンロードファイル</h3><a href='/export/file1'>ダウンロード ファイル１</a><br><br><br><br><a href='/export/file2'>ダウンロード ファイル２</a></html>"


@app.route("/export/file1")
def export_action_file1():
    filepath = "./file1.zip"#"送りたいファイルのパス/ファイル１"
    return send_file(
        filepath,
        as_attachment=True
    )

@app.route("/export/file2")
def export_action__file2():
    filepath = "./file2.zip"#"送りたいファイルのパス/ファイル２"
    return send_file(
        filepath,
        as_attachment=True
    )


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True,host='0.0.0.0', port=80)
