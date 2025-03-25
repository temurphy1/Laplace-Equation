import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from datetime import datetime
current_datetime = datetime.now()
datetime_string = "Month"+ str(current_datetime.month) +"_Day"+ str(current_datetime.day) +"_Hour"+ str(current_datetime.hour) +"_Minute"+ str(current_datetime.minute) +"_Second"+ str(current_datetime.second)

# Numerical integration function using the trapezoidal rule with num_traps
def numerical_integration(func, a, b, num_traps=50):
    """
    Numerically integrates a function func from a to b using the trapezoidal rule
    with the specified number of trapezoids.
    
    Parameters:
        func: The function to integrate (should take a single variable x/theta as input).
        a: The lower limit of integration.
        b: The upper limit of integration.
        num_traps: The number of trapezoids to use for the numerical integration.
        
    Returns:
        Approximation of the integral.
    """
    # Calculate the width of each trapezoid
    width = (b - a) / num_traps
    # Generate the x values for the trapezoids
    x = np.linspace(a, b, num_traps + 1)
    # Compute the function values at each x/theta
    y = func(x)
    # Apply the trapezoidal rule
    integral = np.sum((y[:-1] + y[1:])) * width / 2
    #^^ Is sum([yo+y1, y1+y2, y2+y3, y(n-1)+yn]) * width/2
    return integral

#a is the radius of the circle
a = 1.000

#Boundary conditions here:
#u(a,theta)=f(theta) for -pi<theta<pi, a = radius of circle
f = lambda x: 3*np.sin(x)**4 # Define the function f(x) = sin^4(x)


# Define the function u(r, theta)
def u_polar(r, theta, num_terms=100, show_terms=False):

    result = 0  # Initialize the result

    Ao = (1/(2*np.pi))*numerical_integration(f, -np.pi, np.pi)  # Coefficient for the first term (constant term)
    result += Ao

    for n in range(1, num_terms + 1):  # Loop over the first 10 terms

        f_times_sin = lambda x: f(x) * np.sin(n * x)  # Define the function for numerical integration
        f_times_cos = lambda x: f(x) * np.cos(n * x)  # Define the function for numerical integration

        An = ((a**-n)/np.pi) * numerical_integration(f_times_cos, -1*np.pi, np.pi, num_traps=300)  # Compute Bn using numerical integration
        Bn = ((a**-n)/np.pi) * numerical_integration(f_times_sin, -1*np.pi, np.pi, num_traps=300)  # Compute Bn using numerical integration
        
        result += (r**n) * (An * np.cos(n * theta) + Bn * np.sin(n * theta))  # Add the term to the result

        if show_terms: # Print the terms if show_terms is True, primarily used for debugging
            print("for n=",n," An=", An, " Bn=",Bn)
        

    return result


# Generate r and theta
r = np.linspace(0, a, 200)  # Radial range [0, a]
theta = np.linspace(0, 2 * np.pi, 200)  # Angular range [0, 2π]
r, theta = np.meshgrid(r, theta)  # Create 2D grid for r and theta

# Compute the function values
z = u_polar(r, theta, num_terms=500, show_terms=False)

# Convert to Cartesian coordinates for plotting
x = r * np.cos(theta)
y = r * np.sin(theta)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x, y, z, cmap='viridis') 
#edgecolor='none' removes the grid lines on the surface

# Set labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Set title
ax.set_title('3D Plot of u(r, theta) for HW7P3')

# Set axis limits to include the origin
ax.set_xlim([-1*a, a])  # Ensure x-axis includes 0
ax.set_ylim([-1*a, a])  # Ensure y-axis includes 0
ax.set_zlim([0, 5])  # Ensure z-axis includes 0

# Set equal aspect ratio for the axes
ax.set_box_aspect([1, 1, 1])  # Equal scaling for x, y, z axes


elevation=30 #elevation, in degrees
azimuth=45 #azimuth, in degrees
ax.view_init(elev=elevation, azim=azimuth)  # Example: 30 degrees elevation, 45 degrees azimuth

# Save the plot to a file instead of displaying it
file_name = f"{datetime_string}"+'_3d_plot_'+f"azimuth{azimuth}"+f"_elevation{elevation}"
file_name_png = file_name+'.png'

plt.savefig(file_name)
print(f"Plot saved as {file_name_png}")

