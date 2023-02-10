# DATA534_ProjectAPI

### Package - WeatherForcastAPI

This python-package WeatherForcastAPI contains 6 wrapper functions to get Weather Forcast of any city. These functions process API [http://www.7timer.info/doc.php?lang=en#web_interface](http://www.7timer.info/doc.php?lang=en#web_interface) to get data. Some functions provide daily data and some of them provide summary of data for all multiple days. This package contains 06 internal functions to request API which are not available to user. The list of 6 functions available to user is given below:

1. coordinates(city = 'Kelowna')
2. documentation_cloud_cover(dataframe)
3. documentation_ppt_amt(dataframe)
4. documentation_wind_spd_10m(dataframe)
5. documentation_weather_type(dataframe)
6. wiki_timezone(city = 'Kelowna')

### To install the package 

1. Install the package by typing: pip install Wrapper-Weather-Module-V1
2. Add package to the python instance by typing: import Wrapper-Module as wm

##### Notes: 

* This package comes with a dataset on realtime based on the used provided location using the api listed above. 
* For details please find in our tutorial document.
* Data Resources: https://www.7timer.info/

Footer
