import random

# Expanded word pools with 10 main topics, each with 10 subtopics (sample)
word_pools = {
    "technology": {
        "programming": ["code", "script", "loop", "compile", "dev", "object", "array", "stack", "debug", "variable"],
        "hardware": ["chip", "cpu", "gpu", "ssd", "modem", "sensor", "bus", "motherboard", "transistor", "heat"],
        "networking": ["router", "switch", "ethernet", "tcp", "ip", "latency", "ping", "port", "proxy", "firewall"],
        "ai": ["neural", "model", "tensor", "learning", "agent", "inference", "prompt", "token", "dataset", "loss"],
        "cybersecurity": ["phish", "malware", "firewall", "vpn", "breach", "hash", "exploit", "cipher", "auth", "key"],
        "web": ["html", "css", "script", "react", "node", "dom", "ajax", "json", "render", "cdn"],
        "data": ["sql", "db", "query", "table", "join", "index", "view", "row", "schema", "csv"],
        "robotics": ["servo", "motor", "actuator", "sensor", "arm", "chassis", "autonomy", "path", "grip", "code"],
        "cloud": ["aws", "azure", "gcp", "container", "serverless", "lambda", "bucket", "instance", "scale", "region"],
        "quantum": ["qubit", "gate", "entangle", "superposition", "decoherence", "measure", "circuit", "spin", "state", "unitary"]
    },
    "nature": {
        "plants": ["tree", "fern", "moss", "bark", "leaf", "stem", "blossom", "bud", "vine", "shrub"],
        "animals": ["lion", "wolf", "bear", "owl", "fox", "deer", "hare", "boar", "otter", "moose"],
        "insects": ["ant", "bee", "fly", "moth", "roach", "beetle", "wasp", "grub", "flea", "gnat"],
        "geography": ["hill", "valley", "plateau", "canyon", "island", "coast", "reef", "ridge", "delta", "cliff"],
        "weather": ["storm", "wind", "rain", "hail", "sun", "cloud", "fog", "snow", "gust", "thunder"],
        "space": ["star", "planet", "moon", "asteroid", "comet", "orbit", "galaxy", "quasar", "nebula", "meteor"],
        "ocean": ["wave", "tide", "coral", "sand", "trench", "kelp", "surf", "shell", "depth", "plankton"],
        "sky": ["eclipse", "sunset", "twilight", "aurora", "horizon", "zenith", "skyline", "crescent", "cloud", "halo"],
        "forests": ["pine", "oak", "grove", "thicket", "canopy", "sap", "glade", "wood", "birch", "cedar"],
        "desert": ["dune", "cactus", "arid", "mirage", "scorch", "dust", "sand", "rock", "lizard", "heat"]
    },
    "fantasy": {
        "creatures": ["dragon", "griffin", "elf", "orc", "troll", "nymph", "dwarf", "phoenix", "goblin", "wraith"],
        "magic": ["spell", "wand", "curse", "potion", "hex", "rune", "scroll", "ritual", "aura", "enchant"],
        "weapons": ["sword", "dagger", "bow", "axe", "staff", "orb", "whip", "lance", "blade", "mace"],
        "armor": ["shield", "helmet", "plate", "greaves", "gauntlet", "robe", "tunic", "chainmail", "mantle", "cloak"],
        "lands": ["realm", "isle", "kingdom", "citadel", "glade", "tower", "dungeon", "abyss", "crag", "vale"],
        "heroes": ["knight", "ranger", "mage", "paladin", "rogue", "bard", "druid", "cleric", "warrior", "monk"],
        "villains": ["necromancer", "warlock", "witch", "sorcerer", "overlord", "tyrant", "usurper", "banshee", "beast", "fiend"],
        "races": ["human", "orc", "elf", "gnome", "troll", "fairy", "goblin", "vampire", "werewolf", "hobbit"],
        "items": ["ring", "amulet", "scroll", "gem", "relic", "tome", "potion", "charm", "crystal", "sigil"],
        "quests": ["journey", "hunt", "trial", "riddle", "path", "labyrinth", "curse", "prophecy", "pact", "artifact"]
    },
    "space": {
        "planets": ["mars", "venus", "earth", "jupiter", "saturn", "neptune", "uranus", "mercury", "pluto", "ceres"],
        "stars": ["sirius", "betelgeuse", "vega", "polaris", "rigel", "aldebaran", "deneb", "proxima", "antares", "canopus"],
        "missions": ["apollo", "voyager", "hubble", "curiosity", "perseverance", "spitzer", "kepler", "galileo", "pioneer", "juno"],
        "galaxies": ["milkyway", "andromeda", "triangulum", "whirlpool", "sombrero", "cartwheel", "pinwheel", "messier", "blackeye", "fireworks"],
        "phenomena": ["blackhole", "supernova", "quasar", "pulsar", "nebula", "eclipse", "aurora", "meteor", "comet", "flare"],
        "astronauts": ["armstrong", "gagarin", "glenn", "ride", "collins", "aldrin", "tereshkova", "hadfield", "jemison", "bean"],
        "telescopes": ["hubble", "jameswebb", "keck", "vlt", "alma", "spitzer", "wise", "chandra", "sofia", "tess"],
        "equipment": ["suit", "helmet", "module", "lander", "rover", "probe", "thruster", "hatch", "antenna", "solar"],
        "theories": ["relativity", "gravity", "quantum", "bigbang", "expansion", "inflation", "multiverse", "darkmatter", "spacetime", "string"],
        "astrobiology": ["microbe", "habitat", "extremophile", "oxygen", "carbon", "water", "alien", "signal", "methane", "exoplanet"]
    },
    "history": {
        "eras": ["renaissance", "medieval", "ancient", "victorian", "baroque", "modern", "classical", "industrial", "colonial", "ironage"],
        "leaders": ["caesar", "napoleon", "cleopatra", "alexander", "genghis", "washington", "churchill", "lincoln", "roosevelt", "mao"],
        "wars": ["ww1", "ww2", "coldwar", "civilwar", "revolution", "napoleonic", "crusades", "vietnam", "korean", "gulf"],
        "events": ["independence", "reformation", "renaissance", "holocaust", "goldrush", "greatdepression", "moonlanding", "industrialrevolution", "frenchrevolution", "fallofrome"],
        "civilizations": ["egypt", "rome", "greece", "maya", "inca", "china", "persia", "mesopotamia", "aztec", "babylon"],
        "explorers": ["columbus", "magellan", "cook", "vancouver", "drake", "hudson", "polo", "cabral", "cabot", "daGama"],
        "inventions": ["printingpress", "steamengine", "telephone", "lightbulb", "internet", "wheel", "gunpowder", "compass", "clock", "radio"],
        "philosophy": ["stoicism", "existentialism", "platonism", "nihilism", "empiricism", "rationalism", "idealism", "utilitarianism", "hedonism", "skepticism"],
        "artmovements": ["impressionism", "cubism", "surrealism", "baroque", "rococo", "renaissance", "expressionism", "realism", "abstract", "popart"],
        "architecture": ["gothic", "baroque", "modernism", "brutalism", "romanesque", "neoclassical", "artdeco", "victorian", "postmodern", "minimalism"]
    },
    "music": {
        "genres": ["jazz", "rock", "hiphop", "blues", "metal", "pop", "classical", "punk", "reggae", "electronic"],
        "instruments": ["guitar", "drum", "piano", "violin", "saxophone", "flute", "cello", "bass", "trumpet", "harp"],
        "production": ["track", "beat", "mix", "loop", "vibe", "reverb", "studio", "record", "sample", "master"],
        "artists": ["beatles", "madonna", "beyonce", "elvis", "mozart", "taylor", "drake", "prince", "adele", "rihanna"],
        "performance": ["concert", "gig", "tour", "festival", "show", "encore", "soundcheck", "rehearsal", "jam", "setlist"],
        "vocal": ["alto", "tenor", "baritone", "soprano", "bass", "falsetto", "melisma", "vibrato", "chorus", "solo"],
        "theory": ["scale", "chord", "harmony", "melody", "rhythm", "tempo", "key", "mode", "interval", "tone"],
        "history": ["baroque", "classical", "romantic", "renaissance", "modern", "medieval", "jazzage", "bluesera", "punkrock", "hiphopgolden"],
        "technology": ["synth", "sampler", "midi", "turntable", "microphone", "equalizer", "compressor", "plugin", "daw", "monitor"],
        "notation": ["sheet", "score", "tablature", "clef", "staff", "measure", "rest", "note", "accent", "dynamic"]
    },
    "gaming": {
        "genres": ["rpg", "fps", "moba", "roguelike", "sandbox", "adventure", "sim", "survival", "platformer", "strategy"],
        "platforms": ["pc", "console", "arcade", "handheld", "mobile", "emulator", "cloud", "vr", "retro", "browser"],
        "characters": ["knight", "mage", "rogue", "boss", "npc", "avatar", "zombie", "archer", "healer", "tank"],
        "items": ["sword", "potion", "shield", "bow", "armor", "scroll", "ring", "dagger", "staff", "helmet"],
        "actions": ["attack", "defend", "cast", "loot", "trade", "craft", "levelup", "quest", "heal", "stealth"],
        "maps": ["dungeon", "castle", "forest", "village", "cave", "mountain", "river", "city", "arena", "desert"],
        "enemies": ["goblin", "dragon", "orc", "undead", "troll", "bandit", "witch", "giant", "spider", "zombie"],
        "skills": ["fireball", "heal", "teleport", "shield", "slash", "trap", "summon", "stealth", "charge", "freeze"],
        "guilds": ["knights", "mages", "rogues", "hunters", "berserkers", "assassins", "monks", "paladins", "rangers", "necromancers"],
        "loot": ["gold", "gem", "artifact", "coin", "scroll", "potion", "armor", "weapon", "key", "map"]
    },
    "food": {
        "fruits": ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "pear"],
        "vegetables": ["carrot", "broccoli", "spinach", "potato", "onion", "pepper", "tomato", "cabbage", "celery", "peas"],
        "meats": ["chicken", "beef", "pork", "lamb", "turkey", "duck", "venison", "rabbit", "goat", "salmon"],
        "dairy": ["milk", "cheese", "butter", "yogurt", "cream", "custard", "curd", "ghee", "paneer", "whey"],
        "grains": ["rice", "wheat", "barley", "oats", "corn", "quinoa", "rye", "millet", "sorghum", "buckwheat"],
        "spices": ["pepper", "cinnamon", "nutmeg", "clove", "cardamom", "cumin", "turmeric", "ginger", "saffron", "mustard"],
        "desserts": ["cake", "cookie", "brownie", "pie", "pudding", "icecream", "tart", "mousse", "sorbet", "custard"],
        "drinks": ["water", "juice", "tea", "coffee", "wine", "beer", "soda", "cocktail", "milkshake", "smoothie"],
        "cuisines": ["italian", "mexican", "chinese", "indian", "french", "thai", "japanese", "greek", "spanish", "korean"],
        "baking": ["flour", "yeast", "batter", "dough", "glaze", "icing", "crumb", "proof", "knead", "rise"]
    },
    "movies": {
        "genres": ["action", "comedy", "drama", "thriller", "horror", "sci-fi", "romance", "animation", "fantasy", "documentary"],
        "directors": ["spielberg", "nolan", "kubrick", "scorsese", "tarantino", "hughes", "cameron", "lee", "burton", "allen"],
        "actors": ["deniro", "streep", "depp", "hanks", "lawrence", "cranston", "pitt", "diaz", "jolie", "ferrell"],
        "movies": ["inception", "avatar", "gladiator", "casablanca", "titanic", "matrix", "godfather", "frozen", "joker", "up"],
        "awards": ["oscar", "goldenglobes", "bafta", "sundance", "cannes", "emmy", "grammy", "tony", "criticschoice", "screenactors"],
        "characters": ["joker", "batman", "gandalf", "frodo", "vito", "rocky", "sherlock", "indiana", "harry", "ironman"],
        "studios": ["warnerbros", "universal", "disney", "paramount", "sony", "fox", "lionsgate", "marvel", "pixar", "dreamworks"],
        "quotes": ["bond", "maytheforce", "illbeBack", "hastaLaVista", "theresNoPlace", "here'sJohnny", "youTalkin", "showMeTheMoney", "lifeIsLike", "toInfinity"],
        "soundtracks": ["johnwilliams", "hanszimmer", "howardshore", "dannyelfman", "alexandre", "enio", "alanmenken", "max", "randy", "johann"],
        "specialeffects": ["cgi", "greencreen", "motioncapture", "prosthetics", "animatronics", "miniatures", "mattepaint", "pyrotechnics", "compositing", "rendering"]
    }
}

