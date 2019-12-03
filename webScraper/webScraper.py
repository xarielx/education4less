from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import io
import urllib.request
from urllib.error import HTTPError, URLError

filename = "scholarships.csv"
# f = open(filename, "w")
headers = "scholarship_name, scholarship_link, award_amount, geographic_requisite, enrollment_requisite, major_requisite, description, requirements\n"
# f.write(headers)
with io.open(filename, "w", encoding="utf-8") as f:
    f.write(headers)
    for i in range(768):      # Number of pages plus one
        my_url = 'http://www.collegescholarships.org/financial-aid/?page=' + \
            str(i)
        # opening up the page and grabbing it
        uClient = uReq(my_url)
        page_html = uClient.read()
        # closing connection
        uClient.close()
        # calling soup
        page_soup = soup(page_html, "html.parser")

        # grabs each row on the scholarships
        containers = page_soup.findAll("div", {"class": "row"})
        # filename = "scholarships.csv"
        # f = open(filename, "w")
        # headers = "scholarship_name, scholarship_link, award_amount, geographic_requisite, enrollment_requisite, major_requisite\n"
        # f.write(headers)
        # for container in containers:
        # skip first 3 rows since they are description values, same for last 3
        final_link = ""
        hard_requirements = ""

        for container in containers[3:-3]:
            # finds link of scholarship
            link = container.div.div.a["href"]
            # opening up the page and grabbing the following link
            req = urllib.request.Request(link)
            try:
                uClient1 = urllib.request.urlopen(req)
                page_html1 = uClient1.read()
                # closing connection
                uClient1.close()
                # calling soup
                page_soup1 = soup(page_html1, "html.parser")
                app_linkholder = page_soup1.findAll(
                    "div", {"id": "description"})
                containers1 = page_soup1.findAll(
                    "dt", {"class": None})
                containers2 = page_soup1.findAll(
                    "dd", {"class": None})
                index = 0
                l1 = list()
                for desc in containers1:
                    # print(desc.text + " " + containers2[index].text)'
                    hld_str = containers2[index].text
                    if desc.text.find("Min. award") != -1:
                        hld_str = hld_str.replace(",", "")
                    if desc.text.find("Average award") != -1:
                        hld_str = hld_str.replace(",", "")
                    if desc.text.find("Max. award") != -1:
                        hld_str = hld_str.replace(",", "")
                    temp_str = desc.text.replace(",", "|") + \
                        " " + hld_str.replace(",", "|") + " "
                    temp_str.replace(",", "|")
                    l1.append(temp_str)
                    # print(containers2[index].text)
                    index += 1
                # grabs scholarships final link
                final_link = app_linkholder[0].a["href"]
            except HTTPError as e:
                print(e)
                l1 = list()
                l1.append("Error")
                final_link = link
            except URLError as e:
                print(e)
                l1 = list()
                l1.append("Error")
                final_link = link
            except Exception as e:
                import traceback
                print(e)
                l1 = list()
                l1.append("Error")
                final_link = link
            # uClient1 = uReq(link)
            # page_html1 = uClient1.read()
            # # closing connection
            # uClient1.close()
            # # calling soup
            # page_soup1 = soup(page_html1, "html.parser")
            # app_linkholder = page_soup1.findAll("div", {"id": "description"})
            # # grabs scholarships final link
            # final_link = app_linkholder[0].a["href"]
            # for a in app_linkholder.findAll('a', href=True):
            #     print("Found the URL:", a['href'])
            name_container = container.findAll(
                "h4", {"class": "text-uppercase"})
            name = name_container[0].a.text
            award_amount = container.findAll("p", {"class": "visible-xs"})
            description_container1 = container.findAll("div", attrs={
                'class': "scholarship-description"})
            description = description_container1[0].findAll("p",
                                                            attrs={'class': None})
            descString = description[0]
            new_desc = ""
            # cleans description text
            for x in descString:
                x.replace('<p>', '').replace('</p>', '')
                new_desc = x
            scholarship_value = award_amount[0].strong.text
            conditions = container.findAll("span", {"class": "trim"})
            l = list()
            for condition in conditions:
                myString = condition.text.strip()
                l.append(myString)
            # print("Scholarship Name: " + name)
            # print("Link: " + link)
            # print("Award Amount: " + scholarship_value)
            # for word in l:
            #     index = l.index(word)
            #     if index == 0:
            #         print("Geographic Location: " + word)
            #     if index == 1:
            #         print("Enrollment level: " + word)
            #     if index == 2:
            #         print("Major: " + word)
            # print("\n")
            hard_requirements = ('| '.join(l1))
            f.write(name.replace(",", "|") + "," + final_link.replace(",", "|") + "," + scholarship_value.replace(",", "") +
                    "," + l[0].replace(",", "|") + "," + l[1].replace(",", "|") + "," + l[2].replace(",", "|") + "," + new_desc.replace(",", "|") + "," + hard_requirements + "\n")
            #print(name + "\n")

            # print(hard_requirements)
            # for a in l1:
            #     print(a + " ")
            # print("\n")
