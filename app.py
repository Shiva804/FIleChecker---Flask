from flask import Flask,render_template,request,url_for,redirect
from FileExplorer import file_size,robo1,rootfile,dele

app=Flask(__name__)

@app.route('/')

def index():
    root = rootfile()
    return render_template("index.html",root=root)

@app.route('/',methods=['POST'])

def robo():
    print("came here")
    r1=request.form['dir1']
    t1=request.form['type1']
    robo1(r1,t1)
    return redirect(url_for('index'))


@app.route('/delete',methods=['POST'])

def delete():
    dele()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
