# 🌿 AI-Powered Plant Disease Detection

A Deep Learning based web application that detects plant diseases from leaf images using a Convolutional Neural Network (CNN) and Flask.

The model was trained on 38 plant disease classes and can predict diseases from uploaded leaf images through a simple web interface.

---

## 🚀 Features

* Upload a plant leaf image
* Detect plant diseases using a trained CNN model
* Display prediction confidence score
* Color-coded confidence indicator
* Show alternative predictions when confidence is low
* Responsive web interface built with Bootstrap
* Flask-powered deployment

---

## 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Scikit-Image
* Flask
* HTML
* CSS
* Bootstrap

---

## 📂 Dataset

## Dataset

This project was trained using a modified version of the New Plant Diseases Dataset.

Original dataset source:
https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset

The dataset structure and folder names were reorganized during preprocessing and training.

> The dataset is not included in this repository due to its large size.

---

## 🧠 Model Architecture

The CNN model consists of:

* Conv2D (32 Filters)
* MaxPooling2D
* Conv2D (64 Filters)
* MaxPooling2D
* Conv2D (128 Filters)
* MaxPooling2D
* Flatten Layer
* Dense (128 Neurons)
* Dense (38 Output Classes)

Optimizer:

* Adam

Loss Function:

* Sparse Categorical Crossentropy

---

## 📊 Training Performance

| Metric              | Value  |
| ------------------- | ------ |
| Training Accuracy   | 98.48% |
| Validation Accuracy | 93.89% |
| Validation Loss     | 0.2886 |

---

## 📸 Application Workflow

1. Upload a plant leaf image
2. Image is resized to 150 × 150
3. CNN model predicts the disease class
4. Confidence score is displayed
5. Top-3 predictions are shown when confidence is below 80%

---

## ▶️ Running the Project

### Clone Repository

```bash
git clone https://github.com/waseemvpds/Plant_Disease_Detection.git
cd Plant_Disease_Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

in your browser.

---

## 📁 Project Structure

```text
Plant_Disease_Detection/
│
├── app.py
├── plant_disease_model.keras
├── class_names.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── uploads/
│
└── .gitignore
```

---

## 🔮 Future Improvements

* Disease information and treatment suggestions
* Mobile-friendly UI enhancements
* Support for additional plant species
* Cloud deployment
* Real-time camera prediction
* Model explainability visualizations

---

## 👨‍💻 Author

**Waseem VP**

LinkedIn:
https://www.linkedin.com/in/waseemvpds/

GitHub:
https://github.com/waseemvpds

---

## ⭐ If you found this project useful, consider giving it a star.
