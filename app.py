from flask import Flask,render_template,request
import numpy as np
import os
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model
from skimage.io import imread
from skimage.transform import resize

app=Flask(__name__)

model=load_model("plant_disease_model.keras")

UPLOAD_FOLDER=r"static\uploads"
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

class_names=pickle.load(open("class_names.pkl","rb"))

print("Model Loaded Successfully")
print("Classes Loaded:",len(class_names))
def predict_image(path):
    img=imread(path)
    img=resize(img,(150,150,3))
    img=img.reshape(1,150,150,3)
    pred=model.predict(img)
    Pred_class=class_names[np.argmax(pred)]
    confidence=round(np.max(pred)*100,2)
    if confidence>=95:
        color="success"
    elif confidence>=80:
        color="warning"
    else:
        color="danger"

    top3_idx=np.argsort(pred[0])[-3:][::-1]
    top3=[]
    for i in top3_idx:
        top3.append((class_names[i],
                    round(float(pred[0][i])*100,2)))
    return Pred_class,confidence,color,top3

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])

def predict():
    file=request.files['image']
    filepath=os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
    file.save(filepath)
    disease,confidence,color,top3=predict_image(filepath)
    return render_template("index.html",prediction=disease,confidence=confidence,color=color,image_path=filepath,top3=top3)


if __name__=="__main__":
    app.run(debug=True)