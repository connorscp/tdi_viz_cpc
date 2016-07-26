import os

from bokeh.charts import Bar
from bokeh.embed import components
from flask import Flask, render_template
import pandas as pd


# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# Homepage
@app.route("/")
def index():
    return render_template('index.html')


# 1. Plot Some Data
@app.route("/counts-by-hour", methods=['GET', 'POST'])
def countsByHour():
	q1_counts_by_hour = pd.read_csv('data/q1_counts_by_hour.csv')

	p1 = Bar(q1_counts_by_hour,
         label='index',
         values='vehicle_id',
         title='Counts by Hour',
         xlabel='Timeframe',
         ylabel='Unique Vehicles on Road')

	script, div = components(p)
	print script
	print div

    return render_template('counts-by-hour.html', script=script, div=div)


# 2. Integrating Live Data
@app.route("/live-count-boxplot", methods=['GET', 'POST'])
def liveCountBoxplot():
    return render_template('live-count-boxplot.html')


# 3. Map Some Data
@app.route("/map-static", methods=['GET', 'POST'])
def mapStatic():
    return render_template('map-static.html')


# 4. Animate the Plot
@app.route("/map-animated", methods=['GET', 'POST'])
def mapAnimated():
    return render_template('map-animated.html')

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
