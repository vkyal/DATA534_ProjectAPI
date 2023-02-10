# DATA534_ProjectAPI

[![Build Status][build-shield]][build-url]
[![Release][release-shield]][release-url]
[![Forks][forks-shield]][forks-url]
[![Downloads][downloads-shield]][downloads-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]


<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://github.com/vkyal/DATA534_ProjectAPI/actions/workflows/build.yml/badge.svg
[release-shield]: https://img.shields.io/github/v/release/vkyal/DATA534_ProjectAPI.svg?style=flat-square
[release-url]: https://github.com/vkyal/DATA534_ProjectAPI/releases
[forks-shield]: https://img.shields.io/github/forks/vkyal/DATA534_ProjectAPI.svg?style=flat-square
[forks-url]: https://github.com/vkyal/DATA534_ProjectAPI/network/members
[downloads-shield]: https://img.shields.io/github/downloads/vkyal/DATA534_ProjectAPI/total.svg?style=flat-square
[downloads-url]: https://github.com/vkyal/DATA534_ProjectAPI
[stars-shield]: https://img.shields.io/github/stars/vkyal/DATA534_ProjectAPI.svg?style=flat-square
[stars-url]: https://github.com/vkyal/DATA534_ProjectAPI/stargazers
[license-shield]: https://img.shields.io/github/license/vkyal/DATA534_ProjectAPI.svg?style=flat-square
[license-url]: https://github.com/vkyal/DATA534_ProjectAPI/blob/master/LICENSE
[build-url]: https://github.com/vkyal/DATA534_ProjectAPI/actions/workflows/build.yml

This python-package WeatherForcastAPI contains 6 wrapper functions to get Weather Forcast of any city. These functions process API [http://www.7timer.info/doc.php?lang=en#web_interface](http://www.7timer.info/doc.php?lang=en#web_interface) to get data. Some functions provide daily data and some of them provide summary of data for all multiple days. This package contains 06 internal functions to request API which are not available to user. The list of 6 functions available to user is given below:

### Package - WeatherForcastAPI

1. coordinates(city = 'Kelowna')
2. documentation_cloud_cover(dataframe)
3. documentation_ppt_amt(dataframe)
4. documentation_wind_spd_10m(dataframe)
5. documentation_weather_type(dataframe)
6. wiki_timezone(city = 'Kelowna')

### To install the package 

1. Install the package by typing: `pip install Wrapper-Weather-Module-V3`
2. Add package to the python instance by typing: `from Wrapper_Weather_Module_V3 import main as m`
3. Add the city name for which you want to see the results. For example, Vancouver, Toronto etc.
4. Run the following code to view the table of the forecast:-
```
city_forecast_table = m.main()
city_forecast_table
```
5. Run the following code to view the visualization chart of the forecast:-
```
city_forecast_chart = m.visual()
city_forecast_chart
```

##### Notes: 

* This package comes with a dataset on realtime based on the used provided location using the api listed above. 
* For details please find in our tutorial document.
* Data Resources: https://www.7timer.info/
