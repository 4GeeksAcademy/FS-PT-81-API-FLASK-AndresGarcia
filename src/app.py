from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
{"label": "My first task", "done": False},
{"label": "My second task", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
  json_text = jsonify(todos)
  return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
  request_body = request.json
  todos.append(request_body)
  json_text = jsonify(todos)
  return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
  if 0 <= position < len(todos):
    todos.pop(position)
  else:
    return jsonify({"Error"})
  return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)