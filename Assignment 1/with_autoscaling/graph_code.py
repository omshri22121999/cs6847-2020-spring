import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("summary_hits.csv")

# plt.plot(data.elapsed)
# plt.show()

resp_time = data.elapsed
plt.plot(data.elapsed.expanding().mean())
plt.xlabel("Request")
plt.ylabel("Response Time of The Request")
plt.title("Variation of Response Time")
plt.savefig("response_time.png")
plt.show()
th = pd.read_csv("throughput.csv")
plt.xlabel("Time Elapsed (in s)")
plt.ylabel("Throughput (No. of hits per s")
plt.plot(th["Time_Elapsed"], th["Throughput"], "bo")
plt.savefig("throughput.png")
plt.show()

