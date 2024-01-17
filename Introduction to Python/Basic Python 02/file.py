try:
    with open("source,txt", "r") as source_file:
        content = source_file.read()

    with open("destination.txt", "w") as destination_file:
        destination_file.write(content)

    print("File read and write successfull!")

except FileNotFoundError:
    print("Error: Source file not found.")

except IOError as e:
    print(f"An error occurred: {e}")

finally:
    print("Process complete")