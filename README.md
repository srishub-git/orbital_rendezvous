# Autonomous Orbital Rendezvous via MPC

A Python implementation of Model Predictive Control (MPC) for autonomous 
spacecraft rendezvous and docking.

## Overview
This project implements autonomous orbital rendezvous guidance using Model 
Predictive Control. The chaser spacecraft uses CW (Clohessy-Wiltshire) 
relative orbital dynamics and solves a constrained optimization problem at 
each timestep to compute optimal thrust commands.

## Technical Stack
- Python
- NumPy / SciPy
- CVXPY (convex optimization)
- Matplotlib

## Project Structure
- dynamics/ — CW relative orbital dynamics model
- simulation/ — trajectory propagator
- tests/ — unit tests

## Status
Week 1 — Dynamics model in progress
