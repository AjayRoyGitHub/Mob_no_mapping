# Mobile Number Digit Mapping

phone=input("Enter Your Phone Number: ")
digit_mapping={
    "0":"ZERO",
    "1":"ONE",
    "2":"TWO",
    "3":"THREE",
    "4":"FOUR",
    "5":"FIVE",
    "6":"SIX",
    "7":"SEVEN",
    "8":"EIGHT",
    "9":"NINE"
}
output=""
for ch in phone:
    output=output+digit_mapping.get(ch,"!")+"  "
print(output)
