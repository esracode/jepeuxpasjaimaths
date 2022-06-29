from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import \
    expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://www.jepeuxpasjaimaths.fr")

parcoursLibre = "/html/body/section[2]/div[1]/button[1]"
cycle3 = "/html/body/section[13]/div[3]/button[1]"
calculDeLaMort = "/html/body/section[14]/div[4]/button[5]"
sansMusique = "/html/body/section[18]/div[2]/div[9]/div[3]/label[1]"
commencer = "/html/body/section[18]/div[3]/button"
calcul = '//*[@id="calculaafficher"]'
timer3min = "/html/body/section[18]/div[2]/div[9]/div[1]/label[3]"

button0 = "/html/body/section[19]/div[1]/div[4]/div[3]/div[6]/div[1]"
button1 = "/html/body/section[19]/div[1]/div[4]/div[3]/div[6]/div[2]"
button2 = "/html/body/section[19]/div[1]/div[4]/div[3]/div[6]/div[3]"
button3 = "/html/body/section[19]/div[1]/div[4]/div[3]/div[6]/div[4]"
button4 = "/html/body/section[19]/div[1]/div[4]/div[3]/div[6]/div[5]"

button5 = "/html/body/section[19]/div[1]/div[4]/div[3]/div[7]/div[1]"
button6 = "/html/body/section[19]/div[1]/div[4]/div[3]/div[7]/div[2]"
button7 = "/html/body/section[19]/div[1]/div[4]/div[3]/div[7]/div[3]"
button8 = "/html/body/section[19]/div[1]/div[4]/div[3]/div[7]/div[4]"
button9 = "/html/body/section[19]/div[1]/div[4]/div[3]/div[7]/div[5]"

chiffresToButtonMap = {"0": button0, "1": button1, "2": button2, "3": button3, "4": button4,
                       "5": button5, "6": button6, "7": button7, "8": button8, "9": button9}

def attendsElementEtClique(driver, xpath, timeout=15):
    element = driver.find_element("xpath", xpath)
    WebDriverWait(driver, timeout).until(
        ExpectedConditions.element_to_be_clickable((By.XPATH, xpath))
    )
    element.click()

attendsElementEtClique(driver, parcoursLibre)
attendsElementEtClique(driver, cycle3)
attendsElementEtClique(driver, calculDeLaMort)
attendsElementEtClique(driver, sansMusique)
attendsElementEtClique(driver, timer3min)
attendsElementEtClique(driver, commencer)

WebDriverWait(driver, 15).until(
    ExpectedConditions.element_to_be_clickable((By.XPATH, calcul))
)

for x in range(90):
    element = driver.find_element("xpath", calcul)
    operation = format(element.text).split("=")[0]
    operation = operation.replace('×', '*').replace(':', "/")
    operation = "".join(operation.split())

    print('operation: {0}'.format(operation))
    resultat = str(int(eval(operation))) # on convertit d'abord en entier pour le cas de la division qui retourne un flottant.
    resultat = "".join(resultat.split())
    print('Resultat: {0}'.format(resultat))

    chiffres = list(resultat)
    for i in chiffres:
        print(i)
        attendsElementEtClique(driver, chiffresToButtonMap[i], timeout=1)

    verifier = "/html/body/section[19]/div[1]/div[6]/button"
    element = driver.find_element("xpath", verifier)
    element.click()
    sleep(1)

# driver.quit()
