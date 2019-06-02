from django.shortcuts import render
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
from home.models import Movie
from detail.models import Detail

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def runChrome(link = ''):
    # set option headless for chrome
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('--headless')

    # link chrome driver
    link_Chrome = BASE_DIR + '/chromedriver'

    # obj webdriver chrome
    driver = webdriver.Chrome(link_Chrome, chrome_options = chrome_option) 
    return driver
def getSoup(driver, link = ''):
    # open link on chromedrive
    driver.get(link)
    # page source obj soup
    soup = BeautifulSoup(driver.page_source, 'lxml')
    return soup
def quitChrome(driver):
    driver.quit()
def saveDetail(driver, link = '', stt=''):
    #get bs4
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'lxml')

    #parent name year video Directors Writers
    divMainTop = soup.find("div", {"id": "main_top"})
    #parent Storyline, CompanyCredits
    divMainBottom = soup.find("div", {"id": "main_bottom"})
    #parent name year
    divTitleWrapper = divMainTop.find("div", class_ = "title_wrapper")
    #parent video poster, video, 
    divSlate = divMainTop.find("div", class_="slate")
    #****************************
    movieDetail = Detail()

    if(divSlate == None):
        movieDetail.linkVideoTrailer = ''
        movieDetail.linkVideoPoster = ''
    else:
        #get link video page
        linkVideoPage = "https://www.imdb.com" + divSlate.find("a")["href"]
        # run chromedrive get link video
        soupVideo = getSoup(driver, linkVideoPage)
        #set linkVideoTrailer
        movieDetail.linkVideoTrailer = soupVideo.find("video" , class_ = "jw-video jw-reset")["src"]
        #set linkVideoPoster
        movieDetail.linkVideoPoster = divSlate.find("img")["src"].strip()

    #set stt
    movieDetail.stt = stt
    #set title
    title_wrapper_text = divTitleWrapper.find("h1").get_text().strip()
    movieDetail.title = title_wrapper_text.split('(')[0].strip()
    movieDetail.year = title_wrapper_text.split('(')[1].split(')')[0].strip()
    #set rating
    movieDetail.rating = ''
    spanRating = soup.find("span", {"itemprop": "ratingValue"})
    if (spanRating):
        movieDetail.rating = spanRating.string.strip()
    #set subText, the loai, ngay phat hanh , leng = 4
    movieDetail.subText = divTitleWrapper.find("div", class_ = "subtext").get_text()
    #set linl_poster
    movieDetail.link_poster = divMainTop.find("div", class_= "poster").find("img")["src"].strip()


    #set Storyline
    movieDetail.Storyline = divMainBottom.find("div", {"id": "titleStoryLine"}).find("div", class_ = "inline canwrap").get_text().strip()
    #save to mysql
    movieDetail.save()

def saveMovies(soup):
    #get driver
    driver = runChrome()
    table_data = soup.find('table', class_='chart full-width')
    #get bs4 obj tbody
    tbody_table_data = table_data.find('tbody')
    #run all tr in tbody
    trList = tbody_table_data.find_all('tr')
    for tr in trList:
        td = tr.find_all('td')

        new_Movie = Movie()
        #set mv_stt
        new_Movie.mv_stt = str(td[1].find('div').get_text())
        new_Movie.mv_stt = new_Movie.mv_stt.split('(', 1)[0].strip()

        #set mv_name
        new_Movie.mv_name = str(td[1].find('a').string)

        #set mv_year
        year = str(td[1].find('span', class_='secondaryInfo').string)
        year = year.strip('(')
        new_Movie.mv_year = year.strip(')')

        #set mv_rating
        new_Movie.mv_rating = str(td[2].get_text()).strip()

        #set mv_link_detail
        new_Movie.mv_link_detail =  str('https://www.imdb.com'+td[1].find('a')['href'])

        #call save detail
        saveDetail(driver, new_Movie.mv_link_detail, new_Movie.mv_stt)

        #set mv_link_poster
        new_Movie.mv_link_poster =  str(td[0].find('img')['src'])

        #save to mysql
        new_Movie.save()
    ###
    quitChrome(driver)
def index(request):
    #get page source
    res = requests.get('https://www.imdb.com/chart/moviemeter')
    soup = BeautifulSoup(res.text, 'lxml')
    #save data to mysql
    if request.method == 'POST':
        if request.POST.get('scraping') == 'Scraping':
            Movie.objects.all().delete()
            Detail.objects.all().delete()
            saveMovies(soup)
        if request.POST.get('delete') == 'Delete':
            Movie.objects.all().delete()
            Detail.objects.all().delete()
    # Movie.objects.all().delete()
    # Detail.objects.all().delete()
    data = {"request": request}
    return render(request, 'pages/tool.html', data)
