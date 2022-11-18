data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung"
}
LENDICT = len(data_dict)
print(f"panjang dictionary :{LENDICT}")

KEY = "cup"
CHECKKEY = KEY in data_dict

print(f"apakah {KEY} ada di data_dict:{CHECKKEY}")

print(data_dict.get("cup"))
print(data_dict.get("bro","data tidak di temukann"))

data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"faqih":"faqih si keren"})
print(data_dict)

del data_dict["faqih"]
print(data_dict)
              
