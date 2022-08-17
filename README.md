# The MilkShake Programming Language

Dedicated to the biggest MilkShake lover Igor ❤️

## Installation
```
pip install milkshakelang
```

## Usage
MilkShakeLang commands:
- **give** *[owner]* *[size]* milkshake
- **drink** *[owner]* milkshake *[ounces]*
- **refill** *[owner]* milkshake *[ounces]*

Available MilkShake sizes:
- demi - 3 ounces
- short - 8 ounces
- tall - 12 ounces
- grande - 16 ounces
- venti - 24 ounces
- trenta - 30 ounces

Write MilkShakeLang [script](https://github.com/dayyass/milkshakelang/blob/main/script.milkshake):
```
give Igor venti milkshake
# Igor got Venti MilkShake (24 ounces)

give Dani grande milkshake
# Dani got Grande MilkShake (16 ounces)


drink Igor milkshake 16
# Igor:
# - Drank 16 ounces - so delicious!

drink Igor milkshake 16
# Igor:
# - Drank 8 ounces and finished my milkshake...
# - I want more!

drink Igor milkshake 16
# Igor:
# - There is nothing to drink...
# - Need more milkshake!

drink Dani milkshake 16
# Dani:
# - Drank 16 ounces and finished my milkshake...
# - I want more!


refill Dani milkshake 16
# Dani:
# - Incredible, full cup of milkshake!

refill Igor milkshake 16
# Igor:
# - Wow, 16 ounces of new milkshake!

refill Igor milkshake 16
# MilkShakeOverflowError: Milkshake was spilled on the floor!

```

Run the script:
```
milkshakelang script.milkshake
```

## Requirements
Python >= 3.7
