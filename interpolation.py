import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import csv

time = []
altitude = []
velocity = []
acceleration = []

# Leitura dos dados contido no arquivo .csv
with open('STS-121_2.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=' ')
    for row in spamreader:
        time.append(float(row['time']))
        altitude.append(float(row['altitude']))
        velocity.append(float(row['velocity']))
        acceleration.append(float(row['acceleration']))
 
print(time)
print(altitude)
print(velocity)
print(acceleration)

# Plotagem do conjunto discreto de dados
# Tempo x Altitude, Tempo x Velocidade, Tempo x Aceleracao
for i in range(len(time)):
    plt.plot(time[i], altitude[i], "ro")
    plt.plot(time[i], velocity[i], "go")
    plt.plot(time[i], acceleration[i], "bo")

# Dominio para a funcao interpoladora
interpolator_domain = np.arange(0, 520.0)

# Criacao da funcao Interpoladora Linear e seu conjunto imagem a partir do dominio
# Time x Altitude
altitude_interpolator = sp.interpolate.interp1d(time, altitude)
altitude_interpolator_image = altitude_interpolator.__call__(interpolator_domain)

# Time x Velocity
velocity_interpolator = sp.interpolate.interp1d(time, velocity)
velocity_interpolator_image = velocity_interpolator.__call__(interpolator_domain)

# Time x Acceleration
acceleration_interpolator = sp.interpolate.interp1d(time, acceleration)
acceleration_interpolator_image = acceleration_interpolator.__call__(interpolator_domain)

# Criacao da funcao Interpoladora Cubica e seu conjunto imagem a partir do dominio
# Time x Altitude
#altitude_interpolator = sp.interpolate.interp1d(time, altitude, kind='cubic')
#altitude_interpolator_image = altitude_interpolator.__call__(interpolator_domain)

# Time x Velocity
#velocity_interpolator = sp.interpolate.interp1d(time, velocity, kind='cubic')
#velocity_interpolator_image = velocity_interpolator.__call__(interpolator_domain)

# Time x Acceleration
#acceleration_interpolator = sp.interpolate.interp1d(time, acceleration, kind='cubic')
#acceleration_interpolator_image = acceleration_interpolator.__call__(interpolator_domain)

# Criacao da funcao Interpoladora Invariavel e seu conjunto imagem a partir do dominio
# Time x Altitude
#altitude_interpolator = sp.interpolate.InterpolatedUnivariateSpline(time, altitude)
#altitude_interpolator_image = altitude_interpolator.__call__(interpolator_domain)

# Time x Velocity
#velocity_interpolator = sp.interpolate.InterpolatedUnivariateSpline(time, velocity)
#velocity_interpolator_image = velocity_interpolator.__call__(interpolator_domain)

# Time x Acceleration
#acceleration_interpolator = sp.interpolate.InterpolatedUnivariateSpline(time, acceleration)
#acceleration_interpolator_image = acceleration_interpolator.__call__(interpolator_domain)

# Criacao da funcao Interpoladora Baricentrica e seu conjunto imagem a partir do dominio
# Time x Altitude
#altitude_interpolator = sp.interpolate.BarycentricInterpolator(time, altitude)
#altitude_interpolator_image = altitude_interpolator.__call__(interpolator_domain)

# Time x Velocity
#velocity_interpolator = sp.interpolate.BarycentricInterpolator(time, velocity)
#velocity_interpolator_image = velocity_interpolator.__call__(interpolator_domain)

# Time x Acceleration
#acceleration_interpolator = sp.interpolate.BarycentricInterpolator(time, acceleration)
#acceleration_interpolator_image = acceleration_interpolator.__call__(interpolator_domain)

# Representacao grafica da funcao interpoladora escolhida
plt.plot(interpolator_domain, altitude_interpolator_image, "r", label="Altitude Interpolator")
plt.plot(interpolator_domain, velocity_interpolator_image, "g", label="Velocity Interpolator")
plt.plot(interpolator_domain, acceleration_interpolator_image, "b", label="Acceleration Interpolator")

plt.grid()
plt.legend()
plt.show()

