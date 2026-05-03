class Config:

    #file_path = "D:\OVGU _Saurabh\SEM 3\Review Project\Code\Datasets\sampled_deceptive_opinion_new.csv"

    model = "llama3.1:8b"

    # Define zero-shot classification prompt
    # text placeholder in the prompt template will be replaced with actual review text.
    zero_shot_prompt_template = """
    You are an expert at detecting fake and real reviews.

    Task: Classify the following review of a hotel that is listed on a website as either "fake" or "real". Analyze the language and structure of the review,
	It should not be overly generic or templeted language,should not have sales-like wording.

    Review: "{text}"

    Classify this review as either "fake" or "real" (respond with only one word):"""

    # Define one-shot classification prompt with one example
    one_shot_prompt_template = """
     You are an expert at detecting fake and real reviews.

    Task: Classify the following review of a hotel that is listed on a website as either "real" or "fake". Analyze the language and structure of the review,
	It should not be overly generic or templeted language,should not have sales-like wording and lacks details or specificity.

    Example:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted to. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away! "
    Classification: fake

    Now classify this review:
    Review: "{text}"
    Classify this review as either "real" or "fake" (respond with only one word):"""

    # Define few-shot classification prompt with multiple examples
    few_shot_prompt_template = """
    You are an expert at detecting real and fake reviews.


    Task: Classify the following review of a hotel that is listed on a website as either "real" or "fake". Analyze the language and structure of the review,
	It should not be overly generic or templeted language,should not have sales-like wording and lacks details or specificity.

    Here are some examples:

    Examples:
    Example 1:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: fake
    Example 2:
    Review: "We stayed for a one night getaway with family on a thursday. Triple AAA rate of 173 was a steal. 7th floor room complete with 44in plasma TV bose stereo, voss and evian water, and gorgeous bathroom(no tub but was fine for us) Concierge was very helpful. You cannot beat this location... Only flaw was breakfast was pricey and service was very very slow."
    Classification: real

    Now classify this review:
    Review: "{text}"
    Classify this review as either "real" or "fake" (respond with only one word):"""

    few_shot_prompt_template2 = """
    You are an expert at detecting real and fake reviews.


    Task: Classify the following review of a hotel that is listed on a website as either "real" or "fake". Analyze the language and structure of the review,
	It should not be overly generic or templeted language,should not have sales-like wording and lacks details or specificity.

    Here are some examples:

    Examples:
    Example 1:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: fake
    Example 2:
    Review: "We stayed for a one night getaway with family on a thursday. Triple AAA rate of 173 was a steal. 7th floor room complete with 44in plasma TV bose stereo, voss and evian water, and gorgeous bathroom(no tub but was fine for us) Concierge was very helpful. You cannot beat this location... Only flaw was breakfast was pricey and service was very very slow."
    Classification: real

    Example 3:
    Review: "I have stayed at the James a few times, it is my go to hotel in Chicago. This last trip makes me think it is time to start looking for other options. The Good: Location is awesome, just off Michigan Ave, Trader Joe's across street for some healthier snacking. It is a great location, easy to walk most anywhere. The door staff are very friendly and helpful. The overall feeling is modern, upbeat. Turn down service with cookie is nice. Free Wifi (which worked to varying degrees throughout stay) The Bad: They claim to be a 4.5 star hotel, which to me, means better then a 4 star and online with a 5 star (without a pool). They used to have Kiehls toiletries and now have 'Harmony' brand. Additionally, they now have the large bottles attached to the wall which you get to share with the other guests that stayed in the room before you. It is what I would expect from Holiday Inn or my gym, but not a 4.5 star hotel. I asked about the switch (mainly because when I booked they still had Kiehls in website description) and they claimed that the reason they went the communal bottle route was to be 'green'. That is hard to believe, as it's not like the hotel is making other efforts to be green (they still have incandescent light bulbs, housekeeping leaves the lights and radio on when they do turn down, they don't recycle in room, etc). They are obviously trying to cut costs, and it shows. More: the rooms are in need of some updating, they are looking somewhat tired. My third floor room was quite loud with the motorcyclers trying to prove their manhood out front (not their fault). Don't take the stairs (as the stairwell is straight out of horror movie), even though the wait for one of the two elevators might be awhile. The phone staff was fairly rude (granted, they didn't like me questioning their toiletry change). I feel bad giving such a low rating, but it really did not come close to my expectations (from previous stays there). I will start trying out new hotels in the area."
    Classification: real

    Example 4:
    Review: "The Millennium Hotel Knickerbocker sounds fine, and the website is pretty, but the reality is an over-hyped, overpriced, reality-isn't-as-good-as-fantasy package. The catering they offer is a joke; you can pick up better food for half the price at a dozen or more places in the Chicago area. While the rooms were cleaner than most, there was a lingering unpleasant odor from the cleaners they used that aggravated my sinuses, and when I called to complain about it, a nasal-voiced clerk blew me off. The rooms look small but cozy when you book online, but when you get there in person, you realize just how tiny they are. Trying to fit inside of one makes you think of being in a sardine can -- did I mention that it smelled like cleaning solution? I also found a hair on my supposedly clean bed, which made me wonder just how thorough their housekeeping staff is. In fact, it looks like all of their rooms are comparatively small; you'd get better prices and a far better room from the Hilton."
    Classification: fake

    Now classify this review:
    Review: "{text}"
    Classify this review as either "real" or "fake" (respond with only one word):"""

