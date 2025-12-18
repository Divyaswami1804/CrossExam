from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from logic.rules import analyze_answer
from logic.scorer import calculate_score, determine_verdict
from logic.flip import apply_decision_flip
from llm.adversary import get_gemini_counter

app = Flask(__name__)
CORS(app)


@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        data = request.get_json()

        if not data or 'answer' not in data:
            return jsonify({'error': 'Missing answer field'}), 400

        answer = data['answer'].strip()

        if not answer:
            return jsonify({'error': 'Answer cannot be empty'}), 400

        print(f"Received answer: {answer[:50]}...")

        analysis = analyze_answer(answer)
        print(f"Analysis complete: {len(analysis['flags'])} flags")

        gemini_counter = get_gemini_counter(answer)
        print(f"Gemini response received")

        score = calculate_score(analysis)
        verdict = determine_verdict(score)

        verdict, score = apply_decision_flip(verdict, score)

        result = {
            'flags': analysis['flags'],
            'gemini_counter': gemini_counter,
            'score': score,
            'verdict': verdict,
            'word_count': analysis['word_count']
        }

        print(f"Final verdict: {verdict}, Score: {score}")

        return jsonify(result)

    except Exception as e:
        print(f"Error in /evaluate: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'message': 'Flask server is running'})


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'CrossExam Flask Server',
        'endpoints': ['/health', '/evaluate']
    })


if __name__ == '__main__':
    print("=" * 50)
    print("CrossExam Flask Server Starting...")
    print("Server will run on: http://localhost:5000")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)