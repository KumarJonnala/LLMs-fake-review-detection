class Config:

    file_path = ""

    model = ""

    zero_shot_prompt_template = """
    You are an expert at detecting truthful and deceptive reviews.

    Task: Classify the following hotel or product review as either "truthful" or "deceptive".

    Review: "{text}"

    Classify this review as either "truthful" or "deceptive" (respond with only one word):"""

    # Define one-shot classification prompt with one example
    one_shot_prompt_template = """
    You are an expert at detecting truthful and deceptive reviews.

    Task: Classify the following hotel or product review as either "truthful" or "deceptive".

    Here are some examples: 

    Example 1:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted to. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: deceptive

    Example 2:
    Review: "I received these in and decided to go ahead and test these for strength and if it will be a good workout. I love the medium to the very strongest. The lighter exercise band when stretched rolled up a few times on me and I would have to unroll and start again. I guess because I was pulling it out so hard. The others did fine. I could feel the tightness with those as I stretched it out. I may lay flat and try it on my ankles and legs next. I left out of town so I have not been able to test it that way. But I assure you, you will feel it in your arms. I would consider buying these for my neighbor who also wants to work her arm muscles, because I do not want to loan mine out, as I will continue to use the tighter bands.
    Classification: truthful

    Now classify this review:
    Review: "{text}"
    Classify this review as either "truthful" or "deceptive" (respond with only one word):"""

    # Define few-shot classification prompt with multiple examples
    few_shot_prompt_template = """
    You are an expert at detecting truthful and deceptive hotel or product reviews.

    Task: Classify reviews as either "truthful" or "deceptive".

    Here are some examples:

    Example 1:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted to. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: deceptive

    Example 2:
    Review: "We stayed for a one night getaway with family on a thursday. Triple AAA rate of 173 was a steal. 7th floor room complete with 44in plasma TV bose stereo, voss and evian water, and gorgeous bathroom(no tub but was fine for us) Concierge was very helpful. You cannot beat this location... Only flaw was breakfast was pricey and service was very very slow(2hours for four kids and four adults on a friday morning) even though there were only two other tables in the restaurant. Food was very good so it was worth the wait. I would return in a heartbeat. A gem in chicago..."
    Classification: truthful

    Example 3:
    Review: "OOfos are absolutely amazing shoes. They are lightweight and comfortable. I love the style and the style is so comfortable. I am a 32D"
    Classification: deceptive
    
    Example 4:
    Review: "I received these in and decided to go ahead and test these for strength and if it will be a good workout. I love the medium to the very strongest. The lighter exercise band when stretched rolled up a few times on me and I would have to unroll and start again. I guess because I was pulling it out so hard. The others did fine. I could feel the tightness with those as I stretched it out. I may lay flat and try it on my ankles and legs next. I left out of town so I have not been able to test it that way. But I assure you, you will feel it in your arms. I would consider buying these for my neighbor who also wants to work her arm muscles, because I do not want to loan mine out, as I will continue to use the tighter bands."
    Classification: truthful

    Now classify this review:
    Review: "{text}"
    Classify this review as either "truthful" or "deceptive" (respond with only one word):"""