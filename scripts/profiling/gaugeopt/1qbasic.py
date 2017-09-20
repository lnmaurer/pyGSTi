#!/usr/bin/env python3
from pygsti.construction import std1Q_XYI
from pygsti.algorithms   import gaugeopt_to_target
from pygsti.tools        import timed_block

def main():
    gs_target  = std1Q_XYI.gs_target
    gs_datagen = gs_target.depolarize(gate_noise=0.1, spam_noise=0.001).rotate(0.1)
    with timed_block('Basic gauge opt:'):
        gs_gaugeopt = gaugeopt_to_target(
            gs_datagen, gs_target, tol=1e-7,
            #method="auto",
            method="L-BFGS-B",
            itemWeights={'spam' : 1.0, 'gates':1.0},
            spamMetric='frobenius',
            gatesMetric='frobenius', checkJac=True,
            cptp_penalty_factor=1.0,
            spam_penalty_factor=1.0,
            verbosity=3)
        print("Final Diff = ", gs_gaugeopt.frobeniusdist(gs_target, None, 1.0, 1.0))
        print(gs_gaugeopt.strdiff(gs_target))

if __name__ == '__main__':
    main()
