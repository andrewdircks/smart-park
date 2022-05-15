import os
import psycopg2
import numpy as np
import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
load_dotenv()

conn = psycopg2.connect(
    user=os.environ['DB_USER'],
    host=os.environ['DB_HOST'],
    port=os.environ['DB_PORT'],
    database=os.environ['DB_NAME'],
    password=os.environ['DB_PASSWORD']
)

with conn:
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM PARKING'
    )
    data = cursor.fetchall()

dists = [t[2] for t in data]
times = [t[3] for t in data]
times_fmt = [t.strftime('%-m/%-d %-H') for t in times]
times_fmt_min = [t.strftime('%-m/%-d %-H:%M') for t in times]

# # plt.plot(range(len(times)), dists)
# plt.plot(range(len(parked_dists)), parked_dists)
# plt.xlabel('Time')
# plt.ylabel('Distance To Car (cm)')
# s
def plot_full_signal():
    plt.plot(range(len(times)), dists)
    plt.xlabel('Time (Month/Day Hour)')
    plt.ylabel('Distance To Car (cm)')
    tick_idxs = np.round(np.linspace(0, len(times) - 1, 15)).astype(int)
    plt.xticks(tick_idxs, [times_fmt[i] for i in tick_idxs])
    plt.title('Full Signal')
    plt.show()


def plot_parked_noise():
    parked_dists = dists[2000:2500]
    plt.plot(times[2000:2500], parked_dists)
    plt.xlabel('Time')
    plt.ylabel('Distance To Car (cm)')
    plt.yticks([49, 50, 51])
    plt.title('Parked Car - Noise')
    plt.show()


def plot_exit():
    parked_dists = dists[1360:1400]
    plt.plot(range(len(times[1360:1400])), parked_dists)
    tick_idxs = np.round(np.linspace(0, len(parked_dists) - 1, 5)).astype(int)
    plt.xticks(tick_idxs, [times_fmt_min[i] for i in tick_idxs])
    plt.xlabel('Time')
    plt.ylabel('Distance To Car (cm)')
    plt.title('Car Entering and Exiting Spot')
    plt.show()

def plot_internet_outage():
    outage_dists = dists[35:44]
    plt.scatter(times[35:44], outage_dists)
    plt.xlabel('Time')
    plt.ylabel('Distance To Car (cm)')
    plt.title('Internet Outage')
    plt.show()


def to_csv(dists, times):
    df = pd.DataFrame({
        'timestamp': times,
        'distance': dists
    })
    df.to_csv('data.csv')


plot_full_signal()
# plot_parked_noise()
# plot_exit()
# plot_internet_outage()

# to_csv(dists, times)
