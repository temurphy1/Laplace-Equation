# Laplace-Equation
Application of the Laplace Equation to graph the temperature distribution of a circular plate in steady state heat transfer

For a circle with radius a, the general solution to the Laplace Equation is:
u(r, θ) = A₀ + ∑ₙ₌₁ⁿᵢₙₓ rⁿ (Aₙ cos(nθ) + Bₙ sin(nθ))

Where Aₙ and Bₙ are dependent on the boundary condtions. In this case, a Dirichlet Boundary Condition is applied, meaning that the edge of the plate is held as a function of θ. This repository deals with computing the function u(r, θ) and graphing it on the interval 0<r<a
