import csv

with open(f"./old_data/2022.csv") as file_in:
    csv_reader = csv.reader(file_in, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            code = "-".join(row[0].split(" ")).lower()
            with open(f"../content/2022/{code}.md", "w+") as file_out:
                file_out.write("---\n")
                file_out.write(f"name: \"{row[0]}\"\n")
                file_out.write(f"class: \"2022\"\n")
                file_out.write(f"slug: \"{code}\"\n")
                file_out.write(f"image: \"{row[10]}\"\n")
                file_out.write(f"email: \"{row[4]}\"\n")
                if row[7] != "":
                    file_out.write(f"github: \"https://github.com/{row[7]}\"\n")
                if row[5]  !="":
                    file_out.write(f"twitter: \"https://twitter.com/{row[5]}\"\n")
                if row[4]  != "":
                    file_out.write(f"linkedin: \"https://www.linkedin.com/in/{row[4]}\"\n")
                if row[6]  != "":
                    file_out.write(f"facebook: \"https://www.facebook.com/{row[6]}\"\n")
                file_out.write("---\n")
                file_out.write(row[2])


