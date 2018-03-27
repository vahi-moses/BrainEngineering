import nengo
from nengo.processes import WhiteSignal
import matplotlib.pyplot as plt
from nengo.utils.matplotlib import rasterplot
import json

json_data=open("option.json").read()

data = json.loads(json_data)
print(data)

model = nengo.Network()
with model:
    stim = nengo.Node(WhiteSignal(60, high=5), size_out=1)
    cortex = nengo.Ensemble(n_neurons=int(data["n_neurons"]["cortex"]), dimensions=1, neuron_type=nengo.Izhikevich())
    striatum = nengo.Ensemble(n_neurons=int(data["n_neurons"]["striatum"]), dimensions=1, neuron_type=nengo.Izhikevich())
    GPe = nengo.Ensemble(n_neurons=int(data["n_neurons"]["GPe"]), dimensions=1, neuron_type=nengo.Izhikevich())
    GPi = nengo.Ensemble(n_neurons=int(data["n_neurons"]["GPi"]), dimensions=1, neuron_type=nengo.Izhikevich())
    STN = nengo.Ensemble(n_neurons=int(data["n_neurons"]["STN"]), dimensions=1, neuron_type=nengo.Izhikevich())
    SNr = nengo.Ensemble(n_neurons=int(data["n_neurons"]["SNr"]), dimensions=1, neuron_type=nengo.Izhikevich())
    SNc = nengo.Ensemble(n_neurons=int(data["n_neurons"]["SNc"]), dimensions=1, neuron_type=nengo.Izhikevich())
    Thalamus = nengo.Ensemble(n_neurons=int(data["n_neurons"]["Thalamus"]), dimensions=1, neuron_type=nengo.Izhikevich())
    nengo.Connection(cortex, striatum)
    nengo.Connection(striatum, GPe)
    nengo.Connection(striatum, GPi)
    nengo.Connection(striatum, SNr)
    nengo.Connection(SNc, striatum)
    nengo.Connection(GPe, STN)
    nengo.Connection(STN, GPi)
    nengo.Connection(STN, SNr)
    nengo.Connection(GPi, Thalamus)
    nengo.Connection(SNr, Thalamus)
    nengo.Connection(Thalamus, cortex)
    nengo.Connection(stim, Thalamus)

with model:
    input_tprobe = nengo.Probe(stim)
    striatum_tprobe = nengo.Probe(striatum, synapse=0.01)
    cortex_tprobe = nengo.Probe(cortex, synapse=0.01)
    striatum_probe = nengo.Probe(striatum.neurons)
    cortex_probe = nengo.Probe(cortex.neurons)
    gpe_probe = nengo.Probe(GPe.neurons)
    gpi_probe = nengo.Probe(GPi.neurons)
    stn_probe = nengo.Probe(STN.neurons)
    snr_probe = nengo.Probe(SNr.neurons)
    snc_probe = nengo.Probe(SNc.neurons)
    thalamus_probe = nengo.Probe(Thalamus.neurons)

with nengo.Simulator(model) as sim:
    sim.run(int(data["time"]))


def show_stim():
    plt.plot(sim.trange(), sim.data[input_tprobe], color='k', label="input_probe")
    plt.show()

def show_str():
    rasterplot(sim.trange(), sim.data[striatum_probe])
    plt.show()

def show_cortex():
    rasterplot(sim.trange(), sim.data[cortex_probe])
    plt.show()

def show_gpe():
    rasterplot(sim.trange(), sim.data[gpe_probe])
    plt.show()

def show_gpi():
    rasterplot(sim.trange(), sim.data[gpi_probe])
    plt.show()

def show_stn():
    rasterplot(sim.trange(), sim.data[stn_probe])
    plt.show()

def show_snr():
    rasterplot(sim.trange(), sim.data[snr_probe])
    plt.show()

def show_snc():
    rasterplot(sim.trange(), sim.data[snc_probe])
    plt.show()

def show_thalamus():
    rasterplot(sim.trange(), sim.data[thalamus_probe])
    plt.show()

def show_state_stim_cortex():
    plt.plot(sim.data[input_tprobe], sim.data[cortex_tprobe], color='r')
    plt.show()

def show_state_stim_str():
    plt.plot(sim.data[input_tprobe], sim.data[striatum_tprobe], color='r')
    plt.show()

