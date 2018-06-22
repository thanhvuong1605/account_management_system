# Account management system
Simple application using Flask, Angularjs and MongoDB

## Dependencies

### Install MongoDB
https://docs.mongodb.com/manual/installation/

### Install PIP
https://pip.pypa.io/en/stable/installing/

### Install Flask
http://flask.pocoo.org/docs/1.0/installation/

### Install Flask Dependencies
```bash
pip install pymongo
pip install fabric
```

## Usage
```bash
python app.py
```

## Import accounts.json to MongoDB
```bash
mongoimport --db accounts --collection account --file accounts.json
```

View app at http://localhost:5000/
