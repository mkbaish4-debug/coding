
import random

words = ("able","acid","aged","also","area","army","away","baby","back","ball","band",
        "bank","base","bath","bear","beat","been","bell","best","bill","bird","blow",
        "blue","boat","body","book","born","both","bowl","bulk","burn","busy","call",
        "calm","came","camp","card","care","case","cash","cast","cell","chat","chip",
        "city","club","coat","code","cold","come","cook","cool","copy","cost","crew",
        "crop","dark","data","date","dawn","days","dead","deal","dear","debt","deep",
        "desk","dial","diet","disk","door","down","draw","drop","dual","duty","each",
        "earn","ease","east","easy","edge","else","even","ever","evil","exam","face",
        "fact","fail","fair","fall","farm","fast","fate","fear","feed","feel","feet",
        "fell","file","fill","film","find","fine","fire","firm","fish","five","flat",
        "flow","food","foot","ford","form","four","free","from","fuel","full","fund",
        "game","gate","gave","gear","gene","gift","girl","give","glad","goal","goes",
        "gold","gone","good","gray","grew","grow","hair","half","hall","hand","hang",
        "hard","harm","hate","have","head","hear","heat","held","help","here","hero",
        "high","hill","hire","hold","hole","holy","home","hope","host","hour","huge",
        "hung","hunt","hurt","idea","inch","into","iron","item","join","jump","just",
        "keep","kept","kick","kill","kind","king","knew","know","lack","lady","lake",
        "land","last","late","lead","left","less","life","lift","like","line","link",
        "list","live","load","loan","lock","logo","long","look","lord","lose","loss",
        "lost","love","luck","made","mail","main","make","male","many","mark","mass",
        "meal","mean","meet","menu","mile","milk","mind","mine","miss","mode","moon",
        "more","most","move","much","must","name","near","neck","need","news","next",
        "nice","nick","nine","none","nose","note","okay","once","only","onto","open",
        "over","page","paid","pain","pair","park","part","pass","past","path","peak",
        "pick","pink","pipe","plan","play","plot","plus","poem","poet","pool","poor",
        "port","post","pull","pure","push","race","rain","rank","rare","rate","read",
        "real","rear","rest","rice","rich","ride","ring","rise","risk","road","rock",
        "role","roof","room","root","rope","rose","rule","rush","safe","said","sake",
        "sale","salt","same","sand","save","seat","seed","seek","seem","seen","self",
        "sell","send","sent","ship","shop","shot","show","shut","sick","side","sign",
        "silk","sing","site","size","skin","slip","slow","snow","soft","soil","sold",
        "sole","some","song","soon","sort","soul","spot","star","stay","step","stop",
        "such","suit","sure","take","tale","talk","tall","tank","tape","task","team",
        "tech","tell","tend","term","test","text","than","that","them","then","they",
        "thin","this","thus","time","tiny","told","tone","took","tool","tour","town",
        "tree","trip","true","turn","type","unit","upon","used","user","uses","vary",
        "vast","very","view","vote","wait","walk","wall","want","warm","wash","wave",
        "ways","weak","wear","week","well","went","were","west","what","when","whom",
        "wide","wife","wild","will","wind","wine","wing","wire","wise","wish","with",
        "wood","word","wore","work","yard","year","your","zero","zone", "aardvark",
        "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo",
        "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo",
        "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar", "cattle",
        "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam",
        "cobra", "cockroach", "cod", "coyote", "crab", "crane", "crocodile", "crow",
        "curlew", "deer", "dinosaur", "dog", "dogfish", "dolphin", "donkey", "dormouse",
        "dotterel", "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna",
        "eel", "eland", "elephant",  "elk", "emu", "falcon", "ferret", "finch", "fish",
        "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat",
        "gnu", "goat", "goldfinch", "goldfish", "goose", "gorilla", "goshawk", "grasshopper",
        "grouse", "guanaco", "gull", "hamster", "hare", "hawk", "hedgehog", "heron", "herring",
        "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "ibex", "ibis",
        "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "kingfisher", "koala", "kookabura",
        "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", "lion", "llama", "lobster",
        "locust", "loris", "louse", "lyrebird", "magpie", "mallard", "manatee", "mandrill",
        "mantis", "marten", "meerkat", "mink", "mole", "mongoose", "monkey", "moose", "mosquito",
        "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "oryx",
        "ostrich", "otter", "owl", "ox", "oyster", "panda", "panther", "parrot", "partridge",
        "peafowl", "pelican", "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony",
        "porcupine", "porpoise", "quail", "quelea", "quetzal", "rabbit", "raccoon", "rail",
        "ram", "rat", "raven", "red-deer", "red-panda", "reindeer", "rhinoceros", "rook",
        "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion", "seahorse",
        "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider",
        "spoonbill", "squid", "squirrel", "starling", "stingray", "stoat", "stork", "swallow",
        "swan", "tapir", "tarsier", "termite", "tiger", "toad", "trout", "turkey", "turtle",
        "viper", "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf",
        "wolverine", "wombat", "woodcock", "woodpecker", "worm", "wren", "yak", "zebra")

def match_char(guess, word, unknown):
    if guess in word:
        for index in range(len(word)):
            if word[index] == guess:
                unknown[index] = guess
            else:
                pass
        return unknown
    else:
        return unknown

def hangman(guess, word, hangman_art, hangmankey):
    if guess in word:
        for line in hangman_art.get(hangmankey):
            print(line)
        return hangmankey
    else:
        hangmankey += 1
        for line in hangman_art.get(hangmankey):
            print(line)
        return hangmankey

def main():
    word = random.choice(words)
    unknown = ["_"] * len(word) # learning: strings are immutable so had to choose a list.
    hangman_art =             {0: ("   ",
                                   "   ",
                                   "   "),
                               1: (" o ",
                                   "   ",
                                   "   "),
                               2: (" o ",
                                   " | ",
                                   "   "),
                               3: (" o ",
                                   "/| ",
                                   "   "),
                               4: (" o ",
                                  "/|\\",
                                   "   "),
                               5: (" o ",
                                   "/|\\",
                                   "/  "),
                               6: (" o ",
                                   "/|\\",
                                   "/ \\")}
    hangmankey = 0
    print("*" * 30)
    print("        Hangman Game")
    print("*" * 30)
    print("Guess the word")
    print(" ".join(unknown))
    isrunning = True
    while isrunning:
        guess = input("Enter a character: ")
        print("*" * 30)
        hangmankey = hangman(guess, word, hangman_art, hangmankey)
        print("*" * 30)
        print(" ".join(match_char(guess, word, unknown)))
        if "".join(unknown) == word:
            print("Congratulations you won!")
            isrunning = False
        elif hangmankey >= 6:
            print("You lose! Hangman has arrived!")
            isrunning = False

if __name__ == "__main__":
    main()
