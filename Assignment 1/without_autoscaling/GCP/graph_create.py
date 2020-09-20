import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = [1, 10, 100, 500, 1000, 2000, 5000]
y = []
for i in x:
    f = pd.read_csv("rate_" + str(i) + ".csv")
    g = f[f.responseCode == "200"]
    h = f[f.responseCode == 200]
    m = pd.concat([g, h])
    y.append(m["elapsed"].mean())

plt.plot(x, y)
plt.xlabel("Requests Per Second")
plt.ylabel("Average Response Time")
plt.title("RPS vs RT")
plt.savefig("plot.png")
# plt.show()

with open("Output.csv", "w") as f:
    f.write("Requests Per Second,Response Time\n")
    for i, j in zip(x, y):
        f.write(str(i) + "," + str(j) + "\n")
