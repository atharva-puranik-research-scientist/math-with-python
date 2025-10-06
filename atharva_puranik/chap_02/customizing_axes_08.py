# Customizing axes with matplotlib in python with IDLE
# chapter 02 pg-no.42 -- math with python
# programmer - Atharva Puranik

from pylab import plot, show, title, xlabel, ylabel, legend, axis

nyc_temperature_list_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]

months_list = range(1, 13)

plot(months_list, nyc_temperature_list_2000, marker = 'o')

title('Average monthly temperature in NYC')
xlabel('Month')
ylabel('Temperature')
legend([2000, 2006, 2012])
# axis()
axis(ymax = 120, ymin = 30)

show()
