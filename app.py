from flask import Flask, request, render_template

from src.pipeline.predict_pipeline import CustomData, PredictPipeline


application = Flask(__name__)

app = application


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == 'GET':
        return render_template('home.html')

    else:

        data = CustomData(
            gender=request.form.get('gender'),

            race_ethnicity=request.form.get('race_ethnicity'),

            parental_level_of_education=request.form.get(
                'parental_level_of_education'
            ),

            lunch=request.form.get('lunch'),

            test_preparation_course=request.form.get(
                'test_preparation_course'
            ),

            reading_score=float(
                request.form.get('reading_score')
            ),

            writing_score=float(
                request.form.get('writing_score')
            )
        )

        pred_df = data.get_data_as_data_frame()

        print("Input Data:")
        print(pred_df)

        predict_pipeline = PredictPipeline()

        results = predict_pipeline.predict(pred_df)

        return render_template(
            'home.html',
            results=round(float(results[0]), 2)
        )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)