from flask import Flask, render_template, request, send_file
import datetime
import json

app = Flask(__name__)


def get_maintenance_steps(stage):
    steps = {
        "Germination": "Ensure proper moisture and temperature conditions. Avoid overwatering.",
        "Seedling": "Provide proper nutrients. Monitor for pests and diseases.",
        "Vegetative": "Regular watering and fertilization. Pruning if required.",
        "Flowering": "Monitor pollination. Control pests and provide micronutrients.",
        "Fruiting": "Ensure optimal watering and nutrient supply. Harvest on time."
    }
    return steps.get(stage, "No specific maintenance steps available.")


def generate_report(crop_type, seed_type, stage, days, health):
    report = {
        "Crop Type": crop_type,
        "Seed Type": seed_type,
        "Stage": stage,
        "Days Since Planting": days,
        "Health Condition": health,
        "Maintenance Steps": get_maintenance_steps(stage),
        "Generated On": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return report


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        crop_type = request.form['crop_type']
        seed_type = request.form['seed_type']
        stage = request.form['stage']
        days = request.form['days']
        health = request.form['health']

        report = generate_report(crop_type, seed_type, stage, days, health)
        with open("static/agriculture_report.json", "w") as file:
            json.dump(report, file, indent=4)

        return render_template('index.html', report=report)

    return render_template('index.html', report=None)


@app.route('/download_report')
def download_report():
    return send_file("static/agriculture_report.json", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
