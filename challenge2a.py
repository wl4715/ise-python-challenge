import csv

def compute_row_checksum(row):
    biggest_number = int(row[0])
    lowest_number = int(row[0])
    for value in row:
        unit = int(value)
        if unit > biggest_number:
            biggest_number = unit
        if unit < lowest_number:
            lowest_number = unit

    row_checksum = biggest_number - lowest_number
    return row_checksum

if __name__ == "__main__":
    tsv_file = open("spreadsheet.tsv")
    csv_reader = csv.reader(tsv_file, delimiter="\t")

    total_checksum = 0
    i = 0
    for row in csv_reader:
        row_checksum = compute_row_checksum(row)
        print(f'The checksum for row {i}: {row_checksum} \n')
        total_checksum += row_checksum
        i += 1

    print(f'Total checksum is: {total_checksum}')

    tsv_file.close()
