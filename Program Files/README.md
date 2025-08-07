# Poultry Disease Classification Project

## ✅ Summary
This project uses a Convolutional Neural Network (CNN) to classify poultry images into 4 categories:
- Coccidiosis
- Healthy
- Newcastle
- Salmonella

A custom model was trained on labeled image data and deployed using a Flask web application for real-time prediction.

## 🧪 Testing
Users can upload poultry images through the web interface (`app.py`), and the model will return the predicted disease class.

## 📦 Contents
- `app.py` - Flask app to run the interface
- `templates/index.html` - HTML UI
- `static/` - Folder to store uploaded images
- `test_images/` - Sample folder for new predictions
- `poultry_model.h5` - Trained model file
- `requirements.txt` - List of dependencies
- `README.md` - Project summary and instructions

## 🚀 How to Run
1. Install requirements:
   ```
   pip install -r requirements.txt
   ```

2. Run the Flask app:
   ```
   python app.py
   ```

3. Open your browser at:
   ```
   http://127.0.0.1:5000/
   ```

Upload an image and view the prediction!

---

📬 For help, contact the developer.