def get_valid_input(prompt, valid_options):
    """Prompt the user until a valid input is given."""
    prompt_str = f"{prompt} ({', '.join(valid_options)}): "
    while True:
        user_input = input(prompt_str).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

def generate_username(topic, subtopic, min_length, max_length, num_digits, require_uppercase, joiner):
    words = random.choices(word_pools[topic][subtopic], k=2)
    username = joiner.join(words)
    
    if num_digits > 0:
        username += ''.join(random.choices("0123456789", k=num_digits))
    if require_uppercase:
        username += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if len(username) < min_length:
        username += ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=min_length - len(username)))
    elif len(username) > max_length:
        username = username[:max_length]
    return username

def main():
    topics = list(word_pools.keys())
    topic = get_valid_input("Enter a topic", topics)
    
    subtopics = list(word_pools[topic].keys())
    subtopic = get_valid_input(f"Enter a subtopic for '{topic}'", subtopics)
    
    while True:
        try:
            min_length = int(input("Minimum username length: "))
            max_length = int(input("Maximum username length: "))
            if min_length > max_length:
                print("Minimum length cannot be greater than maximum length.")
                continue
            break
        except ValueError:
            print("Please enter valid integers for lengths.")
    
    while True:
        try:
            num_digits = int(input("Number of digits to include: "))
            if num_digits > max_length:
                print("Number of digits cannot exceed maximum length.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for number of digits.")
    
    require_uppercase = get_valid_input("Require at least one uppercase letter? (yes/no)", ["yes", "no"]) == "yes"
    
    joiner = get_valid_input("Choose joiner: hyphen (-), underscore (_), or none", ["-", "_", "none"])
    if joiner == "none":
        joiner = ""
    
    username = generate_username(topic, subtopic, min_length, max_length, num_digits, require_uppercase, joiner)
    print("\nGenerated Username:", username)

if __name__ == "__main__":
    main()