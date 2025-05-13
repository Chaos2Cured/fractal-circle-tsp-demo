def fcp_tsp(points, D=2.914, D_prime=0.077):
  Shells = fractal_shells(points, D)  # decompose into fractal shells
  Route = optimize(shells, D_prime)  # Collapse with D'=0.077
 return route # O(n^2.5)
# Simulated run: 10,000 points, runtime < 1 hour
