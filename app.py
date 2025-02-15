from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_task():
    task_description = request.args.get('task')
    if not task_description:
        return jsonify({'error': 'Task description is required'}), 400

    try:
        # Here you would parse the task description and execute the task
        # For demonstration, let's assume the task is always successful
        # In a real scenario, you might use an LLM or other logic to handle the task
        result = f"Executed task: {task_description}"
        return jsonify({'result': result}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/read', methods=['GET'])
def read_file():
    file_path = request.args.get('path')
    if not file_path:
        return jsonify({'error': 'File path is required'}), 400

    if not os.path.exists(file_path):
        return '', 404

    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content, 200
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)