from flask import Flask,render_template,request

app=Flask(__name__)
# Dummy prediction function (replace with your actual model)
def predict_price(avg_rooms, avg_bedrooms, population):
    # Implement your model prediction here
    # This is just a placeholder return value
    return (avg_rooms + avg_bedrooms + population) * 1000

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        avg_rooms = request.form['avgAreaNumberOfRooms']
        avg_bedrooms = request.form['avgAreaNumberOfBedrooms']
        population = request.form['areaPopulation']
        
        # Convert inputs to float
        try:
            avg_rooms = float(avg_rooms)
            avg_bedrooms = float(avg_bedrooms)
            population = float(population)
        except ValueError:
            # Handle the exception if conversion fails
            return "Invalid input. Please ensure all fields are numbers."
        
        prediction = predict_price(avg_rooms, avg_bedrooms, population)
        
        # Pass the prediction to the result template
        return render_template('result.html', prediction=prediction)
if __name__=='__main__':
    app.run()