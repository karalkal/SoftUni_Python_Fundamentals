full_path = input()
# print(full_path.rfind(chr(92)))
cut_from = full_path.rfind(chr(92))
# from "\" but excluding, therefore +1
full_file_name = full_path[cut_from + 1:]
full_file_name = full_file_name.split(".")
print(f"File name: {full_file_name[0]}\nFile extension: {full_file_name[1]}")