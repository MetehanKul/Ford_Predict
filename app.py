from flask import Flask, render_template, request
import pickle
import numpy as np
import traceback

app = Flask(__name__)

# Modeli yükle
model = None
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    if hasattr(model, 'predict'):
        print(f"Model yüklendi: {type(model)}")
    else:
        print("Yüklenen nesne bir model değil.")
except Exception as e:
    print(f"Model yüklenirken bir hata oluştu: {e}")


@app.route('/')
def anasayfa():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def tahmin_et():
    try:
        # Formdan gelen verileri alıyoruz
        model_adı = request.form.get('model')
        yıl = float(request.form.get('year', 0))
        şanzıman = request.form.get('transmission')
        kilometre = float(request.form.get('mileage', 0))
        yakıt_türü = request.form.get('fuelType')
        vergi = float(request.form.get('tax', 0))
        yakıt_tüketimi = float(request.form.get('mpg', 0))
        motor_hacmi = float(request.form.get('engineSize', 0))

        # Şanzıman ve yakıt türü gibi kategorik verileri encode et
        şanzıman_kodlanmış = {'Automatic': 0, 'Manual': 1, 'Semi-Auto': 2}.get(şanzıman, 0)
        yakıt_türü_kodlanmış = {'Petrol': 0, 'Diesel': 1, 'Hybrid': 2, 'Electric': 3, 'Other': 4}.get(yakıt_türü, 0)

        # Model adı gibi kategorik veriyi sayısal formata dönüştürme
        model_adı_kodlanmış = {
            'Fiesta': 0, 'Focus': 1, 'Puma': 2, 'Kuga': 3, 'EcoSport': 4, 'C-MAX': 5, 'Mondeo': 6, 'Ka+': 7,
            'Tourneo Custom': 8, 'S-MAX': 9, 'B-MAX': 10, 'Edge': 11, 'Tourneo Connect': 12, 'Grand C-MAX': 13,
            'KA': 14, 'Galaxy': 15, 'Mustang': 16, 'Grand Tourneo Connect': 17, 'Fusion': 18, 'Ranger': 19,
            'Streetka': 20, 'Escort': 21, 'Transit Tourneo': 22, 'Focus': 23
        }.get(model_adı,
              -1)  # Varsayılan olarak -1 kullanıyoruz

        # Özellikleri bir araya getir
        özellikler = np.array([
            model_adı_kodlanmış,  # Model adı kodlanmış
            yıl,
            şanzıman_kodlanmış,
            kilometre,
            yakıt_türü_kodlanmış,
            vergi,
            yakıt_tüketimi,
            motor_hacmi
        ]).reshape(1, -1)


        if model is not None and hasattr(model, 'predict'):
            tahmin = model.predict(özellikler)
            tahmin_metni = f"Tahmin edilen fiyat: {tahmin[0]:.2f} $"
        else:
            tahmin_metni = "Model yüklenirken bir hata oluştu"

        return render_template('index.html', prediction_text=tahmin_metni)

    except Exception as e:
        error_message = f"Bir hata oluştu: {e}\n{traceback.format_exc()}"
        print(error_message)
        return render_template('index.html', prediction_text=error_message)


if __name__ == '__main__':
    app.run(debug=True)
