import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Load the CSV file
file_path = "weather_data.csv"  # Ensure the CSV is in the same directory
df = pd.read_csv(file_path)

# Data Analysis
avg_temp = df["Temperature (\u00b0C)"].mean()
avg_humidity = df["Humidity (%)"].mean()
avg_wind_speed = df["Wind Speed (m/s)"].mean()

max_temp_city = df.loc[df["Temperature (\u00b0C)"].idxmax(), "City"]
min_temp_city = df.loc[df["Temperature (\u00b0C)"].idxmin(), "City"]

# Visualization 1: Bar Chart for Temperature & Humidity
plt.figure(figsize=(8, 5))
plt.bar(df["City"], df["Temperature (\u00b0C)"], color='coral', label="Temperature (\u00b0C)")
plt.bar(df["City"], df["Humidity (%)"], color='lightblue', label="Humidity (%)", alpha=0.7)
plt.xlabel("City")
plt.ylabel("Value")
plt.title("Temperature & Humidity Levels by City")
plt.legend()
plt.xticks(rotation=45)
plt.savefig("temp_humidity_chart.png")
plt.close()

# Visualization 2: Pie Chart for Weather Conditions
condition_counts = df["Condition"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(condition_counts, labels=condition_counts.index, autopct="%1.1f%%", colors=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.title("Weather Conditions Distribution")
plt.savefig("weather_condition_chart.png")
plt.close()

# Generate PDF Report
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Automated Weather Report", ln=True, align="C")
pdf.ln(10)

# Summary Statistics
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, f"Average Temperature: {avg_temp:.2f}\u00b0C", ln=True)
pdf.cell(200, 10, f"Average Humidity: {avg_humidity:.2f}%", ln=True)
pdf.cell(200, 10, f"Average Wind Speed: {avg_wind_speed:.2f} m/s", ln=True)
pdf.cell(200, 10, f"Hottest City: {max_temp_city}", ln=True)
pdf.cell(200, 10, f"Coldest City: {min_temp_city}", ln=True)
pdf.ln(10)

# Add Bar Chart
pdf.cell(200, 10, "Temperature & Humidity Levels:", ln=True)
pdf.image("temp_humidity_chart.png", x=10, y=None, w=180)
pdf.ln(60)

# Add Pie Chart
pdf.cell(200, 10, "Weather Conditions Distribution:", ln=True)
pdf.image("weather_condition_chart.png", x=40, y=None, w=120)
pdf.ln(10)

# Save PDF
pdf.output("Weather_Report.pdf")

print("Report Generated: Weather_Report.pdf")
