import requests as rs

def extract_temperature():
    csv_url="https://docs.google.com/spreadsheets/d/e/2PACX-1vSQ5aS9-OpsowXMdzK3H91FjIPpKxjSznYS9FuOi30Eh-eqUdwcKJY6heMi4jJgWqpcmhTQUGKd1oOM/pub?gid=0&single=true&output=csv"
    res=rs.get(url=csv_url)
    open(r'../Capstone temp/temperature.csv', 'wb').write(res.content)

def extract_occupancy():
    csv_url="https://docs.google.com/spreadsheets/d/e/2PACX-1vTS_oL-9DHpocSYimL26A5ttYQJiK2rtkcAlBZkTsr44LoEqZpYXwaCBe9LAC2p3OhBW9JagcSFxzyt/pub?gid=0&single=true&output=csv"
    res=rs.get(url=csv_url)
    open(r'../Capstone temp/occupancy.csv', 'wb').write(res.content)


