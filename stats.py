import requests
import csv

state = input("Please select a U.S. state: ")

url = f"https://disease.sh/v3/covid-19/states/{state}"

bio_data = requests.get(url, timeout=10).json()

# Error handling
if "message" in bio_data:
    print("That state does not exist")
else:
    updated = bio_data.get("updated")
    cases = bio_data.get("cases", 0)
    today_cases = bio_data.get("todayCases", 0)
    active = bio_data.get("active", 0)
    recovered = bio_data.get("recovered", 0)
    deaths = bio_data.get("deaths", 0)
    today_deaths = bio_data.get("todayDeaths", 0)
    tests = bio_data.get("tests", 0)

    fatality_rate = round(deaths / cases, 4) if cases else 0

    print("Last updated:", updated)
    print("Total cases:", cases)
    print("New cases today:", today_cases)
    print("Active cases:", active)
    print("Recovered:", recovered)
    print("Deaths:", deaths)
    print("New deaths today:", today_deaths)
    print("Tests:", tests)
    print("Fatality rate:", fatality_rate)

    with open("disease-stats.csv", "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if f.tell() == 0:
            w.writerow([
                "updated",
                "cases",
                "new_cases",
                "active",
                "recovered",
                "deaths",
                "new_deaths",
                "tests",
                "fatality_rate"
            ])
        w.writerow([
            updated,
            cases,
            today_cases,
            active,
            recovered,
            deaths,
            today_deaths,
            tests,
            fatality_rate
        ])

    print("Success! Saved CSV file.")
