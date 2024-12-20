document.getElementById('diabetes-form').onsubmit = async function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(event.target);
    const jsonData = Object.fromEntries(formData.entries());

    // Convert numeric fields from strings to numbers
    jsonData.pregnancies = Number(jsonData.pregnancies);
    jsonData.glucose = Number(jsonData.glucose);
    jsonData.bloodpressure = Number(jsonData.bloodpressure);
    jsonData.skinthickness = Number(jsonData.skinthickness);
    jsonData.insulin = Number(jsonData.insulin);
    jsonData.bmi = Number(jsonData.bmi);
    jsonData.diabetespedigreefunction = Number(jsonData.diabetespedigreefunction);
    jsonData.age = Number(jsonData.age);

    const response = await fetch('/api/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(jsonData),
    });

    const result = await response.json();

    // Display prediction result
    const resultDiv = document.getElementById('result');
    
    if (response.ok) {
        if (result.prediction === 1) {
            resultDiv.innerHTML = "<h3>Prediction: Diabetic</h3>";
        } else {
            resultDiv.innerHTML = "<h3>Prediction: Non-Diabetic</h3>";
        }
    } else {
        resultDiv.innerHTML = `<h3>Error: ${result.error}</h3>`;
    }
};