# Project: Job listings Web Scraper
# Author: Kritika 
# Web Scraping using Python

# Import required libraries
import requests                    #open websites
from bs4 import BeautifulSoup      #read HTML, extract data
import pandas as pd                #create tables, orgainze scraped data
pd.set_option('display.max_columns', None)
url= "https://internshala.com/jobs/"  #storing website link in url

headers= {                         #Browser request header
    "Uset-Agent": "Mozilla/5.0"    #it is a common browser identity
}

response = requests.get(url, headers=headers)   #sends request to server and download webpage content

print(response.status_code)   #it tells whether request succeeded

soup= BeautifulSoup(response.text, "html.parser")  #response.text contains entire HTML code of website

jobs= soup.find_all("div", class_= "individual_internship")   #Find all job cards

print(len (jobs) ) #print number of jobs cards found

# Empty lists to store scraped data
job_titles = []            # Stores job titles       
company_names = []         # Stores company names
locations = []             # Stores job locations
salaries = []              # Stores salary details
skills_list = []           # Stores required skills
posted_dates = []          # Stores postiong dates

# Loop through each job card
for job in jobs:

    # Extract Job Title
    title = job.find("h2", class_="job-internship-name").text.strip()


    # Extract Company Name
    company = job.find("p", class_="company-name").text.strip()


    # Extract job Location
    location = job.find("p", class_="locations").text.strip()


    # Extract Salary information
    salary_tag = job.find("span", class_="desktop")
    
    # Check if salary exists
    if salary_tag:
        salary = salary_tag.text.strip()
    else:
        salary = "Not Available"


    # Extract all required Skills
    skills = job.find_all("div", class_="job_skill")
    
    # Empty list to store skills for one job
    skill_names = []
    
    # Loop through each skill
    for skill in skills:
        skill_names.append(skill.text.strip())
    
    # Convert skills list into single text
    skills_text= ", ".join(skill_names)


    # Extract posted Date
    date_tag= job.find("div", class_="status-success")
    
    # Check if posted date exists
    if date_tag:
        posted_date= date_tag.text.strip()
    else:
        posted_date= "Not Available"


    # Add extracted Data Into Lists
    job_titles.append(title)
    company_names.append(company)
    locations.append(location)
    salaries.append(salary)
    skills_list.append(skills_text)
    posted_dates.append(posted_date)


# Create DataFrame/table using pandas
data = pd.DataFrame({
    "Job Title": job_titles,
    "Company": company_names,
    "Location": locations,
    "Salary": salaries,
    "Skills": skills_list,
    "Posted Date": posted_dates
})

# Print Table
print(data)

# Save dataset into CSV file
data.to_csv("jobs_data.csv", index=False) 


print("Web Scraping Project 1 Completed Successfully")


