import unittest
from functions import coordinates, documentation_cloud_cover, documentation_ppt_amt, documentation_weather_type, documentation_wind_spd_10m, wiki_timezone
import pandas as pd
#from unidecode import unidecode
df = pd.read_excel('convertcsv.xlsx')

class TestFunctions(unittest.TestCase):
    
    def setUp(self):
        print('Set up of coordinates function initiating')
        self.cord_1 = coordinates('Delhi')
        self.cord_2 = coordinates('Kelowna')
        self.cord_3 = coordinates('Vancouver')
        self.cord_4 = coordinates('Kolkaa')
        self.cc = documentation_cloud_cover(df)
        self.ppt_amt = documentation_ppt_amt(df)
        self.wind_spd = documentation_wind_spd_10m(df)
        self.weather = documentation_weather_type(df)
        self.city_1 = wiki_timezone('Delhi')
        self.city_2 = wiki_timezone('Kelowna')
        self.city_3 = wiki_timezone('Vancouver')
        self.city_4 = wiki_timezone('Kolkata')
 

    def test_coordinates(self):       
        self.assertEqual(self.cord_1, ['28.61000', ' 77.23000'])
        self.assertEqual(self.cord_2, ['49.88806', ' -119.49556'])
        self.assertEqual(self.cord_3, ['49.26111', ' -123.11389'])
        self.assertEqual(self.cord_4, "City doesn't exist!")  
           
    def test_documentation_cloud_cover(self):       
        self.assertEqual(self.cc.iloc[1,10], '94%-100%')
        self.assertNotEqual(self.cc.iloc[2,10], '54%-100%')
        self.assertEqual(self.cc.iloc[3,10], '94%-100%')
        self.assertNotEqual(self.cc.iloc[4,10], '84%-94%')
        
    def test_documentation_ppt_amt(self):
        self.assertEqual(self.ppt_amt.iloc[1,10], '0-0.25mm/hr')
        self.assertNotEqual(self.ppt_amt.iloc[2,10], '54%-100%')
        self.assertEqual(self.ppt_amt.iloc[3,10], '0-0.25mm/hr')
        self.assertIsNotNone(self.ppt_amt.iloc[4,10])
        
    def test_documentation_wind_spd_10m(self):
        self.assertEqual(self.wind_spd.iloc[1,10], '0.3-3.4m/s (light)')
        self.assertNotEqual(self.wind_spd.iloc[2,10], '54%-100%')
        self.assertEqual(self.wind_spd.iloc[3,10], '0.3-3.4m/s (light)')
        self.assertIsNotNone(self.wind_spd.iloc[4,10])
        
    def test_documentation_weather_type(self):
        self.assertEqual(self.weather.iloc[1,10], 'Total cloud cover over over 80%')
        self.assertNotEqual(self.weather.iloc[2,10], '54%-100%')
        self.assertEqual(self.weather.iloc[23,10], 'Precipitation rate less than 4mm/hr')
        self.assertIsNotNone(self.weather.iloc[4,10])
    
    def test_wiki_timezone(self):
        self.assertEqual(self.city_1, 6)
        self.assertNotEqual(self.city_2, '54%-100%')
        self.assertEqual(self.city_3, -8)
        self.assertIsNotNone(self.city_4)
    

    def tearDown(self):
        print('Testing of documentation_cloud_cover module completed.')
 
unittest.main(argv=[''], verbosity=2, exit=False)
