memory = {}
print("Memory AI Ready da!")

while True:
    msg = input("\nNee sollu da (exit to stop:)").strip().lower()

    if msg == "exit":
        print(f"Na kathukitta visayam:{memory}")
        print("Bye da! Memory save pannitten!")
        break

    if "my name is" in msg:
        name = msg.replace("my name is","").strip()
        memory["name"] = name
        print(f"Ok da {name},peru nyabagam vachutten da!")

    elif "What is my name" in msg:
        if "name" in memory:
            print(f"Un peru {memory['name']} da!")  
        else:
            print("Nee innum peru sollave illa da !")

    elif "i like" in msg:
        like=msg.replace("i like","").strip()
        memory["likes"] = like
        print(f"Ohh {like} pudikkuma da? Semma!")
    
    else:
        print("Purinjukitten da! Enakku kathukudu da! 'my name is...' nu sollu!")