# --- External Imports ---
from shiny.express import input, render, ui
from shiny import reactive
from collections import deque
import random
from datetime import datetime
import matplotlib.pyplot as plt

# --- UI Initialization ---
ui.page_opts(title="PyShiny Express: Live Data (Basic)", fillable=True)

# --- Sidebar Layout ---
with ui.sidebar(open="open"):
    ui.h2("Antarctic Explorer", class_="text-center")
    ui.p(
        "A demonstration of real-time temperature readings in Antarctica.",
        class_="text-center",
    )

# --- Input Control ---
ui.input_slider("n", "N", 0, 100, 20)

# --- Demonstrating Deque Usage ---
empty_deque = deque()
print("Empty deque:", empty_deque)

temp_deque_F = deque([56, 58, 47, 54, 55])
print("Deque (F):", temp_deque_F)

temp_list_C = [5, 6, 8, 4, 3, 2]
temp_deque_C = deque(temp_list_C)
print("Deque (C):", temp_deque_C)

temp_deque_F.extend([60, 62, 64, 61])
print("Updated Deque (F):", temp_deque_F)

# --- Reactive Timer Constants ---
UPDATE_INTERVAL_SECS: int = 1

# Maintain a rolling 24-hour buffer (max 86400 / UPDATE_INTERVAL_SECS readings)
temperature_history = deque(maxlen=int(86400 / UPDATE_INTERVAL_SECS))

# --- Reactive Temperature Generator ---
@reactive.calc()
def reactive_calc_combined():
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)
    temp = round(random.uniform(-18, -16), 1)
    timestamp = datetime.now()
    temperature_history.append({"temp": temp, "timestamp": timestamp})
    return {"temp": temp, "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S")}

# --- UI Content ---
ui.h2("Current Temperature")

@render.text
def display_temp():
    data = reactive_calc_combined()
    return f"{data['temp']} °C"

ui.p("Warmer than usual")

ui.hr()

ui.h2("Current Date and Time")

@render.text
def display_time():
    data = reactive_calc_combined()
    return data["timestamp"]

@render.code
def txt():
    return f"n*2 is {input.n() * 2}"

# --- Plot using matplotlib ---
@render.plot
def temp_trend_plot():
    times = [entry["timestamp"].strftime("%H:%M:%S") for entry in temperature_history]
    temps = [entry["temp"] for entry in temperature_history]

    plt.figure(figsize=(8, 4))
    plt.plot(times, temps, marker='o')
    plt.title("Temperature Trend (Last 24 Hours)")
    plt.xlabel("Time")
    plt.ylabel("Temp (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()

# --- Layout with Plot Output ---
with ui.layout_columns():
    with ui.card():
        ui.card_header("Temperature Trend (Last 24 Hours)")
        


