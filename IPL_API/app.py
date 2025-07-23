from flask import Flask,jsonify, request
import ipl

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route('/api/teams')
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)

@app.route('/api/teamvteam')
def teamVteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = ipl.teamVteamAPI(team1,team2)
    print(response)
    return jsonify(response)

@app.route('/api/team-record')
def team_record():
    team = request.args.get('team')

    response = ipl.team_recordAPI(team)
    return jsonify(response)

@app.route('/api/batsman-record')
def batting_record():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Missing 'name' parameter"}), 400
    response = ipl.batsmanAPI(name)
    return jsonify(response)

@app.route('/api/bowler-record')
def bowling_record():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Missing 'name' parameter"}), 400
    response = ipl.bowlerAPI(name)
    return jsonify(response)

app.run(debug =True)