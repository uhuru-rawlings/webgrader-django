from django.shortcuts import render
import requests, json
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from ssl import SSLError
from requests.exceptions import Timeout


def check_website_view(request):
    website_speed = ""
    responsiveness = ""
    seo_score = ""
    error = ""
    url = ""
    if request.method == 'POST':
        # Get the URL from the submitted form data
        url = request.POST.get('website_url', '')
    
        API_KEY="AIzaSyCQBP6nmcrgxTou0uax1SYzQRQnDwC2kF0"
        api_endpoint = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={API_KEY}&category=performance&category=accessibility&category=seo&category=pwa&category=best-practices"

        # api_params = {
        #     'url': url,
        #     'key': API_KEY,
        #     'category':'performance',
        #     'category':'accessibility',
        #     'category':'seo',
        #     'category':'pwa',
        #     'category':'best-practices'
        # }

        # Send the API request
        response = requests.get(api_endpoint)

        # Parse the response JSON and extract the relevant data
        response_json = response.json()

        performance = float(response_json['lighthouseResult']['categories']['performance']['score']) * 100
        accessibility = float(response_json['lighthouseResult']['categories']['accessibility']['score']) * 100
        bestpractices = float(response_json['lighthouseResult']['categories']['best-practices']['score']) * 100
        seo = float(response_json['lighthouseResult']['categories']['seo']['score']) * 100
        pwa = float(response_json['lighthouseResult']['categories']['pwa']['score']) * 100
        
        fullPageScreenshot = response_json['lighthouseResult']['fullPageScreenshot']['screenshot']['data']
        context = {
            "title": "RK Digital | Website Status Checker",
            "url": url,
            'performance': int(performance),
            'accessibility': int(accessibility),
            'bestpractices': int(bestpractices),
            'seo': int(seo),
            'pwa': int(pwa),
            'fullPageScreenshot': fullPageScreenshot,
            'success': "#28A745",
            'warning': "#FFC517",
            'danger': "#DF4857"
        }
        return render(request, "results.html", context)


        
    context = {'url': url,
               'website_speed': website_speed,
               'responsiveness': responsiveness,
               'seo_score': seo_score,
               'error': error,
               'title': "RK Digital | Website Status Checker",
                # special    
               }

    return render(request, 'index.html', context)



# def get_page_speed(request):
#     speed_score = ""
#     responsive_score = ""
#     seo_score = ""
#     render_time = ""
#     error = ""
#     url = ""
#     if request.method == "POST":
#         # Replace with your own API key
#         api_key = "AIzaSyBjHe0ZOucTsqHPptsFTIZYbBLMKZ9ApHA"
        
#         url = request.POST['website_url']
#         # Set up the API endpoint
#         lighthouse = Lighthouse(url)
#         report = lighthouse.generate_report()
        
#         speed_score = report["categories"]["performance"]["score"] * 100
#         responsive_score = report["categories"]["accessibility"]["score"] * 100
#         seo_score = report["categories"]["seo"]["score"] * 100
#     else:
#         error = "Oops! something went wrong"
        
#     context = {
#         "website_speed": speed_score,
#         "responsiveness": responsive_score,
#         "seo_score": seo_score,
#         'error': error,
#         "url": url
#     }
#     return render(request, "index.html", context)
        
# import requests

# def get_page_speed(request):
#     speed_score = ""
#     responsive_score = ""
#     seo_score = ""
#     error = ""
#     url = ""
    
#     if request.method == "POST":
#         url = request.method == "POST"
#         endpoint = "https://www.webpagetest.org/runtest.php"
#         api_key = "YOUR_API_KEY"

#         params = {
#             "url": url,
#             "f": "json",
#             "k": api_key,
#             "runs": 1,
#             "mobile": 1,
#             "location": "Dulles:Chrome"
#         }

#         try:
#             response = requests.get(endpoint, params=params)
#             data = response.json()

#             # Extract relevant data from the API response
#             speed_score = data["data"]["average"]["firstView"]["score_gzip"]
#             responsive_score = data["data"]["average"]["firstView"]["score_usecdn"]
#             seo_score = data["data"]["average"]["firstView"]["score_cdn"]

#         except requests.exceptions.RequestException as e:
#             print("An error occurred while fetching data from the WebPageTest API:", e)
#             return None
        
#     context = {
#         "website_speed": speed_score,
#         "responsiveness": responsive_score,
#         "seo_score": seo_score,
#         'error': error,
#         "url": url
#     }
