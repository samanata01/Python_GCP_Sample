from flask import Flask,jsonify

app=Flask(__name__)
#App running on flask's defsult port 5000
@app.route('/', methods=['GET'])
def home():
    message='Welcome in Home Page'
    return jsonify({'myres':message})

@app.route('/cal/<int:num>',methods=['GET'])
def cal(num):

    message='number is: '+ str(num)
    sq=num*num
    return jsonify({
        'serversays':message,
        'square': sq
        })

fruits=['apple','Banana','Orange']
@app.route('/fruits', methods=['GET'])
def getfr():
    return jsonify({
        'mfr':fruits
    })

@app.route('/fruits/<string:fr>', methods=['GET'])
def addfr(fr):
    fruits.append(fr)
    return jsonify({
        'mfr':fruits
    })

if __name__=='__main__':
    app.run(debug=True)
