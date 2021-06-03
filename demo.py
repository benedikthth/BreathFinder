from numpy.lib import index_tricks
import pyedflib.edfreader as Reader
import BreathFinder as BF
import matplotlib.pyplot as plt
import dill

### Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, 
### P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, 
### PhysioToolkit, and PhysioNet:  Components of a new research 
### resource for complex physiologic signals. Circulation [Online].
### 101 (23), pp. e215–e220.
###
### Demo signal segment is sourced from https://physionet.org/content/shhpsgdb/1.0.0/ 
###     more specifically 0000.edf.







# load the signal segment from the demo file
pickle = dill.load(open('signal_segment.dill', 'rb'))
# -||-
signal = pickle['signal']
fs = pickle['fs']

# Estimate the run time.
rte = BF.estimate_run_time(signal, fs)
print(f'Breathfinder will take approximately {rte/60} minutes to process this {len(signal)/fs/60} minute long signal')
# Perform the breath finding procedure
breaths = BF.find_breaths(signal, fs)
# Define a list of alternating colors for the breath visualisation
colors = ['red', 'blue', 'green', 'blue']
# Create a plot
fig, ax = plt.subplots()
# Plot the signal, with the x axis in seconds.
ax.plot([x/fs for x in range(len(signal))], signal)
# For each breath in the result
for i ,b in enumerate(breaths):
    # Draw a span on the signal representing the detected span
    ax.axvspan(b[0], b[0]+b[1], facecolor=colors[i%len(colors)], alpha=0.5)
# show the signal, and the detected breaths.
plt.show()
