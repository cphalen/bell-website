import json

# this script reads in the JSON files in the old_data directory and writs
# new markdown files in the content directory of the Hugo site so Hugo
# can render the historical data

migrations = ["Honorary", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]

for migration in migrations:
    with open(f"old_data/{migration}.json") as file_in:
        profiles = json.load(file_in)
        for profile in profiles:
            with open(f"../content/{migration}/{profile['code']}.md", "w+") as file_out:
                file_out.write("---\n")
                file_out.write(f"name: \"{profile['name']}\"\n")
                file_out.write(f"class: \"{migration}\"\n")
                file_out.write(f"image: \"{profile['image']}\"\n")
                file_out.write(f"email: \"{profile['socials']['email']}\"\n")
                file_out.write(f"slug: \"{profile['code']}\"\n")
                file_out.write(f"github: \"{profile['socials']['github']}\"\n")
                file_out.write(f"twitter: \"{profile['socials']['twitter']}\"\n")
                file_out.write(f"linkedin: \"{profile['socials']['linkedin']}\"\n")
                file_out.write(f"facebook: \"{profile['socials']['facebook']}\"\n")
                file_out.write("---\n")
                file_out.write(profile['desc'])
