# Customizing graphs with matplotlib in python with IDLE
# chapter 02 pg-no.41 -- math with python
# programmer - Atharva Puranik

from pylab import plot, show, title, xlabel, ylabel, legend

nyc_temperature_list_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temperature_list_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temperature_list_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]

months_list = range(1, 13)

plot(months_list, nyc_temperature_list_2000, months_list, nyc_temperature_list_2006, months_list, nyc_temperature_list_2012, marker = 'o')

title('Average monthly temperature in NYC')
xlabel('Month')
ylabel('Temperature')
legend([2000, 2006, 2012])

show()
