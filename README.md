# Introduction

This repository contains the work I carried during my research internship on CaloINN, a generative model designed to simulate calorimeter showers in high-energy physics.

It was introduced in the CaloChallenge https://arxiv.org/pdf/2410.21611 and is described in details here:  https://arxiv.org/pdf/2312.09290.

It’s implementation and installation instructions are available here : https://github.com/heidelberg-hepml/CaloINN.

The goal of my work was to explore and improve the evaluation strategy of the model, and better understand its generalization abilities.

## First task : Modified classifier

I trained a new binary classifier to distinguish between Geant4 and CaloINN-generated showers. 

The default one was trainded to work accross all the dataset even the most complex ones and I was only working with the simplest one. So I created one suited for this dataset and it achieved similar performance with better balance between training and validation performances than the default one.

## Second task : Interpolation ability

Link to the slides : https://docs.google.com/presentation/d/1jx-MW-ouCg9Mh47UmSEipwo6ShP4LfuDstoIUW8cMYE/edit?usp=sharing

Since the energies in the Callochallenge's datatsets are discrete following powers of 2, I studied how well CaloINN interpolates to incident energies it has not seen during training because in practice we might want to generate showers at in-between energies. To do this I removed all events from one specific energy from the training set and test the model on these events. (Slide 20-21)

I considered 3 different scenarios : a low, a medium and a high energy since the complexity of showers varies a lot accross the energy range.
For the medium energy, 16 GeV, I had good interpolation from the model. (Slides 22, 23).
Then for 512 MeV events, I had good interpolation ability from the model but its performance remains limited due to the high-level of detail of the low-energy showers (Slides 24, 25, 26). For 2 TeV events, I saw that high-energy events are easier to reconstruct but can be tricky due to the small number of events (Slides 27, 28).
To make sure that the low A.U.C score obtained for 2 TeV was due to the poor learning from the classifier and not to a particularly good performance of CaloINN for this specific energy, I did two supplementary checks (Slide 29) :
-	Retrain the classifier on a dataset where the number of 16 GeV events is reduced to match the number of 2 TeV events. 
-	Retrain the classifier on the whole dataset and test it only for 2 TeV events.
These confirms the initial idea that the classifier did not have enough learning data to learn anything meaningful.
