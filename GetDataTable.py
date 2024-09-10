from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException

class DataTableExtract:
    def gettabledata(driver,sub_path):
        actions = ActionChains(driver)
        element = driver.find_element(By.XPATH, "//div[@id='all_{}']//li[@class='hasmore']//span[text()='Share & Export']".format(sub_path))
        if sub_path != 'player_fantasy':
            driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(1)
        actions.move_to_element(element).perform()
        actions.perform()
        element = driver.find_element(By.XPATH, "//div[@id='all_{}']//button[@tip='Get a link directly to this table on this page']".format(sub_path))
        element.click()
        element = driver.find_element(By.XPATH, "//pre[@id='csv_{}']".format(sub_path))
        return(element)

    def getplayer(driver, player, team_name):
        element = driver.find_element(By.XPATH, "//input[@class='ac-input completely']")
        element.click()
        element.send_keys(player)
        element, answer = DataTableExtract.checknames(driver, player)
        if  answer == 1:
            return(DataTableExtract.clickplayer(driver, player, team_name, element))
        elif answer == 0:
            driver.refresh()
            return(0)
        else:
            return(DataTableExtract.fixplayer(player, team_name))

    def fixplayer(player, team_name):
        print("Click the right player and enter (1) or enter (0) if can't fix to skip player.")
        print("Player: {}".format(player))
        print("Team name: {}".format(team_name))
        answer = input()
        while answer not in ['0', '1']:
            print("Click the right player and enter (1) or enter (0) if can't fix to skip player.")
            answer = input()
        return(int(answer))

    def changeyear(driver):
        new_web = driver.current_url[:-4] + "2022" if driver.current_url.split("/")[-1] == '2021' else driver.current_url[:-4] + "/fantasy/2021"
        driver.get(new_web)
        return()

    def clickplayer(driver, player, team_name, element):
        element.click()
        try:
            element = driver.find_element(By.XPATH, "//div[@id='meta']//a[text()='{}']".format(team_name))
            return(1)
        except NoSuchElementException:
            return(0)

    def checkyear(driver, search_index):
        years = driver.find_elements(By.XPATH, "//div[@class='ac-dropdown']//span[@class='search-results-years']")
        if years[search_index].text.split('\n')[0].split('-')[-1] == '2022':
            return(1)
        else:
            return(0)

    def checknames(driver, player):
        elements = driver.find_elements(By.XPATH, "//div[@class='ac-dropdown']//span[@class='search-results-item']")
        names = [x.text for x in elements]
        year_flag = False
        for search_index, name in enumerate(names):
            player_flag = False
            if name == player:
                player_flag = True
                if DataTableExtract.checkyear(driver, search_index) == 1:
                    year_flag = True
                    break
        if year_flag and player_flag:
            return(elements[search_index],1)
        if year_flag == False and player_flag:
            return([],0)
        else: 
            return([],-1)

    def getinjuries(driver, team):
        actions = ActionChains(driver)
        sub_path = "@id='all_{}_injury_report'".format(team)
        element = driver.find_element(By.XPATH, "//div[{}]//li[@class='hasmore']//span[text()='Share & Export']".format(sub_path))
        actions.move_to_element(element).perform()
        actions.perform()
        element = driver.find_element(By.XPATH, "//div[{}]//button[@tip='Get a link directly to this table on this page']".format(sub_path))
        element.click()
        element = driver.find_element(By.XPATH, "//pre[@id='csv_{}_injury_report']".format(team))
        return(element)    