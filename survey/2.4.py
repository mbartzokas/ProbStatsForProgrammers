import Pmf
import matplotlib.pyplot as pyplot

def RemainingLifetimes(pmfLifetimes, age):
    pmf = pmfLifetimes.Copy("Remaining lifetimes")
    for lifetime in pmf.Values():
       freq = pmf.GetDict().pop(lifetime)
       remainingLifetime = lifetime - age
       if remainingLifetime > 0:
           pmf.GetDict()[remainingLifetime] = freq
    return pmf

histLifetimes = Pmf.MakeHistFromDict({70: '10', 65: '8', 67:'9', 55: '5', 35: '1', 80: '2'}, "Lifetime frequencies")
vals, freqs = histLifetimes.Render()
pyplot.bar(vals, freqs)
pyplot.show()

# remainingLifetimes = RemainingLifetimes(histLifetimes, 47)
# vals, freqs = remainingLifetimes.Render()
# pyplot.bar(vals, freqs)
# pyplot.show()
