document.addEventListener('DOMContentLoaded', function() {
    // Formu ve inputları seç
    const modelSelect = document.getElementById('model');
    const transmissionSelect = document.getElementById('transmission');
    const fuelTypeSelect = document.getElementById('fuelType');

    // Seçilecek olan araç modellerini belirledik
    const models = ['Fiesta', 'Focus', 'Puma', 'Kuga', 'EcoSport', 'C-MAX',
        'Mondeo', 'Ka+', 'Tourneo Custom', 'S-MAX', 'B-MAX', 'Edge', 'Tourneo Connect',
        'Grand C-MAX', 'KA', 'Galaxy', 'Mustang', 'Grand Tourneo Connect', 'Fusion', 'Ranger', 'Streetka', 'Escort', 'Transit Tourneo'];
    models.forEach(model => {
        const option = document.createElement('option');
        option.value = model;
        option.textContent = model;
        modelSelect.appendChild(option);
    });

    // Şanzıman ve yakıt türü seçeneklerini tanımladık
    const transmissions = ['Otomatik', 'Manuel', 'Yarı-Otomatik'];
    transmissions.forEach(transmission => {
        const option = document.createElement('option');
        option.value = transmission;
        option.textContent = transmission;
        transmissionSelect.appendChild(option);
    });
    // yakıt türü
    const fuelTypes = ['Benzin', 'Dizel', 'Hybrid', 'Elektirik', 'Diğer'];
    fuelTypes.forEach(fuelType => {
        const option = document.createElement('option');
        option.value = fuelType;
        option.textContent = fuelType;
        fuelTypeSelect.appendChild(option);
    });


    document.getElementById('predictionForm').addEventListener('submit', function(event) {
        const year = document.getElementById('year').value;
        const mileage = document.getElementById('mileage').value;
        const tax = document.getElementById('tax').value;
        const mpg = document.getElementById('mpg').value;
        const engineSize = document.getElementById('engineSize').value;

        if (!year || !mileage || !tax || !mpg || !engineSize) {
            alert('Lütfen tüm alanları doldurun.');
            event.preventDefault();
        }
    });
});
