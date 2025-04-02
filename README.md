# HealthIndices_API

### Overview
The **Body Roundness Index (BRI)** is a geometric health metric introduced in 2013 to evaluate body shape and fat distribution using waist circumference and height. Unlike BMI, BRI provides a more nuanced assessment of total and visceral fat, offering better predictions for health risks such as cardiovascular disease and diabetes.

### Features

Built on top of <a href="https://github.com/zaqks/U2Net_BodyMeasurement">U2Net_BodyMeasurement</a> Model:

- **Input:** Two images (front and side view).
- **Output:** BRI score with associated health risk predictions.
- **Calibration:** Customizable for improved accuracy.

### Why BRI?
- **More Accurate:** Accounts for fat distribution, unlike BMI which overlooks lean vs. fat mass.
- **Health Insights:** Higher BRI scores (≥6.9) correlate with increased risks of mortality and metabolic diseases.

### Demo
<img width="100%" src="docs/demo.gif">
