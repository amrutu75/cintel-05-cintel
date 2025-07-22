import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly

ui.page_opts(title="Filling layout", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
from collections import deque
# Create an empty deque
empty_deque = deque()
print(empty_deque) 

# Create a deque by passing in a list with values
temp_deque_F = deque( [56, 58, 47, 54, 55] )
print(temp_deque_F)  

# Create a deque by passing in a list variable
temp_list_C = [5, 6, 8, 4, 3, 2]
temp_deque_C = deque( temp_list_C )
print(temp_deque_C )
temp_deque_F.append(60)
temp_deque_F.append(62)
temp_deque_F.append(64)
temp_deque_F.append(61)
temp_deque_F.pop()  
temp_deque_F.popleft()  
len(temp_deque_F) 
from collections import deque

# Initialize deque with a max length of 3 to store last 3 stock prices
msft_prices = deque(maxlen=3)

# Clear the deque (we might call this at the start of a new day)
msft_prices.clear()

# Simulate updating the stock price with new values
msft_prices.append(310.35)
print("MSFT stock prices:", list(msft_prices))

msft_prices.append(312.31)
print("MSFT stock prices:", list(msft_prices))

msft_prices.append(315.25)
print("MSFT stock prices:", list(msft_prices))

msft_prices.append(317.41)
print("MSFT stock prices:", list(msft_prices))

