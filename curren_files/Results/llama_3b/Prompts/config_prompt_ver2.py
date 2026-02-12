class Config:

    file_path = "/home/aluc31or/LLM_Project/Amazon_Human_VS_ComputerFake.csv"
    # model = "gemma:2b"
    model = "llama3.2:3b"
    
    zero_shot_depth0_width0_ver2 = """
    Role
    You are an expert at classifying fake and real reviews.

    Task
    Classify the following hotel or product review as either fake or real.

    Review
    "{text}"

    Guidelines:
    - Fake reviews often use generic, exaggerated, or marketing-style language.
    - Real reviews usually contain natural wording and specific details.

    Answer with your classification.
    Use one of these labels:
    fake or real
    """

    zero_shot_depth1_width1_ver2 = """
    Role
    You are an expert linguistic analyst specializing in classifying real and fake online reviews.

    Task
    Your task is to classify a given hotel or product review as either fake or real.

    Context
    You are provided with a single review written by a customer.
    Some reviews may be artificially generated, exaggerated, or written with promotional intent rather than genuine experience.

    Review
    "{text}"

    Classification Rules (internal use only):
    - Fake reviews often contain generic or templated language.
    - Fake reviews may exaggerate praise or criticism.
    - Marketing-style or promotional wording is a strong indicator of deception.
    - Real reviews usually include natural language and specific experiential details.

    CRITICAL OUTPUT REQUIREMENT — STRICTLY ENFORCED
    You must output ONLY ONE WORD.
    You must NOT provide explanations, reasoning, analysis, or commentary.
    Any output other than exactly one of the following words is INVALID.

    Classify this review as either "fake" or "real" (respond with only one word):
    """


    one_shot_depth1_width1_ver2 = """
    Role
    You are an expert linguistic analyst specializing in classifying real and fake online reviews.

    Task
    Classify a given hotel or product review as either fake or real.

    Context
    You will classify the review based on linguistic cues that distinguish genuine customer experiences from artificially generated or promotional content.

    Classification Rules for internal use only do NOT write them in output:
    - Fake reviews often contain generic or templated language.
    - Fake reviews may exaggerate praise or criticism.
    - Marketing-style or promotional wording is a strong indicator of deception.
    - Real reviews usually include natural language and specific experiential details.

    Review to Classify
    "{text}"

    CRITICAL OUTPUT REQUIREMENT — STRICTLY ENFORCED
    - You must output ONLY ONE WORD.
    - Do NOT write classification Rules and Context.
    - Do NOT provide explanations, reasoning, or analysis.
    - Any additional text will invalidate the output.

    Answer with your classification.
    Use one of these labels:
    real or fake

    Example (for reference only — do NOT explain)
    Review:
    "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted to. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"

    Classification:
    fake
    """

    few_shot_depth1_width1_ver2 = """
    Role
    You are an expert linguistic analyst specializing in classifying real and fake online reviews.

    Task
    Classify a given hotel or product review as either fake or real.

    Context
    You will classify the review based on linguistic cues that distinguish genuine customer experiences from artificially generated or promotional content.

    Classification Rules for internal use only do NOT write them in output:
    - Fake reviews often contain generic or templated language.
    - Fake reviews may exaggerate praise or criticism.
    - Marketing-style or promotional wording is a strong indicator of deception.
    - Real reviews usually include natural language and specific experiential details.

    Review to Classify
    "{text}"

    CRITICAL OUTPUT REQUIREMENT — STRICTLY ENFORCED
    - You must output ONLY ONE WORD.
    - Do NOT write classification Rules and Context.
    - Do NOT provide explanations, reasoning, or analysis.
    - Any additional text will invalidate the output.

    Answer with your classification.
    Use one of these labels:
    real or fake

    Examples (for reference only — do NOT explain)

    Example 1:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: fake
    Example 2:
    Review: "We stayed for a one night getaway with family on a thursday. Triple AAA rate of 173 was a steal. 7th floor room complete with 44in plasma TV bose stereo, voss and evian water, and gorgeous bathroom(no tub but was fine for us) Concierge was very helpful. You cannot beat this location... Only flaw was breakfast was pricey and service was very very slow."
    Classification: real
    Example 3:
    Review: "Great Watch. I have had this watch for a long time and it works great. I have one in my car and the other in my office. The watch itself is a great watch and is very easy to use. It is a perfect size for my wrist and is very easy to wear. I have used it with a portable watch and I can tell the watch is very well made. I have worn it with a watch band and it is very comfortable. I will buy another one for my phone. I would highly recommend this watch.Perfect for my kids. I love them.These are super lightweight and lightweight. I have used them for a couple of months and they are still working great. I would definitely recommend them to my son for those times when he is not going to be wearing a helmet.These work great. I have used them for about a month and they are still doing great.Works as advertised.This is my second pair of glasses, and I really like the quality of the material. The material is thin and very soft, and it's comfortable to wear. The material is also very easy to clean, and I haven't had a problem with the plastic being damaged. I also have the odd case on my older pair, which I got for my husband when I was a kid. The fact that it's made of a durable material is"
    Classification: fake
    Example 4:
    Review: "I received these in and decided to go ahead and test these for strength and if it will be a good workout. I love the medium to the very strongest. The lighter exercise band when stretched rolled up a few times on me and I would have to unroll and start again. I guess because I was pulling it out so hard. The others did fine. I could feel the tightness with those as I stretched it out. I may lay flat and try it on my ankles and legs next. I left out of town so I have not been able to test it that way. But I assure you, you will feel it in your arms. I would consider buying these for my neighbor who also wants to work her arm muscles, because I do not want to loan mine out, as I will continue to use the tighter bands.
    Classification: real
    """