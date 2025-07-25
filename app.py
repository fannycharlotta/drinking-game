from flask import Flask, render_template, jsonify

app = Flask(__name__)

challenges = [
    "Would you rather kiss your ex or your best friends ex",
    "What's the last text you sent?",
    "Never have I ever 'forgotten' to use protection",
    "Who's most likely to hook up with their ex?",
    "Never have I ever sent nudes",
    "Have you ever faked feeling while in bed?",
    "When's the last time you had sex - and was it good?",
    "Do you have a go-to person for hookups? Say their name or take a shot",
    "Text your last sneaky link 'I miss you' or take a shot",
    "Who's the most likely to date two people at once?",
    "Never have I ever forgot how I got home",
    "Drink if you don't like someone's partner",
    "Open 'my eyes only' or drink 4",
    "Drink if you have dated someone younger than you",
    "Have you ever faked an orgasm?",
    "Never have I ever ghosted someone",
    "Who's most likely to ghost after sex?",
    "Never have I ever lied on a dating app",
    "Take a sip if you've kissed more than 2 people in this room",
    "Let someone go through your camera roll for 15 seconds",
    "Share your last spicy photo or drink twice",
    "Never have I ever been proposed to",
    "Who's most likely to catch feeling after a one night stand?",
    "Make a rule",
    "Never have I ever had sex in a public place",
    "It's a 9 but they like to lick your toes",
    "Take a selfie with someone and caption it 'sneaky link vibes'",
    "What's the most public place you've done it?",
    "Never have I ever flirted with someone I wasn't attracted to",
    "Give someone in the room a lap dance",
    "Never have I ever kissed someone whose first name I didn't know",
    "Name the person with the craziest ex",
    "Sit on someone's lap for the next 2 rounds",
    "Make out with someone for 10 seconds or take 5 BIG sips",
    "Never have I ever used hancuffs in bed",
    "Would you rather hook up with your boss or your friend's sibling?",
    "Never have I ever made a sex tape",
    "Have a drink for every ex you have had",
    "Never have I ever had sex in a car",
    "Who's most likely to post a thirst trap on their social media?",
    "Never have I ever wanted to have a threesome with a current partner and my ex",
    "If you had to hook up with someone in this room, whou would you NOT pick - and why?",
    "How many people have you kissed this year?",
    "Never have I ever hooked up with someone twice my age",
    "Never have I ever drunk texted an ex",
    "If you have broken up with someone over text, have a drink",
    "If you're in a relationship, have a drink",
    "Drink if you want to have sex after this game",
    "Kiss someone or drink",
    "Take 1 article of clothing off or take a shot",
    "Recreate your favorite sex position",
    "It's a 10, but they're Christinas ex",
    "Who's most likely to become a stipper?",
    "Would you rather marry the person to your right or ",
    "Who's most likely to have sex on the first date?",
    "Name the person you liked the least when you first met them",
    "Never have I ever hooked up with someone just for a place to sleep",
    "Who's most likely to get a sugar daddy/mommy?",
    "Kiss the person to your left",
    "Never have I ever stalked an ex's new partner",
    "Allow someone in the room to go through your DMs for 15 seconds",
    "Who's most likely to lie about their bodycount?",
    "Kiss the person to your right",
    "The one with the highest snapscore drinks",
    "Have you ever had a crush on one of your friend's partners?",
    "Flash someone",
    "The one with the most hoes drinks",
    "Drink your bodycount",
    "Never have I ever broken up with someone",
    "Describe your last hookup in 5 words",
    "Would you rather have sex with your worst tinder match or with the person to your left?",
    "Who's most likely to catch feelings after a one-night stand?",
    "Who's the last person you kissed, or drink",
    "Phones out on the table. First person to receive a notification has to take 5 sips",
    "The group votes on the most likely to get back with an ex. That person drinks.",
    "If you're single, have a drink",
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

