from flask import Flask, request, render_template
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
model = load_model("poultry_model.h5")
class_names = ['Coccidiosis', 'Healthy', 'Newcastle', 'Salmonella']

UPLOAD_FOLDER = 'static'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    image_path = None
    if request.method == "POST":
        f = request.files["file"]
        file_path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(file_path)

        img = image.load_img(file_path, target_size=(128, 128))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        pred = model.predict(img_array)
        predicted_class = class_names[np.argmax(pred)]

        prediction = predicted_class
        image_path = file_path

    return render_template("index.html", prediction=prediction, image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)
