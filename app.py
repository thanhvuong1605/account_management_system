from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask,render_template,jsonify,json,request
from fabric import *

application = Flask(__name__)

client = MongoClient('localhost:27017')
db = client.accounts

@application.route('/')
def showAccountList():
    return render_template('list.html')

@application.route("/getAccountList",methods=['GET'])
def getAccountList():
    try:
        accounts = db.account.find()
        accountList = []
        for account in accounts:
            print (account)
            accountItem = {
                    'account_number':account['account_number'],
                    'balance':account['balance'],
                    'firstname':account['firstname'],
                    'lastname':account['lastname'],
                    'age':account['age'],
                    'gender':account['gender'],
                    'address':account['address'],
                    'employer':account['employer'],
                    'email':account['email'],
                    'city':account['city'],
                    'state':account['state'],
                    'id': str(account['_id'])
                    }
            accountList.append(accountItem)
    except Exception as e:
        return str(e)
    return json.dumps(accountList)

@application.route("/addAccount",methods=['POST'])
def addAccount():
    try:
        json_data = request.json['info']
        account_number = json_data['account_number']
        balance = json_data['balance']
        firstname = json_data['firstname']
        lastname = json_data['lastname']
        age = json_data['age']
        gender = json_data['gender']
        address = json_data['address']
        employer = json_data['employer']
        email = json_data['email']
        city = json_data['city']
        state = json_data['state']

        db.account.insert_one({
            'account_number':account_number,'balance':balance,'firstname':firstname,'lastname':lastname,'age':age,'gender':gender,'address':address,
            'employer':employer,'email':email,'city':city,'state':state
            })
        return jsonify(status='OK',message='inserted successfully')
    except Exception as e:
        return jsonify(status='ERROR',message=str(e))


@application.route('/getAccount',methods=['POST'])
def getAccount():
    try:
        accountID = request.json['id']
        account = db.account.find_one({'_id':ObjectId(accountID)})
        accountDetail = {
                'account_number':account['account_number'],
                'balance':account['balance'],
                'firstname':account['firstname'],
                'lastname':account['lastname'],
                'age':account['age'],
                'gender':account['gender'],
                'address':account['address'],
                'employer':account['employer'],
                'email':account['email'],
                'city':account['city'],
                'state':account['state'],
                'id': str(account['_id'])
                }
        return json.dumps(accountDetail)
    except Exception as e:
        return str(e)

@application.route('/updateAccount',methods=['POST'])
def updateAccount():
    try:
        json_data = request.json['info']
        accountID = json_data['id']
        account_number = json_data['account_number']
        balance = json_data['balance']
        firstname = json_data['firstname']
        lastname = json_data['lastname']
        age = json_data['age']
        gender = json_data['gender']
        address = json_data['address']
        employer = json_data['employer']
        email = json_data['email']
        city = json_data['city']
        state = json_data['state']

        db.account.update_one({'_id': ObjectId(accountID)},{'$set':{'account_number':account_number,'balance':balance,'firstname':firstname,'lastname':lastname,'age':age,'gender':gender,'address':address,
        'employer':employer,'email':email,'city':city,'state':state}})
        return jsonify(status='OK',message='updated successfully')
    except Exception as e:
        return jsonify(status='ERROR',message=str(e))


@application.route("/deleteAccount",methods=['POST'])
def deleteAccount():
    try:
        accountID= request.json['id']
        db.account.remove({'_id':ObjectId(accountID)})
        return jsonify(status='OK',message='deletion successful')
    except Exception as e:
        return jsonify(status='ERROR',message=str(e))

if __name__ == "__main__":
    application.run(host='0.0.0.0')
