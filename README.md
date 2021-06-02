![screenshot](https://user-images.githubusercontent.com/7534594/120475771-4e89d300-c399-11eb-874a-619ffcb5b925.png)

---
A python3 module implemented an algorithm designed to locate individual breaths within a PSG using the thoracic RIP signal.
The algorithm was validated on a thoracic RIP signal that was sampled with 25hz sampling frequency. Currently, the algorithm is un-validated on any other sampling frequency.

The result of the evaluation was that this algorithm found around 94\$ of breaths correctly, with only 5\% of predictions being false positives. This algorithm was then
---
## Installation:
```console
bla@bla:~$ git clone git@github.com:benedikthth/BreathFinder.git

bla@bla:~$ cd BreathFinder

bla@bla:~$ pip install -e .
```
Currently, the package is in development, and is not released on PiPy.
The installation was tested on an ubuntu 20 system.


## Usage:

The following use cases assume that you have loaded a thoracic RIP signal in the form of a python list into the variable `signal`, and that you stored the sampling frequency of the signal in the variable `sampling_frequency`. 

```python
import BreathFinder as BF
breath_locations = BF.find_breaths(signal, sampling_freuency)
# output is a list of breaths in the format [start, duration]
# where start is the timestamp of the breath-start in seconds
# since the signal start, and duration is the
# duration of the breath in seconds.
# breath_locations = [[1, 2], ...]
```

The BreathFinder run time can be estimated using the `estimate_run_time` function.
```python
import BreathFinder as BF
et = BF.estimate_run_time(signal, sampling_frequency)
print(f'The algorithm is estimated to process this recording in {et/60} minutes')
```
This is just an estimation however, the algorithm may take more, or less time to locate the breaths within the signal.


---
## Contact information
If there are any issues with the installation, running the algorithm, or general questions, please send me a message at [b@spock.is](mailto:b@spock.is?subject=Issue%20With%20BreathFinder)