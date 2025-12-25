import requests


API_KEY = "40aa0d4e83e6496a8dc50352251712"


class Weather:
    def get_weather(self):
        try:
           
            city = input("Enter the city name: ")

          
            url = (
                f"http://api.weatherapi.com/v1/current.json"
                f"?key={API_KEY}&q={city}&aqi=no"
            )

      
            response = requests.get(url)

         
            response.raise_for_status()

          
            return response.json()

        except requests.exceptions.HTTPError:
            print("City not found or API key is invalid.")
        except requests.exceptions.ConnectionError:
            print("Internet connection problem.")
        except Exception as e:
            print("Some error occurred:", e)

        return None

    def display_weather(self, data):

        if data is None:
            return

     
        print("\nWeather Report")
        print("--------------------------")
        print(f"City        : {data['location']['name']}")
        print(f"Temperature : {data['current']['temp_c']} °C")
        print(f"Humidity    : {data['current']['humidity']} %")
        print(f"Condition   : {data['current']['condition']['text']}")
        print("--------------------------")


weather = Weather()
result = weather.get_weather()
weather.display_weather(result)
