from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from models.task import Task

app = Flask(__name__)


SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.yaml'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)

tasks = []
task_id_control = 1

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data["title"], description=data["description"])
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Task created successfully", "id": new_task.id})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    all_tasks = [task.to_dict() for task in tasks]
    output = {
        'total_tasks': len(all_tasks),
        'tasks': all_tasks,
    }
    return jsonify(output)

@app.route("/tasks/<int:id>", methods=["GET"])
def get_task_by_id(id):
    for task in tasks:
       if task.id == id:
           return jsonify(task.to_dict())
    return jsonify({"message": "Task not found"})

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted successfully"})
    return jsonify({"message": "Task not found"}), 404

@app.route("/tasks/<int:id>", methods=["PUT"])
def updato_task(id):
    data = request.get_json()
    for task in tasks:
        if task.id == id:
            task.title = data["title"]
            task.description = data["description"]
            task.completed = data["completed"]
            return jsonify({"message": "Task updated successfully"})
    return jsonify({"message": "Task not found"}), 404

if __name__ == '__main__':
  app.run(debug=True)