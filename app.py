from agent import agent
from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS


import pandas as pd


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Maverick Analytics AI Microservice"})


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]

    """Save the csv file """
    save_path = f"./uploads/{file.filename}"
    with open(save_path, "wb+") as destination:
        destination.write(file.read())

    """return a success response status code"""
    response = jsonify({"filename": f"{file.filename}"})
    response.status_code = 200

    return response


@app.route("/query", methods=["POST"])
def analyse():
    query = request.form["query"]
    filename = request.form["filename"]

    try:
        print(filename)
        file = "./uploads/" + filename
        df = pd.read_csv(file)
        print(df.head(3))
        """create an agent"""
        agents = agent(df)
        print("agent created")
        response = agents.invoke(query)
        response = response["output"]
        return jsonify({"answer": response})
    except Exception as e:
        print(e)
        response = {"error": "something happened"}
        return response


if __name__ == "__main__":
    app.run(debug=True)
