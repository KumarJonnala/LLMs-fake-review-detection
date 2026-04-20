class Config:

    file_path = "/home/sohy47ma/ReviewProject/fake_reviews_prediction/Datasets/sampled_deceptive_opinion_new.csv"
    model = "llama3.2:3b"

    # depth:Modifiers(with/without), Width:Information(less/detailed)

    # Define zero-shot classification prompt
    # text placeholder in the prompt template will be replaced with actual review text.

    zero_shot_prompt_template1 = """
    Classify the following review as either "truthful" or "deceptive".  
    Review: "{text}"
    Respond with: truthful or deceptive(respond with only one word)
    """

    zero_shot_prompt_template2 = """
    You are an expert at detecting fake and deceptive reviews.
    Task: Classify the following hotel review or a product review as either "truthful" or "deceptive". Analyze the language and structure of the review, It should not be overly generic or templeted language,should not have sales-like wording.
    Review: "{text}"
    Classify this review as either "truthful" or "deceptive" (respond with only one word):
    """

    zero_shot_prompt_template3 = """
    You are an expert at detecting fake and deceptive reviews. Carefully analyze the following review for signs such as:
    - Overly generic or vague language
    - Exaggerated praise or criticism
    - Repetitive or templated phrasing
    - Marketing-like wording or unnatural flow
    - Specific details vs. general statements
    After analyzing, classify the review as "truthful" or "deceptive".
    Review: "{text}"
    Classify this review as either "truthful" or "deceptive" (respond with only one word):
    """
    
    # depth:Modifiers(with/without), Width:Information(less/detailed)

    zero_shot_depth0_width0 ="""
    Task:
    Classify the following review as either "truthful" or "deceptive".
    Review: "{text}"
    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.

    """

    zero_shot_depth0_width1 ="""
    Context:
    The review may be either a hotel review or a product review.
    Deceptive reviews often resemble advertisements or templates and lack authentic personal experience.

    Task:
    Classify the following review as either "truthful" or "deceptive".
    Review: "{text}"
    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """

    zero_shot_depth1_width0 ="""
    You are an expert at classifying fake and deceptive reviews.
    Task:
    Classify the following review as either "truthful" or "deceptive".
    Review: "{text}"
    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """

    zero_shot_depth2_width1 ="""
    You are an expert at classifying fake and deceptive reviews.

    Analyze the review carefully using these signals:
    - Overly generic or vague language
    - Exaggerated praise or criticism
    - Repetitive or templated phrasing
    - Marketing-like wording or unnatural flow
    - Specific details vs. general statements

    Apply these criteria strictly.
    Do not assume authenticity unless it is clearly demonstrated.

    Context:
    The review may be either a hotel review or a product review.
    Deceptive reviews often resemble advertisements or templates and lack authentic personal experience.

    Task:
    Classify the following review as either "truthful" or "deceptive".

    Review: "{text}"

    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """

    zero_shot_depth3_width1 ="""
    You are an expert at classifying fake and deceptive reviews.

    Analyze the review carefully using these signals:
    - Overly generic or vague language
    - Exaggerated praise or criticism
    - Repetitive or templated phrasing
    - Marketing-like wording or unnatural flow
    - Specific details vs. general statements

    Apply these criteria strictly.
    Do not assume authenticity unless it is clearly demonstrated.

    Decision rule:
    Only classify a review as "truthful" if there is strong, explicit evidence of a genuine personal experience.
    If evidence is weak, mixed, or ambiguous, classify it as "deceptive".

    Context:
    The review may be either a hotel review or a product review.
    Deceptive reviews often resemble advertisements or templates and lack authentic personal experience.

    Task:
    Classify the following review as either "truthful" or "deceptive".

    Review: "{text}"

    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """

    

    # Define one-shot classification prompt with one example   

    one_shot_prompt_template1 = """
    Task: Classify the following review of a hotel or product as either "truthful" or "deceptive".
    Example:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted to. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away! "
    Classification: deceptive
    Now classify this review:
    Review: "{text}"
    Classification (respond with only one word):
    """

    one_shot_prompt_template2 = """
    You are an expert at classifying truthful and deceptive reviews.
    Task: Classify the following review of a hotel or Amazon product as either "truthful" or "deceptive". Look for vague language, exaggerated praise, or sales-like wording in the review.
    Example:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: deceptive
    Now classify this review:
    Review: "{text}"
    Classification (respond with only one word):
    """

    one_shot_prompt_template3 = """
    You are an expert at classifying truthful and deceptive reviews.
    Task: Classify the following review of a hotel or Amazon product as either "truthful" or "deceptive". Carefully analyze the review considering:
    - Overly generic or vague language
    - Exaggerated praise or criticism
    - Templated or sales-like wording
    - Lack of details or specificity
    - Natural flow versus marketing style
    Example:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: deceptive
    Now classify this review:
    Review: "{text}"
    Classify this review as either "truthful" or "deceptive" (respond with only one word):
    """

    one_shot_depth0_width0 = """
    Task: Classify the following review of a hotel or product as either "truthful" or "deceptive".
    Example:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted to. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away! "
    Classification: deceptive
    Now classify this review:
    Review: "{text}"
    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """

    one_shot_depth0_width1 = """
    Context:
    The review may be a hotel review or a product review.
    Deceptive reviews often resemble advertisements and lack authentic personal experience.

    Task: Classify the following review of a hotel or product as either "truthful" or "deceptive".
    Example:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted to. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away! "
    Classification: deceptive
    Now classify this review:
    Review: "{text}"
    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """

    one_shot_depth1_width0 = """
    You are an expert at classifying truthful and deceptive reviews.
    
    Task: Classify the following review of a hotel or product as either "truthful" or "deceptive".
    Example:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted to. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away! "
    Classification: deceptive
    Now classify this review:
    Review: "{text}"
    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """
    
    one_shot_depth2_width1 = """
    You are an expert at classifying truthful and deceptive reviews.

    Carefully and critically analyze the review using the following criteria:
    - Overly generic or vague language
    - Exaggerated praise or criticism
    - Templated or sales-like wording
    - Lack of details or specificity
    - Natural flow versus marketing style

    Apply these criteria strictly.
    Do not make assumptions or give the benefit of the doubt.

    Context:
    The review may be a hotel review or a product review.
    Deceptive reviews often resemble advertisements and lack authentic personal experience.

    
    Task: Classify the following review of a hotel or product as either "truthful" or "deceptive".
    Example:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted to. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away! "
    Classification: deceptive
    Now classify this review:
    Review: "{text}"
    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """

    one_shot_depth3_width1 = """
    You are an expert at classifying truthful and deceptive reviews.

    Carefully and critically analyze the review using the following criteria:
    - Overly generic or vague language
    - Exaggerated praise or criticism
    - Templated or sales-like wording
    - Lack of details or specificity
    - Natural flow versus marketing style

    Apply these criteria strictly.
    Do not make assumptions or give the benefit of the doubt.

    Decision rule:
    Only classify a review as "truthful" if there is strong, explicit evidence of a genuine personal experience.
    If evidence is weak, mixed, or ambiguous, classify it as "deceptive".

    Context:
    The review may be a hotel review or a product review.
    Deceptive reviews often resemble advertisements and lack authentic personal experience.

    
    Task: Classify the following review of a hotel or product as either "truthful" or "deceptive".
    Example:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted to. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away! "
    Classification: deceptive
    Now classify this review:
    Review: "{text}"
    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """

    # Define few-shot classification prompt with multiple examples
    few_shot_prompt_template1 = """
    You are an expert at classifying truthful and deceptive reviews.
    Task: Classify the following review of a hotel or Amazon product as either "truthful" or "deceptive".

    Examples:
    Example 1:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: deceptive
    Example 2:
    Review: "We stayed for a one night getaway with family on a thursday. Triple AAA rate of 173 was a steal. 7th floor room complete with 44in plasma TV bose stereo, voss and evian water, and gorgeous bathroom(no tub but was fine for us) Concierge was very helpful. You cannot beat this location... Only flaw was breakfast was pricey and service was very very slow."
    Classification: truthful
    Now classify this review:
    Review: "{text}"
    Classify this review as either "truthful" or "deceptive" (respond with only one word):
    """

    few_shot_prompt_template2 = """
    You are an expert at classifying truthful and deceptive reviews.
    Task: Classify the following review of a hotel or Amazon product as either "truthful" or "deceptive". Consider whether the review sounds genuine, specific, and experience-based versus vague, exaggerated, or promotional.
    Examples:

    Example 1:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted to. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: deceptive
    Example 2:
    Review: "We stayed for a one night getaway with family on a thursday. Triple AAA rate of 173 was a steal. 7th floor room complete with 44in plasma TV bose stereo, voss and evian water, and gorgeous bathroom(no tub but was fine for us) Concierge was very helpful. You cannot beat this location... Only flaw was breakfast was pricey and service was very very slow(2hours for four kids and four adults on a friday morning) even though there were only two other tables in the restaurant. Food was very good so it was worth the wait. I would return in a heartbeat. A gem in chicago..."
    Classification: truthful
    Example 3:
    Review: "The Palmer House Hilton, while it looks good in pictures, and the outside, is actually a disaster of a hotel. When I went through, the lobby was dirty, my room hadn't been cleaned, and smelled thoroughly of smoke. When I requested more pillows, the lady on the phone scoffed at me and said she'd send them up. It took over an hour for 2 pillows. This hotel is a good example that what you pay for isn't always what you get. I will not be returning."
    Classification: deceptive
    Example 4:
    Review: "Triple A rate with upgrade to view room was less than $200 which also included breakfast vouchers. Had a great view of river, lake, Wrigley Bldg. & Tribune Bldg. Most major restaurants, Shopping, Sightseeing attractions within walking distance. Large room with a very comfortable bed."
    Classification: truthful
    Now classify this review:
    Review: "{text}"
    Classify this review as either "truthful" or "deceptive" (respond with only one word):
    """

    few_shot_prompt_template3 = """
    You are an expert at classifying truthful and deceptive reviews.
    
    Task: Classify the following review of a hotel or Amazon product as either "truthful" or "deceptive". Carefully analyze the review based on the following criteria:
    - Truthful reviews typically include concrete details, balanced opinions, and natural language
    - Deceptive reviews often contain exaggerated claims, vague statements, templated phrasing, or sales-like wording
    - Lack of specificity or overly emotional tone can indicate deception
    Here are some examples:
    Example 1:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted to. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: deceptive
    Example 2:
    Review: "We stayed for a one night getaway with family on a thursday. Triple AAA rate of 173 was a steal. 7th floor room complete with 44in plasma TV bose stereo, voss and evian water, and gorgeous bathroom(no tub but was fine for us) Concierge was very helpful. You cannot beat this location... Only flaw was breakfast was pricey and service was very very slow(2hours for four kids and four adults on a friday morning) even though there were only two other tables in the restaurant. Food was very good so it was worth the wait. I would return in a heartbeat. A gem in chicago..."
    Classification: truthful
    Example 3:
    Review: "The Palmer House Hilton, while it looks good in pictures, and the outside, is actually a disaster of a hotel. When I went through, the lobby was dirty, my room hadn't been cleaned, and smelled thoroughly of smoke. When I requested more pillows, the lady on the phone scoffed at me and said she'd send them up. It took over an hour for 2 pillows. This hotel is a good example that what you pay for isn't always what you get. I will not be returning."
    Classification: deceptive
    Example 4:
    Review: "Triple A rate with upgrade to view room was less than $200 which also included breakfast vouchers. Had a great view of river, lake, Wrigley Bldg. & Tribune Bldg. Most major restaurants, Shopping, Sightseeing attractions within walking distance. Large room with a very comfortable bed."
    Classification: truthful
    Now classify this review:
    Review: "{text}"
    Analyze carefully and classify this review as either "truthful" or "deceptive" (respond with only one word):
    """

    few_shot_depth0_width0 = """
    Classify the following review as either "truthful" or "deceptive".

    Examples:
    Example 1:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: deceptive
    Example 2:
    Review: "It holds a lot of water, it's clean and utilitarian and best of all, it doesn't take up too much room in the fridge!"
    Classification: truthful
    Now classify this review:
    Review: "{text}"
    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """

    few_shot_depth0_width1 = """
    Context:
    The review may be a hotel review or a product review.
    Truthful reviews usually reflect genuine experiences.
    Deceptive reviews often resemble promotional or templated content.

    Classify the following review as either "truthful" or "deceptive".

    Examples:
    Example 1:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: deceptive
    Example 2:
    Review: "We stayed for a one night getaway with family on a thursday. Triple AAA rate of 173 was a steal. 7th floor room complete with 44in plasma TV bose stereo, voss and evian water, and gorgeous bathroom(no tub but was fine for us) Concierge was very helpful. You cannot beat this location... Only flaw was breakfast was pricey and service was very very slow."
    Classification: truthful
    Example 3:
    Review: "Great Watch. I have had this watch for a long time and it works great. I have one in my car and the other in my office. The watch itself is a great watch and is very easy to use. It is a perfect size for my wrist and is very easy to wear. I have used it with a portable watch and I can tell the watch is very well made. I have worn it with a watch band and it is very comfortable. I will buy another one for my phone. I would highly recommend this watch.Perfect for my kids. I love them.These are super lightweight and lightweight. I have used them for a couple of months and they are still working great. I would definitely recommend them to my son for those times when he is not going to be wearing a helmet.These work great. I have used them for about a month and they are still doing great.Works as advertised.This is my second pair of glasses, and I really like the quality of the material. The material is thin and very soft, and it's comfortable to wear. The material is also very easy to clean, and I haven't had a problem with the plastic being damaged. I also have the odd case on my older pair, which I got for my husband when I was a kid. The fact that it's made of a durable material is"
    Classification: deceptive
    Example 4:
    Review: "I received these in and decided to go ahead and test these for strength and if it will be a good workout. I love the medium to the very strongest. The lighter exercise band when stretched rolled up a few times on me and I would have to unroll and start again. I guess because I was pulling it out so hard. The others did fine. I could feel the tightness with those as I stretched it out. I may lay flat and try it on my ankles and legs next. I left out of town so I have not been able to test it that way. But I assure you, you will feel it in your arms. I would consider buying these for my neighbor who also wants to work her arm muscles, because I do not want to loan mine out, as I will continue to use the tighter bands.
    Classification: truthful
    Now classify this review:
    Review: "{text}"
    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """

    few_shot_depth1_width0 = """
    You are an expert at classifying truthful and deceptive reviews.

    Classify the following review as either "truthful" or "deceptive".

    Examples:
    Example 1:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: deceptive
    Example 2:
    Review: "We stayed for a one night getaway with family on a thursday. Triple AAA rate of 173 was a steal. 7th floor room complete with 44in plasma TV bose stereo, voss and evian water, and gorgeous bathroom(no tub but was fine for us) Concierge was very helpful. You cannot beat this location... Only flaw was breakfast was pricey and service was very very slow."
    Classification: truthful
    Example 3:
    Review: "Great Watch. I have had this watch for a long time and it works great. I have one in my car and the other in my office. The watch itself is a great watch and is very easy to use. It is a perfect size for my wrist and is very easy to wear. I have used it with a portable watch and I can tell the watch is very well made. I have worn it with a watch band and it is very comfortable. I will buy another one for my phone. I would highly recommend this watch.Perfect for my kids. I love them.These are super lightweight and lightweight. I have used them for a couple of months and they are still working great. I would definitely recommend them to my son for those times when he is not going to be wearing a helmet.These work great. I have used them for about a month and they are still doing great.Works as advertised.This is my second pair of glasses, and I really like the quality of the material. The material is thin and very soft, and it's comfortable to wear. The material is also very easy to clean, and I haven't had a problem with the plastic being damaged. I also have the odd case on my older pair, which I got for my husband when I was a kid. The fact that it's made of a durable material is"
    Classification: deceptive
    Example 4:
    Review: "I received these in and decided to go ahead and test these for strength and if it will be a good workout. I love the medium to the very strongest. The lighter exercise band when stretched rolled up a few times on me and I would have to unroll and start again. I guess because I was pulling it out so hard. The others did fine. I could feel the tightness with those as I stretched it out. I may lay flat and try it on my ankles and legs next. I left out of town so I have not been able to test it that way. But I assure you, you will feel it in your arms. I would consider buying these for my neighbor who also wants to work her arm muscles, because I do not want to loan mine out, as I will continue to use the tighter bands.
    Classification: truthful
    Now classify this review:
    Review: "{text}"
    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """  

    few_shot_depth1_width1 = """
    You are an expert at classifying truthful and deceptive reviews.

    Carefully analyze reviews using these principles:
    - Truthful reviews include concrete details, balanced opinions, and natural language
    - Deceptive reviews contain exaggerated claims, vague statements, templated phrasing, or sales-like wording
    - Overly emotional tone or lack of specificity can indicate deception

    Context:
    The review may be a hotel or product review.
    Deceptive reviews often attempt to persuade rather than describe genuine experience.

    Classify the following review as either "truthful" or "deceptive".

    Examples:
    Example 1:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: deceptive
    Example 2:
    Review: "We stayed for a one night getaway with family on a thursday. Triple AAA rate of 173 was a steal. 7th floor room complete with 44in plasma TV bose stereo, voss and evian water, and gorgeous bathroom(no tub but was fine for us) Concierge was very helpful. You cannot beat this location... Only flaw was breakfast was pricey and service was very very slow."
    Classification: truthful
    Example 3:
    Review: "Great Watch. I have had this watch for a long time and it works great. I have one in my car and the other in my office. The watch itself is a great watch and is very easy to use. It is a perfect size for my wrist and is very easy to wear. I have used it with a portable watch and I can tell the watch is very well made. I have worn it with a watch band and it is very comfortable. I will buy another one for my phone. I would highly recommend this watch.Perfect for my kids. I love them.These are super lightweight and lightweight. I have used them for a couple of months and they are still working great. I would definitely recommend them to my son for those times when he is not going to be wearing a helmet.These work great. I have used them for about a month and they are still doing great.Works as advertised.This is my second pair of glasses, and I really like the quality of the material. The material is thin and very soft, and it's comfortable to wear. The material is also very easy to clean, and I haven't had a problem with the plastic being damaged. I also have the odd case on my older pair, which I got for my husband when I was a kid. The fact that it's made of a durable material is"
    Classification: deceptive
    Example 4:
    Review: "I received these in and decided to go ahead and test these for strength and if it will be a good workout. I love the medium to the very strongest. The lighter exercise band when stretched rolled up a few times on me and I would have to unroll and start again. I guess because I was pulling it out so hard. The others did fine. I could feel the tightness with those as I stretched it out. I may lay flat and try it on my ankles and legs next. I left out of town so I have not been able to test it that way. But I assure you, you will feel it in your arms. I would consider buying these for my neighbor who also wants to work her arm muscles, because I do not want to loan mine out, as I will continue to use the tighter bands.
    Classification: truthful
    Now classify this review:
    Review: "{text}"
    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """


    few_shot_depth2_width1 = """
    You are an expert at classifying truthful and deceptive reviews.

    Carefully analyze reviews using these principles:
    - Truthful reviews include concrete details, balanced opinions, and natural language
    - Deceptive reviews contain exaggerated claims, vague statements, templated phrasing, or sales-like wording
    - Overly emotional tone or lack of specificity can indicate deception

    Apply these criteria strictly.
    Do not assume authenticity unless it is clearly demonstrated.

    Context:
    The review may be a hotel or product review.
    Deceptive reviews often attempt to persuade rather than describe genuine experience.

    Classify the following review as either "truthful" or "deceptive".

    Examples:
    Example 1:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: deceptive
    Example 2:
    Review: "We stayed for a one night getaway with family on a thursday. Triple AAA rate of 173 was a steal. 7th floor room complete with 44in plasma TV bose stereo, voss and evian water, and gorgeous bathroom(no tub but was fine for us) Concierge was very helpful. You cannot beat this location... Only flaw was breakfast was pricey and service was very very slow."
    Classification: truthful
    Example 3:
    Review: "Great Watch. I have had this watch for a long time and it works great. I have one in my car and the other in my office. The watch itself is a great watch and is very easy to use. It is a perfect size for my wrist and is very easy to wear. I have used it with a portable watch and I can tell the watch is very well made. I have worn it with a watch band and it is very comfortable. I will buy another one for my phone. I would highly recommend this watch.Perfect for my kids. I love them.These are super lightweight and lightweight. I have used them for a couple of months and they are still working great. I would definitely recommend them to my son for those times when he is not going to be wearing a helmet.These work great. I have used them for about a month and they are still doing great.Works as advertised.This is my second pair of glasses, and I really like the quality of the material. The material is thin and very soft, and it's comfortable to wear. The material is also very easy to clean, and I haven't had a problem with the plastic being damaged. I also have the odd case on my older pair, which I got for my husband when I was a kid. The fact that it's made of a durable material is"
    Classification: deceptive
    Example 4:
    Review: "I received these in and decided to go ahead and test these for strength and if it will be a good workout. I love the medium to the very strongest. The lighter exercise band when stretched rolled up a few times on me and I would have to unroll and start again. I guess because I was pulling it out so hard. The others did fine. I could feel the tightness with those as I stretched it out. I may lay flat and try it on my ankles and legs next. I left out of town so I have not been able to test it that way. But I assure you, you will feel it in your arms. I would consider buying these for my neighbor who also wants to work her arm muscles, because I do not want to loan mine out, as I will continue to use the tighter bands.
    Classification: truthful
    Now classify this review:
    Review: "{text}"
    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """

    few_shot_depth3_width1 = """
    You are an expert at classifying truthful and deceptive reviews.

    Carefully analyze reviews using these principles:
    - Truthful reviews include concrete details, balanced opinions, and natural language
    - Deceptive reviews contain exaggerated claims, vague statements, templated phrasing, or sales-like wording
    - Overly emotional tone or lack of specificity can indicate deception

    Apply these criteria strictly.
    Do not assume authenticity unless it is clearly demonstrated.

    Decision rule:
    Only classify a review as "truthful" if there is strong, explicit evidence of a genuine personal experience.
    If evidence is weak, mixed, or ambiguous, classify it as "deceptive".

    Context:
    The review may be a hotel or product review.
    Deceptive reviews often attempt to persuade rather than describe genuine experience.

    Classify the following review as either "truthful" or "deceptive".

    Examples:
    Example 1:
    Review: "As a former Chicagoan, I'm appalled at the Amalfi Hotel Chicago. First of all, I was expecting luxury and hospitality, neither of which I received. There's an Experience Designer who is supposed to be like a 'personal concierge,' but my experience with my ED was terrible. I felt like he was trying to pressure me into staying more days than I wanted. Not only that, but I couldn't understand what he was saying most of the time because he was talking so fast. When I finally got to my room, I was disappointed with the quality of the furniture and the room's cleanliness. I had to ask for a maid to come and give me clean towels because some of the towels in the bathroom were damp. On top of that, the bed was messily done; I could have done a better job on my own bed at home. I was angry at this point, because I was paying a lot of money for every night I was staying at Amalfi, and I didn't expect to be greeted with wet towels. I needed to use the Wi-Fi to download some important documents, and the internet was surprisingly slow. Even a very basic hotel or motel could have offered better, maybe even faster internet access. When I finally checked out of the Amalfi, I made sure that my supposed personal concierge knew all of the problems I'd had with my room and the hotel. I was glad to see the Amalfi getting smaller in the mirror as I drove away!"
    Classification: deceptive
    Example 2:
    Review: "We stayed for a one night getaway with family on a thursday. Triple AAA rate of 173 was a steal. 7th floor room complete with 44in plasma TV bose stereo, voss and evian water, and gorgeous bathroom(no tub but was fine for us) Concierge was very helpful. You cannot beat this location... Only flaw was breakfast was pricey and service was very very slow."
    Classification: truthful
    Example 3:
    Review: "Great Watch. I have had this watch for a long time and it works great. I have one in my car and the other in my office. The watch itself is a great watch and is very easy to use. It is a perfect size for my wrist and is very easy to wear. I have used it with a portable watch and I can tell the watch is very well made. I have worn it with a watch band and it is very comfortable. I will buy another one for my phone. I would highly recommend this watch.Perfect for my kids. I love them.These are super lightweight and lightweight. I have used them for a couple of months and they are still working great. I would definitely recommend them to my son for those times when he is not going to be wearing a helmet.These work great. I have used them for about a month and they are still doing great.Works as advertised.This is my second pair of glasses, and I really like the quality of the material. The material is thin and very soft, and it's comfortable to wear. The material is also very easy to clean, and I haven't had a problem with the plastic being damaged. I also have the odd case on my older pair, which I got for my husband when I was a kid. The fact that it's made of a durable material is"
    Classification: deceptive
    Example 4:
    Review: "I received these in and decided to go ahead and test these for strength and if it will be a good workout. I love the medium to the very strongest. The lighter exercise band when stretched rolled up a few times on me and I would have to unroll and start again. I guess because I was pulling it out so hard. The others did fine. I could feel the tightness with those as I stretched it out. I may lay flat and try it on my ankles and legs next. I left out of town so I have not been able to test it that way. But I assure you, you will feel it in your arms. I would consider buying these for my neighbor who also wants to work her arm muscles, because I do not want to loan mine out, as I will continue to use the tighter bands.
    Classification: truthful
    Now classify this review:
    Review: "{text}"
    STRICT OUTPUT RULE: Respond with exactly ONE word: truthful or deceptive.
    Do not include anything else.
    """