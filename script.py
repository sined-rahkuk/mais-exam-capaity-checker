from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from win10toast import ToastNotifier
from time import sleep
from random import randint
from winsound import Beep

WEB_DRIVER_PATH = r"D:\Google Drive\pythonCrawler\chromedriver.exe"
chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(WEB_DRIVER_PATH, chrome_options=chrome_options)

MAIS_URL = "https://student.tuke.sk/student/home.mais?login=true"


def auth_and_get():
  driver.get(MAIS_URL)
  driver.execute_script("document.getElementsByClassName('button')[0].click()")
  driver.execute_script('document.getElementsByTagName("input")[1].value = "ЛОГИН";document.getElementsByTagName("input")[2].value = "ПАРОЛЬ";document.getElementsByClassName("button")[1].click()')
  driver.get("https://student.tuke.sk/student/termin/prihlasovanie.mais?smi=3.2")
  driver.execute_script("document.getElementById('filterPredmetId').selectedIndex = '2';onPredmetChange()")
  sleep(0.5)
  
def get_cislo():
  cislo = driver.execute_script('return document.getElementsByClassName("basic_grid")[0].getElementsByTagName("tr")[1].getElementsByTagName("td")[4].innerHTML')
  cislo = cislo.split("/")[1]
  return cislo

def main():
  auth_and_get()
  cislo = get_cislo()


  while cislo == "70":
    sleep(randint(5, 10))
    driver.refresh()
    print(cislo)
    cislo = get_cislo()

  if(cislo != "70"):
    while True:
      nt = ToastNotifier()
      nt.show_toast("SKUSKA", "PRIHLAS SA HNED!")
      Beep(1000, 1000)
      sleep(2)
  


if __name__ == "__main__":
  main()







