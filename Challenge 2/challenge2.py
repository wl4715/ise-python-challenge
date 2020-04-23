import csv

def compute_row_checksum(row):
    biggest_number = int(row[0]) # first number of the row as reference
    lowest_number = int(row[0]) # first number of the row as reference
    for value in row:
        if int(value) > biggest_number:
            biggest_number = int(value)
        if int(value) < lowest_number:
            lowest_number = int(value)

    row_checksum = biggest_number - lowest_number
    return row_checksum

def compute_row_evendivision(row):
    i = 0
    while i < len(row): # for every single number of the row
        j = 0
        while j < len(row): # iterate through all the number of the row and check
                            # ensure it's evenly divisible and it's not dividing itself
            if int(row[i]) % int(row[j]) == 0 and int(row[i]) != int(row[j]):
                row_evendivision = int(row[i])/int(row[j])
                break
            j += 1
        i += 1

    return row_evendivision

if __name__ == "__main__":
    tsv_file = open("spreadsheet.tsv")
    tsv_reader = csv.reader(tsv_file, delimiter="\t")

    total_checksum = 0
    total_evendivision = 0
    i = 0
    for row in tsv_reader:
        row_checksum = compute_row_checksum(row)
        print(f'The checksum for row {i}: {row_checksum}')
        total_checksum += row_checksum

        row_evendivision = compute_row_evendivision(row)
        print(f'The even division for row {i}: {row_evendivision} \n')
        total_evendivision += row_evendivision

        i += 1

    print(f'Total checksum is: {total_checksum}')
    print(f'Total even division is: {total_evendivision}')

    tsv_file.close()
