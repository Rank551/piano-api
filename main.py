# Abdul Malik Hub - Official Cloud Piano API Server (2026)
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

OFFICIAL_SHEETS = {
    "solas": "[0et] u o a s d s a [qey] u o a s d s a [0et] p o i u y t [qey] i u y t r e [9wt] o u o t o",
    "interstellar": "t o s f t o s f r o a f r o a f [et] [eu] [ei] [eo] p o i u y t e",
    "rushe": "e e e e o p a s d f g h j k l z x c v b n m e e e e"
}

@app.route('/')
def home():
    return "Abdul Malik Hub Piano Server is Online! 🚀"

@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        data = request.json
        video_url = data.get("url", "").lower()
        
        if not video_url:
            return jsonify({"error": "No URL provided"}), 400
            
        chosen_notes = OFFICIAL_SHEETS["solas"]
        chosen_speed = 0.14
        
        for key in OFFICIAL_SHEETS.keys():
            if key in video_url:
                chosen_notes = OFFICIAL_SHEETS[key]
                if key == "interstellar": chosen_speed = 0.30
                if key == "rushe": chosen_speed = 0.07
                break

        return jsonify({
            "notes": chosen_notes,
            "speed": chosen_speed
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
