class Config:

    #file_path = "/home/bumu60du/fake_review_detection/Datasets/Amazon_Human_VS_ComputerFake.csv"

    #model = "gemma3:12b"

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

