# Introduction

This repository contains the work I carried during my research internship on CaloINN, a generative model designed to simulate calorimeter showers in high-energy physics. It was introduced in the CaloChallenge https://arxiv.org/pdf/2410.21611 and is described in details here:  https://arxiv.org/pdf/2312.09290 . It’s implementation and installation instructions are available here : https://github.com/heidelberg-hepml/CaloINN.
The goal of my work was to explore and improve the evaluation strategy of the model, and better understand its generalization abilities.

## Modified classifier

I trained a new binary classifier to distinguish between Geant4 and CaloINN-generated showers. 
It achieved similar performance with better balance between training and validation performances. 

## Interpolation ability

Link to the slides : https://docs.google.com/presentation/d/1jx-MW-ouCg9Mh47UmSEipwo6ShP4LfuDstoIUW8cMYE/edit?usp=sharing

I studied how well CaloINN interpolates to incident energies it has not seen during training.
By removing all events from one specific energy from the training set and test the model on these events. (Slide 20-21)

I first retrained CaloINN on a dataset without any 16 GeV events. (Slides 22, 23).
Then I did the same thing without any 512 2MeV events (Slides 24, 25, 26).
Finally, without any 2 TeV events (Slides 27, 28).
Also I did two supplementary checks (Slide 29) :
-	Retrain the classifier on a dataset where the number of 16 GeV events is reduced to match the number of 2 TeV events.
-	Retrain the classifier on the whole dataset and test it only for 2 TeV events
