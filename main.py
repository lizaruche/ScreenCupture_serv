from app import app
from constant import NO_IMG
from flask import request, jsonify, render_template, abort

STREAM = []

@app.route('/base64_img', methods=['POST'])
def dsfadas():
    request_data = request.get_json()

    base64_img = None
    img_format = None

    if request_data:
        if 'base64_img' in request_data:
            base64_img = request_data['base64_img']

        if 'format' in request_data:
            img_format = request_data['format']
    
    STREAM.append(f'data:image/{img_format};base64,{base64_img}')

    return jsonify({"message": "success"})


@app.route('/get_frame', methods=['GET'])
def get_frames():
    if len(STREAM) > 0:
        return jsonify({"last_frame": STREAM[-1],"success": 200})
    else:
        return jsonify({"success": 400})


@app.route('/clear_frames')
def clear_frames():
    STREAM.clear()
    return jsonify({"message": "STREAM IS CLEAR"})


@app.route('/number_of_frames')
def num_frames():
    return jsonify({"message": f"STREAM HAS {len(STREAM)} frames"})


@app.route('/')
def preview():
    return render_template('preview.html', no_img=NO_IMG, last_pack=len(STREAM))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
    