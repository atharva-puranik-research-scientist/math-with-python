# Program to demonstrate average annual temperature with  matplotlib in python with IDLE
# chapter 02 pg-no.37 -- math with python
# programmer - Atharva Puranik

from pylab import plot, show

nyc_temperature_list = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]

years_list = range(2000, 2013)

plot(years_list, nyc_temperature_list, marker = 'o')
show()
