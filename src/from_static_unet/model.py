"""
The model for from-static-unet.

a small U-Net with a timestep embedding, trained as DDPM (1000 noise steps, cosine
schedule), with DDIM sampling for speed.

forward() accepts return_cache=True and returns a dict of internal activations, and a
patch argument (or forward hooks) overwrites a named activation for interventions.
"""

# TODO: implement. See README.md for the plan.
