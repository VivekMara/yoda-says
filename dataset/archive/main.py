import csv
input_file = "dataset\\archive\\SW_EpisodeVI.txt"
output_file = "dataset\\yoda_dialogues_episode_6.csv"



# with open("dataset\\archive\\SW_EpisodeV.txt") as f:
#     for line in f:
#         # print(f"Processing line: {line.strip()}")
#         parts = line.split('"')
#         if parts[3] == 'YODA':
#             # print(parts[5])
#             with open("dataset\\yoda.txt", "w") as file:
#                 file.write(parts[5]+"\n")

with open(input_file, encoding="utf-8") as f, open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Character", "Dialogue"])
    for line in f:
        # print(f"Processing line: {line.strip()}")
        parts = line.split('"')
        character = parts[3].strip()
        # dialogue = parts[5]
        if character == 'YODA':
            # print(parts[5])
            writer.writerow([character,parts[5]])

            