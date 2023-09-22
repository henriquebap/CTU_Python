from roboflow import Roboflow
import os, json

print("Current working directory:", os.getcwd())

rf = Roboflow(api_key="fFzjCpFlDM2cN1D0XgOj")

project = rf.workspace().project("bike-only")

model = project.version(2).model

image_path = r"H:\\User\\Desktop\\rqiue2.0\\Fiap\\CT_Python_Class\\CTU_Python\\PS2\\API\\images\\bicycleModel.jpg"
prediction_result = model.predict(image_path, confidence=40, overlap=30).json()
print(prediction_result)

def explore_json(obj, prefix=""):
    if isinstance(obj, dict):
        for key, value in obj.items():
            explore_json(value, prefix + key + ".")
    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            explore_json(item, prefix + str(index)+ ".")
    else:
        print(f"Campo: {prefix[:-1]}, Valor: {obj}")
        
explore_json(prediction_result)


