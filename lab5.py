# Lab 5 Kalen Thomas

# Cat function
def cat_greeting(word):
    print(f'Cat says {word}')
    print('Cat says nothing')
cat_greeting("mee")

  # Step 2
def generate_superhero_power():
   name = "Kalen"
   power = "teleport"
   print(f"{name}'s power is {power}")
# Step 3

def generate_superhero_power1():
    power = "teleport"
    return power
print(generate_superhero_power1())

# Step 4

def generate_superhero_power2(username,super_power):
    message = username + "has the power of" + super_power +"!"
# Step 5
def cat_greeting_loop():
    for i in range(5):
        print(f'the cat says {greetings}')
        greetings = ["meow","mo","mew","purr"]

        cat_greeting_loop()    
# Step 6
def generate_multiple_powers(powers):
    for i in powers:
        print(i)

powers_test = ["teleport","flying","speed","strength"]
generate_multiple_powers(powers_test)