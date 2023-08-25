from roboflow import Roboflow
import os

print("Current working directory:", os.getcwd())

rf = Roboflow(api_key="fFzjCpFlDM2cN1D0XgOj")

project = rf.workspace().project("bike-only")

model = project.version(2).model

image_path = r"H:\\User\\Desktop\\rqiue2.0\\Fiap\\CT_Python_Class\\CTU_Python\\PS2\\API\\images\\bicycleModel.jpg"
prediction_result = model.predict(image_path, confidence=40, overlap=30).json()
print(prediction_result)

#model.predict(image_path, confidence=40, overlap=30).save("prediction.jpg")

#hosted_prediction_result = model.predict(image_path, hosted=True, confidence=40, overlap=30).json()
#print(hosted_prediction_result)

#print(model.predict(image_path, hosted=True, confidence=40, overlap=30).json())