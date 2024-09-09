from flask import Flask, jsonify
from sqlalchemy import text, create_engine
from flask_sqlalchemy import SQLAlchemy


app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:master2@localhost/projet"

db  = SQLAlchemy()
db.init_app(app)


@app.route('/', methods=['GET'])
def get_data():
    data = db.session.execute(text(f"SELECT * FROM test ORDER BY id")).all()
    data = [x._asdict() for x in data]
    return jsonify(object="list", data=data)


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=4000, debug=True)