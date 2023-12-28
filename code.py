import wifi
import time
import socketpool
import adafruit_requests
import ssl

# Replace with your Wi-Fi network credentials
SSID = ""
PASSWORD = ""
quotes_url = "https://www.adafruit.com/api/quotes.php"

try:
    print("Connecting to Wi-Fi...")
    wifi.radio.connect(SSID, PASSWORD)
    print("Connected to", SSID)

    # Print the IP address
    print("IP address:", wifi.radio.ipv4_address)
    
    pool = socketpool.SocketPool(wifi.radio)
    requests = adafruit_requests.Session(pool, ssl.create_default_context())
    #  pings adafruit quotes
    print("Fetching text from %s" % quotes_url)
    #  gets the quote from adafruit quotes
    response = requests.get(quotes_url)
    print("-" * 40)
    #  prints the response to the REPL
    print("Text Response: ", response.text)
    print("-" * 40)
    response.close()

except Exception as e:
    print("Error connecting to Wi-Fi:", e)
    time.sleep(10)  # Wait 10 seconds before retrying
    microcontroller.reset()  # Reset the microcontroller
    

    

