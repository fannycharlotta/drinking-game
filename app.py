from flask import Flask, render_template, jsonify

app = Flask(__name__)

challenges = [
    "What's the last text you sent?",
    "Never have I ever 'forgotten' to use protection",
    "Never have I ever sent nudes",
    "When's the last time you had sex?",
    "Do you have a go-to person for hookups? Say their name or take a shot",
    "Text your last sneaky link 'I miss you' or take a shot",
    "Who's the most likely to date two people at once?",
    "Never have I ever forgot how I got home",
    "Drink if you don't like someone's partner",
    "Open 'my eyes only' or drink 4",
    "Drink if you have dated someone younger than you",
    "Have you ever faked an orgasm?",
    "Who's most likely to ghost after sex?",
    "Take a sip if you've kissed more than 1 person in this room",
    "Never have I ever been proposed to",
    "Make a rule",
    "Make a rule",
    "Never have I ever had sex in a public place",
    "It's a 9 but they like to lick your toes",
    "Take a selfie with someone and caption it 'sneaky link vibes'",
    "What's the most public place you've done it?",
    "Never have I ever flirted with someone I wasn't attracted to",
    "Give someone in the room a lap dance",
    "Name the person with the craziest ex",
    "Sit on someone's lap for the next 2 rounds",
    "Make out with someone for 10 seconds or take 5 BIG sips",
    "Have a drink for every ex you have had",
    "Never have I ever had sex in a car",
    "Who's most likely to post a thirst trap on their social media?",
    "If you had to hook up with someone in this room, who would you NOT pick - and why?",
    "How many people have you kissed this year?",
    "Never have I ever drunk texted an ex",
    "If you have broken up with someone over text, have a drink",
    "If you're in a relationship, have a drink",
    "Drink if you want to have sex after this game",
    "Kiss someone or drink",
    "Take 1 article of clothing off or take a shot",
    "Recreate your favorite sex position",
    "It's a 10, but they're Christinas ex",
    "Would you rather marry the person to your right or the person to your left?",
    "Name the person you liked the least when you first met them",
    "Who's most likely to get a sugar daddy/mommy?",
    "Kiss the person to your left",
    "Never have I ever stalked an ex's new partner",
    "Allow someone in the room to go through your DMs for 15 seconds",
    "Kiss the person to your right",
    "Flash someone",
    "The one with the most hoes drinks",
    "Never have I ever broken up with someone",
    "Describe your last hookup in 3 words",
    "Would you rather have sex with your worst tinder match or with the person to your left?",
    "Who's most likely to catch feelings after a one-night stand?",
    "Who's the last person you kissed, or drink",
    "Phones out on the table. First person to receive a notification has to take 5 sips",
    "The group votes on the most likely to get back with an ex. That person drinks.",
    "If you're single, have a drink",
    "What's your biggest turn on?",
    "What's your biggest dating ick?",
    "Have you ever snooped through someone's phone?",
    "Most likely to text an ex tonight",
    "Most likely to fall in love first sight?",
    "Most likely to end up on reality TV?",
    "Never have I ever pretended to like someones gift",
    "Show your most recent selfie",
    "Never have I ever gotten blocked",
    "Never have I ever had an fake account",
    "Never have I ever been catfished",
    "Never have I ever been on a dating app",
    "Never have I ever gotten kicked out of a bar",
    "Never have I ever been friend-zoned",
    "Mission: You have 10 seconds to bring a 'käpy', or take 3 sips",
    "Misson: You have 30 seconds to take a selfie with Irina, or take 3 sips",
    "Never have I ever been ghosted",
    "Never have I ever cancelled on somebody because someone better came along",
    "What's your biggest turn off?",
    "Choose a bitch",
    "What's the worst date you've ever been on?",
    "Silent round",
    "No eye-contact during the next round",
    "No names during the next round",
    "No swearing during the next round",
    "Take a sip if you've stalked someone in the last 24 hours",
    "Majority: You can be friends with an ex",
    "Majority: You can hook up with an ex",
    "Majority: Ghosting is sometimes acceptable",
    "Punishment: You have to end your sentence with 'bitch' for the next 3 rounds",
    "Punishment: You have to end your sentence with 'babygirl' for the next 3 rounds",
    "Punishment: You have to end your sentence with 'daddy' for the next 3 rounds",
    "Majority: You can have a girl/boy bestfriend",
]


current_index = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/challenge')
def challenge():
    global current_index

    # Get current challenge
    challenge_text = challenges[current_index]

    # Move to the next one, loop around if at the end
    current_index = (current_index + 1) % len(challenges)

    return jsonify({"challenge": challenge_text})

if __name__ == '__main__':
    app.run(debug=True)

