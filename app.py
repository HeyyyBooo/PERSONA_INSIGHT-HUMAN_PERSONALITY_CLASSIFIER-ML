# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:45:15 2024

@author: narze
"""




import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load("personality.pkl")

df = pd.DataFrame()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    global df
    
    input_features = [x for x in request.form.values()]
    
    
    for i in range(len(input_features)) :
        input_features[i]=int(input_features[i])
    features_value = np.array(input_features)
    

    output_arr = model.predict([features_value])
    output=output_arr[0].round(2)
    if(output==0):
        return render_template('page1.html', prediction_text='The Giver',desc='The Giver is a compassionate and altruistic individual, always seeking to contribute to the well-being of others. They derive immense satisfaction from helping those in need and creating a harmonious environment. Their selflessness and generosity make them valued members of any community.')
    elif(output==1):
        return render_template('page1.html', prediction_text='The Champion', desc='The Champion is an energetic and passionate advocate for causes they believe in. They fearlessly stand up for justice and are driven by a deep sense of purpose. Their enthusiasm and charisma inspire others to join their noble pursuits, making them natural leaders in social and political arenas.')
    elif(output==2):
        return render_template('page1.html', prediction_text='The Commander', desc='The Commander is a decisive and assertive personality, displaying strong leadership qualities. They excel in taking charge, making tough decisions, and driving projects forward. Their confidence and strategic thinking make them effective leaders in various domains.')
    elif(output==3):
        return render_template('page1.html', prediction_text='The Visionary', desc='The Visionary is an imaginative and forward-thinking individual, constantly exploring new ideas and possibilities. They possess a creative spark that fuels their innovative thinking, making them instrumental in shaping the future and pushing boundaries in different fields.')
    elif(output==4):
        return render_template('page1.html', prediction_text='The Provider', desc='The Provider is a dependable and nurturing personality, always ensuring the well-being and comfort of those around them. They derive fulfillment from creating a stable and secure environment for their loved ones and are adept at anticipating and meeting the needs of others.') 
    elif(output==5):
        return render_template('page1.html', prediction_text='The Performer',desc='The Performer is a charismatic and lively individual who thrives in the spotlight. They have a natural flair for entertaining and captivating audiences, whether on stage or in social settings. Their exuberance and creativity make them the life of the party.')
    elif(output==6):
        return render_template('page1.html', prediction_text='The Supervisor',desc='The Supervisor is an organized and detail-oriented individual, adept at managing people and resources efficiently. They excel in coordinating tasks and ensuring that projects are executed with precision. Their leadership style is marked by a focus on structure and accountability.')
    elif(output==7):
        return render_template('page1.html', prediction_text='The Doer', desc='The Doer is an action-oriented and pragmatic individual, driven by a strong work ethic. They thrive in hands-on situations, tackling challenges head-on and achieving tangible results. Their practical approach and perseverance make them valuable contributors in various fields.')
    elif(output==8):
        return render_template('page1.html', prediction_text='The Counselor', desc='The Counselor is an empathetic and insightful individual, skilled at understanding and supporting others emotionally. They excel in offering guidance and advice, creating a safe space for people to express their thoughts and feelings.')
    elif(output==9):
        return render_template('page1.html', prediction_text='The Idealist ',desc='The Idealist is a dreamer and an optimist, always striving for a better and more harmonious world. They are motivated by a sense of purpose and work tirelessly to bring their ideals to fruition. Their passion for social and humanitarian causes sets them apart.')
    elif(output==10):
        return render_template('page1.html', prediction_text='The Mastermind',desc='The Mastermind is a strategic and analytical thinker, capable of solving complex problems with ease. They possess a keen intellect and excel in devising innovative solutions. Their ability to see the bigger picture and plan for the future makes them natural leaders in various fields.')
    elif(output==11):
        return render_template('page1.html', prediction_text='The Thinker ',desc='The Thinker is a contemplative and introspective individual, constantly seeking to deepen their understanding of the world. They thrive in intellectual pursuits and are driven by a quest for knowledge and wisdom. Their thoughtful and reflective nature sets them apart in academic and philosophical circles.')
    elif(output==12):
        return render_template('page1.html', prediction_text='The Nurturer',desc='The Nurturer is a caring and supportive individual, dedicated to the well-being and growth of those around them. They excel in creating a nurturing environment and providing emotional support. Their compassion and patience make them pillars of strength in personal and professional relationships.')
    elif(output==13):
        return render_template('page1.html', prediction_text='The Composer', desc='The Composer is a creative and artistic personality, expressing themselves through various forms of art. They have a keen sense of aesthetics and are adept at creating beauty in the world. Their artistic talents enrich the lives of those around them.')
    elif(output==14):
        return render_template('page1.html', prediction_text='The Inspector',desc='The Inspector is a meticulous and detail-oriented individual, possessing a keen eye for accuracy and order. They excel in quality control and ensuring that processes adhere to standards. Their commitment to precision makes them valuable in roles requiring attention to detail.')
    elif(output==15):
        return render_template('page1.html', prediction_text='The Craftsman',desc='The Inspector is a meticulous and detail-oriented individual, possessing a keen eye for accuracy and order. They excel in quality control and ensuring that processes adhere to standards. Their commitment to precision makes them valuable in roles requiring attention to detail.')
    
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    